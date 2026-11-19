TRIAGE FAULT SELDON
DESIGN: R17 planner before user; concrete choices; dependent work alone waits (T-197).
Removed: fixed unit choices, M3 refusals/hold, and one-shot polling.
Files: decisions.py, recovery.py, scheduler.py, units.py; journey and front-door fixture.
Src Python: 4199 -> 4334 (+135); golden cases 44 -> 52; regression twins fail on supplied base.
Gate askUser ONCE: 52 passed, 471.46s suite/473.01s wall; afterward deleted internal-field assertion, syntax OK, no rerun.
Base: supplied f69cc3f snapshot; assigned 2946398 absent. No delivery commit, real providers or .env reads.
Next/risk: lead integrates waveLoop/validate (dropped-work C, waived progression, unit-stop return guard); real acceptance unproven.
