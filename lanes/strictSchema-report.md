TRIAGE FAULT SELDON
DESIGN: STEER overwrote the strict builder's required fields; permissive stubs hid the 400, and fault recovery encouraged repeated retries.
Removed: optional-required override and fixed retry-first bypass; empty change arrays use the existing merge, all answer objects remain builder-owned and closed.
Files: src/seldon/{schema,questions,decisions,run}.py; tests/seldon/{test_journey,wave_loop_journey,test_front_door}.py (7 files).
src lines: 4627 -> 4644 (+17); Python 4548 -> 4565. Existing recovery history tracks identical causes, ignoring changing receipt wrappers; no new state fields/caps/product validator.
Behaviour: base STEER RED with exact 400 -> strict-stub two-wave scripted C; provider fault -> planner -> identical fault -> recommended Stop/pause -> reopen/retry. Cold imports: 25 PASS.
Gate: sole bash scripts/gate.sh strictSchema, venv first PATH: 64 passed (base 64), 0 skipped, 381.23s suite/383.09s wall; longest test 194.31s. No post-gate fixes/re-gate.
Base 8fd8743 tree matches supplied 26e185c; patch applies to base. T-201 delivered/uncommitted; lead landing/native validation remain. No real provider calls, .env reads or >5min hang.
