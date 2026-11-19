TRIAGE FAULT SELDON + DESIGN — T-184: uncounted worker-question returns and premature local rework of wave-owned gaps.
Removed shackles 2/3/4: keyword lookup/cache; all questions use COACH then recovery.recover; proof-owner JUDGE condition; both discovery-validation calls deleted.
Files: src/seldon/{units.py,inference.py}, tests/seldon/test_journey.py; patch against ee762c2b2f275792b786d936b539e44f9c001826.
Src lines: total 4429 -> 4411 (net -18); units.py 197 -> 181, inference.py 103 -> 101. Journeys prove wave repair and one user question/sibling DONE/reopen/resume.
Commands use PATH=C:/Users/oren/codex-harness/.venv/Scripts first; PYTHONPATH=src;tests/seldon; python -m pytest -x -q <target> -p no:cacheprovider --basetemp=C:/seldon/tests/thinOneWayBack-<n>/pytest.
Focused target tests/seldon/test_journey.py: -k 'question or coach-facts or wave-gap' (n1 setup error; n2 2 passed/1 fixture failure); -k 'wave-gap or repeating_worker' (n3/n4 fixture failures corrected; n5 2 passed, 23.50s).
Full target tests/seldon (n6), once: 23 passed in 305.90s, base 21 -> 23 (+2); progress continued throughout. git diff --check, AST parse and reverse patch check passed.
TICKETS T-184 updated, tracking.py valid; delivered pending lead landing (in_progress per tracking rules). No real providers, gate.sh, commit, .env reads or product acceptance; real-run validation remains with lead.
