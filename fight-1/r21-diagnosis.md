CHARTER: serves C9/C16/C18; identifies an I1 structure/semantics mismatch. Read-only; no tests or edits. **The supplied artifacts identify r21 at `aee12fe`, despite the “round 19” label.**

1. **Outcome and reach:** `STALLED-no-progress`, **1,961.641 seconds**, three turns. **A accepted → Spec attempted → planning Steer exhausted → PAUSED.** No B, Build, post-build Judge, or C; no application files delivered. **18 outer planner MCP calls**; **19 internal provider invocations**: 16 planner, one judge, two mechanical. **Zero reported refusal codes**; structural validation repeatedly rejected answers. One simulated-user decision, **“yes”**, accepted A; **“Please continue.”** subsequently resumed planning. Human identity remained unverified. The retained oracle reports startup failure; API/importer/UI remain unverified. [Report](/C:/Users/oren/codex-harness/work/fight-1/fight-seldon-r21.json), [oracle](/C:/Users/oren/codex-harness/work/fight-1/oracle-seldon-r21.json).

2. **First failed forward transition:** after A acceptance at **event 65**, Spec outline succeeds at **83**. Trace response **94** preserves all 46 nodes but drops all **four targets and five scenarios**; **95** rejects membership. Retry **102** restores membership but contains invalid parent kinds; **103** rejects those. Retry **110** returns only 20 nodes; **111** steers.

   **The decisive charter mismatch appears at event 121:** parent repair exposes reciprocal *reference fields*, which CODE rejects as a cycle. Retained response **102** contains:
   `st_ce9041232b.testRefs → te_a7ea42d51e`
   and
   `te_a7ea42d51e.stopConditionRefs → st_ce9041232b`.

   These are verification cross-links. [`run_content.py:136`](/C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_content.py:136) recursively hashes referenced nodes, making their revisions mutually dependent. Meanwhile, the repair consumer changes **only `parents`**, leaving those fields untouched ([line 50](/C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_content.py:50)). Events **129/137** repeat the failure; **138** pauses. Evidence: [run database, events table](/C:/seldon/runs/fight-1/seldon/20261108T110136-a74849-001-shelflife/.codex-harness/plan.sqlite3).

3. **TRIAGE: DESIGN** — revision binding incorrectly requires semantic cross-references to form a DAG, then offers a repair that cannot modify the failing edges. The initial membership errors are real, but do not explain the persistent cycle failure. **Siblings:** test↔decision, test↔stop-condition, and other reciprocal trace references. Changing ShelfLife’s parent choices cannot remove this class.

4. **ONE simplest rule:**

   | Owner | Rule | Tradeoff |
   |---|---|---|
   | **CODE** | Bind trace references to canonical, nonrecursive content revisions; reciprocal semantic links must never recursively determine each other’s revision. | Preserves LLM-owned relationship meaning and deterministic stale detection; requires one shared revision definition across writers and readers. |

5. **Improved versus r20:** Unicode status readback succeeds, the simulated user answers A, scope locks, and Seldon reaches Spec plus automatic steering/resumption. r20 stopped before A could be answered. Decisions improve **0 → 1**, refusals remain **0**, while outer calls rise **2 → 18**. **Delivery remains unproven:** the blocker moved from transport to trace materialization. [r20 diagnosis](/C:/Users/oren/codex-harness/work/fight-1/r20-diagnosis.md).