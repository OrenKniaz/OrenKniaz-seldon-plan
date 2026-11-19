DIAGNOSIS (read-only; Seldon delivery). Real-provider ShelfLife round 5, Seldon = main 6114561 + exec1 candidate (source ~/codex-harness/work/lanes/stage-exec1). Summary ./fight-seldon.json: BLOCKED-roundtable after 1197s, 0 user decisions, 12-turn limit; refusals spine-trace-invalid, plan-b-prerequisites-missing, plan-spine-stale, successful-review-required, plan-b-consent-required, tool-input-or-operation-error x5. Final planner message: "browser-tool access must be restored before Seldon's required review can proceed. I cannot enable that permission myself." Log ./run-seldon-r5.log; slot C:/seldon/runs/fight-1/seldon/20261105T221825-fe39ab-001-shelflife. Round 4 (./r4-diag.md, ./fight-seldon-r4.json) PASSED review and reached execute with the same brief.
Answer ≤25 lines:
1. Exactly what blocked review: which tool/reviewer call, error text, which Seldon module/line or which provider/config. Who needed "browser-tool access" — a reviewer subprocess, the planner, or a Seldon check? Why did round 4 not hit it?
2. TRIAGE: BUG|DESIGN — why — siblings. Seldon defect, provider/environment, or the planner misreading an error? Was a required review ever launched?
3. The 5 tool errors and the spine/trace refusals: same cause or different (one line each).
4. Did the run waste its turns on avoidable loops? Is 12 turns a sensible cap for the simulated user?
5. One concrete fix per distinct cause, with owner (Seldon module, fight harness, or environment). Never suggest changing OS security settings.
No files changed, no tests, no provider launches.
