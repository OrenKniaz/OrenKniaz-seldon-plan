T-82/T-83: behaviour-only final questions, CODE execution facts, contained guide observations, Git-tree-local verdict retention; no commits/providers/dependencies.
src lines: gitwork 144→156; judgment 180→223; plan 173→176; proof 113→115; questions 255→257.
src lines: run 208→223; schema 93→92; units 166→171; guide 0→34; source net +115.
test lines: test_journey 858→960; run_report 108→111; 43 behaviour journeys completed vs base 38 (one pytest test).
Gate RED: scale 98.59s ≥90; pytest wall 358.65s >270 (suite assertion not reached); both timing assertions preserved. Lint: same 10 findings as base; diff check clean.
Realistic 1/50 units: largest DEMO 3,623/3,623 B; PRODUCT 5,227/5,227 B; retained recorded-source replay DEMO 15,650 B / PRODUCT 16,867 B.
Final calls/bytes before→after: realistic 1: 4/70,643→4/15,937; 50: 53/1,177,210→53/193,464; docs-only fix: 10/34,018→6/22,245 (base replay paths differ).
c01 facts replay: largest DEMO 80,350→28,213 B, PRODUCT 86,205→33,823 B; 20/1,409,005→9/223,328 calls/bytes, excluding its unobservable legacy guide and duplicate unchanged subjects; not a completed rerun.
Rule note: guide walking requires explicit Markdown path links and JSON argv fences; arbitrary Markdown/manual interactions cannot be CODE-observed as execution. Legacy c01 guide is blocked; no observation fabricated.
Evidence: C:/seldon/tests/behav-{5,9,10}; patch vs 731f336, owner constants unchanged. Read-only .git denied add -N; new guide included via read-only no-index diff; no denied-action retry. Next: T-77 timing.
