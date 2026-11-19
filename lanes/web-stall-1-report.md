CHARTER: serves C18/C26 — violates no I#; existing DV4/DV9 remain.
TRIAGE: BUG — idle sleep suspended work/watchdogs; siblings: cockpit fetch, status poll, golden pipe/startup/cleanup waits.
BLOCKED: host suspension exhausted the 150-minute wall timebox; candidate UNVALIDATED; run-3 tree termination denied, cleanup unverified.

| Run | Tree | Duration (s) | Outcome |
| --- | --- | ---: | --- |
| 1 | unchanged 2p | 266.66 | PASS |
| 2 | pre-2p scratch clone | 269.58 | PASS; also WinError 10053 |
| 3 | 2p + held-request probe | 3102.12 wrapper / 12300.34 pytest | TIMEOUT / FAIL before cockpit probe; host slept |
Root: Kernel-Power 507 records 3642.75+2642.43s asleep in retained 6548s run, and 3631.53s in 3790s run; no evidence of a 2p-specific process/socket leak.
Fix candidate: scoped Windows idle-sleep inhibition/restoration in audit_process; bounded cockpit fetch/readback, status polls, golden RPC writes/replies, HTTP startup and teardown; no global settings changed.
Validation: changed Python/JS syntax and git diff --check pass; held-request RED not reached; ZERO post-edit web passes; full golden gate NOT RUN. Next: required three <=360s passes, then one green <=600s gate.
Versus HEAD~1, including 2p: PROD +35/-22 (net +13) · TEST +172/-77 (net +95); DOC/CONFIG +50/-0; test cases unchanged, runtime acceptance unproven.
Combined replacement candidate: web-stall-1.patch; SHA256 fc659783dcd960f58de623addaf0a2163d2b768db5acbdfa6b33b47c4bddfdd5. No pushes; do not promote before the missing proof.
