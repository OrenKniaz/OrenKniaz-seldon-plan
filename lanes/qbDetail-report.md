TRIAGE FAULT SELDON + BUG (T-210).
Root cause at src/seldon/architecture.py:126–142. ARCHITECT accepted 0/5/13 commitments across waves 1–3, so detail.py:27/140 merged zero areas and plan.py:308 raised.
Fix keeps existing commitment backfill, then re-asks ARCHITECT if wave 1 selects no area. The correction names the wave goal, area owners, later assignments and what commitment handles to send.
Files are src/seldon/architecture.py, tests/seldon/test_journey.py, tests/seldon/fixtures/quietbench-a01-planning.json and tests/seldon/test_front_door.py.
Source lines 5005 → 5015 (+10), Python 4926 → 4936. Lane snapshot 7a37e3e and canonical 750a352 have the same tree.
Copied store and recorded-answer journey RED with the exact ValueError. Strict golden twins GREEN through EXECUTE and planner/user pause in 4.78 s. All 27 modules cold-imported.
Sole gate bash scripts/gate.sh qbDetail with venv first on PATH yielded 81 passed and 2 front-door marker timeouts in 815.67 s.
T-211 test-only wait guards corrected, 3 affected journeys passed in 68.82 s. Full gate ran once. Main landing and real Quiet Bench validation remain pending.
