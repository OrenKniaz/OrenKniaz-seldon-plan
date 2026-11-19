CC — round 4. Re-review of 7a1e592f: REJECT (lanes/stage-pub1-reviewH2.md). Prior P1 (request->binding) and P2 are CLOSED; recov1, verdict consumption and delivery identity confirmed intact — keep them.

P1 — Crash before ROOT request publication remains unrecoverable. planner_jobs.py:240 reattaches the existing directory without completing its missing request; run_loop.py:481 skips recovery disposition; planner_recovery.py:147 retains the same admission identity; ordinary continuation reselects that incomplete directory; NEXT calls inspection at run_loop.py:940 which reads the missing request at planner_recovery.py:163; repair/replan also requires it at run_loop.py:897. Must recover with no manual filesystem repair and no change to accepted work.
Rule: an admission without its root request never entered — complete or discard it at the single admission owner, then ordinary continuation proceeds. Prefer the shorter: treat a directory without a request as not-admitted (same rule as recov1: no write-ahead marker means not entered), so reattach re-admits rather than reselects.

Test: the root fault twin at tests/python/core/test_golden_path.py:421/:4251 currently returns after asserting STEER/held (:4262) — extend it through supported continuation to accepted C. Pending alone proves nothing.

This is the last kill-point round: enumerate every write in admission in order (root dir -> root request -> segment dir -> segment request -> binding -> Popen -> launch receipt -> entry -> terminal -> cleanup) in your report as a table: kill here -> what restart does -> which twin proves it (or "same branch as row N"). Any row without a defined outcome is a finding you must fix.

Do NOT edit source during a gate (your last gate was invalidated by a mid-gate edit). Freeze, then run ONE full gate (tag pub1d). rev1 may load the host; report pure timeouts separately. Update stage-pub1.patch + .sha256; append "Round 4". Final: SHA, delta, gate line. NO LANE-LOCAL SHAS; no commit/push.
