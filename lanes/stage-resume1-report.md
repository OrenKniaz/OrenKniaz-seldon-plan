CHARTER: serves C2/C18/C23 — violates no I6/I9.
TRIAGE: DESIGN — controller replacement discarded completed progress; siblings: pre-entry Build loss, successive controller losses, and stale Contracts evidence.
SIMPLEST: resume the earliest unfinished admitted work; retain completed current work with its ORIGINAL evidence and judgment.

| LLM-or-CODE | Owner; benefit / cost |
| --- | --- |
| CODE | planner_jobs owns handoff/outcomes; planner_recovery retains disposition/allowance authority. Deterministic continuation preserves semantic credit; an independent successor repository adds a clone, whose observed crash blocks this candidate. |

NOT READY. Base: canonical Seldon main 2a833b6; all six changed files matched it before edits. No commit/push, shared installation, actual-provider launch, security/settings change, or denied-action retry.

Changed: src/codex_harness/core/{audit_process,planner_jobs,planner_recovery,run_loop}.py; tests/python/core/test_golden_path.py; docs/legacy-capability-audit.md. Deleted files: 0.

| Delta | Added / deleted | Net |
| --- | --- | --- |
| Source, 4 files | +81 / -39 | +42 |
| Tests, 1 file | +66 / -32 | +34 |
| Discovery ledger, 1 file | +23 / -0 | +23 |

Source: 32,097 -> 32,139; existing ceiling unchanged. Pytest cases: 12 -> 12, zero new cases; ceiling 19 unchanged. No unit tests. The extended controller twins use the existing HTTP parallel parent slot and are removed from the main CLI journey.

The handoff seeds a successor-confined run/repository while completed beads retain original attempt paths, receipts and judgment bindings. Judgment/revision/verifier/receipt/observation freshness rejects stale reuse. The run/job guard in attempt_provenance is unchanged. Recovery proof retains the triggering raw process probe. No added sleep/grace period or change to the two-recovery bound, denial/unknown-launch HOLD, sole recovery decider, or PUB1 terminal-last rule.

Gate: FAILED, exit 1 — 9 passed, 2 failed in 817.26s; browser 1 skipped in 4.68s. Gate log wall span: 823.59s; exceeds the 600s target. Pure timeouts: 0.
Exactly one invocation: `bash ~/codex-harness/work/lanes/golden-gate.sh ~/codex-harness/work/lanes/stage-resume1 resume1`.
Log: golden-resume1.log. Temporary evidence: C:/seldon/tests/resume1. Source/tests remained byte-identical to the pre-gate freeze; only ledger/report prose changed afterward. Syntax, diff whitespace, and reverse patch applicability checks passed.

- TRIAGE: BUG — http-domains failed in the new handoff: Git clone returned 3221225477 (0xC0000005). No cause guess or retry. Raw command/stderr: C:/seldon/tests/resume1/p/popen-gw0/w0-controller-False-False/.codex-harness/worker-jobs/9e36a9ae71d9/runs/05306b98bb78/evidence/git-failures.jsonl. Successor dispatch and current/stale interruption journeys to C remain unproven; the stale and separate entered-controller variants were not reached after this first failure.
- TRIAGE: DESIGN — recovery-twin-2 still expects completed Contracts work in faultWork after Build entry (test_golden_path.py:4708). Retained proof has Contracts admitted, Build-only faultWork, unknown launch, and abandon/HOLD. Update this obsolete ownership expectation to unfinished Build while retaining the HOLD checks; no assertion was weakened after the gate.
- Browser: UNVERIFIED, skipped on Chromium launch failure. The retained diagnostic includes GPU-process failure and Access denied during browser cleanup; the outer owned Job reports quiescence with zero remaining processes. Diagnostic: C:/seldon/tests/resume1/w/web-browser-readiness.json. No privilege repair or retry.

Last proven product outcome: ordinary CLI reaches C, including denial zero-readmission and recovery checks. The new forced pre-entry loss charges only Build and retains processObservation={running:false, identity:null, openProcessError:87}. This identifies the probe branch, not the historical controller-death cause. Full successor continuation, stale-evidence rerun to C, browser and actual-provider/full-vision acceptance are not established.

Next: repair the clone handoff and the old twin's work-identity expectation, then validate a revised candidate with a newly authorized gate. This frozen failed candidate is delivered without a second gate.

Patch SHA256: ce8d0efa09a75bd411b37e00139502a51ad751c69f2aad6628773bef8afc9084
Artifacts: stage-resume1.patch; stage-resume1.sha256; stage-resume1-report.md.

Round 2

CHARTER: serves C2/C18/C23 — violates no I6/I9.
TRIAGE: DESIGN — replace clone/seeding with a recorded handoff of the existing admitted job/run/repository.
SIMPLEST: revoked pre-entry controllers resume current admitted progress in place; completed Contracts keeps ORIGINAL evidence and judgment. No clone is required by the guard.

| LLM-or-CODE | Owner; benefit / constraint |
| --- | --- |
| CODE | planner_recovery owns the segment-bound decision and stop release; run_loop consumes it. No copy/clone or widened path guard. Pre-entry ownership fencing permits in-place continuation; stale evidence gets ordinary fresh execution, entered/denied/uncertain work retains HOLD. |

Delta vs canonical base 2a833b6: source +66/-43 = +23 net (32,097 -> 32,120); tests +104/-55 = +49; discovery ledger +47/-0. Same four production files, golden file and ledger as Round 1; zero deleted files/new modules/new pytest cases (12 -> 12). Existing ceilings unchanged. New fault cost uses the existing HTTP parallel parent slot; no additional main-journey steps. Source review: PASS by exactly one independent Tier 2 reviewer, after repairing the direction caller dropping resolved.resumeRun.

Focused: recovery-twin-2 PASS in focused.log. In focused2.log, all three controller twins PASS: same job/repo and one original Contracts attempt/judgment through C after readmit/readmit/steer/direction; stale observation -> new Contracts evidence/judgment -> C; entered-without-outcome -> HOLD. The enclosing fixture failed on a separate ShelfLife path-guard refusal. That child subsequently passed in the one full gate; its original failure remains retained, not relabeled inherited. Logs live under C:/seldon/tests/resume1b.

Gate: FAILED, exit 1. Exactly ONE resume1b gate: 10 passed, 1 failed in 1309.36s; browser 1 skipped in 6.12s. Log wall span 1317.83s; main_path_golden 1122.69s; 600s target missed. Requested controller journeys, recovery-twin-2, denial, ordinary HTTP and ShelfLife passed. Source/tests remained byte-identical after freeze; only report/ledger prose changed afterward. Syntax, whitespace and reverse patch-application checks passed.

Primary blocker: worker-job-path-outside-workspace while answering the hardcoded-receipt judge, tests/python/core/test_golden_path.py:4034, workspace C:/seldon/tests/resume1b/p/popen-gw1/w0/single-build/stub. The dependency-free product had reached C; this later judge subjourney failed. Full traceback: golden-resume1b.log:698. Sibling: focused ShelfLife guard refusal. Cause and candidate attribution are unresolved; the path guard is unchanged and was not weakened. Owner: planner_jobs path confinement/caller. Next: capture the actual rejected path/root/resolution at the owning guard and diagnose the refusal before repair; exit test is both admitted paths completing without refusal or widened confinement.

Pure-timeout gate failures: 0. A later scripted-provider 170-second answer wait expired (fixture exit 3); it is SECONDARY to the path-guard refusal. This corrects the interim timeout diagnosis and is not grounds to relabel the primary failure. No retry/grace timer was added. Browser: UNVERIFIED on Chromium launch failure; diagnostic C:/seldon/tests/resume1b/w/web-browser-readiness.json. No privilege/settings repair.

Last proven changed outcome: current Contracts survives replacement in the ORIGINAL admitted run/repo through C; only unfinished Build is charged, the same-job two-recovery bound holds, stale evidence reruns, and raw liveness probes remain retained. Recov1 write-ahead certainty/HOLD/bound and PUB1 terminal-last rules remain intact. Full-gate acceptance is NOT established because of the guard failure; browser and actual-provider/full-vision acceptance remain unproven. Source stayed frozen and no second gate ran. No commit/push, shared installation or actual-provider launch.

Patch SHA256: 3b3be73e084ae35e1357ef815bf106de81c5c03de55f1717a2a627ea9d4da8d8
Artifacts: stage-resume1.patch; stage-resume1.sha256; stage-resume1-report.md.

Round 3

CHARTER: serves C2/C18/C23 — violates no I6/I9.
TRIAGE: BUG — unavailable/malformed optional originals aborted recovery.
SIMPLEST / CODE: read/parsing/shape failures in retention eligibility leave resume=None and select ordinary fresh execution. Authorization, fencing, outcome publication and stop release are outside the handler. The path guard changes only its message: same error prefix, plus planner_jobs._inside, refused path and owning root; no allowance/predicate change.

Cumulative vs canonical 2a833b6: source +69/-44 = +25 net (Round 3 +2 net); tests +113/-56 = +57 net; ledger +59/-0. Same six changed files, zero deleted files/new modules/new pytest cases (12 -> 12). Existing stale twin extended with actual original receipt deletion/malformed JSON. One independent targeted source review: PASS, no material findings.

Focused receipt journeys: missing-receipt RED observed before repair with Errno 2 (red.log). After repair, missing PASS (missing.log) and malformed PASS (malformed.log): each requires ordinary Contracts rerun, a fresh binding with no inherited judgment, exactly two Contracts attempts, and completion to C.

Delivery alone, twice, sequentially, identical frozen source, no xdist or other test journey:
- Attempt 1: PASS, 1 passed in 563.21s; basetemp C:/seldon/tests/resume1c/d1, delivery-1.log.
- Attempt 2: PASS, 1 passed in 363.00s; basetemp C:/seldon/tests/resume1c/d2, delivery-2.log.
Both commands select only tests/python/core/test_approval_v2_journey.py::test_canonical_plan_contracts_red_build_validation_pass[delivery]. Both complete main delivery, dependency-free C, and the stub-judge rejection. Recorded path-guard refusals across the delivery/single-build/stub databases: zero in each attempt. The earlier failure did NOT reproduce (0/2); neither a patch cause nor a load-only cause is established. The earlier guard issue remains unresolved, with improved diagnostics for any next occurrence. Pure timeouts in these attempts: zero.

Logs/workspaces are under C:/seldon/tests/resume1c. Original source/test bytes remained unchanged throughout both delivery attempts; only ledger/report prose changed afterward. Whitespace and reverse patch-application checks passed. No full gate was run (per instruction); Round 2 remains the last full-gate evidence. No retry/grace timer, guard relaxation, commit/push, shared install or actual-provider launch. Browser/actual-provider/full-vision acceptance is not claimed.

Patch SHA256: 0333bf6f66eccbfe1a73544220f38bf09ac7005f9e7cfe21825774b002522620
Artifacts: stage-resume1.patch; stage-resume1.sha256; stage-resume1-report.md.
