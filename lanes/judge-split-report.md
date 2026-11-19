TRIAGE: DESIGN — T-131; binding R15 deletion-only correction on 8b6f2bf; split additions fully reverted.
Files: src/seldon/{questions,units,inference,judgment,flow_review}.py; tests/seldon/test_journey.py; +42/-79, net -37; src net -36.
Deleted bounded_unit/UnitTooLarge, WORK/JUDGE/ARCHITECT/DETAIL size refusals, max_bytes and all twice-original refusals/catches; byte measurements retained.
Journey: 1 passed, 18 deselected, 14.93 s; one 253422-byte JUDGE, DONE, recoveries 0, one WORK, check/product bytes unchanged through C.
python -m pytest -x -q tests/seldon -k test_large_judge_journey -p no:cacheprovider --basetemp=C:/seldon/tests/jsplit-6/pytest
Environment: C:/Users/oren/codex-harness/.venv/Scripts first on PATH; PYTHONPATH=src;tests/seldon; TEMP/TMP/TMPDIR=C:/seldon/tests/jsplit-6.
Grep: no brief caps, max_bytes parameter or UnitTooLarge; broad matches remain only processes.py:205 IO chunk 65536 and providers.py:157 project_doc_max_bytes=0 (unrelated owners).
No commit/providers/dependencies/full gate; replays unchanged. Tracking update/validator blocked by PermissionError on ladder/STATUS.json; lead serial gate pending.
