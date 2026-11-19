TRIAGE FAULT SELDON DESIGN — T-203; STEER's remaining horizon replaced the full wave history.
Root cause: base src/seldon/architecture.py:107 indexes wave 2 into one wave; merge at :102 lost completed wave 1.
Fix: normalize full/remaining STEER waves at answer consumption; retain history; store exceptionType/message/innermost src location, keeping short user text and recovery identity.
Files (6): architecture.py, questions.py, decisions.py; test_journey.py, wave_loop_journey.py, fixtures/shelflife-wave2-steer.json. Src lines 4644 -> 4657 (+13).
Proof: copied slot wave2Detail-2 reproduces IndexError offline; exact recorded JSON replay selects all 3 areas; two-wave base RED28.43s, fixed journey/recovery3P120.23s; all25 module imports PASS.
Gate: bash scripts/gate.sh wave2Detail, venv first PATH, once:64 passed/0 skipped429.99s; no post-gate edits or re-gate; patch reverse-check/diff-check PASS.
Fixture: exact call-f441e70b17e9429894404c54b578e150/answer.txt; journey translates domain handles. No recorded wave-2 DETAIL answer exists: failure preceded its call; executable DETAIL retained.
Base: supplied e4543c9 tree equals canonical deaad8d b5706478e27ff20cc4a2e4c67b20b0752b81bb2b. No providers/commit/.env reads; temp only wave2Detail-<n>; main landing and native validation remain.
