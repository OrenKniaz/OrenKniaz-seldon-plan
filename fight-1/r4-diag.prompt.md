DIAGNOSIS (read-only; Seldon delivery). Real-provider ShelfLife run, round 4, on Seldon main 6114561 (source: ~/codex-harness/work/sprint-20261027/semantic-cc). Run summary: ./fight-seldon.json (outcome BLOCKED-execute after 1221s, 4 user decisions, 83 planner MCP calls, 12-turn limit; refusals plan-b-prerequisites-missing x1, plan-b-consent-required x1, tool-input-or-operation-error x5). Final planner message: blocker D2, "Has the Seldon controller been repaired, or is there a supported diagnostic route?". Run log ./run-seldon-r4.log; project slot C:/seldon/runs/fight-1/seldon/20261105T202544-ab7852-001-shelflife (plan/ holds the store and receipts). Previous rounds: round3 files in this folder.
Answer, ≤25 lines:
1. What exactly failed at execute: which tool call(s), error text, which Seldon module/line raised it (file:line in semantic-cc).
2. TRIAGE: BUG|DESIGN — why — sibling cases. Is it a Seldon defect, a provider/environment issue, or the planner misusing a tool? Did the run ever launch a worker?
3. The 5 tool-input-or-operation-errors: same cause or different? One line each.
4. Is any of this already addressed by in-flight lanes: 2b (budgets deleted, launch auth via planner_jobs/attempt_provenance), 2d (bounded lifetimes/recovery), 2a2 (pending findings hold publication)?
5. One concrete fix (owner module) per distinct cause.
No files changed, no tests, no provider launches.
