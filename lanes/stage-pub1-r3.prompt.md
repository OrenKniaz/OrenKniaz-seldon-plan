CC — round 3. Independent Sol high review of af0e0cd6: REJECT (lanes/stage-pub1-reviewH.md). Both are crash windows the PUB1 rule must close:

P1 — Admission unrecoverable between request publication and cursor binding. planner_jobs.py:592, planner_recovery.py:34. Kill after the segment request is written but before its binding commits: latest_segment() returns the job directory, pointing recovery at root records instead of the admitted segment; cleanup expects segment fields absent from the job request; recovery raises instead of settling the admission. Your admission twin only holds/releases the writer — it must cover death + restart at exactly this point.

P2 — Interrupted revalidation resurrects an earlier completed status. planner_jobs.py:401, run_loop.py:679. After PASS, refresh verification, publish the new pending run/selection, then kill before complete_continuation(). Restart quarantines and clears the effect, disabling the pending guard; public status reports the old terminal's `completed` while projecting the new pending run. Pending must survive loss of the active cursor. Existing twins kill after outcome publication and miss this gap.

Rule (unchanged): incomplete publications stay PENDING and RECOVERABLE; completion is bound to the selected outcome; a crash between any two writes never yields a wrong claim, a raise, or a permanent stall. Fix at the owners; no new framework/store/lock/counter. Check siblings: every other kill point between two writes in the items you changed.

Add fault twins (journey, outcome-only) that kill at exactly these two windows and restart: P1 -> admission settles (readmit or held per recov1 rules), never raises; P2 -> status stays pending for the new publication, never reports the old completed, and the run continues.

Focused runs only (basetemp C:/seldon/tests/pub1c), plus at most ONE full gate if focused pass (tag pub1c; rev1 may load the host — report pure timeouts separately). Update stage-pub1.patch + .sha256; append "Round 3" to the report. Final: SHA, delta, focused + gate line. NO LANE-LOCAL SHAS; no commit/push.
