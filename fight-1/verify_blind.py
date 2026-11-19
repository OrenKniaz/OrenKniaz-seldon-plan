"""Smoke: blind assignment and label-only reporting from two real fixture runs.

Protects against leaking input identities or evaluating only one contender.
The single-product oracle smoke and fake-Codex runs do not cover this boundary.
No mocked product answers: both copied fixtures serve HTTP and run in Chromium.
"""
import json
from pathlib import Path
import shutil
import sys
import time
import uuid

import blind
import oracle


def main():
    suffix = time.strftime('%Y%m%dT%H%M%S') + '-' + uuid.uuid4().hex[:6]
    output = oracle.HERE / 'blind-smoke' / suffix
    isolated = oracle.TESTS / 'blind-smoke' / suffix
    output.mkdir(parents=True)
    isolated.mkdir(parents=True)
    first = oracle.TESTS / 'fake'
    second = isolated / 'other-fixture'
    shutil.copytree(first, second, ignore=shutil.ignore_patterns('__pycache__'))
    # Configure only smoke output roots; the oracle and products remain real.
    blind.HERE = oracle.HERE = output
    blind.TESTS = oracle.TESTS = isolated
    sys.argv = ['blind.py', str(first), str(second)]
    assert blind.main() == 0
    key = json.loads((output / 'blind-key.json').read_text(encoding='utf-8'))
    assert set(key['assignments']) == {'A', 'B'}
    assert set(key['assignments'].values()) == {str(first.resolve()), str(second.resolve())}
    table = (output / 'compare.md').read_text(encoding='utf-8')
    assert str(first) not in table and str(second) not in table and 'other-fixture' not in table
    for label in ('A', 'B'):
        result = json.loads((output / f'oracle-{label}.json').read_text(encoding='utf-8'))
        assert result['label'] == label and result['totals']['fail'] == 0
        assert result['totals']['pass'] >= 38
        for width in (375, 1440):
            assert (isolated / f'{label}-{width}.png').stat().st_size > 1000
    print('PASS: two real fake-product evaluations; private A/B key; label-only table; screenshots')
    print('Smoke outputs:', output)


if __name__ == '__main__':
    main()
