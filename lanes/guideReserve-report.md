TRIAGE FAULT SELDON BUG — T-228, related to T-223.
Root cause `src/seldon/plan.py:366` on 6433526 refused a redundant guide claim before binding the product unit's scope.
ARCHITECT and DETAIL remove and record overlapping scope entries, preserve the guide owner and area, and ask for a product path if the scope empties.
Files `src/seldon/{plan,architecture,detail,run}.py`, `tests/seldon/test_journey.py`, and `tests/seldon/fixtures/quietbench-q01-guide-scopes.json`.
Tracked `src/seldon` lines 5,933 → 5,948. Patch applies to canonical 6433526, whose tree matches the lane snapshot.
Exact q01 wave-one replan answers r239/r385 replayed at the wave-two boundary. Base RED matched the refusal. Strict GREEN reached EXECUTE with the page paths and guide owner intact. Guide-only repeated through planner correction to user pause.
Sole bare gate `bash scripts/gate.sh guideReserve` passed 103 tests in 352.09 s. All 27 cold imports passed.
Main landing and a real Terra rerun remain pending.
