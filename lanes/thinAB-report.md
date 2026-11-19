Merged A+B journeys: parallel-contract wave gap publishes before repair; COACH facts; repeating-question user wait/reopen/resume; docstring and discovery assertion.
Removed unused questions.validate_discoveries and test_journey.py.rej; no other new src edits beyond supplied B changes. Src Python lines: 4389 -> 4365 (-24 vs lane A).
Environment: ~/codex-harness/.venv/Scripts first on PATH; PYTHONPATH="src;tests/seldon".
python -m pytest -x -q tests/seldon -p no:cacheprovider --basetemp=C:/seldon/tests/thinAB-2/pytest => 23 passed in 327.84s (base 21 -> 23); no hang.
Initial thinAB-1 setup error: basetemp parent absent; created thinAB-2 parent and reran. git diff --check passed; no real providers, gate.sh, commit or .env reads.
