Base 63c503c (owned files identical to 5800d4a); uncommitted patch: 9 files, 2 new, omitted none; apply/readback/reverse-check PASS.
src/seldon lines: architecture.py 67->193, detail.py 0->81, plan.py 202->306, schema.py 120->162.
src/seldon lines: questions.py 306->368, run.py 189->206, states.py 57->58.
Test lines: test_architect.py 0->289, test_journey.py 1951->1959: minimal golden fixture wiring; new behaviour journeys.
Ported area grouping, local ownership/link checks, contract endpoints, exact-file prerequisites and subdivision from frozen abfd4a5/6733da7; no inspections or M3 continuation.
RUN: A -> ARCHITECT -> DETAIL -> REVIEW; one DETAIL contract-gap -> ARCHITECT re-ask; REVIEW/REPAIR and one merged B unchanged.
Gate: 13 passed vs base 13 in 185.81s; golden 144.53s, retained scale50 57.33s; C:/seldon/tests/m2arch-9/gate.log; timing assertions unchanged.
New journeys 38.33s: 3 areas/2 contracts + concurrent scoped DETAIL + reopen -> scripted C 15.94s; gap -> scripted C 20.14s; second gap refuses B 1.09s; oversized split -> B 1.16s; 1/50 plans -> B.
Actual recorded planning-question bytes at 1/50 units: ARCHITECT 3590/3590; DETAIL 11077/11077; retained real-question replay and WORK/JUDGE/FLOW/PRODUCT size bounds PASS.
Wrong/unproven: full gate is 5.81s above the quiet 180s target; 16 inherited lint diagnostics (0 on changed lines); no real ARCHITECT/DETAIL execution. T-105 updated; no commits, dependencies or real providers.
