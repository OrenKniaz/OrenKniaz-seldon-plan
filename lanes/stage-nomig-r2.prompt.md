CC — nomig round 2 (small). Patch d69d4da7 is independently APPROVED. Host gate: test_module_size failed (your focused runs missed this guard):
  acceptance_revision.py count 116, ceiling 164 (ratchet ceiling down to current)
  acceptance_runs.py count 304, ceiling 365 (ratchet ceiling down to current)
  mcp_planner.py count 280, ceiling 278 (grew: do not raise)
  plan_store.py count 851, ceiling 834 (grew: do not raise)
Fix: lower the two shrunk ceilings and TOTAL_CEILING to the real new total; bring mcp_planner and plan_store to at or below their ceilings by moving the refusal/format-admission logic into a small focused module or by real simplification (no line joining). Then run ONLY tests/python/core/test_module_size.py and test_suite_budget plus the refusal journey (basetemp C:/seldon/tests/nomig). NO full gate. (The other gate failure, http-domains provider timed-out, overlapped another lane and is not yours unless it recurs.) Update stage-nomig.patch + .sha256; append "Round 2". Final: SHA, delta, guard line. NO LANE-LOCAL SHAS; no commit/push.
