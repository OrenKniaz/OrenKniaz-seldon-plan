CHARTER: serves C9/C16/C18; identifies an I1/I10 structure-versus-semantics mismatch. Read-only; no tests or edits. The supplied **r22 artifacts identify `97d059b`**, despite the “round 19” label.

1. **Outcome and reach:** `STALLED-no-progress`, **2,065.516 seconds**, three turns. **A accepted → Spec outline completed → trace failed → planning Steer/repair pending.** No B, Build, post-build Judge, or C; no product files delivered. **17 outer planner MCP calls**; internal records show **16 invocation starts, 14 completions**: 11 planner, one judge, two mechanical. **Zero reported refusal codes**, but repeated structural rejections and two 900-second MCP timeouts. One simulated-user decision, **“yes,”** accepted A; **“Please continue.”** resumed planning. Human identity remained unverified. [Report](fight-seldon-r22.json). The retained oracle reports server startup failure; API/importer/UI remain unverified. [Oracle](oracle-seldon-r22.json).

2. **First failed forward transition:** event **86** asks the LLM to return the complete trace envelope. Response **94** preserves all **43 nodes** but omits **five targets and five scenarios**; **95** rejects membership. Response **102** restores membership but supplies invalid parents; **103** rejects them. Response **110** returns only the 16 requested parent corrections; **111** rejects incomplete membership.

   This exposes the charter mismatch: structural preservation has become repeated LLM work. After continuation, the same sequence recurs at **160–177**. Repair **186** finally preserves everything and corrects the parents, then **187** rejects **`server.py` as an unknown trace handle**. The schema permits arbitrary strings in `codeRefs`, although the canonical contract requires **code-node references**. Evidence: [run database, events table](/C:/seldon/runs/fight-1/seldon/20261108T135743-3e80ed-001-shelflife/.codex-harness/plan.sqlite3), [schema producer](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_schemas.py:77), [consumer](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_content.py:102).

3. **TRIAGE: DESIGN** — the shared question/consumer contract lets the LLM reconstruct deterministic structure and submit structurally impossible choices, then spends retries correcting them. The `server.py` rejection is valid; the weak question contract creates the failure class. **Siblings:** omitted targets/scenarios, partial repairs rejected as deletions, invalid parent kinds, and paths supplied to `codeRefs`/`testRefs`/`resultRefs`. Patching ShelfLife filenames would leave that class intact.

4. **ONE simplest rule:**

   | Owner | Rule | Tradeoff |
   |---|---|---|
   | **CODE** | Retain the canonical trace envelope and ask the LLM only for typed edits whose references are constrained to eligible handles. | Removes structural copying and impossible choices; requires the question schema to use the consumer’s existing field/kind contract. |

5. **Improved versus r21:** source now uses **nonrecursive content revisions** and permits repairs beyond parent fields; r21’s cycle error does not recur in these records. Repair **186** gets beyond parent correction to reference binding. **That is narrower progress, not completed trace integration.** A acceptance, decisions (**1**), and reported refusals (**0**) are unchanged; outer calls fall **18 → 17**, elapsed time rises about **104 seconds**, and delivery remains blocked. [r21 diagnosis](r21-diagnosis.md).

