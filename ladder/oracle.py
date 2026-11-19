"""Brief-owned black-box HTTP/UI oracles. No contender source inspection."""
import argparse
import concurrent.futures
import csv
import http.client
import importlib.util
import io
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import threading
import time
import uuid

HERE = Path(__file__).resolve().parent


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def require(condition, message):
    if not condition:
        raise AssertionError(message)


class Oracle:
    def __init__(self, product, evidence, case):
        self.product, self.evidence, self.case = product, evidence, case
        self.checks, self.process, self.log = [], None, None
        self.data = evidence / ('store.json' if case == 'notes' else 'data.sqlite3')
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', 0))
            self.port = sock.getsockname()[1]

    def check(self, name, operation):
        try:
            value = operation()
            self.checks.append(dict(name=name, status='pass', evidence=value))
            return True
        except (AssertionError, OSError, ValueError, KeyError, IndexError, ArithmeticError, TypeError, RuntimeError,
                subprocess.SubprocessError) as exc:
            self.checks.append(dict(name=name, status='fail', evidence=f'{type(exc).__name__}: {exc}'))
            return False

    def request(self, method, path, payload=None, raw=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.port, timeout=8)
        try:
            body = raw if raw is not None else (json.dumps(payload) if payload is not None else None)
            connection.request(method, path, body, {'Content-Type': 'application/json'})
            response = connection.getresponse()
            content = response.read().decode('utf-8')
            try:
                content = json.loads(content)
            except ValueError:
                pass
            return response.status, content
        finally:
            connection.close()

    def expect(self, method, path, code, payload=None, raw=None):
        actual, body = self.request(method, path, payload, raw)
        require(actual == code, f'{method} {path}: expected {code}, got {actual}: {body}')
        if code == 400:
            require(isinstance(body, dict) and isinstance(body.get('error'), str) and body['error'],
                    f'400 must contain nonempty JSON error: {body}')
        return body

    def start(self):
        command = [sys.executable, '-I', str(self.product / 'server.py'), '--port', str(self.port)]
        if self.case != 'counter':
            command += ['--store' if self.case == 'notes' else '--db', str(self.data)]
        self.log = (self.evidence / 'server.log').open('ab')
        env = {k: v for k, v in os.environ.items() if k not in ('PYTHONPATH', 'PYTHONHOME', 'SELDON_INIT')}
        self.process = subprocess.Popen(command, cwd=self.product, stdout=self.log, stderr=self.log, env=env)
        deadline = time.monotonic() + 12
        while time.monotonic() < deadline:
            if self.process.poll() is not None:
                raise RuntimeError(f'server exited {self.process.returncode}; see server.log')
            try:
                self.request('GET', '/api/absent')
                return dict(command=command, port=self.port)
            except OSError:
                time.sleep(.1)
        raise TimeoutError('Server startup exceeded 12 seconds')

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=5)
        if self.log:
            self.log.close()
        self.process, self.log = None, None

    def restart(self, path):
        before = self.expect('GET', path, 200)
        self.stop()
        self.start()
        require(self.expect('GET', path, 200) == before, 'Stored data changed after restart')
        return before

    def parallel(self, count, operation):
        barrier = threading.Barrier(count)
        def job(index):
            barrier.wait(timeout=10)
            return operation(index)
        with concurrent.futures.ThreadPoolExecutor(max_workers=count) as pool:
            return list(pool.map(job, range(count)))

    def notes(self):
        require(self.expect('GET', '/api/notes', 200) == [], 'Fresh store is not empty')
        note = self.expect('POST', '/api/notes', 201, {'text': 'Rice, beans'})
        require(type(note['id']) is int and note['text'] == 'Rice, beans', str(note))
        other = self.expect('POST', '/api/notes', 201, {'text': 'Second'})
        require(note['id'] != other['id'], 'Duplicate IDs')
        require(self.expect('GET', f'/api/notes/{note["id"]}', 200) == note, 'Readback mismatch')
        before = self.expect('GET', '/api/notes', 200)
        for payload in ({}, {'text': ''}, {'text': 1}, {'text': 'x' * 201}):
            self.expect('POST', '/api/notes', 400, payload)
        self.expect('POST', '/api/notes', 400, raw='{broken')
        require(self.expect('GET', '/api/notes', 200) == before, 'Invalid write mutated store')
        self.restart('/api/notes')
        self.expect('DELETE', f'/api/notes/{note["id"]}', 204)
        self.expect('GET', f'/api/notes/{note["id"]}', 404)
        require(self.expect('GET', '/api/notes', 200) == [other], 'Delete readback failed')
        self.expect('DELETE', '/api/notes/99999999', 404)
        self.restart('/api/notes')
        return 'create/read/delete; unique IDs; invalid JSON/text rejected without writes; file persistence'

    def counter(self):
        require(self.expect('GET', '/api/counter', 200) == {'value': 0}, 'Initial counter differs')
        for payload in ({}, {'amount': 0}, {'amount': -1}, {'amount': True}, {'amount': 1.5}):
            self.expect('POST', '/api/increment', 400, payload)
        self.expect('POST', '/api/increment', 400, raw='{broken')
        require(self.expect('GET', '/api/counter', 200) == {'value': 0}, 'Invalid increment mutated counter')
        results = self.parallel(40, lambda _: self.request('POST', '/api/increment', {'amount': 1}))
        require(all(code == 200 for code, _ in results), str(results))
        require(sorted(body['value'] for _, body in results) == list(range(1, 41)),
                'Concurrent replies must each report a distinct committed increment')
        require(self.expect('GET', '/api/counter', 200) == {'value': 40}, 'Lost concurrent increments')
        require(self.expect('POST', '/api/increment', 200, {'amount': 7}) == {'value': 47}, 'Amount ignored')
        self.expect('GET', '/api/absent', 404)
        return {'simultaneous_increments': 40, 'final_value': 47}

    def kanban(self):
        require(self.expect('GET', '/api/tasks', 200) == [], 'Fresh database is not empty')
        task = self.expect('POST', '/api/tasks', 201, {'title': 'Rice, "beans"'})
        require(type(task['id']) is int and task['status'] == 'todo' and task['title'] == 'Rice, "beans"', str(task))
        updated = self.expect('PATCH', f'/api/tasks/{task["id"]}', 200, {'status': 'doing'})
        require(updated['id'] == task['id'] and updated['status'] == 'doing', str(updated))
        before = self.expect('GET', '/api/tasks', 200)
        self.expect('POST', '/api/tasks', 400, {'title': ''})
        self.expect('POST', '/api/tasks', 400, {'title': 'x' * 81})
        self.expect('PATCH', f'/api/tasks/{task["id"]}', 400, {'status': 'invalid'})
        self.expect('POST', '/api/tasks', 400, raw='{broken')
        require(self.expect('GET', '/api/tasks', 200) == before, 'Invalid task mutation changed data')
        exported = self.expect('GET', '/api/export.csv', 200)
        rows = list(csv.DictReader(io.StringIO(exported)))
        require(rows == [dict(id=str(task['id']), title=task['title'], status='doing')], str(rows))
        self.restart('/api/tasks')
        self.expect('PATCH', '/api/tasks/99999999', 404, {'status': 'done'})
        self.expect('DELETE', f'/api/tasks/{task["id"]}', 204)
        require(self.expect('GET', '/api/tasks', 200) == [], 'Delete did not persist')
        self.expect('DELETE', f'/api/tasks/{task["id"]}', 404)
        return 'SQLite CRUD, validation, quoted CSV export, persistence and 404'

    def booking(self):
        require(self.expect('GET', '/api/slots', 200) == [], 'Fresh database is not empty')
        first = self.expect('POST', '/api/slots', 201, {'start': '2030-01-02T10:00', 'end': '2030-01-02T11:00'})
        require(type(first['id']) is int and first['booked_by'] is None, str(first))
        second = self.expect('POST', '/api/slots', 201, {'start': '2030-01-02T11:00', 'end': '2030-01-02T12:00'})
        require(first['id'] != second['id'], 'Duplicate IDs')
        self.expect('POST', '/api/slots', 409, {'start': '2030-01-02T10:30', 'end': '2030-01-02T11:30'})
        before = self.expect('GET', '/api/slots', 200)
        self.expect('POST', '/api/slots', 400, {'start': 'bad', 'end': 'bad'})
        self.expect('POST', '/api/slots', 400, {'start': '2030-01-02T12:00', 'end': '2030-01-02T11:00'})
        self.expect('POST', '/api/slots', 400, raw='{broken')
        self.expect('POST', f'/api/slots/{first["id"]}/book', 400, {'name': ''})
        require(self.expect('GET', '/api/slots', 200) == before, 'Invalid slot request changed data')
        results = self.parallel(2, lambda i: self.request('POST', f'/api/slots/{first["id"]}/book', {'name': f'Guest {i}'}))
        require(sorted(code for code, _ in results) == [200, 409], str(results))
        winner = next(body for code, body in results if code == 200)
        require(winner['booked_by'] in ('Guest 0', 'Guest 1'), str(winner))
        saved = next(row for row in self.expect('GET', '/api/slots', 200) if row['id'] == first['id'])
        require(saved['booked_by'] == winner['booked_by'], 'Winning booking lost')
        self.expect('POST', f'/api/slots/{first["id"]}/book', 409, {'name': 'Later'})
        self.expect('POST', '/api/slots/99999999/book', 404, {'name': 'Missing'})
        self.restart('/api/slots')
        return 'adjacent slots, overlapping rejection, atomic booking conflict, persistence'

    def importer(self):
        path = self.evidence / 'import.csv'
        if self.case == 'kanban':
            script, endpoint = 'import_tasks.py', '/api/tasks'
            rows = [['title', 'status'], ['Imported task', 'todo'], ['', 'todo'], ['Invalid', 'broken']]
        else:
            script, endpoint = 'import_slots.py', '/api/slots'
            rows = [['start', 'end'], ['2030-01-03T10:00', '2030-01-03T11:00'], ['bad', 'bad'],
                    ['2030-01-03T10:30', '2030-01-03T11:30']]
        with path.open('w', encoding='utf-8', newline='') as stream:
            csv.writer(stream).writerows(rows)
        before = self.expect('GET', endpoint, 200)
        self.stop()
        try:
            command = [sys.executable, '-I', str(self.product / script), str(path), '--db', str(self.data)]
            result = subprocess.run(command, cwd=self.product, capture_output=True, text=True, timeout=12)
            require(result.returncode == 0 and result.stdout.strip() == 'imported 1, skipped 2',
                    f'{result.returncode}: {result.stdout} {result.stderr}')
            command[3] = str(self.evidence / 'missing.csv')
            missing = subprocess.run(command, cwd=self.product, capture_output=True, text=True, timeout=12)
            require(missing.returncode == 2 and bool((missing.stdout + missing.stderr).strip()), 'Unreadable CSV must exit 2')
        finally:
            self.start()
        after = self.expect('GET', endpoint, 200)
        require(len(after) == len(before) + 1, 'Imported row missing from canonical API')
        if self.case == 'kanban':
            require(any(row['title'] == 'Imported task' and row['status'] == 'todo' for row in after), str(after))
        else:
            require(any(row['start'].startswith('2030-01-03T10:00') for row in after), str(after))
        return 'valid CSV imported into server SQLite; invalid rows skipped; missing input exits 2'

    def ui(self):
        verify = module(HERE.parent / 'run-farm' / 'verify.py', 'ladder_browser')
        executable = verify.chromium()
        if executable is None:
            self.checks.append(dict(name='browser-availability', status='unverified', evidence='Chromium cache missing'))
            return
        browser, cdp = None, None
        try:
            profile = self.evidence / 'browser-profile'
            with (self.evidence / 'browser.log').open('wb') as log:
                browser = subprocess.Popen([str(executable), '--headless', '--disable-gpu', '--no-first-run',
                                            '--no-default-browser-check', '--disable-background-networking',
                                            '--remote-debugging-port=0', f'--user-data-dir={profile}', 'about:blank'],
                                           stdout=log, stderr=log)
            deadline = time.monotonic() + 12
            while not (profile / 'DevToolsActivePort').exists() and time.monotonic() < deadline:
                time.sleep(.05)
            port = int((profile / 'DevToolsActivePort').read_text().splitlines()[0])
            connection = http.client.HTTPConnection('127.0.0.1', port, timeout=8)
            try:
                connection.request('GET', '/json')
                targets = json.loads(connection.getresponse().read())
            finally:
                connection.close()
            cdp = verify.CDP(next(t['webSocketDebuggerUrl'] for t in targets if t['type'] == 'page'))
            cdp.call('Page.enable')
            cdp.call('Runtime.enable')
            cdp.call('Emulation.setDeviceMetricsOverride', width=375, height=812, deviceScaleFactor=1, mobile=True)
            cdp.call('Page.navigate', url=f'http://127.0.0.1:{self.port}/')
            deadline = time.monotonic() + 8
            while time.monotonic() < deadline:
                if cdp.evaluate("document.readyState === 'complete' && !!document.body && document.body.innerText.length > 10"):
                    break
                time.sleep(.1)
            require(cdp.evaluate('document.documentElement.scrollWidth <= innerWidth'), 'Mobile horizontal overflow')
            cdp.key('Tab')
            require(cdp.evaluate("document.activeElement !== document.body && (getComputedStyle(document.activeElement).outlineStyle !== 'none' || getComputedStyle(document.activeElement).boxShadow !== 'none')"), 'Keyboard focus not visible')
            if self.case == 'kanban':
                require(cdp.evaluate("!!document.querySelector('a[href=\"/api/export.csv\"]')"), 'CSV export link missing')
                require(cdp.evaluate("(() => {let f=document.querySelector('form#task-form'), i=f?.querySelector('[name=title]');if(!i)return false;i.value='UI task';i.dispatchEvent(new Event('input',{bubbles:true}));f.requestSubmit();return true})()"), 'Task form missing')
                def created():
                    return next((r for r in self.expect('GET', '/api/tasks', 200) if r['title'] == 'UI task'), None)
                task = self.poll(created)
                selector = f'[data-task-id="{task["id"]}"]'
                self.poll(lambda: cdp.evaluate(f'!!document.querySelector({json.dumps(selector)})'))
                require(cdp.evaluate(f"(() => {{let b=document.querySelector({json.dumps(selector + ' button[data-action=advance]')});if(!b)return false;b.click();return true}})()"), 'Advance action missing')
                self.poll(lambda: any(r['id'] == task['id'] and r['status'] == 'doing' for r in self.expect('GET', '/api/tasks', 200)))
                require(cdp.evaluate(f"(() => {{let b=document.querySelector({json.dumps(selector + ' button[data-action=delete]')});if(!b)return false;b.click();return true}})()"), 'Delete action missing')
                self.poll(lambda: all(r['id'] != task['id'] for r in self.expect('GET', '/api/tasks', 200)))
            else:
                slot = next(r for r in self.expect('GET', '/api/slots', 200) if r['booked_by'] is None)
                selector = f'[data-slot-id="{slot["id"]}"]'
                self.poll(lambda: cdp.evaluate(f'!!document.querySelector({json.dumps(selector)})'))
                expression = f"(() => {{let e=document.querySelector({json.dumps(selector)}),i=e?.querySelector('[name=name]'),b=e?.querySelector('button[data-action=book]');if(!i||!b)return false;i.value='UI guest';i.dispatchEvent(new Event('input',{{bubbles:true}}));b.click();return true}})()"
                require(cdp.evaluate(expression), 'Booking controls missing')
                self.poll(lambda: any(r['id'] == slot['id'] and r['booked_by'] == 'UI guest' for r in self.expect('GET', '/api/slots', 200)))
                self.poll(lambda: cdp.evaluate("document.body.innerText.includes('UI guest')"))
            require(not cdp.errors, str(cdp.errors))
            screenshot = self.evidence / 'mobile.png'
            import base64
            screenshot.write_bytes(base64.b64decode(cdp.call('Page.captureScreenshot', format='png')['data']))
            return '375px UI actions persisted through real API; visible keyboard focus; mobile.png'
        finally:
            if cdp:
                cdp.close()
            if browser and browser.poll() is None:
                browser.terminate()
                try:
                    browser.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    browser.kill()
                    browser.wait(timeout=5)

    def poll(self, operation):
        deadline = time.monotonic() + 8
        while time.monotonic() < deadline:
            value = operation()
            if value:
                return value
            time.sleep(.1)
        raise AssertionError('UI/API condition did not become true within 8 seconds')

    def run(self):
        try:
            if self.check('server startup on free loopback port', self.start):
                self.check('README delivered', lambda: require((self.product / 'README.md').is_file(), 'README missing'))
                if self.check(self.case + ' API contract', getattr(self, self.case)) and self.case in ('kanban', 'booking'):
                    self.check('CSV producer -> SQLite -> server API', self.importer)
                    self.check('UI -> API -> storage at 375px', self.ui)
        finally:
            self.stop()
        return dict(checks=self.checks, totals={status: sum(c['status'] == status for c in self.checks)
                                              for status in ('pass', 'fail', 'unverified')})


def shelflife(product, evidence):
    # Reuse the original oracle, including its UI checks; redirect only its owned outputs.
    fight = HERE.parent / 'fight-1'
    sys.path.insert(0, str(fight))
    oracle = module(fight / 'oracle.py', 'fight_oracle')
    oracle.HERE = evidence
    oracle.TESTS = evidence / 'isolated-products'
    return oracle.Oracle(product, 'ladder-' + uuid.uuid4().hex[:12]).run()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('product', type=Path)
    parser.add_argument('evidence', type=Path)
    parser.add_argument('case', choices=['notes', 'counter', 'kanban', 'booking', 'shelflife', 'quietbench'])
    args = parser.parse_args()
    args.evidence.mkdir(parents=True, exist_ok=True)
    from quietbench_oracle import quietbench
    result = (quietbench(args.product, args.evidence) if args.case == 'quietbench' else
              shelflife(args.product, args.evidence) if args.case == 'shelflife'
              else Oracle(args.product, args.evidence, args.case).run())
    (args.evidence / 'oracle.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
