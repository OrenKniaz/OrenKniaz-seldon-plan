TRIAGE: BUG — reported RECOVERY-1 regression is unreproduced; no causal repair claimed — sibling cases: none established.
CC full gate retained: 17/18 batch passed and web passed (241.08s); successor failed with VERIFIED-QUIESCENT but missing controllerAndChildren.stopReason. That original failure remains open.
CC runtime records at C:/seldon/tests/scen-cov-1-pub/p/popen-gw0/w0 are access-denied to this lane. Failed successor inspect/terminal/dispatch records requested; denied access was not retried.
Change this turn: print the actual inspect proof and job record immediately before the existing RECOVERY-1 assertion. worker-stalled, zero-process, poisoned-write and quarantine assertions are unchanged.
No speculative production recovery, graph or spine change: inspect returns the quiescence control unchanged; absence of stopReason alone does not identify the earlier failure.
Only authorized CLI test target ran twice: full PASS in 128.32s; final full PASS in 185.08s AFTER the last tracked-file edit. No source or ledger edits followed the final run.
Printed successful-run proof: stopReason=worker-stalled, membershipVerifiedBeforePayload=true, quiescenceVerified=true, seven processes before teardown and zero afterward; stalled worker had no natural terminal record.
Both full CLI passes include ShelfLife admitted root delivery/C in three decisions and the existing failed-Contracts -> stalled-Build -> completed-readmission journey. This does not reproduce or explain CC’s earlier failure.
Ruff for golden file and git diff --check passed. Suite remains 19 versus base 19; no new test files, other test commands, commits, pushes or real provider launches this turn.
Patch: scen-cov-1.patch; SHA256 154164597cbbf0a5a25737478b22aa8bbe8b724aaacb51df9d0c80a4150f00d7; matching scen-cov-1.patch.sha256 regenerated. Base 7c8923dbed18c9c2e17fe781f20197dfb963964a / main 6b2ba9a.
Next: obtain CC’s failed successor records under the authorized scratch root, identify its actual owning failure, then authorize any further repair/validation. Original full ShelfLife/provider acceptance remains unproven.
