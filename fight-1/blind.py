"""Randomize two contender directories and produce a label-only comparison."""
import argparse
import json
from pathlib import Path
import secrets

from oracle import HERE, Oracle, TESTS


def compare(results):
    by_label = {r['label']: r for r in results}
    checks = list(dict.fromkeys(c['check'] for r in results for c in r['checks']))
    lines = ['# ShelfLife blind comparison', '',
             '| Check | A | B |', '|---|---|---|']
    for name in checks:
        values = []
        for label in ('A', 'B'):
            found = next((c for c in by_label[label]['checks'] if c['check'] == name), None)
            values.append(found['status'].upper() if found else 'UNVERIFIED')
        lines.append('| ' + name.replace('|', '/') + ' | ' + ' | '.join(values) + ' |')
    for status in ('pass', 'fail', 'unverified'):
        lines.append(f'| Total {status} | {by_label["A"]["totals"][status]} | {by_label["B"]["totals"][status]} |')
    lines += ['', 'Evidence: oracle-A.json and oracle-B.json. Screenshots: A-375.png, A-1440.png, B-375.png, B-1440.png in the isolated tests folder.',
              'Unverified checks earn no pass credit. Visual design and contrast require blind screenshot review.',
              'The private assignment key is excluded from this comparison.']
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('first', type=Path)
    parser.add_argument('second', type=Path)
    args = parser.parse_args()
    products = [args.first.resolve(), args.second.resolve()]
    if not all(p.is_dir() for p in products):
        parser.error('both product directories must exist')
    if products[0] == products[1]:
        parser.error('supply two different product directories')
    key = HERE / 'blind-key.json'
    if key.exists() or any((TESTS / label).exists() for label in ('A', 'B')):
        parser.error('existing blind key or A/B test copies; preserve them and use a clean evaluation workspace')
    secrets.SystemRandom().shuffle(products)
    # Exclusive creation prevents silently changing a previously issued assignment.
    with key.open('x', encoding='utf-8') as stream:
        json.dump({'private': 'CC only; do not share with blind reviewers',
                   'assignments': dict(zip(('A', 'B'), map(str, products)))}, stream, indent=2)
        stream.write('\n')
    results = [Oracle(product, label).run() for label, product in zip(('A', 'B'), products)]
    (HERE / 'compare.md').write_text(compare(results), encoding='utf-8')
    print('Blind comparison written: compare.md (labels A/B only)')
    return int(any(r['totals']['fail'] for r in results))


if __name__ == '__main__':
    raise SystemExit(main())
