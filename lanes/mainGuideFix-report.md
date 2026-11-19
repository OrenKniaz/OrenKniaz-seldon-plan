TRIAGE FAULT SELDON | BUG: split guide observations checked generated paths before walkthrough execution and cleaned its checkout between steps; fixture is correct.
Fix: execute real JSON/argv steps in order in one disposable checkout, check paths last, clean afterward; PRODUCT still excludes guide:paths.
Files: src/seldon/{guide,judgment,proof}.py; tests/seldon/{kit_journey,test_journey}.py (includes guideEvidence-main changes).
Src vs base 5afdbc8 (b95331c snapshot): +15/-15, net 0; main semantic-cc test tree also inspected (20 Python files in each snapshot).
RED: same selection with mainGuideFix-2/pytest: walkthrough[False] failed in 28.92s, guide:paths missing fixtures/sample.csv; first -1 attempt was a missing temp-parent setup error.
Command: venv/Scripts first on PATH; PYTHONPATH="src;tests/seldon"; python -m pytest -x -q tests/seldon -k "guide_walkthrough_journey or clean_core_golden or check_kit" -p no:cacheprovider --basetemp=C:/seldon/tests/mainGuideFix-3/pytest
Result: 6 passed, 114 deselected in 757.70s; collection 120 vs base 119 (inherited broken-guide parameter); diff-check and reverse apply-check passed.
Delivery: full diff against 5afdbc8; T-183 updated in place, awaiting lead landing; no commit/providers/.env reads; active proof exceeded 10 min but no five-minute hang.
