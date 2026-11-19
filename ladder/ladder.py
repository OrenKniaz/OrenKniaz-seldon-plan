"""Blocker-clearance ladder. Stdlib only. Dry runs never install or launch Codex."""
import argparse
import datetime as dt
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import sys
import time
import uuid

HERE = Path(__file__).resolve().parent
FARM = HERE.parent / 'run-farm' / 'farm.py'
RUNS = Path('C:/seldon/runs/ladder')
TESTS = Path('C:/seldon/tests/ladder-1')
CLEAN = {'ACCEPTED-VERIFIED', 'DELIVERED-VERIFIED'}
LIMITS = {'L0': 2, 'L1': 12, 'L2': 12, 'L3': 3}
RUN_SECONDS = {'L0': 360, 'L1': 720, 'L2': 1200, 'L3': 2400}


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    with temporary.open('w', encoding='utf-8') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def append(path, text):
    with path.open('a', encoding='utf-8') as stream:
        stream.write(text + '\n')
        stream.flush()
        os.fsync(stream.fileno())


def load_farm():
    spec = importlib.util.spec_from_file_location('ladder_farm', FARM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_briefs(level):
    briefs = [json.loads(p.read_text(encoding='utf-8-sig'))
              for p in sorted((HERE / 'briefs' / level).glob('*.json'))]
    if len({b['id'] for b in briefs}) != len(briefs):
        raise ValueError(f'{level}: give each brief a distinct id')
    for brief in briefs:
        if not {'id', 'kind', 'message', 'profile', 'files', 'oracle'} <= brief.keys() or not brief['oracle']:
            raise ValueError(f'Invalid brief schema: {brief.get("id")}')
    return briefs


def usage_limit(row):
    # Only provider-error receipts/stderr count; a product/planner mention is insufficient.
    if row['outcome'] != 'ERROR':
        return False
    texts = []
    for turn in row['turns']:
        if turn.get('error'):
            texts.append(json.dumps(turn['error']))
        stderr = Path(turn['receipt']).with_suffix('.err')
        if stderr.exists():
            texts.append(stderr.read_text(encoding='utf-8', errors='replace'))
    return bool(re.search(r'usage[_ -]?limit|usage_limit_reached|used up.*(?:usage|limit)|'
                          r'exceeded.*(?:usage|quota)|(?:usage|quota).*exceeded',
                          '\n'.join(texts), re.I))


class Ladder:
    def __init__(self, farm, parallel, home=HERE, dry=False):
        self.farm, self.parallel, self.home, self.dry = farm, parallel, home, dry
        home.mkdir(parents=True, exist_ok=True)
        state_path = home / 'STATE.json'
        self.state = (json.loads(state_path.read_text(encoding='utf-8')) if state_path.exists()
                      else dict(level='L0', clean_window=0, installed_sha=None, pending=[]))
        if self.state['level'] not in (*LIMITS, 'DONE') or self.state['clean_window'] < 0:
            raise ValueError('Invalid STATE.json; inspect it before running')
        self.events = []

    def stopped(self):
        return (HERE / 'STOP').exists() or (self.home / 'STOP').exists()

    def persist(self):
        save(self.home / 'STATE.json', self.state)

    def event(self, **event):
        event = dict(utc=utc(), **event)
        self.events.append(event)
        append(self.home / 'events.jsonl', json.dumps(event))

    def step(self, sha=None, scenario='clean'):
        if self.stopped() or self.state['level'] == 'DONE':
            return []
        args = argparse.Namespace(parallel=self.parallel, runtime=self.farm.RUNTIME,
                                  codex=shutil.which('codex.cmd') or shutil.which('codex') or 'codex',
                                  model='gpt-6.1-sol', effort='medium', dry_run=self.dry, offset=0)
        # The real loop always checks/install_build between cohorts; dry SHA is explicitly fake.
        installed = sha if self.dry else self.farm.install_build(args)
        if not installed:
            raise ValueError('Missing installed SHA')
        if installed != self.state['installed_sha']:
            previous = self.state['clean_window']
            self.state.update(installed_sha=installed, clean_window=0, pending=[], sweep_clean=True,
                              gate_pending=self.state['level'] != 'L0')
            self.event(kind='sha-reset', sha=installed, previous_clean_window=previous, clean_window=0)
            self.persist()
        if self.stopped():
            return []
        gate = self.state.get('gate_pending', False)
        level = ('L' + str(int(self.state['level'][1]) - 1)) if gate else self.state['level']
        all_briefs = load_briefs(level)
        if gate:
            all_briefs = all_briefs[:1]  # LADDER.md lower-level spot gate for a newly installed SHA.
        pending = [] if gate else self.state.get('pending', [])
        if not pending:
            self.state['sweep_clean'] = True
        if set(pending) - {b['id'] for b in all_briefs}:
            raise ValueError('Unknown pending brief in STATE.json')
        briefs = [b for b in all_briefs if b['id'] in pending] if pending else all_briefs
        args.sha, args.briefs = installed, len(briefs)
        args.run_seconds = RUN_SECONDS[level]
        tag = self.home.name if self.dry else 'live'
        output = RUNS / level / tag
        args.verify_root = TESTS / tag / 'verify'
        slot_root = TESTS / tag / level / 'slots'
        failed, quota, verified = False, False, set()

        def result(row):
            nonlocal failed, quota
            if usage_limit(row):
                quota = True
                self.event(kind='usage-limit-rerun', run_id=row['run_id'], level=level)
                return False
            if row['outcome'] in CLEAN:
                verified.add(row['brief'])
                if not failed and not gate and level != 'L0':
                    self.state['clean_window'] += 1
            else:
                if not failed:
                    message = next((t.get('last_message', '') for t in reversed(row['turns'])
                                    if t.get('last_message')), '')[:400]
                    receipts = output / row['run_id']
                    append(self.home / 'BLOCKERS.md', json.dumps(dict(
                        utc=utc(), level=level, run_id=row['run_id'], sha=installed,
                        refusal_code=self.farm.failure_code(row), outcome=row['outcome'],
                        last_planner_message=message, receipts_path=str(receipts)), ensure_ascii=False))
                    self.event(kind='blocker', level=level, run_id=row['run_id'])
                failed = True
                self.state['clean_window'] = 0
                self.state['sweep_clean'] = False
            self.persist()
            return not failed and not quota and not self.stopped()

        rows = self.farm.cohort(args, briefs, slot_root=slot_root, output_root=output,
                                fake_scenario=scenario if self.dry else None,
                                fake_artifacts=HERE / 'dry-fixtures' if self.dry else None,
                                stop=self.stopped, on_result=result)
        if gate:
            if rows and all(row['outcome'] in CLEAN for row in rows):
                self.state['gate_pending'] = False
                self.event(kind='lower-level-spot-verified', level=level, sha=installed,
                           run_id=rows[0]['run_id'])
            self.persist()
            return rows
        # Only the failed/unstarted/quota briefs remain in this sweep. Drain in-flight jobs
        # but do not count their successes after a blocker as a new clean window.
        self.state['pending'] = [b['id'] for b in briefs if b['id'] not in verified]
        complete = len(rows) == len(briefs) and not failed and not quota
        if level == 'L0' and complete and self.state.get('sweep_clean', True):
            self.state['clean_window'] += 1
        if (not failed and not self.stopped() and not self.state['pending']
                and self.state['clean_window'] >= LIMITS[level]):
            next_level = 'DONE' if level == 'L3' else 'L' + str(int(level[1]) + 1)
            append(self.home / 'PROMOTIONS.md', f'{utc()} | {level} -> {next_level} | SHA {installed} | clean window {self.state["clean_window"]}')
            self.state.update(level=next_level, clean_window=0, pending=[])
            self.event(kind='promotion', previous_level=level, level=next_level, sha=installed)
            print(f'PROMOTED {level} -> {next_level}', flush=True)
        self.persist()
        return rows


def dry_run(farm, parallel):
    home = HERE / 'dry-runs' / ('dry-' + uuid.uuid4().hex[:12])
    ladder = Ladder(farm, parallel, home, dry=True)
    # Integration proof: real farm fake subprocesses -> real artifact verifier -> state writer.
    # Protects reset/promotion and blocker gating; legacy farm checks only failed fake artifacts.
    ladder.step('FAKE-SHA-A')
    assert ladder.state['level'] == 'L0' and ladder.state['clean_window'] == 1
    ladder.step('FAKE-SHA-B')
    assert any(e['kind'] == 'sha-reset' and e['previous_clean_window'] == 1 for e in ladder.events)
    assert ladder.state['level'] == 'L0' and ladder.state['clean_window'] == 1
    rows = ladder.step('FAKE-SHA-B', {'1': 'blocker'})
    assert any(r['outcome'] == 'BLOCKED-reviewer-unavailable' for r in rows)
    assert ladder.state['level'] == 'L0' and ladder.state['clean_window'] == 0
    assert 'reviewer-unavailable' in (home / 'BLOCKERS.md').read_text(encoding='utf-8')
    while ladder.state['level'] == 'L0' and not ladder.stopped():
        ladder.step('FAKE-SHA-B')
    if ladder.stopped():
        print('Dry run stopped; no proof claimed:', home)
        return
    assert ladder.state['level'] == 'L1'
    assert 'L0 -> L1' in (home / 'PROMOTIONS.md').read_text(encoding='utf-8')
    evidence = dict(scope='FAKE executable/artifact/state integration only; no real Seldon acceptance',
                    home=str(home), state=ladder.state, events=ladder.events,
                    proved=['two clean L0 cohorts promote to L1', 'blocker recorded; no advance',
                            'SHA change resets nonzero clean window'])
    save(home / 'dry-run-evidence.json', evidence)
    print('DRY-RUN PASS:', home / 'dry-run-evidence.json')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['run', 'status'])
    parser.add_argument('--parallel', type=int, default=4)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    if args.parallel < 1:
        parser.error('parallel must be positive')
    if args.command == 'status':
        state = json.loads((HERE / 'STATE.json').read_text(encoding='utf-8'))
        print(json.dumps(dict(state=state, stopped=(HERE / 'STOP').exists(),
                             lock=(HERE / '.ladder.lock').read_text(encoding='utf-8')
                             if (HERE / '.ladder.lock').exists() else None), indent=2))
        return
    lock = HERE / '.ladder.lock'
    try:
        with lock.open('x', encoding='utf-8') as stream:
            json.dump(dict(pid=os.getpid(), utc=utc(), dry_run=args.dry_run), stream)
    except FileExistsError:
        parser.error('Ladder locked; inspect .ladder.lock owner before removing a stale lock')
    try:
        if (HERE / 'STOP').exists():
            print('STOP present; no cohort started')
            return
        farm = load_farm()
        for level in LIMITS:
            load_briefs(level)
        if args.dry_run:
            dry_run(farm, args.parallel)
        else:
            ladder = Ladder(farm, args.parallel)
            while not ladder.stopped() and ladder.state['level'] != 'DONE':
                rows = ladder.step()
                # Quota exhaustion should not busy-loop; STOP remains responsive.
                if any(usage_limit(row) for row in rows):
                    for _ in range(60):
                        if ladder.stopped():
                            break
                        time.sleep(1)
    finally:
        lock.unlink()


if __name__ == '__main__':
    main()
