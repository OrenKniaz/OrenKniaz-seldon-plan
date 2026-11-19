TRIAGE FAULT SELDON
DESIGN: shared M3 contracts only; T-194 (T-193 belongs to mergeFix); base 7ee32618fa5351e5655da120bcc52ede7cad5f17.
Removed: VISION unknowns and obsolete DECIDE prompt; recordings adapted to the new answer shapes.
Files: four owned src files; test_journey.py, test_front_door.py and four recordings.
Src lines: 4261 -> 4278 (+31/-14); no new states, question kinds, validators or caps.
Gate: bash scripts/gate.sh freeze, venv first PATH: 43 passed, 1 failed, 437.42s; no >5min hang.
Post-gate: front-door test waited for gate state before its request; helper fixed test-only, AST checked; not re-gated.
Bridge: CHECK-IN approve retained until wiring; DECIDE remains superset. No providers/commit/.env reads; temp freeze-1.
