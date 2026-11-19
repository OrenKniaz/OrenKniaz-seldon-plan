LANE no-caps (ticket T-131). Worktree ~/codex-harness/work/lanes/judge-split (Seldon main after T-130/T-132). Temp only under C:/seldon/tests/jsplit-<n>. Do NOT run scripts/gate.sh (the lead gates serially). Prove with the narrowest journeys: `python -m pytest -x -q tests/seldon -k <narrowest test> -p no:cacheprovider --basetemp=C:/seldon/tests/jsplit-<n>/pytest` with ~/codex-harness/.venv/Scripts first on PATH. Do not commit. No new dependencies. Do not edit CHARTER.md or BLUEPRINT.md. Behaviour-only journeys, no unit tests. No real provider calls.

OWNER DECISION (Oren, 2026-11-13, binding): no hard size budgets anywhere in a run. A question is never refused, failed or sent back for being large. Runs finish; size is measured and reported so we learn where to improve efficiency later. CHARTER non-goals already say "budgets in v1" and BLUEPRINT §5 drops "the 64 KB error as a limit"; the code drifted.

TRIAGE: DESIGN. f02 on ad3a8a6: u002 FAILED "JUDGE brief is 84772 bytes (limit 65536); reduce the scoped text"; the REWORK also made workers delete tests and product to fit (f02 u002 checks 48.5->25.6 KB; f01 u001/u004 "passed" by shrinking). Context: ~/codex-harness/work/ladder/design-review/build-stage-2026-11-13-fable.md section 2 (diagnosis only; its split design is NOT wanted now).
RULE: size is a measurement, never a gate.

DELETE (this lane is mostly deletion; net lines must go down):
- questions.bounded_unit and every call to it; the UnitTooLarge class and every except/arm that catches it (units.run_unit, inference.call, judgment, refresh_units, anywhere else).
- inference.call `max_bytes` and the "FACTS corrections exceed twice the original subject brief" refusal, and every caller passing max_bytes (judgment.py, flow_review.py, the JUDGE uncertain re-ask limit).
- Any prompt or exact-failure text telling a worker or planner to reduce, shrink or narrow scoped text because of size.
- Test assertions that require a size refusal or a shrink (big-source, big-product, product-source-oversize and similar): replace each with the outcome twin below, do not keep the old expectation.
Grep src/seldon for 65536, max_bytes, UnitTooLarge, "limit", "exceeds" to be sure nothing is left. Do NOT touch retry/recovery counts or provider timeouts (separate ticket).
KEEP measuring: the run report already prints "Largest questions (bytes)" per kind; keep it. The 1-vs-50 REVIEW bytes test assertion is a dev measurement and stays.
JOURNEYS (outcome only): twin = a unit whose check sources + product make the JUDGE brief > 100 KB -> one JUDGE call, unit DONE, recoveries 0, one WORK launch, product and check bytes at P unchanged from the worker's return, and the largest JUDGE size appears in the report. Fault twin = same with a planning subject > 100 KB (ARCHITECT or DETAIL) -> run reaches B, no refusal.
LEAD DECISIONS THAT MUST SURVIVE: everything on main (v1.6 Rules 1-2, owner-only repair, T-126 base-only, T-130 user words, T-132 providers, plan.owners, P10, FLOW, judge-minimal, timing asserts, recorded replays reaching B or C; re-record changed replay questions only through the existing recorder and say so).
DELIVER in ~/codex-harness/work/lanes: judge-split.patch (git diff --binary incl. new files), judge-split-report.md at most 8 lines: TRIAGE line, files and net lines, each deleted cap, journey command and seconds, anything wrong.
