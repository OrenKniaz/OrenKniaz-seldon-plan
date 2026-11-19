"""ShelfLife comparison driver. --dry-run launches only the local fake executable."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import uuid

HERE = Path(__file__).resolve().parent
RUNS = Path(os.environ.get('FIGHT_RUNS', 'C:/seldon/runs/fight-1'))
FARM = HERE.parent / 'run-farm' / 'farm.py'
MODEL, EFFORT = os.environ.get('FIGHT_MODEL', 'gpt-6.1-sol'), 'medium'


def load_farm():
    spec = importlib.util.spec_from_file_location('fight_farm', FARM)
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True  # importing a neighbour must not write its cache
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    # Farm is concurrently maintained. Keep its output root local, and defer its
    # optional product verifier to our separately invoked blind oracle.
    module.HERE = HERE
    if hasattr(module, 'product_check'):
        module.product_check = lambda *a: dict(verdict='unverified', evidence='Deferred to blind oracle.py',
                                               screenshots=[], checks=[])
    return module


def brief():
    return dict(id='shelflife', kind='web',
                message=(HERE / 'shelflife-brief.md').read_text(encoding='utf-8-sig'),
                profile={'audience': 'one household, ordinary home cooks',
                         'style': 'clean, calm, readable; muted green and neutral colours',
                         'platform': 'local browser on phone and desktop',
                         'sections': 'expiring soon, pantry list, add item',
                         'preferences': 'use brief defaults, SQLite, no accounts or cloud services'},
                files=['server.py', 'import_items.py', 'README.md'])


def command(farm, args, slot, output, thread=None):
    """Share all farm flags, replacing only its Seldon MCP configuration."""
    original = farm.codex_command(args, slot, output, MODEL, EFFORT, thread)
    native = []
    index = 0
    while index < len(original):
        if original[index] == '-c' and original[index + 1].startswith('mcp_servers.seldon.'):
            index += 2
        else:
            native.append(original[index])
            index += 1
    return native  # Plain Codex: Seldon flags stripped; no Seldon server is configured globally.


def response(farm, message, spec):
    prompt, rule = farm.user_reply(message, spec)
    if prompt is None:
        prompt = '; '.join(f'{k}: {v}' for k, v in spec['profile'].items()) + '; keep all existing project restrictions and use the brief defaults. If those do not resolve the question, report the blocker through Seldon.'
    return prompt, rule


def native(farm, args, spec, slot, logs):
    slot.mkdir(parents=True, exist_ok=False)
    logs.mkdir(parents=True, exist_ok=False)
    turns, replies = [], []
    start, thread, prompt = time.monotonic(), None, spec['message']
    outcome, error = 'TURN-LIMIT', None
    try:
        for number in range(1, 13):
            prefix = logs / f'turn{number:02d}'
            turn = dict(number=number, receipt=str(prefix.with_suffix('.jsonl')), thread=thread)
            turns.append(turn)
            turn.update(farm.execute(command(farm, args, slot, prefix.with_suffix('.md'), thread),
                                     slot, prefix, prompt, start + 40 * 60))
            farm.receipt_score(turns)
            if turn['exit_code'] or turn.get('error'):
                raise RuntimeError(f'Codex failed at turn {number}; see receipt/stderr')
            thread = turn.get('thread')
            if not thread or not turn['last_message']:
                raise RuntimeError('Missing thread or final message')
            message = turn['last_message']
            # user_reply also detects non-question approval/acceptance cards.
            prompt, rule = response(farm, message, spec)
            if '?' not in message and not farm.approval_card(message) and rule not in ('approval', 'acceptance'):
                outcome = 'FINISHED'
                break
            if number < 12:
                replies.append(dict(after_turn=number, rule=rule, text=prompt))
    except (OSError, ValueError, RuntimeError, TimeoutError, subprocess.SubprocessError) as exc:
        outcome, error = 'ERROR', str(exc)
    try:
        score, _ = farm.receipt_score(turns)
    except (OSError, ValueError) as exc:
        outcome, error = 'ERROR', f'{error or ""}; invalid receipts: {exc}'
        score = dict(tokens={}, token_coverage='invalid receipts', planner_mcp_calls=None, shell_commands=None)
    return dict(side='native', slot=str(slot), turns=turns, replies=replies,
                decisions=sum(r['rule'] != 'continue' for r in replies),
                wall_seconds=round(time.monotonic() - start, 3), outcome=outcome, error=error, **score)


def fake():
    """Protocol fake: real driver, init/status, resumed thread, approvals and receipts."""
    argv = sys.argv[2:]
    slot = Path(argv[argv.index('-C') + 1]) if '-C' in argv else Path.cwd()
    if 'init' in argv:
        print('fake init/check only')
        return
    state = slot / '.fake-turn'
    number = int(state.read_text()) if state.exists() else 0
    if 'status' in argv:
        print(json.dumps({'structuredContent': {'phase': 'accept' if number >= 3 else 'plan',
                                              'acceptance': {'accepted': number >= 3}}}))
        return
    prompt = sys.stdin.read()
    if number == 0:
        assert prompt == brief()['message'], 'first prompt must be the unchanged brief'
    else:
        assert 'resume' in argv and argv[argv.index('resume') + 1] == 'fake-thread'
        assert 'audience:' in prompt if number == 1 else prompt == 'yes'
    is_native = not any(a.startswith('mcp_servers.seldon.') for a in argv)
    assert any('model_reasoning_effort="medium"' == a for a in argv)
    assert argv[argv.index('-m') + 1] == MODEL
    if is_native:
        assert not any('seldon-init' in a or 'seldon_mcp' in a for a in argv)
    number += 1
    state.write_text(str(number))
    messages = ['What audience and style do you prefer?', 'Reply Yes to approve.', 'Delivered ShelfLife.']
    emitted = [{'type': 'thread.started', 'thread_id': 'fake-thread'},
               {'type': 'item.completed', 'item': {'type': 'command_execution', 'exit_code': 0}}]
    if not is_native:
        emitted.append({'type': 'item.completed', 'item': {'type': 'mcp_tool_call',
                        'server': 'seldon', 'tool': 'harness_plan_status', 'result': {}}})
    emitted += [{'type': 'item.completed', 'item': {'type': 'agent_message', 'text': messages[number - 1]}},
                {'type': 'turn.completed', 'usage': {'input_tokens': number * 100, 'output_tokens': number * 10}}]
    for event in emitted:
        print(json.dumps(event))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('side', choices=['seldon', 'native'])
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    lock = HERE / f'.fight-{args.side}.lock'  # one per side so both contenders run concurrently
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    try:
        with os.fdopen(fd, 'w') as stream:
            json.dump({'pid': os.getpid(), 'side': args.side}, stream)
        farm = load_farm()
        spec = brief()
        batch = time.strftime('%Y%m%dT%H%M%S') + '-' + uuid.uuid4().hex[:6]
        logs = HERE / ('dry-runs' if args.dry_run else 'receipts') / batch
        logs.mkdir(parents=True)
        args.model, args.effort = MODEL, EFFORT
        args.runtime = farm.RUNTIME
        args.sha = 'FAKE' if args.dry_run else (farm.source_sha() if args.side == 'seldon' else None)
        args.codex_cmd = [shutil.which('codex.cmd') or shutil.which('codex') or 'codex']
        args.runtime_cmd = [str(args.runtime)]
        roots = logs / 'slots' if args.dry_run else RUNS
        if args.dry_run:
            args.codex_cmd = args.runtime_cmd = [sys.executable, str(HERE / 'fight.py'), '--_fake']
        # Do not inherit Seldon's initialization marker into the plain Codex subprocess.
        marker = os.environ.pop('SELDON_INIT', None)
        try:
            if args.side == 'seldon':
                root = roots / 'seldon'
                root.mkdir(parents=True, exist_ok=True)
                row = farm.run_one(args, spec, 1, batch, root, logs)
            else:
                row = native(farm, args, spec, roots / 'native', logs / 'native')
        finally:
            if marker is not None:
                os.environ['SELDON_INIT'] = marker
        row.update(side=args.side, model=MODEL, effort=EFFORT, dry_run=args.dry_run,
                   farm_sha256=hashlib.sha256(FARM.read_bytes()).hexdigest(),
                   brief_sha256=hashlib.sha256((HERE / 'shelflife-brief.md').read_bytes()).hexdigest(),
                   final_message=row['turns'][-1].get('last_message', '') if row['turns'] else '',
                   turn_count=len(row['turns']), user_decisions=row['decisions'])
        row['tool_calls'] = sum(e.get('item', {}).get('type') in ('command_execution', 'mcp_tool_call', 'tool_call')
                                for t in row['turns'] for e in farm.events(Path(t['receipt'])))
        row['mcp_calls'] = sum(e.get('item', {}).get('type') == 'mcp_tool_call'
                               for t in row['turns'] for e in farm.events(Path(t['receipt'])))
        if args.dry_run:
            assert row['turn_count'] == 3 and row['user_decisions'] == 2, row
            assert row['tokens'] == {'input_tokens': 300, 'output_tokens': 30}, row
            assert row['outcome'].startswith('ACCEPTED') if args.side == 'seldon' else row['outcome'] == 'FINISHED', row
            assert row['mcp_calls'] == (3 if args.side == 'seldon' else 0), row
        target = HERE / f'fight-{args.side}.json'
        target.write_text(json.dumps(row, indent=2) + '\n', encoding='utf-8')
        print(f'{args.side}: {row["outcome"]}; {target}')
        return int(row['outcome'] == 'ERROR')
    finally:
        lock.unlink()


if __name__ == '__main__':
    if sys.argv[1:2] == ['--_fake']:
        fake()
    else:
        raise SystemExit(main())
