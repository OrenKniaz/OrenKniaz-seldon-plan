"""Brief-only black-box oracle; never imports or reads a contender's source."""
import argparse
import concurrent.futures
import csv
import datetime as dt
import http.client
import json
import os
from pathlib import Path
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
from urllib.parse import urlencode

HERE = Path(__file__).resolve().parent
TESTS = Path('C:/seldon/tests/fight-1')


def product_environment():
    env = dict(os.environ)
    for name in ('PYTHONPATH', 'PYTHONHOME', 'SELDON_INIT'):
        env.pop(name, None)
    return env


def label_value(value):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,39}', value):
        raise argparse.ArgumentTypeError('label must be 1-40 letters, digits, underscores or hyphens')
    return value


def free_port():
    with socket.socket() as sock:
        sock.bind(('127.0.0.1', 0))
        return sock.getsockname()[1]


class Oracle:
    def __init__(self, product, label):
        self.product, self.label = product.resolve(), label_value(label)
        self.target = TESTS / self.label
        self.checks = []
        self.process = None
        self.log = None
        self.port = free_port()
        self.base = f'http://127.0.0.1:{self.port}'

    def record(self, name, status, evidence):
        self.checks.append(dict(check=name, status=status, evidence=evidence))

    def check(self, name, operation):
        try:
            evidence = operation()
            self.record(name, 'pass', evidence if evidence is not None else 'assertions passed')
            return True
        except Exception as exc:
            self.record(name, 'fail', f'{type(exc).__name__}: {exc}')
            return False

    def request(self, method, path, payload=None, raw=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.port, timeout=8)
        body = raw if raw is not None else (json.dumps(payload) if payload is not None else None)
        try:
            connection.request(method, path, body, {'Content-Type': 'application/json'})
            response = connection.getresponse()
            data = response.read()
            try:
                parsed = json.loads(data)
            except (ValueError, UnicodeDecodeError):
                parsed = data.decode('utf-8', errors='replace')
            return response.status, parsed
        finally:
            connection.close()

    def expect(self, method, path, codes, payload=None, raw=None):
        status, body = self.request(method, path, payload, raw)
        assert status in codes, f'{method} {path}: expected {codes}, got {status}: {str(body)[:300]}'
        if status == 400:
            assert isinstance(body, dict) and isinstance(body.get('error'), str) and body['error'], f'missing error string: {body}'
        return body

    def items(self, query=None):
        body = self.expect('GET', '/api/items' + ('?' + urlencode(query) if query else ''), (200,))
        rows = body.get('items') if isinstance(body, dict) else body
        assert isinstance(rows, list), f'expected item array: {body}'
        return rows

    def create(self, **changes):
        payload = dict(name='Oracle rice', quantity=3, unit='bags', expires=None)
        payload.update(changes)
        before = {r['id'] for r in self.items()}
        self.expect('POST', '/api/items', (200, 201), payload)
        matches = [r for r in self.items() if r['id'] not in before and r['name'] == payload['name']]
        assert len(matches) == 1, f'created row absent or ambiguous: {matches}'
        return matches[0]

    def start(self):
        self.log = (self.target / 'oracle-server.log').open('ab')
        self.process = subprocess.Popen([sys.executable, '-S', 'server.py', '--port', str(self.port), '--db', str(self.db)],
                                        cwd=self.target, stdout=self.log, stderr=self.log, env=product_environment())
        deadline = time.monotonic() + 12
        while time.monotonic() < deadline:
            if self.process.poll() is not None:
                raise RuntimeError(f'server exited {self.process.returncode}; see {self.label}/oracle-server.log')
            try:
                self.request('GET', '/api/items')
                return
            except OSError:
                time.sleep(.1)
        raise TimeoutError('server did not become reachable in 12 seconds')

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

    def prepare(self):
        TESTS.mkdir(parents=True, exist_ok=True)
        assert self.product.is_dir(), 'product directory does not exist'
        assert self.product != self.target.resolve(), 'source and isolated copy must differ'
        assert not self.target.exists(), f'{self.target} already exists; use a new label (copies are never overwritten)'
        # Reject links rather than copying unrelated host files through a product link.
        for path in self.product.rglob('*'):
            assert not path.is_symlink() and not path.is_junction(), f'linked product entry rejected: {path.name}'
        shutil.copytree(self.product, self.target, ignore=shutil.ignore_patterns('.git', '__pycache__', '.venv'))
        self.temp = tempfile.TemporaryDirectory(prefix='oracle-db-', dir=self.target)
        self.db = Path(self.temp.name) / 'pantry.sqlite3'
        self.start()
        return 'isolated product copy, free loopback port, fresh temporary database'

    def api_checks(self):
        def root():
            body = self.expect('GET', '/', (200,))
            assert isinstance(body, str) and '<' in body, 'root did not return HTML'
            assert (self.target / 'README.md').is_file(), 'README.md missing'
            return 'GET / = 200 HTML; README exists (contents not inspected)'
        self.check('fresh folder and UI endpoint', root)
        self.check('GET /api/items initially empty', lambda: require(self.items() == [], 'fresh DB must be empty'))
        today = dt.date.today()
        self.dates = {'expired': str(today - dt.timedelta(days=2)), 'soon': str(today + dt.timedelta(days=3)),
                      'today': str(today), 'later': str(today + dt.timedelta(days=30))}

        def crud():
            row = self.create(name='Oracle CRUD')
            assert {'id', 'name', 'quantity', 'unit', 'expires', 'created_at'} <= row.keys(), row
            assert row['quantity'] == 3 and row['unit'] == 'bags' and row['expires'] is None and row['created_at'], row
            path = f'/api/items/{row["id"]}'
            changes = dict(name='Oracle updated', quantity=5, unit='jars', expires=self.dates['soon'])
            self.expect('PATCH', path, (200, 204), changes)
            updated = next(r for r in self.items() if r['id'] == row['id'])
            assert all(updated[k] == v for k, v in changes.items()), updated
            self.expect('POST', path + '/consume', (200, 204), {'amount': 2})
            assert next(r for r in self.items() if r['id'] == row['id'])['quantity'] == 3
            self.expect('POST', path + '/consume', (409,), {'amount': 4})
            assert next(r for r in self.items() if r['id'] == row['id'])['quantity'] == 3, '409 mutated quantity'
            self.expect('PATCH', path, (200, 204), {'expires': None, 'quantity': 0})
            self.expect('DELETE', path, (200, 204))
            assert row['id'] not in {r['id'] for r in self.items()}
            return 'create/read/update all fields/consume/409/zero quantity/delete, checked stored values'
        self.check('CRUD endpoints and over-consume 409', crud)

        invalid = [('empty name', dict(name='', quantity=1)), ('name over 80 chars', dict(name='x' * 81, quantity=1)),
                   ('negative quantity', dict(name='Bad', quantity=-1)), ('fractional quantity', dict(name='Bad', quantity=1.5)),
                   ('text quantity', dict(name='Bad', quantity='one')), ('boolean quantity', dict(name='Bad', quantity=True)),
                   ('impossible date', dict(name='Bad', quantity=1, expires='2026-02-30')),
                   ('non-date expiry', dict(name='Bad', quantity=1, expires='tomorrow')),
                   ('non-text unit', dict(name='Bad', quantity=1, unit=5))]
        for name, payload in invalid:
            def validation(payload=payload):
                before = self.items()
                self.expect('POST', '/api/items', (400,), payload)
                assert self.items() == before, 'invalid create changed data'
                return {'request': payload, 'status': 400, 'unchanged': True}
            self.check(f'create rejects {name} with 400', validation)
        self.check('malformed JSON 400', lambda: self.expect('POST', '/api/items', (400,), raw='{broken'))

        def invalid_updates():
            row = self.create(name='Validation target')
            path = f'/api/items/{row["id"]}'
            for payload in ({'quantity': -1}, {'name': ''}, {'expires': 'bad'}, {'unit': 7}):
                self.expect('PATCH', path, (400,), payload)
            for payload in ({'amount': -1}, {'amount': 1.5}, {'amount': 'one'}, {}):
                self.expect('POST', path + '/consume', (400,), payload)
            assert next(r for r in self.items() if r['id'] == row['id'])['quantity'] == 3
            self.expect('DELETE', path, (200, 204))
            return 'invalid PATCH and consume inputs return JSON errors without changing quantity'
        self.check('PATCH and consume validation 400', invalid_updates)
        for method, suffix, payload in [('PATCH', '', {'quantity': 1}), ('DELETE', '', None), ('POST', '/consume', {'amount': 1})]:
            self.check(f'unknown id 404 {method}{suffix}',
                       lambda m=method, s=suffix, p=payload: self.expect(m, '/api/items/999999999' + s, (404,), p))

        def sorting():
            for name, date in [('Later oats', self.dates['later']), ('No expiry', None),
                               ('Soon apples', self.dates['soon']), ('Expired beans', self.dates['expired']),
                               ('Today rice', self.dates['today'])]:
                self.create(name=name, expires=date)
            rows = self.items()
            keys = [(r['expires'] is None, r['expires'] or '') for r in rows]
            assert keys == sorted(keys), keys
            queried = self.items({'q': 'Soon apples'})
            assert [r['name'] for r in queried] == ['Soon apples'], queried
            filtered = self.items({'expiring_within': 7})
            names = {r['name'] for r in filtered}
            assert {'Soon apples', 'Today rice'} <= names and not {'Later oats', 'No expiry'} & names, names
            combined = self.items({'q': 'Soon apples', 'expiring_within': 7})
            assert [r['name'] for r in combined] == ['Soon apples'], combined
            return {'ordered_names': [r['name'] for r in rows], 'within_7': sorted(names), 'combined_filter': True}
        self.check('expiry order, name search and combined filters', sorting)

        def consume_race():
            row = self.create(name='Last unit', quantity=1)
            barrier = threading.Barrier(2)
            def consume(_):
                barrier.wait(timeout=5)
                return self.request('POST', f'/api/items/{row["id"]}/consume', {'amount': 1})[0]
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                codes = list(pool.map(consume, range(2)))
            assert sorted(codes) == [200, 409], codes
            assert next(r for r in self.items() if r['id'] == row['id'])['quantity'] == 0
            return {'simultaneous_statuses': codes, 'final_quantity': 0}
        self.check('atomic last-unit concurrent consumes', consume_race)

        def create_race():
            before = len(self.items())
            barrier = threading.Barrier(30)
            def create(index):
                barrier.wait(timeout=10)
                return self.request('POST', '/api/items', {'name': f'Parallel {index}', 'quantity': 1})[0]
            with concurrent.futures.ThreadPoolExecutor(max_workers=30) as pool:
                codes = list(pool.map(create, range(30)))
            rows = self.items()
            parallel = [r for r in rows if r['name'].startswith('Parallel ')]
            assert all(c in (200, 201) for c in codes), codes
            assert len(rows) == before + 30 and len(parallel) == len({r['id'] for r in parallel}) == 30
            return {'statuses': codes, 'added_rows': 30, 'unique_ids': 30}
        self.check('30 simultaneous creates retain 30 rows', create_race)

        def persistence():
            before = self.items()
            self.stop()
            self.start()
            assert self.items() == before, 'data changed after restart'
            return {'rows_preserved': len(before)}
        self.check('SQLite persistence across restart', persistence)

        def importer():
            self.stop()
            path = Path(self.temp.name) / 'items.csv'
            with path.open('w', newline='', encoding='utf-8') as stream:
                writer = csv.writer(stream)
                writer.writerows([['name', 'quantity', 'unit', 'expires'],
                                 ['Imported lentils', '2', 'bags', self.dates['soon']],
                                 ['Imported salt', '0', '', ''], ['', '1', '', ''],
                                 ['Bad quantity', '-1', '', ''], ['Bad date', '1', '', '2026-02-30']])
            result = subprocess.run([sys.executable, '-S', 'import_items.py', str(path), '--db', str(self.db)],
                                    cwd=self.target, capture_output=True, text=True, timeout=15, env=product_environment())
            assert result.returncode == 0, f'exit {result.returncode}: {result.stderr[:300]}'
            assert result.stdout.strip() == 'imported 2, skipped 3', repr(result.stdout)
            self.start()
            rows = self.items()
            imported = [r for r in rows if r['name'].startswith('Imported ')]
            assert len(imported) == 2 and {r['quantity'] for r in imported} == {0, 2}, imported
            assert not any(r['name'] in ('Bad quantity', 'Bad date', '') for r in rows)
            return {'stdout': result.stdout.strip(), 'exit': 0, 'rows_visible_via_API': 2}
        self.check('importer summary, invalid-row skipping and shared database', importer)
        if self.process is None or self.process.poll() is not None:
            self.check('restart after importer', self.start)

        def missing_import():
            result = subprocess.run([sys.executable, '-S', 'import_items.py', str(Path(self.temp.name) / 'absent.csv'),
                                     '--db', str(self.db)], cwd=self.target, capture_output=True, text=True, timeout=15,
                                    env=product_environment())
            assert result.returncode == 2 and (result.stderr.strip() or result.stdout.strip()), (result.returncode, result.stdout, result.stderr)
            return {'exit': 2, 'error': (result.stderr or result.stdout).strip()[:300]}
        self.check('unreadable import file exits 2 with error', missing_import)

    def run(self):
        started = time.monotonic()
        try:
            if self.check('isolated server startup', self.prepare):
                self.api_checks()
                from oracle_ui import run_ui
                run_ui(self)
            else:
                self.record('API, importer and UI checks', 'unverified', 'startup failed; see isolated server startup')
        except Exception as exc:
            self.record('oracle continuation', 'fail', f'{type(exc).__name__}: {exc}')
        finally:
            self.stop()
            if hasattr(self, 'temp'):
                self.check('temporary database cleanup', self.temp.cleanup)
        result = dict(label=self.label, checks=self.checks,
                      totals={status: sum(c['status'] == status for c in self.checks) for status in ('pass', 'fail', 'unverified')},
                      wall_seconds=round(time.monotonic() - started, 3),
                      policy='Brief-only black box; no contender source inspected. 2xx accepted where brief omits a success code. UI semantic discovery failures are reported, not inferred passes.')
        (HERE / f'oracle-{self.label}.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        return result


def require(condition, message):
    assert condition, message
    return message


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('product_dir', type=Path)
    parser.add_argument('label', type=label_value)
    args = parser.parse_args()
    result = Oracle(args.product_dir, args.label).run()
    print(json.dumps({'label': result['label'], 'totals': result['totals']}))
    return int(bool(result['totals']['fail']))


if __name__ == '__main__':
    raise SystemExit(main())
