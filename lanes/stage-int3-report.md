CHARTER: serves C26/C14/C24 — violates no I#.
TRIAGE: DESIGN — older-main overlaps; sibling cases: schema guidance/diagnostics, golden worker fixtures and audit ledger; both lanes retained.
Base: e8235a8eee5186b11107b631f314fa1ab4bbd590; applied EXEC2 ef40ed99a09a1286a6d265704de855176a8b5d07d922e968083890f197b85c55, independently APPROVE-WITH-FOLLOWUPS.
Conflicts: SCHEMA1 examples/nested diagnostics + served schema; main ShelfLife/recovery + served workers/golden assertions; every ledger row retained; aggregate ceiling 34854→34846 (actual), per-file ceilings already exact.
PROD: +191/-193 (net -2); TEST: +81/-6 (net +75); 19 cases vs base 19; no new test files or unit tests.
Gates: single golden file web GREEN/240.40s, cli GREEN/329.79s; full gate 1 GREEN 19/19 (18/386.49s + web 1/193.84s), wall 582.33s <600s; 1 of max 2 full runs used, after last edit.
Risk/next: P2 API-only browser preflight remains deferred; scripted-provider suite evidence only, real-provider/ladder acceptance unperformed; no commit/push.
Patch: ../stage-int3.patch (vs base); SHA256 3108994b6febf98affd81ca3c2fb4725c1d7153d6c39a5919c1345ce2e0352f0; sidecar ../stage-int3.patch.sha256.
