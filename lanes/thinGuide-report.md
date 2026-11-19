TRIAGE: BUG — guide paths ran before generated outputs existed; cleanup between steps erased walkthrough state.
Fix: run real JSON/argv steps in order in one disposable checkout, paths last, clean afterward; PRODUCT still excludes guide:paths.
Files: src/seldon/guide.py, src/seldon/proof.py, tests/seldon/test_journey.py; src +8/-8 net 0 vs base 7c0e141475f9a915736ec212883f5e6aaf6b5211.
RED: generated-path/dependent-step journey failed on base source (1 failed/20 deselected,21.20s); no fixtures changed.
Command: venv/Scripts first on PATH; PYTHONPATH="src;tests/seldon"; python -m pytest -x -q tests/seldon -k "guide_walkthrough_journey or clean_core_golden or check_kit" -p no:cacheprovider --basetemp=C:/seldon/tests/thinGuide-2/pytest
Result: 4 passed/17 deselected in76.78s; collection20->21; thin has no clean_core_golden; diff/reverse-apply checks pass; T-183 updated, lead landing pending; no commit/provider calls/.env reads.
