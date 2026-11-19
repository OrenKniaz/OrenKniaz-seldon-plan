"""Quiet Bench black-box fight. The public interface is in the shared brief."""
import cmath
import csv
import io
import json
import math
import random
import re
import struct
import subprocess
import sys
import wave
from copy import deepcopy
from pathlib import Path


class Unverified(RuntimeError):
    pass


def quietbench(product, evidence):
    # Imported by the ladder oracle so ordinary cases keep their original owner.
    from oracle import Oracle, require

    class Bench(Oracle):
        def __init__(self):
            super().__init__(product, evidence, 'quietbench')
            self.data = evidence / 'sessions'
            self.saved = []

        def check(self, name, operation):
            def record():
                try:
                    return operation()
                except Unverified as exc:
                    return exc

            passed = super().check(name, record)
            if passed and isinstance(self.checks[-1]['evidence'], Unverified):
                self.checks[-1].update(status='unverified', evidence=str(self.checks[-1]['evidence']))
                return False
            return passed

        def success(self, method, path, payload=None):
            status, body = self.request(method, path, payload)
            require(200 <= status < 300,
                    f'{method} {path}: HTTP {status}: {str(body)[:400]}')
            return body

        def start(self):
            # Reuse the existing bounded server lifecycle, with the dream's --data spelling.
            return self.start_bench()

        def start_bench(self):
            import os
            import time
            self.log = (evidence / 'server.log').open('ab')
            env = {k: v for k, v in os.environ.items() if k not in ('PYTHONPATH', 'PYTHONHOME')}
            cmd = [sys.executable, '-B', '-E', '-s', str(product / 'server.py'), '--port', str(self.port),
                   '--data', str(self.data)]
            self.process = subprocess.Popen(cmd, cwd=product, env=env, stdout=self.log, stderr=self.log)
            deadline = time.monotonic() + 12
            while time.monotonic() < deadline:
                require(self.process.poll() is None, 'server exited; see server.log')
                try:
                    self.request('GET', '/')
                    return cmd
                except OSError:
                    time.sleep(.1)
            raise RuntimeError('server did not start')

        def cli_result(self, *args):
            return subprocess.run([sys.executable, '-B', '-E', '-s', str(product / 'bench.py'), *args,
                                     '--data', str(self.data)], cwd=product, capture_output=True,
                                    text=True, timeout=30)

        def cli(self, *args, json_output=True):
            result = self.cli_result(*args)
            require(result.returncode == 0, result.stdout + result.stderr)
            return json.loads(result.stdout) if json_output else result.stdout

        def session(self, id):
            return self.success('GET', '/api/sessions/' + str(id))

        def complete(self, session):
            return self.poll(lambda: (s if (s := self.session(session['id']))
                                     ['status'] in ('completed', 'stopped') else None))

        def run_cli(self, settings):
            return self.cli('run', '--settings', json.dumps(settings))

        def end_to_end(self):
            s = self.run_cli(settings)
            require(self.cli('show', s['id']) == s, 'CLI run/show differ')
            self.saved.append(s)
            require(self.session(s['id']) == s, 'API/CLI differ')
            require(s['id'] in self.session_ids(self.cli('list')), 'CLI list lost session')
            other = self.complete(self.success('POST', '/api/runs', settings))
            require(other['id'] != s['id'], 'creation reused a saved ID')
            self.saved.append(other)
            require(s['status'] == other['status'] == 'completed', 'uninterrupted run did not complete')
            require(close_bands(band_values(other['bands']), band_values(s['bands'])),
                    'API and CLI band numbers differ on identical settings')
            return {'cli': s['id'], 'api': other['id'], 'bands': s['bands']}

        @staticmethod
        def session_ids(rows):
            require(isinstance(rows, list), 'session list must be an array')
            return {row['id'] if isinstance(row, dict) else row for row in rows}

        def fixed(self):
            args = {**settings, 'filter': 'fixed', 'signal': {**settings['signal'], 'frequencies': [500]}}
            # The dream requires a fixed example but leaves its coefficient setting to the guide.
            guide = self.guide_text()
            example = re.search(r'"filter"\s*:\s*"fixed"\s*,\s*"([^"\n]+)"\s*:\s*(\[[^\n\]]+\])', guide)
            if example:
                key, taps = example.groups()
                args[key] = json.loads(taps)
            result = self.cli_result('run', '--settings', json.dumps(args))
            if result.returncode and not example:
                raise Unverified('Fixed-filter input is unspecified and the guide supplied no usable coefficient example')
            require(result.returncode == 0, result.stdout + result.stderr)
            s = json.loads(result.stdout)
            require(s['status'] == 'completed' and s['bands'] and s['output'], 'wave-1 fixed run missing')
            require(self.session(s['id']) == s, 'fixed run was not saved and shown')
            self.saved.append(s)
            return s['id']

        def numbers(self):
            rng = random.Random(918731)
            rows = []
            for kind in ('tones', 'band-noise'):
                signal = ([.15 * math.sin(2 * math.pi * 437 * n / 8000)
                           + .13 * math.sin(2 * math.pi * 1733 * n / 8000) for n in range(8192)]
                          if kind == 'tones' else [rng.uniform(-.2, .2) for _ in range(8192)])
                # Own hidden WAV, not the contender's generator or claimed metrics.
                path = evidence / (kind + '.wav')
                with wave.open(str(path), 'wb') as out:
                    out.setparams((1, 2, 8000, 0, 'NONE', 'not compressed'))
                    out.writeframes(b''.join(struct.pack('<h', round(v * 32767)) for v in signal))
                signal = [round(v * 32767) / 32768 for v in signal]
                taps = [rng.uniform(.35, .48), 0, rng.uniform(.32, .46)]
                args = {**settings, 'signal': {'kind': 'wav', 'path': str(path)}, 'path': taps}
                adaptive = self.run_cli(args)
                desired = fir(signal, taps)
                fixed = [d - f for d, f in zip(desired, fir(signal, settings['path']), strict=True)]
                e, output = adaptive['residual'], adaptive['output']
                require(adaptive['status'] == 'completed' and adaptive['processed_samples'] == len(signal),
                        'hidden WAV did not complete')
                require(all(len(adaptive[k]) == len(signal) for k in ('desired', 'residual', 'output')),
                        'sample arrays do not match imported length')
                require(all(math.isclose(a, b, abs_tol=.001) for a, b in zip(desired, adaptive['desired'])),
                        'simulated path does not match imported samples and path')
                require(any(all(math.isclose(d + sign*y, r, abs_tol=.001) for d, y, r in
                                zip(adaptive['desired'], output, e)) for sign in (-1, 1)),
                        'residual does not agree with desired and anti-noise samples')
                reported = band_values(adaptive['bands'])
                require(reported.keys() == {tuple(b) for b in settings['bands']}, 'requested bands missing')
                powers = [spectrum(x) for x in (adaptive['desired'], e, fixed)]
                measured = []
                for (lo, hi), claimed in reported.items():
                    start, end = math.ceil(lo * 8192 / 8000), math.ceil(hi * 8192 / 8000)
                    for edge in ({end, end + 1} if hi == 4000 else (end,)):
                        before, after, baseline = [sum(abs(x)**2 for x in p[start:edge]) for p in powers]
                        db = 10 * math.log10(before / max(1e-30, after))
                        if abs(db - claimed) < 1.5 and after < min(before, baseline):
                            break
                    else:
                        raise AssertionError(f'{kind} {lo}–{hi} Hz: measured {db:.3f} dB, reported {claimed}, or no improvement over fixed')
                    measured.append({'low': lo, 'high': hi, 'measured_db': db, 'reported_db': claimed})
                require(sum(v*v for v in e[-2048:]) < sum(v*v for v in e[:2048]), 'residual did not fall')
                rows.append({'signal': kind, 'bands': measured})
            return rows

        def safety(self):
            limit = .01
            s = self.run_cli({**settings, 'limit': limit})
            require(s['status'] == 'completed' and len(s['output']) == settings['samples'],
                    'limiter run did not return the full output')
            require(s['limited'] is True and all(math.isfinite(v) and abs(v) <= limit + 1e-9 for v in s['output']),
                    'limiter did not hold the configured level')
            return s['id']

        def divergence(self):
            # A large admissible step and a strong correlated input can make LMS unstable.
            # Compare the counterfactual at a wider cap so ordinary clipping is not called divergence.
            signal = {**settings['signal'], 'frequencies': [500], 'amplitude': .95}
            for step in (2.0, 1.0, .5):
                args = {**settings, 'signal': signal, 'step_size': step}
                result = self.cli_result('run', '--settings', json.dumps(args))
                if result.returncode:
                    continue
                wide = json.loads(result.stdout)
                residual = wide['residual']
                if (len(residual) != settings['samples'] or sum(v*v for v in residual[-2048:]) <=
                        max(sum(v*v for v in wide['desired'][-2048:]), sum(v*v for v in residual[:2048]))):
                    continue
                s = self.run_cli({**args, 'limit': .1})
                require(s['status'] == 'completed' and len(s['output']) == settings['samples'],
                        'divergence stress run did not return the full output')
                require(s['limited'] is True and all(math.isfinite(v) and abs(v) <= .1 + 1e-9 for v in s['output']),
                        'limiter did not hold under unstable settings')
                return {'id': s['id'], 'step_size': step}
            raise Unverified('No accepted stress settings demonstrated unstable cancellation; the interface specifies no divergence trigger')

        def stop_run(self):
            for samples in (8192, 32768, 131072):
                status, run = self.request('POST', '/api/runs', {**settings, 'samples': samples})
                if samples != settings['samples'] and 400 <= status < 500:
                    continue  # The interface does not declare a maximum run length.
                require(200 <= status < 300, f'stop probe creation returned HTTP {status}')
                if run['status'] == 'completed':
                    continue
                require(run['status'] == 'running', 'new run did not begin in running state')
                status, ack = self.request('POST', f'/api/runs/{run["id"]}/stop')
                try:
                    final = self.complete(run)
                except AssertionError as exc:
                    current = self.session(run['id'])
                    raise AssertionError(f'Stop returned HTTP {status} for {samples} samples, but session remained '
                                         f'{current["status"]} at {current["processed_samples"]} samples') from exc
                if final['status'] == 'completed':
                    require(final['processed_samples'] == samples, 'stop left a partial run marked completed')
                    continue
                require(200 <= status < 300, f'stop returned HTTP {status}')
                require(final['status'] == 'stopped' and 0 <= final['processed_samples'] <= samples,
                        f'Stop saved invalid sample count {final["processed_samples"]} for a {samples}-sample run')
                if final['processed_samples'] == samples:
                    continue
                cursor = run['processed_samples']
                require(final['processed_samples'] >= cursor, 'stopped cursor moved backward')
                if isinstance(ack, dict) and ack.get('status') == 'running' and 'processed_samples' in ack:
                    cursor = ack['processed_samples']
                    require(0 <= final['processed_samples'] - cursor <= settings['block_size'],
                            'stop exceeded one block after acknowledgement')
                elif final['processed_samples'] - cursor > settings['block_size']:
                    raise Unverified(f'Run stopped at {final["processed_samples"]} samples after creation at {cursor}; '
                                     'no in-flight stop cursor bounds processing to one block')
                return {'id': final['id'], 'cursor': cursor, 'processed': final['processed_samples']}
            raise Unverified('No in-flight run was observable within the bounded probe; the interface specifies no minimum run time')

        def storage(self):
            require(self.saved, 'no canonical sessions for restart')
            before = [self.session(s['id']) for s in self.saved]
            require(before == self.saved, 'saved sessions changed before restart')
            self.stop()
            self.start()
            after = [self.session(s['id']) for s in self.saved]
            require(before == after == [self.cli('show', s['id']) for s in after], 'restart changed saved values')
            return [s['id'] for s in after]

        def legacy(self):
            import shutil
            original = self.data
            expected = json.loads((evidence/'wave1-sessions.json').read_text('utf-8'))
            require(bool(expected), 'wave-1 snapshot must contain a real saved session')
            legacy = evidence/'legacy-readback'
            shutil.copytree(evidence/'wave1-data',legacy)
            self.stop()
            self.data = legacy
            try:
                self.start()
                for old in expected:
                    actual = self.session(old['id'])
                    require(all(actual.get(k)==v for k,v in old.items()), 'wave-1 saved values changed')
                return [s['id'] for s in expected]
            finally:
                self.stop()
                self.data = original
                self.start()

        def export_import(self):
            require(bool(self.saved), "no saved session to export")
            s = self.saved[0]
            exported = self.cli('export', s['id'], json_output=False)
            reader = csv.DictReader(io.StringIO(exported))
            rows = list(reader)
            require(rows and all(None not in row and None not in row.values() for row in rows),
                    'CSV has no data or has inconsistent row widths')
            aliases = {
                'low': ('low', 'low_hz', 'lower', 'lower_hz', 'band_low', 'band_low_hz'),
                'high': ('high', 'high_hz', 'upper', 'upper_hz', 'band_high', 'band_high_hz'),
                'attenuation_db': ('attenuation_db', 'attenuation', 'reduction_db'),
                'desired': ('desired', 'desired_sample', 'before', 'before_cancellation', 'primary'),
                'residual': ('residual', 'residual_sample', 'error', 'after', 'after_cancellation'),
                'output': ('output', 'output_sample', 'anti_noise', 'antinoise', 'limited_anti_noise'),
            }
            headers = {re.sub(r'\W+', '_', h.casefold()).strip('_'): h for h in reader.fieldnames}
            columns = {key: next((headers[name] for name in names if name in headers), None)
                       for key, names in aliases.items()}
            if all(columns[key] for key in ('low', 'high', 'attenuation_db')):
                bands = [{key: float(row[columns[key]]) for key in ('low', 'high', 'attenuation_db')}
                         for row in rows]
                require(close_bands(band_values(bands), band_values(s['bands'])), 'CSV differs from saved bands')
                layout = 'bands'
            elif all(columns[key] for key in ('desired', 'residual', 'output')):
                for key in ('desired', 'residual', 'output'):
                    require(len(rows) == len(s[key]) and all(math.isclose(float(row[columns[key]]), value,
                             rel_tol=1e-6, abs_tol=1e-6) for row, value in zip(rows, s[key])),
                            f'CSV {key} samples differ from saved samples')
                layout = 'samples'
            else:
                layout = None
            before = self.session_ids(self.cli('list'))
            bad = evidence / 'bad.wav'
            bad.write_bytes(b'not a wave file')
            result = self.cli_result('run', '--settings',
                json.dumps({**settings, 'signal': {'kind': 'wav', 'path': str(bad)}}))
            require(result.returncode != 0 and (result.stdout+result.stderr).strip(), 'bad WAV accepted silently')
            require(self.session_ids(self.cli('list')) == before, 'bad WAV saved a session')
            if layout is None:
                raise Unverified('Invalid WAV rejected without saving; CSV layout is unspecified and its columns could not be matched')
            return {'layout': layout, 'rows': len(rows), 'invalid_wav_rejected': True}

        def guide_text(self):
            path = product / 'docs/try-it.md'
            return path.read_text('utf-8') if path.is_file() else ''

        def guide(self):
            import os
            import shlex
            import shutil
            guide = self.guide_text()
            require(guide.strip(), 'docs/try-it.md is missing or empty')
            fresh = evidence/'fresh-copy'
            shutil.copytree(product, fresh, ignore=lambda _, names: [n for n in names
                if n.casefold().startswith('.env') or n in ('.git', '.seldon', '__pycache__')])
            commands = []
            for block in re.findall(r'```[^\n]*\n(.*?)```', guide, re.S):
                for line in block.splitlines():
                    line = line.strip().removeprefix('$ ').removeprefix('PS> ')
                    if not re.match(r'(?:python(?:3(?:\.12)?)?|py|node) ',line):
                        continue
                    args = [a[1:-1] if len(a)>1 and a[0]==a[-1] and a[0] in ("'",'"') else a
                            for a in shlex.split(line,posix=False)]
                    if len(args) > 1 and Path(args[1]).name in ('server.py', 'bench.py'):
                        commands.append(args)
            servers = [a for a in commands if Path(a[1]).name == 'server.py']
            if not commands or len(servers) != 1:
                raise Unverified('Guide start/CLI command format needs a manual walkthrough')
            cli = {a[2]: a for a in commands if Path(a[1]).name == 'bench.py' and len(a) > 2}
            require({'run', 'list', 'show', 'export'} <= cli.keys(), 'Guide lacks examples for run/list/show/export')
            if not re.search(r'\b(?:ctrl|control)\s*[+-]\s*c\b', guide, re.I):
                raise Unverified('Guide stop method needs a manual walkthrough')

            data = evidence/'guide-data'
            data.mkdir()
            def prepare(args, session_id=None):
                args = args.copy()
                if '>' in args:
                    offset = args.index('>')
                    if offset != len(args) - 2:
                        raise Unverified('Guide redirection needs a manual walkthrough')
                    args = args[:offset]  # Capture the documented redirect in evidence instead.
                if any(a in ('&', ';', '&&', '|', '>>') for a in args):
                    raise Unverified('Guide uses shell composition that needs a manual walkthrough')
                args[:1] = [sys.executable, '-B', '-E', '-s']
                if '--data' in args:
                    index = args.index('--data') + 1
                    value = args[index]
                    if value.startswith(('$', '<')) or value in ('DIR', 'DATA_DIR'):
                        args[index] = str(data)
                    else:
                        target = (fresh / value).resolve()
                        if not target.is_relative_to(fresh.resolve()):
                            raise Unverified('Guide data path is outside the fresh copy')
                if session_id is not None and args[5] in ('show', 'export'):
                    value = args[6]
                    if re.fullmatch(r'<?(?:session[-_ ]?)?id>?', value, re.I):
                        args[6] = str(session_id)
                if '--settings' in args:
                    value = args[args.index('--settings') + 1]
                    if not value.startswith('{'):
                        target = (fresh / value).resolve()
                        if not target.is_relative_to(fresh.resolve()) or target.name.casefold().startswith('.env'):
                            raise Unverified('Guide settings file is outside the fresh copy or unavailable for inspection')
                        if not target.exists():
                            target.write_text(json.dumps(settings), encoding='utf-8')
                return args

            server = prepare(servers[0])
            if '--port' in server and server[server.index('--port') + 1] in ('PORT', '<port>'):
                server[server.index('--port') + 1] = str(self.port)
            port = int(server[server.index('--port') + 1])
            self.stop()
            oracle_port = self.port
            self.port = port
            transcript = []
            try:
                self.log = (evidence/'guide-server.log').open('ab')
                options = {}
                if os.name == 'nt':
                    options = {'creationflags': subprocess.CREATE_NEW_CONSOLE, 'startupinfo': subprocess.STARTUPINFO(
                        dwFlags=subprocess.STARTF_USESHOWWINDOW, wShowWindow=subprocess.SW_HIDE)}
                    # An automation host may ignore console Ctrl+C and pass that setting to children.
                    # Reset it in the private console to match a server started in a user's terminal.
                    console_start = '''
import ctypes
import os
import runpy
import sys

if not ctypes.windll.kernel32.SetConsoleCtrlHandler(None, False):
    raise OSError('Could not enable Ctrl+C in the private console')
sys.argv.pop(0)
sys.path[0] = os.path.dirname(os.path.abspath(sys.argv[0]))
runpy.run_path(sys.argv[0], run_name='__main__')
'''
                    server = [sys._base_executable, *server[1:4], '-c', console_start, *server[4:]]
                self.process = subprocess.Popen(server, cwd=fresh, stdout=self.log, stderr=self.log, **options)
                def ready():
                    require(self.process.poll() is None, 'Guide server exited; see guide-server.log')
                    try:
                        return self.request('GET', '/')[0] == 200
                    except OSError:
                        return False
                self.poll(ready)
                session = None
                for operation in ('run', 'list', 'show', 'export'):
                    args = prepare(cli[operation], session and session['id'])
                    result = subprocess.run(args, cwd=fresh, capture_output=True, text=True, timeout=30)
                    require(result.returncode == 0, result.stdout + result.stderr)
                    if operation == 'run':
                        session = json.loads(result.stdout)
                        require(self.session(session['id']) == session, 'Guide CLI and server use different data')
                    elif operation == 'list':
                        require(session['id'] in self.session_ids(json.loads(result.stdout)), 'Guide list lost the run')
                    elif operation == 'show':
                        require(json.loads(result.stdout) == session, 'Guide show changed the run')
                    else:
                        require(len(list(csv.reader(io.StringIO(result.stdout)))) > 1, 'Guide export has no data')
                        (evidence/'guide-export.csv').write_text(result.stdout, encoding='utf-8')
                    transcript.append({'argv': args, 'operation': operation})
                send_ctrl_c(self.process)
                self.process.wait(timeout=8)
                try:
                    self.request('GET', '/')
                except (ConnectionError, OSError):
                    return transcript
                raise AssertionError('Guide server still responds after Ctrl+C')
            finally:
                self.stop()
                self.port = oracle_port
                self.start()

        def page(self):
            import base64
            import http.client
            import time
            from oracle import module, HERE
            verify = module(HERE.parent / 'run-farm/verify.py', 'quietbench_browser')
            executable = verify.chromium()
            if executable is None:
                raise Unverified('Browser unavailable; page unproven')
            profile = evidence / 'browser-profile'
            browser, cdp = None, None
            try:
                with (evidence / 'browser.log').open('wb') as log:
                    browser = subprocess.Popen([str(executable), '--headless', '--disable-gpu',
                        '--no-first-run', '--disable-background-networking', '--remote-debugging-port=0',
                        f'--user-data-dir={profile}', 'about:blank'], stdout=log, stderr=log)
                deadline = time.monotonic()+12
                while not (profile/'DevToolsActivePort').exists() and time.monotonic()<deadline:
                    time.sleep(.05)
                if not (profile/'DevToolsActivePort').exists():
                    raise Unverified('Browser did not expose its local debug port')
                port = int((profile/'DevToolsActivePort').read_text().splitlines()[0])
                def page_target():
                    con = http.client.HTTPConnection('127.0.0.1', port, timeout=8)
                    try:
                        con.request('GET', '/json/list')
                        targets = json.loads(con.getresponse().read())
                        return next((t['webSocketDebuggerUrl'] for t in targets if t['type'] == 'page'), None)
                    except OSError:
                        return None
                    finally:
                        con.close()
                try:
                    target = self.poll(page_target)
                except AssertionError as exc:
                    raise Unverified('Browser did not expose a page target') from exc
                cdp = verify.CDP(target)
                cdp.call('Page.enable')
                cdp.call('Runtime.enable')
                cdp.call('Page.navigate', url=f'http://127.0.0.1:{self.port}/')
                self.poll(lambda: cdp.evaluate("document.readyState === 'complete' && !!document.querySelector('textarea[name=settings]')"))
                require(cdp.evaluate("""(() => {const t = document.querySelector('textarea[name=settings]');
                    return !!(t.getAttribute('aria-label')?.trim() ||
                        t.getAttribute('aria-labelledby')?.split(/\\s+/).some(id => document.getElementById(id)?.innerText.trim()) ||
                        [...t.labels].some(label => label.innerText.trim()));})()"""), 'Settings textarea has no accessible label')
                before = self.session_ids(self.success('GET', '/api/sessions'))
                page_settings = {**settings, 'path': [.35, 0, .45]}
                value = json.dumps(json.dumps(page_settings))
                started = cdp.evaluate(f"""(() => {{const t = document.querySelector('textarea[name=settings]');
                    t.value = {value}; for (const type of ['input', 'change']) t.dispatchEvent(new Event(type, {{bubbles:true}}));
                    const button = {page_button('start run', 'run', 'start', 'run simulation', 'start simulation')};
                    if (!button) return false; button.click(); return true;}})()""")
                if not started:
                    labels = cdp.evaluate("[...document.querySelectorAll('button, [role=button], input[type=submit]')]"
                                          ".map(b => [b.innerText, b.getAttribute('aria-label'), b.value])")
                    raise AssertionError(f'Start run control missing (button labels: {labels})')
                created = self.poll(lambda: next(iter(self.session_ids(self.success('GET', '/api/sessions')) - before), None))
                actual = self.complete({'id': created})
                require(actual['status'] == 'completed', 'page run did not complete')
                reference = self.run_cli(page_settings)
                require(close_bands(band_values(actual['bands']), band_values(reference['bands'])),
                        'page and CLI results differ for the entered settings')
                cli = self.cli('show', str(actual['id']))
                require(cli == actual, 'page producer not visible through CLI')
                def visible(session):
                    text = cdp.evaluate('document.body.innerText')
                    id = str(session['id'])
                    return id in text and displays_numbers(text.replace(id, ''), band_values(session['bands']).values())
                self.poll(lambda: visible(actual))
                cdp.call('Page.reload')
                if not self.saved:
                    raise Unverified('No independent saved session for the page reload walkthrough')
                old = self.saved[0]
                selector = json.dumps('[data-session-id="'+str(old['id'])+'"]')
                self.poll(lambda: cdp.evaluate(f'!!document.querySelector({selector})'))
                cdp.evaluate(f'document.querySelector({selector}).click()')
                self.poll(lambda: visible(old))
                a, b = self.comparison_pair()
                require(cdp.evaluate(f"""(() => {{const a = document.querySelector('select[name=compare-a]');
                    const b = document.querySelector('select[name=compare-b]'); if (!a || !b) return false;
                    a.value = {json.dumps(str(a['id']))}; b.value = {json.dumps(str(b['id']))};
                    if (!a.value || !b.value) return false;
                    for (const select of [a,b]) select.dispatchEvent(new Event('change', {{bubbles:true}}));
                    const button = {page_button('compare', 'compare runs', 'compare sessions')};
                    if (!button) return false; button.click(); return true;}})()"""), 'Compare controls missing')
                expected = self.comparison(a, b)
                def compared():
                    text = cdp.evaluate("document.querySelector('[data-comparison]')?.innerText || ''")
                    return displays_numbers(text, band_values(expected, 'delta_db').values())
                self.poll(compared)
                for width in (1280,375):
                    cdp.call('Emulation.setDeviceMetricsOverride',width=width,height=812,deviceScaleFactor=1,mobile=width==375)
                    (evidence/f'page-{width}.png').write_bytes(base64.b64decode(cdp.call('Page.captureScreenshot',format='png')['data']))
                return {'pageSession':actual['id'],'reloaded':old['id'],'comparison':expected,
                        'screenshots':['page-1280.png','page-375.png']}
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

        def comparison_pair(self):
            if not self.saved:
                raise Unverified('No saved sessions available for comparison')
            a = self.saved[0]
            for b in self.saved[1:]:
                if band_values(a['bands']) != band_values(b['bands']):
                    return a, b
            b = self.run_cli({**settings, 'path': [.4, 0, .45]})
            self.saved.append(b)
            require(band_values(a['bands']) != band_values(b['bands']), 'distinct inputs produced indistinguishable bands')
            return a, b

        def comparison(self, a, b):
            from urllib.parse import urlencode
            diff = self.success('GET', '/api/compare?' + urlencode({'a': a['id'], 'b': b['id']}))
            first, second = band_values(a['bands']), band_values(b['bands'])
            require(first.keys() == second.keys(), 'comparison inputs use different bands')
            expected = {band: second[band] - first[band] for band in first}
            require(close_bands(band_values(diff, 'delta_db'), expected), 'compare band boundaries or B minus A values differ')
            return diff

    brief = json.loads((Path(__file__).parent/'briefs/L3/4-quietbench.json').read_text())
    settings = deepcopy(brief['oracleInterface']['settings'])
    bench = Bench()
    try:
        if bench.check('server starts with --data', bench.start):
            bench.check('CLI -> canonical API, identical band numbers', bench.end_to_end)
            bench.check('wave-1 fixed-filter run preserved', bench.fixed)
            bench.check('hidden tones and noise: independently measured attenuation and convergence', bench.numbers)
            bench.check('limiter holds configured level', bench.safety)
            bench.check('limiter holds during divergence', bench.divergence)
            bench.check('stop within one block', bench.stop_run)
            bench.check('save/restart/reload equality', bench.storage)
            bench.check('CSV rows and invalid WAV atomicity', bench.export_import)
            bench.check('per-band comparison', lambda: bench.comparison(*bench.comparison_pair()))
            bench.check('page start/browse/reload/compare parity', bench.page)
            bench.check('fresh-copy guide commands start and stop', bench.guide)
            if (evidence/'wave1-data').is_dir() and (evidence/'wave1-sessions.json').is_file():
                bench.check('wave-1 saved shape loads after schema growth',bench.legacy)
            else:
                bench.checks.append(dict(name='wave-1 saved shape loads after schema growth',
                    status='unverified',evidence='Retain real wave-1 store as wave1-data and API list/show JSON as wave1-sessions.json before later waves'))
            bench.checks.append(dict(name='page craft (ShelfLife rubric)',status='unverified',
                evidence='No craft rubric or viewport requirement supplied in the dream or shared interface; screenshots are observational'))
    finally:
        bench.stop()
    return dict(checks=bench.checks, totals={s:sum(c['status']==s for c in bench.checks)
                                           for s in ('pass','fail','unverified')})


def band_values(rows, field='attenuation_db'):
    values = {(row['low'], row['high']): row[field] for row in rows}
    if not values or len(values) != len(rows) or not all(math.isfinite(v) for v in values.values()):
        raise AssertionError('Missing, duplicate, or non-finite band values')
    return values


def close_bands(actual, expected):
    return actual.keys() == expected.keys() and all(
        math.isclose(actual[band], value, rel_tol=1e-6, abs_tol=1e-6) for band, value in expected.items())


def fir(signal, taps):
    return [sum(tap * signal[n - i] for i, tap in enumerate(taps) if n >= i) for n in range(len(signal))]


def page_button(*labels):
    return r"""[...document.querySelectorAll('button,[role=button],input[type=submit],input[type=button]')].find(b => {
        const labelled = (b.getAttribute('aria-labelledby') || '').split(/\s+/)
            .map(id => document.getElementById(id)?.innerText || '').join(' ').trim();
        const name = labelled || b.getAttribute('aria-label') || b.innerText || b.value || '';
        const words = name.toLowerCase().match(/[a-z0-9]+/g) || [];
        return """ + json.dumps(labels) + r""".includes(words.join(' '));})"""


def displays_numbers(text, values):
    from decimal import Decimal
    text = re.sub(r'\b[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\b', '', text, flags=re.I)
    tokens = re.findall(r'(?<![\w.])[+\-]?(?:\d+(?:\.\d+)?|\.\d+)(?:e[+\-]?\d+)?',
                        text.replace('−', '-'), re.I)
    numbers = [Decimal(token) for token in tokens]
    return bool(text) and all(any(abs(float(n) - v) <= .5 * 10.0**n.as_tuple().exponent + 1e-9
                                  for n in numbers) for v in values)


def send_ctrl_c(process):
    import os
    import signal
    if os.name != 'nt':
        process.send_signal(signal.SIGINT)
        return
    # Attach only to the fresh server's private console. Keep the sender immune to its own Ctrl+C.
    sender = '''
import ctypes
import sys
import time

console = ctypes.windll.kernel32
console.FreeConsole()
if not console.AttachConsole(int(sys.argv[1])):
    sys.exit(1)
if not console.SetConsoleCtrlHandler(None, True) or not console.GenerateConsoleCtrlEvent(0, 0):
    sys.exit(2)
time.sleep(.2)
'''
    result = subprocess.run([sys.executable, '-B', '-c', sender, str(process.pid)], timeout=5)
    if result.returncode:
        raise Unverified(f'Could not deliver Ctrl+C to the isolated guide console (exit {result.returncode})')


def spectrum(values):
    """Independent stdlib radix-2 DFT; no contender's DSP or metric implementation."""
    if len(values) == 1:
        return values
    even, odd = spectrum(values[::2]), spectrum(values[1::2])
    twiddled = [cmath.exp(-2j*math.pi*k/len(values))*v for k,v in enumerate(odd)]
    return [a+b for a,b in zip(even,twiddled)] + [a-b for a,b in zip(even,twiddled)]
