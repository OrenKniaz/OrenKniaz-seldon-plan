TRIAGE FAULT SELDON BUG — src/seldon/plan_review.py:15 and src/seldon/judgment.py:15 paired planner order with area nodes key-sorted by src/seldon/store.py:16-17.
u01 r40 gave import the interface unit and r52 flagged interface as ownerless. The recorded and permuted plans exposed the swap in both question producers on the base.
Fix uses each outline area's handle for REVIEW ownership and final commitment evidence. The zip audit found no other independent plan-collection joins.
Files changed are src/seldon/judgment.py, src/seldon/plan_review.py, tests/seldon/test_journey.py and tests/seldon/fixtures/shelflife-u01-area-join.json.
The strict-schema u01 replay went RED → GREEN and verified subject units, commitments, checks and final observation routing. Final observations were scripted because u01 stopped before validation.
Source lines 4898 → 4896. The checkout tree matches fd51495. Patch forward and reverse apply checks passed. All 27 cold imports passed.
Single full gate `bash scripts/gate.sh areaJoin` ran with the venv first on PATH and passed 77 tests in 332.31 s. T-209 awaits main landing and live confirmation.
