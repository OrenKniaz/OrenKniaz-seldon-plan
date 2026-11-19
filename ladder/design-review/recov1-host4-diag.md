CHARTER: serves C2/C18/C23/C25 — violates no I#.

**TRIAGE: DESIGN — the twin requires an intermediate launch order the product does not promise.** Explicit resume succeeded; subsequent recovery exhausted its allowance before the selected packet hook ran. Verified source HEAD: `4e2c055`. No tests or edits.

1. **Exact ordering**

   The [logged recovery chain](~/codex-harness/work/ladder/design-review/publish-recov1c-red.log:721), oldest first:

   - **Pause:** publication `820df…` receives `steer`. User-control cleanup deliberately does this: [run_loop.py:528](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_loop.py:528).
   - **Explicit resume succeeds:** `820df… → 5aea…`, with `steeringJudgmentId=b9b47…`. Continue resolves the paused disposition into readmission: [run_loop.py:465](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_loop.py:465). This readmission is excluded from automatic-recovery counting: [planner_recovery.py:328](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_recovery.py:328).
   - **Automatic recovery #1:** C fails normally in `5aea… → d381…`.
   - **Automatic recovery #2:** `d381…` loses its controller **before payload entry**; its outcomes are B/C “not launched.” Missing beads become fault outcomes, with launch certainty true before `started.json`: [planner_jobs.py:485](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_jobs.py:485). Activation recovery readmits it as `7cb…`: [run_loop.py:604](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_loop.py:604).
   - **Hook skipped, then exhaustion:** this is the `afterReadmission=1` twin. Its packet hook requires the **global count to equal exactly 1**: [test_golden_path.py:430](~/codex-harness/work/sprint-20261027/semantic-cc/tests/python/core/test_golden_path.py:430). `d381…` never reaches it; `7cb…` sees count **2**, skips it, and C fails normally. Recovery therefore selects `steer`: [planner_recovery.py:340](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_recovery.py:340).

   `held=false` permits recovery; it does **not** override exhaustion. `afterPermission=STEER` is later presentation of the unanswered planner question: [run_loop.py:1380](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_loop.py:1380).

2. **Product bug or test race?**

   **The packet assertion is an order-sensitive test defect.** C18 includes crashes/stalls; it does not promise every readmission reaches packet construction. The log proves resume and two automatic readmissions, followed by correctly bound exhaustion.

   **Why `d381…` disappeared remains unresolved.** It could independently expose a product/runtime defect. Empty controller stderr and this dump cannot establish its cause. Ordinary expiry is implausible: approval-to-exhaustion took about **42 seconds**, while each build admission receives **540 seconds** here ([run_loop.py:987](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_loop.py:987)).

3. **Sibling orderings**

   The same ordinal assumption breaks when a resumed successor dies before entry, expires before packet construction, or another legitimate same-work recovery consumes the selected ordinal. An unrelated recovery can also perturb this hook because it counts globally. Genuine unknown-launch and permission-denial holds are separate valid outcomes; they must retain their actual classification.

4. **One simplest rule**

   **Bind verification to canonical same-work outcomes, never to a presumed intermediate recovery ordinal.**

   | Ownership | Rule / tradeoff | Estimated delta |
   |---|---|---|
   | **CODE — golden twin** | Assert retained resume → two automatic same-work readmissions → bound exhaustion → successful continuation after repair/direction. Preserves the product promise without requiring every admission to launch. | **0 production lines; approximately 30–50 test lines changed** |

   Keep packet-boundary coverage by acknowledging injection at an actual selected packet entry, independent of the global counter. **An uninjected journey cannot count as packet-fault coverage.** No new recovery counter, lock, or production exception is justified by this dump.

5. **Load dependence**

   **Plausible, but not established.** A quiet rerun may avoid the intervening controller loss and pass. There is insufficient evidence to call that *likely*, and a pass would not explain the disappearance or repair the twin’s ordering assumption.