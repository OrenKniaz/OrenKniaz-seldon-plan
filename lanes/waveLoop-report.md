TRIAGE FAULT SELDON
DESIGN: R10/R11/R17 progressive waves; planning continues while check-in answers hold work and C.
Removed: one-wave finish, later B repeats, per-run repair, repair clearing consent, revision-bound fixups.
Files: run.py, plan_review.py, fixups.py; test_journey.py, test_front_door.py, wave_loop_journey.py.
Src Python: 4290 -> 4334 (+44); cases 46 -> 49; diff vs supplied base 9fe54fd (wavePlan included).
Gate ONCE: bash scripts/gate.sh waveLoop, venv first PATH; 49 failed/55.00s (56.77s wall), missing decisions.holds; no re-gate.
Composite askUser sources in memory: two-wave C, real kill/reopen, old-check owner repair, per-wave review and C steer to wave 3 pass; scope/retained planning pass.
BLOCKED: T-199 needs protected askUser integration; T-196/T-197 waiver words break plan.built on further waves. No protected edits, real providers, commit or .env reads.
