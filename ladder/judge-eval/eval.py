"""Recorded questions -> current Seldon provider -> compared findings (C14/R9).

Native stream parsing reuses terraReplay/replay.py. No retries or grader calls.
Recall is adjudicated against the answer key after replay, never by keyword overlap.
"""
import argparse
import ast
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
from threading import Event

HERE = Path(__file__).resolve().parent
SOURCE = Path(os.environ.get('SELDON_SOURCE',
    '~/codex-harness/work/sprint-20261027/semantic-cc/src'))
sys.path.insert(0, str(SOURCE))
sys.dont_write_bytecode = True
from seldon import features, providers, questions, schema

LABELS = ('MUST_CATCH', 'MUST_NOT_FLAG', 'CONTROL', 'EVIDENCE_GAP', 'CODE_QUALITY')

# The retained replay imports an obsolete source checkout at module scope. Reuse
# its independent stream decoder without executing that historical initialization.
REPLAY = Path('C:/seldon/tests/terraReplay/replay.py')
tree = ast.parse(REPLAY.read_text('utf-8'))
namespace = {'json': json, 'Path': Path}
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef)
                             and n.name == 'stream'], type_ignores=[]), str(REPLAY), 'exec'), namespace)
stream = namespace['stream']


def load(path):
    return json.loads(Path(path).read_text('utf-8-sig'))


def cases(path):
    rows = [json.loads(line) for line in Path(path).read_text('utf-8-sig').splitlines() if line.strip()]
    assert len({r['id'] for r in rows}) == len(rows), 'Duplicate case id'
    for row in rows:
        assert row['label'] in LABELS
        assert row['answer_key'] and row['evidence']
        original = Path(row['question_path'])
        assert hashlib.sha256(original.read_bytes()).hexdigest() == row['question_sha256']
        assert load(original) == row['question'], 'Recorded question changed'
    return rows


def current(row):
    old = row['question']
    answer_schema = old['schema']['properties']['answer']
    if 'findings' in answer_schema.get('properties', {}):
        # Folded JUDGE uses its own subject-indexed schema, examples and brief.
        return {key: value for key, value in old.items() if key != 'execution'}
    owners = set()
    targets = set(old['targets'])
    for branch in answer_schema['anyOf']:
        gap = branch['properties'].get('gaps', {}).get('items', {}).get('properties', {})
        owners.update(gap.get('owners', {}).get('items', {}).get('enum', []))
        targets.update(gap.get('target', {}).get('enum', []))
    q = questions.build(old['kind'], old['facts'], old['targets'],
                        images=old.get('images', []), owners=sorted(owners))
    q['schema'] = schema.answer_schema(old['kind'], sorted(targets), sorted(owners))
    # Accepted-commitment judgments have an additional current owner-authored brief.
    if old['kind'] == 'PRODUCT' and old['prompt'].startswith('Was this accepted commitment'):
        from seldon import judgment
        tree = ast.parse(Path(judgment.__file__).read_text('utf-8'))
        assignment = next(n for n in ast.walk(tree) if isinstance(n, ast.Assign)
                          and any(isinstance(t, ast.Subscript) and isinstance(t.slice, ast.Constant)
                                  and t.slice.value == 'prompt' for t in n.targets))
        q['prompt'] = eval(compile(ast.Expression(assignment.value), judgment.__file__, 'eval'),
                           {'questions': questions})
    return q


def validate_question(q):
    for image in q.get('images', []):
        assert Path(image).is_file(), f'Missing recorded image: {image}'
    schema.validate(q['examples'][0], q['schema'])
    strict(q['schema'])


def blocking_findings(answer, subject=None):
    if 'findings' in answer:
        findings = answer['findings']
        return [gap for key, finding in findings.items()
                if 'gaps' in finding and (subject is None or subject == key)
                for gap in questions.must_fix(finding)]
    return questions.must_fix(answer) if 'gaps' in answer else []


def strict(node):
    if isinstance(node, dict):
        if node.get('type') == 'object':
            assert node.get('additionalProperties') is False
            assert set(node['required']) == set(node['properties'])
        for child in node.values(): strict(child)
    elif isinstance(node, list):
        for child in node: strict(child)


def report(rows, results, grades, output):
    by_id = {r['id']: r for r in results}
    lines = ['# Judge eval', '', 'Recall uses explicit semantic adjudications; missing adjudications remain unscored.']
    for kind in ['ALL', *sorted({r['question']['kind'] for r in rows})]:
        group = [r for r in rows if kind == 'ALL' or r['question']['kind'] == kind]
        catches = [r for r in group if r['label'] == 'MUST_CATCH']
        negatives = [r for r in group if r['label'] in ('CONTROL', 'MUST_NOT_FLAG')]
        errors = sum(bool(by_id.get(r['id'], {}).get('error')) for r in group)
        evaluated_negatives = [r for r in negatives if by_id.get(r['id'], {}).get('answer')
                               and not by_id[r['id']].get('error')]
        pending = [r for r in catches if r['id'] not in grades]
        hits = sum(grades.get(r['id'], {}).get('matches_key', False) and
                   bool(by_id.get(r['id'], {}).get('must_fix')) for r in catches)
        alarms = sum(bool(by_id.get(r['id'], {}).get('must_fix')) for r in evaluated_negatives)
        recall = f'{hits}/{len(catches)}' if catches and not pending else 'N/A' if not catches else f'pending ({len(pending)})'
        gaps = sum(r['label'] == 'EVIDENCE_GAP' for r in group)
        lines.append(f'- {kind}: recall {recall}; false alarms {alarms}/{len(evaluated_negatives)} answered negatives ({len(negatives)} attempted); evidence gaps {gaps}; errors {errors}.')
    lines.extend(['', '| Case | Label | Must-fix | Match | Error |', '|---|---|---|---|---|'])
    for row in rows:
        result = by_id.get(row['id'], {})
        lines.append(f"| {row['id']} | {row['label']} | {len(result.get('must_fix', []))} | "
                     f"{grades.get(row['id'], {}).get('matches_key', '')} | {' '.join(str(result.get('error', '')).split()).replace('|', '/')[:350]} |")
    Path(output).write_text('\n'.join(lines)+'\n', 'utf-8')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('case_set', type=Path)
    p.add_argument('--dry', action='store_true')
    p.add_argument('--arm', choices=('control', 'prompts2'), default='control')
    p.add_argument('--model', default='gpt-6.1-terra')
    p.add_argument('--output', type=Path, default=HERE/'report.md')
    p.add_argument('--run-dir', type=Path)
    p.add_argument('--results', type=Path, help='Score retained results without provider calls')
    p.add_argument('--grades', type=Path, help='JSON id -> {matches_key: boolean, reason: text}')
    args = p.parse_args()
    if args.case_set.resolve() != HERE / 'tune.jsonl':
        p.error('Choose the canonical tune.jsonl. Holdout is sealed.')
    os.environ['SELDON_ON'] = 'prompts2' if args.arm == 'prompts2' else ''
    os.environ['SELDON_OFF'] = ''
    assert features.enabled('prompts2') == (args.arm == 'prompts2')
    rows = cases(args.case_set)
    prepared = {r['question_path']: current(r) for r in rows}
    for question in prepared.values():
        validate_question(question)
    print(dict(cases=len(rows), labels=dict(Counter(r['label'] for r in rows)),
               questions=len(prepared), arm=args.arm,
               kinds=dict(Counter(r['question']['kind'] for r in rows))), flush=True)
    if args.dry:
        for question in prepared.values():
            prompt, instructions = providers.render_question(question, images=question.get('images', []))
            assert prompt and instructions
        print('DRY: recorded provenance, images, schemas, examples and native rendering valid; no provider calls.')
        return
    grades = load(args.grades) if args.grades else {}
    if args.results:
        results = [json.loads(line) for line in args.results.read_text('utf-8').splitlines()]
        assert all(result['arm'] == args.arm for result in results)
    else:
        root = Path('C:/seldon/tests').resolve()
        if args.run_dir is None or args.run_dir.resolve().parent != root or not re.fullmatch(r'judgeEval2-\d+', args.run_dir.name):
            p.error('--run-dir must be a fresh C:/seldon/tests/judgeEval2-<n> directory')
        args.run_dir.mkdir(exist_ok=False)
        temp = args.run_dir/'temp'; temp.mkdir()
        os.environ['TEMP'] = os.environ['TMP'] = str(temp)
        home = args.run_dir/'codex-home'; home.mkdir()
        shutil.copyfile(Path.home()/'.codex/auth.json', home/'auth.json')
        os.environ['CODEX_HOME'] = str(home)
        inv = load(Path(rows[0]['question_path']).with_name('invocation.json'))
        command = inv['command']; prefix = command[:command.index('exec')]
        config = providers.roles()
        for role in config:
            if 'model' in config[role]: config[role].update(model=args.model, effort='medium', timeout=300)
        provider = providers.Provider(args.run_dir/'calls', {'codexCommand': prefix, 'providers': config})
        results = []
        stop = Event()
        def run(path):
            if stop.is_set():
                return dict(error='Batch stopped after provider error')
            folder = None
            def started(path):
                nonlocal folder
                folder = path
            try:
                question = prepared[path]
                raw, _ = provider.invoke(question, started)
                decoded = json.loads(raw); schema.validate(decoded, question['schema'])
                answer = decoded['answer']
                parsed = stream(folder/'stdout.bin')
                assert parsed['usage'] and not parsed['errors'] and not parsed['tool_activity']
                result = dict(answer=answer, folder=str(folder), error=None)
            except Exception as exc:
                stop.set()
                result = dict(folder=str(folder), error=str(exc))
            print(json.dumps(dict(call=Path(path).parent.name, error=result['error'])), flush=True)
            return result
        # One batch; no exact-fix retries or separate model-based grading calls.
        with ThreadPoolExecutor(max_workers=3) as pool, (args.run_dir/'results.jsonl').open('x', encoding='utf-8') as out:
            for path, result in zip(prepared, pool.map(run, prepared)):
                for row in rows:
                    if row['question_path'] == path:
                        entry = dict(result, id=row['id'], arm=args.arm,
                                     must_fix=blocking_findings(result.get('answer', {}), row.get('subject')))
                        results.append(entry)
                        out.write(json.dumps(entry, ensure_ascii=False)+'\n')
                out.flush()
    ids = {r['id'] for r in rows}
    assert len(results) == len(ids) and {r['id'] for r in results} == ids
    for key, grade in grades.items():
        assert isinstance(grade['matches_key'], bool) and grade['reason']
        assert key in ids
    report(rows, results, grades, args.output)


if __name__ == '__main__':
    main()
