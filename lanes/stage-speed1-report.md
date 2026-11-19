TRIAGE: DESIGN — child output was lost to pytest truncation; the intermittent child failure is undiagnosed — sibling cases: HTTP, CLI.
CHARTER: serves C14/C18/C24/C26 — violates no I#.
STATUS: NOT READY TO LAND; diagnostics implemented and three consecutive local GREEN gates <=540s; original publish failure did not reproduce and remains undiagnosed/unfixed.
CAUSE: UNESTABLISHED — retained publish child workspace denies access; its existing pytest log omits the failing child traceback/refusal details.
CHANGE: failed children retain full stdout/stderr in <child-workspace>/journey-failure.log; assertion includes its absolute path and last 60 lines.
R2 RUN 1: 19/19 GREEN, CLI 291.09s + web 193.11s; measured wall 486.28s.
R2 RUN 2: 19/19 GREEN, CLI 300.46s + web 196.27s; measured wall 500.16s.
R2 RUN 3, after last source edit: 19/19 GREEN, CLI 272.95s + web 186.15s; measured wall 461.30s. Three full runs used of five allowed.
PRESERVED: 19 cases and all original journey bodies/assertions, fault twins, cold entries and deadlines; no retries, unit tests, new test files or pushes. PROD: +0/-0 (net 0; dev only) · TEST: +57/-3.
EVIDENCE: C:/seldon/tests/stage-speed1/r2-run{1,2,3}.log and *-timing.json; CC reports real-provider ShelfLife load during failed publish; current provider activity unverified.
PATCH: diff vs 00d3f980dbe86b6c9c04affa77fbcb2b9097373f; ../stage-speed1.patch; SHA256 74f750f9f4d3defd72e3ffd78e83730c2a22ee4100ba7f1823ebe4637bfbeb85; ../stage-speed1.patch.sha256.
NEXT: CC supply a readable copy of failed publish child plan.sqlite3 plus WAL and worker receipts under C:/seldon/tests/stage-speed1/retained-publish; diagnose/fix before treating stability passes as closure.
