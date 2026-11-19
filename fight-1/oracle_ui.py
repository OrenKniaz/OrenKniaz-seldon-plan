"""Stdlib Chromium CDP client and DOM-only UI checks for oracle.py."""
import base64
import hashlib
import http.client
import json
import os
from pathlib import Path
import socket
import struct
import subprocess
import time
from urllib.parse import urlsplit


class CDP:
    def __init__(self, url):
        parsed = urlsplit(url)
        self.sock = socket.create_connection((parsed.hostname, parsed.port), timeout=8)
        key = base64.b64encode(os.urandom(16)).decode()
        self.sock.sendall((f'GET {parsed.path} HTTP/1.1\r\nHost: {parsed.netloc}\r\n'
                           f'Upgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\n'
                           'Sec-WebSocket-Version: 13\r\n\r\n').encode())
        header = b''
        while not header.endswith(b'\r\n\r\n'):
            header += self.read(1)
            if len(header) > 16384:
                raise RuntimeError('oversized websocket handshake')
        accept = base64.b64encode(hashlib.sha1((key + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11').encode()).digest())
        assert b' 101 ' in header and accept in header, 'CDP websocket handshake failed'
        self.number, self.errors, self.external_requests = 0, [], []

    def read(self, count):
        result = bytearray()
        while len(result) < count:
            block = self.sock.recv(count - len(result))
            if not block:
                raise ConnectionError('Chromium websocket closed')
            result.extend(block)
        return bytes(result)

    def send(self, data, opcode=1):
        data = data.encode() if isinstance(data, str) else data
        length, mask = len(data), os.urandom(4)
        head = bytes([0x80 | opcode])
        head += bytes([0x80 | length]) if length < 126 else (bytes([0xFE]) + struct.pack('!H', length) if length < 65536 else bytes([0xFF]) + struct.pack('!Q', length))
        self.sock.sendall(head + mask + bytes(v ^ mask[i % 4] for i, v in enumerate(data)))

    def receive(self):
        chunks = bytearray()
        while True:
            a, b = self.read(2)
            size = b & 127
            if size == 126:
                size = struct.unpack('!H', self.read(2))[0]
            elif size == 127:
                size = struct.unpack('!Q', self.read(8))[0]
            mask = self.read(4) if b & 128 else None
            payload = self.read(size)
            if mask:
                payload = bytes(v ^ mask[i % 4] for i, v in enumerate(payload))
            opcode = a & 15
            if opcode == 8:
                raise ConnectionError('Chromium closed websocket')
            if opcode == 9:
                self.send(payload, 10)
                continue
            if opcode == 10:
                continue
            chunks.extend(payload)
            if a & 128:
                return json.loads(chunks)

    def call(self, method, params=None):
        self.number += 1
        number = self.number
        self.send(json.dumps({'id': number, 'method': method, 'params': params or {}}))
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            message = self.receive()
            if message.get('id') == number:
                if 'error' in message:
                    raise RuntimeError(message['error'])
                return message.get('result', {})
            name, data = message.get('method'), message.get('params', {})
            if name == 'Runtime.exceptionThrown':
                self.errors.append(data)
            if name == 'Runtime.consoleAPICalled' and data.get('type') == 'error':
                self.errors.append(data)
            if name == 'Log.entryAdded' and data.get('entry', {}).get('level') == 'error':
                self.errors.append(data)
            if name == 'Network.requestWillBeSent':
                url = data.get('request', {}).get('url', '')
                parsed = urlsplit(url)
                if parsed.scheme in ('http', 'https', 'ws', 'wss') and parsed.hostname not in ('127.0.0.1', 'localhost', '::1'):
                    self.external_requests.append(url)
        raise TimeoutError(f'CDP timeout: {method}')

    def js(self, expression):
        result = self.call('Runtime.evaluate', {'expression': expression, 'returnByValue': True, 'awaitPromise': True})
        if 'exceptionDetails' in result:
            raise RuntimeError(result['exceptionDetails'])
        return result.get('result', {}).get('value')

    def wait(self, expression, seconds=5):
        deadline = time.monotonic() + seconds
        while time.monotonic() < deadline:
            if self.js(expression):
                return
            time.sleep(.08)
        raise AssertionError(f'UI condition not reached: {expression[:180]}')

    def close(self):
        self.sock.close()


def chromium():
    root = Path.home() / 'AppData' / 'Local' / 'ms-playwright'
    for pattern in ('chromium-*/chrome-win64/chrome.exe', 'chromium-*/chrome-win/chrome.exe',
                    'chromium_headless_shell-*/chrome-win/headless_shell.exe',
                    'chromium_headless_shell-*/chrome-win64/headless_shell.exe'):
        paths = sorted(root.glob(pattern), reverse=True)
        if paths:
            return paths[0]
    return None


HELPERS = r"""
const visible=e=>!!e && !!(e.offsetWidth||e.offsetHeight||e.getClientRects().length) && getComputedStyle(e).visibility!=='hidden';
const desc=e=>[e.getAttribute('aria-label'),e.placeholder,e.name,e.id,...Array.from(e.labels||[],l=>l.innerText),e.innerText].filter(Boolean).join(' ').toLowerCase();
const inputs=(root=document)=>Array.from(root.querySelectorAll('input,select,textarea')).filter(visible);
const field=(re,root=document)=>inputs(root).find(e=>re.test(desc(e)));
const addForm=()=>field(/quantity|qty/)?.closest('form');
const set=(e,v)=>{if(!e)throw Error('semantic control not found'); const p=e.tagName==='SELECT'?HTMLSelectElement.prototype:HTMLInputElement.prototype;Object.getOwnPropertyDescriptor(p,'value').set.call(e,v);e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));};
const buttons=()=>Array.from(document.querySelectorAll('button,[role=button],input[type=submit]')).filter(visible);
const text=()=>document.body.innerText;
const click=async locate=>{const end=Date.now()+5000;while(Date.now()<end){const e=locate();if(visible(e)&&!e.matches(':disabled')&&!e.closest('[aria-disabled="true"],[inert]')){e.click();return e;}await new Promise(r=>setTimeout(r,80));}throw Error('Control did not become enabled');};
"""


def run_ui(oracle):
    executable = chromium()
    names = ['375 layout and console', '1440 layout and console', 'expiring soon and expired marking',
             'search', 'expiry filter', 'inline validation', 'add form', 'consume action', 'delete action',
             'empty state', 'API-error state', 'visible keyboard focus', 'readable contrast and calm design']
    if executable is None:
        for name in names:
            oracle.record('UI ' + name, 'unverified', 'Chromium absent from user Playwright cache')
        return
    browser = client = log = None
    try:
        from oracle import free_port
        port = free_port()
        profile = oracle.target / 'oracle-chromium-profile'
        log = (oracle.target / 'oracle-chromium.log').open('wb')
        browser = subprocess.Popen([str(executable), '--headless', '--disable-gpu', '--no-sandbox',
                                    '--no-first-run', '--no-default-browser-check',
                                    '--disable-background-networking', '--disable-component-update',
                                    '--disable-sync', '--remote-debugging-address=127.0.0.1',
                                    f'--remote-debugging-port={port}', f'--user-data-dir={profile}', 'about:blank'],
                                   stdout=log, stderr=log)
        deadline = time.monotonic() + 12
        endpoint = None
        while time.monotonic() < deadline:
            try:
                connection = http.client.HTTPConnection('127.0.0.1', port, timeout=1)
                connection.request('GET', '/json/list')
                pages = json.loads(connection.getresponse().read())
                connection.close()
                endpoint = next(p['webSocketDebuggerUrl'] for p in pages if p['type'] == 'page')
                break
            except (OSError, ValueError, StopIteration):
                time.sleep(.1)
        if not endpoint:
            raise RuntimeError('Chromium debugging endpoint unavailable; see oracle-chromium.log')
        client = CDP(endpoint)
        for domain in ('Page', 'Runtime', 'Log', 'Network'):
            client.call(domain + '.enable')

        def js(body):
            return client.js('(async()=>{' + HELPERS + body + '})()')

        def load():
            client.call('Page.navigate', {'url': oracle.base + '/'})
            client.wait("document.readyState==='complete'")
            # Wait for the page's API-backed rendering rather than only navigation.
            client.wait("document.body && /Soon apples|Expired beans/.test(document.body.innerText)")

        # Use only API to install the same visible scenario for either contender.
        for row in oracle.items():
            oracle.expect('DELETE', f'/api/items/{row["id"]}', (200, 204))
        for name, date in [('Soon apples', oracle.dates['soon']), ('Expired beans', oracle.dates['expired']),
                           ('Later oats', oracle.dates['later']), ('No expiry', None)]:
            oracle.create(name=name, expires=date)
        for width, height in ((375, 812), (1440, 900)):
            def layout(width=width, height=height):
                client.call('Emulation.setDeviceMetricsOverride', {'width': width, 'height': height,
                            'deviceScaleFactor': 1, 'mobile': False})
                load()
                dimensions = js('return {viewport:innerWidth,document:document.documentElement.scrollWidth,body:document.body.scrollWidth};')
                shot = oracle.target.parent / f'{oracle.label}-{width}.png'
                image = client.call('Page.captureScreenshot', {'format': 'png', 'captureBeyondViewport': False})
                shot.write_bytes(base64.b64decode(image['data']))
                assert dimensions['document'] <= width and dimensions['body'] <= width, dimensions
                assert not client.errors, str(client.errors)[:1000]
                return {'viewport': [width, height], 'dimensions': dimensions, 'screenshot': shot.name, 'console_errors': 0}
            oracle.check(f'UI {width} layout and console', layout)

        def soon():
            result = js(r"""
const heading=Array.from(document.querySelectorAll('h1,h2,h3,h4,[role=heading]')).find(e=>/expiring soon/i.test(e.innerText));
if(!heading)throw Error('Expiring soon heading absent');
let region=heading.parentElement;
while(region && !/Soon apples/.test(region.innerText))region=region.parentElement;
if(!region||region===document.body)throw Error('No distinct expiring-soon region containing near-expiry item');
let expired=Array.from(document.querySelectorAll('li,tr,article,[class]')).filter(visible).filter(e=>/Expired beans/.test(e.innerText)&&/expired|overdue|past due/i.test(e.innerText)).sort((a,b)=>a.innerText.length-b.innerText.length)[0];
return {section:region.innerText.slice(0,700),expired:expired?expired.innerText.slice(0,300):null};
""")
            assert result['expired'], 'expired item lacks a visible expired/overdue label'
            assert 'Later oats' not in result['section'] and 'No expiry' not in result['section'], result
            return result
        oracle.check('UI expiring soon and expired marking', soon)

        def change_filter(body):
            before = js('return text();')
            result = js(body)
            # Allow live filtering first, then use the focused control's form.
            time.sleep(.5)
            if js('return text();') == before:
                submit = js("""
const e=document.activeElement;const form=e.form||e.closest('form');
if(!form)return 'none';
const b=Array.from(form.elements).find(e=>visible(e)&&e.type==='submit');
if(b){await click(()=>Array.from(form.elements).find(e=>visible(e)&&e.type==='submit'));return 'clicked';}return 'enter';
""")
                if submit == 'enter':
                    for event in ('keyDown', 'keyUp'):
                        client.call('Input.dispatchKeyEvent', {'type': event, 'key': 'Enter', 'code': 'Enter',
                                                             'windowsVirtualKeyCode': 13})
            return result

        def search():
            change_filter("const e=field(/search/)||inputs().find(e=>e.type==='search');e.focus();set(e,'Soon apples');")
            client.wait("document.body.innerText.includes('Soon apples')&&!document.body.innerText.includes('Later oats')&&!document.body.innerText.includes('No expiry')")
            change_filter("const e=field(/search/)||inputs().find(e=>e.type==='search');e.focus();set(e,'');")
            client.wait("document.body.innerText.includes('Later oats')")
            return 'search narrows full list to matching name and clearing restores it'
        oracle.check('UI search', search)

        def expiry_filter():
            selected = change_filter(r"""
const selects=inputs().filter(e=>e.tagName==='SELECT');
for(const e of selects){const option=Array.from(e.options).find(o=>/7|soon|week/i.test(o.text));if(option){e.focus();set(e,option.value);return {kind:'select',description:desc(e),value:option.value};}}
const b=buttons().find(e=>/7 days|next week|expiring soon|expiry filter/i.test(desc(e)));if(b){await click(()=>buttons().find(e=>/7 days|next week|expiring soon|expiry filter/i.test(desc(e))));return {kind:'button',description:desc(b)};}
const c=inputs().find(e=>e.type==='checkbox'&&/expir|soon/i.test(desc(e)));if(c){c.focus();await click(()=>inputs().find(e=>e.type==='checkbox'&&/expir|soon/i.test(desc(e))));return {kind:'checkbox',description:desc(c)};}
throw Error('No semantic expiry-filter control found');
""")
            client.wait("document.body.innerText.includes('Soon apples')&&!document.body.innerText.includes('Later oats')&&!document.body.innerText.includes('No expiry')")
            load()
            return selected
        oracle.check('UI expiry filter', expiry_filter)
        # Reset between checks even if a failed assertion left a filter active.
        load()

        def validation():
            before = js("const form=addForm();return form?form.innerText:'';")
            js(r"""
const form=addForm();if(!form)throw Error('Add form absent');
const n=field(/(^|\s)(item.?name|name)(\s|$)/,form);const q=field(/quantity|qty/,form);set(n,'');if(q)set(q,'-1');
await click(()=>Array.from(form.querySelectorAll('button,input[type=submit]')).find(e=>e.type==='submit')||form.querySelector('button'));return true;
""")
            client.wait('(()=>{' + HELPERS + "const f=addForm();return f&&f.innerText!==" + json.dumps(before) + "&&/required|enter|invalid|must|cannot|positive|at least/i.test(f.innerText)})()")
            return 'invalid submission displays inline text inside add form'
        oracle.check('UI inline validation', validation)

        def add():
            before = {r['id'] for r in oracle.items()}
            js(r"""
const form=addForm();if(!form)throw Error('Add form absent');
const n=field(/(^|\s)(item.?name|name)(\s|$)/,form);set(n,'UI test quinoa');
const fields=inputs(form);const q=fields.find(e=>/quantity|qty/.test(desc(e)));set(q,'2');
const u=fields.find(e=>/unit/.test(desc(e)));if(u)set(u,'bags');
const d=fields.find(e=>e.type==='date'||/expir/.test(desc(e)));if(d)set(d,'');
await click(()=>Array.from(form.querySelectorAll('button,input[type=submit]')).find(e=>e.type==='submit')||form.querySelector('button'));
""")
            client.wait("document.body.innerText.includes('UI test quinoa')")
            matches = [r for r in oracle.items() if r['id'] not in before and r['name'] == 'UI test quinoa']
            assert len(matches) == 1 and matches[0]['quantity'] == 2, matches
            return 'form submission creates quantity=2 row visible through API and UI'
        oracle.check('UI add form', add)

        def action(kind):
            rows = [r for r in oracle.items() if r['name'] == 'UI test quinoa']
            assert len(rows) == 1, 'UI-created row unavailable; cannot prove dependent action'
            row = rows[0]
            # Arm auto-accept only for this observed delete/consume interaction.
            client.js("window.confirm=()=>true; window.prompt=(m,d)=>d||'1'")
            locate = r"""
const itemRegion=()=>{
const leaf=Array.from(document.querySelectorAll('*')).filter(visible).filter(e=>e.children.length===0&&e.innerText==='UI test quinoa')[0];
let row=leaf?.closest('li,tr,article,[role=row],[role=listitem]')||leaf;
while(row&&row!==document.body){if(row.querySelector('button,[role=button]'))return row;row=row.parentElement;}return null;};
const controls=()=>Array.from(itemRegion()?.querySelectorAll('button,[role=button]')||[]).filter(visible);
"""
            result = js(locate + r"""
const b=await click(()=>controls().find(e=>REPLACE.test(desc(e))));
return {control:desc(b),row:itemRegion()?.innerText.slice(0,250)};
""".replace('REPLACE', '/consume|use|eat|−|minus/i' if kind == 'consume' else '/delete|remove|trash/i'))
            confirmed = False
            deadline = time.monotonic() + 5
            while time.monotonic() < deadline:
                stored = [r for r in oracle.items() if r['id'] == row['id']]
                if (kind == 'delete' and not stored) or (kind == 'consume' and stored and stored[0]['quantity'] == row['quantity'] - 1):
                    return result
                if kind == 'delete' and not confirmed:
                    confirmation = js(locate + r"""
const confirm=()=>controls().find(e=>/\b(yes|confirm)\b/i.test(desc(e))&&!/\b(cancel|no)\b/i.test(desc(e)));
if(!confirm())return null;const b=await click(confirm);return {control:desc(b),row:itemRegion()?.innerText.slice(0,250)};
""")
                    if confirmation:
                        result['confirmation'] = confirmation
                        confirmed = True
                time.sleep(.1)
            raise AssertionError('UI action did not change API data as expected')
        oracle.check('UI consume action', lambda: action('consume'))
        oracle.check('UI delete action', lambda: action('delete'))

        def focus():
            client.js('document.activeElement.blur()')
            found = []
            count = js("return Array.from(document.querySelectorAll('a[href],button,input,select,textarea,[tabindex],[contenteditable=true]')).filter(e=>visible(e)&&e.tabIndex>=0&&!e.matches(':disabled')&&!e.closest('[inert]')).length;")
            # Native controls can expose several internal Tab stops per element.
            for _ in range(count * 4 + 1):
                client.call('Input.dispatchKeyEvent', {'type': 'keyDown', 'key': 'Tab', 'code': 'Tab', 'windowsVirtualKeyCode': 9})
                client.call('Input.dispatchKeyEvent', {'type': 'keyUp', 'key': 'Tab', 'code': 'Tab', 'windowsVirtualKeyCode': 9})
                result = js("const e=document.activeElement;const s=getComputedStyle(e);return {tag:e.tagName,description:desc(e).slice(0,100),expiry:e===inputs(addForm()||document).find(e=>e.type==='date'||/expir/.test(desc(e))),focusVisible:e.matches(':focus-visible'),outline:s.outlineStyle,width:s.outlineWidth,shadow:s.boxShadow};")
                if result['tag'] not in ('BODY', 'HTML'):
                    found.append(result)
                    if result['expiry']:
                        break
            assert found and found[-1]['expiry'], {'error': 'Tab never reached the expiry input', 'focusable_elements': count, 'visited': found}
            for result in found:
                assert result['focusVisible'] and ((result['outline'] not in ('none', 'hidden') and float(result['width'].replace('px', '')) > 0) or result['shadow'] != 'none'), result
            return found
        oracle.check('UI visible keyboard focus', focus)
        # Automated geometry cannot certify taste or every foreground/background pair.
        oracle.record('UI readable contrast and calm design', 'unverified', 'screenshots saved for blind visual review; no subjective design pass inferred')
        oracle.check('UI healthy interactions console', lambda: assert_no_errors(client))
        oracle.check('UI runtime stays local', lambda: assert_local(client))

        def empty():
            for row in oracle.items():
                oracle.expect('DELETE', f'/api/items/{row["id"]}', (200, 204))
            client.call('Page.navigate', {'url': oracle.base + '/'})
            client.wait("document.readyState==='complete'&&/empty|no items|nothing|add your first|pantry is clear/i.test(document.body.innerText)")
            return js('return text().slice(0,900);')
        oracle.check('UI empty state', empty)

        def api_error():
            before = js('return text();')
            client.call('Network.setBlockedURLs', {'urls': ['*/api/*']})
            client.call('Page.navigate', {'url': oracle.base + '/'})
            client.wait("document.readyState==='complete'&&document.body.innerText.split('\\n').some(line=>!" +
                        json.dumps(before.splitlines()) + ".includes(line)&&/error|fail|unable|could ?n[o'’]t|can ?n[o'’]t|try again|retry|unavailable|offline/i.test(line))")
            return {'fault': 'browser blocks API requests', 'visible_text': js('return text().slice(0,900);'),
                    'expected_fault_console_errors': len(client.errors)}
        oracle.check('UI API-error state', api_error)
    except Exception as exc:
        oracle.record('UI browser setup or continuation', 'fail', f'{type(exc).__name__}: {exc}')
        completed = {c['check'] for c in oracle.checks}
        for name in names:
            if 'UI ' + name not in completed:
                oracle.record('UI ' + name, 'unverified', 'browser setup/continuation failed')
    finally:
        if client:
            try:
                client.call('Browser.close')
            except (OSError, ConnectionError, RuntimeError):
                pass
            client.close()
        if browser:
            try:
                browser.wait(timeout=5)
            except subprocess.TimeoutExpired:
                if os.name == 'nt':
                    subprocess.run(['taskkill', '/PID', str(browser.pid), '/T', '/F'],
                                   stdout=log, stderr=log, timeout=10)
                else:
                    browser.kill()
                browser.wait(timeout=5)
        if log:
            log.close()


def assert_no_errors(client):
    client.js('true')  # drain queued protocol events
    assert not client.errors, str(client.errors)[:1200]
    return 'zero console errors and uncaught exceptions before intentional API failure'


def assert_local(client):
    client.js('true')
    assert not client.external_requests, client.external_requests
    return 'observed browser HTTP/WebSocket requests stay on loopback'
