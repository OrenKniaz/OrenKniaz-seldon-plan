TRIAGE: DESIGN — shared provider data imported high-level orchestration — sibling cases: seldon_cli/seldon_mcp/mcp_planner/plan_cli and all installed console entries.
CHARTER: serves C14/C20/C24/C26 — violates no I#.
Changed: worker_packet_budget owns provider capacity; all consumers use it; redundant global maximum deleted. Limits and 1j/consent/retry behavior unchanged.
PROD: +8/-12 (net -4) · TEST: +77/-0 (net +77); audit +27/-0.
Cases versus base: 19/19 passed versus 19; golden 2/2; no new test file or unit test.
Regression/gap: cold installed imports exposed the cycle hidden by provider-host preimports; fresh -I startup covers six installed entries, four modules, init persistence/check/registered MCP/removal.
Observed RED: 1 failed/5.29s; repaired fixture initially misexpected retained-policy deletion/11.65s; corrected focused golden 2 passed/629.06s.
Final: bash ../golden-gate.sh . stage-hot1, after last patch edit, ONE run; exit 0; 18 passed/499.22s + browser 1 passed/175.86s; wall 677.09s.
Acceptance: NOT GREEN against the required ≤600s fast ceiling (miss 77.09s); existing fast marks retained. Behavioral/structural checks all passed; no skips reported.
Patch: ../stage-hot1.patch; exact diff versus lane base 4cf3cd0bb9e33c5793b940c9bd238b1593a8c1cc (base 50a5e3f snapshot); gate log ../golden-stage-hot1.log.
SHA256: 8408ce5ab3fbfc860f4e7b911a3e2ea55d4a519bfd9c3530643bbda006d6c264
Risk/next: shared golden runtime owner must meet 600s without reducing coverage before HOT1 acceptance; actual-provider/host-app/ladder acceptance unproven; no pushes.
