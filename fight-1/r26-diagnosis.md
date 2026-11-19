CHARTER: serves C9/C16/C18 and I1/I6/I10. Read-only diagnosis of **`8dd872d`**; no tests or edits.

1. **Outcome and reach:** **`STALLED-no-progress`**, **2,031.047 seconds**. **A accepted → Spec outlined → diagnostic Judge/Steer → PAUSED at `plan/trace`.** Spec never persisted: only vision and reviewer-selection nodes remain. No B, Build, post-build Judge, or C; no delivered product files. **20 outer planner MCP calls; 20 internal invocations: 17 planner, 2 mechanical, 1 judge.** Zero reported MCP refusals, but **12 internal answer rejections** and **two no-progress holds**. Two simulated-user “yes” replies: the first accepted A; the last meant continuation, not another gate approval. Two intervening “Please continue” replies. Identity remained unverified. The retained oracle reports startup failure; API/importer/UI remain unverified. [Report](fight-seldon-r26.json), [oracle](oracle-seldon-r26.json).

2. **First deviation:** event **83** records an outline with **zero beads**, accepted at **85**; compiler validation eventually rejects missing build/requirement coverage at **113**. The first refusal, **97**, instead exposes execution-descriptor constraints, followed by runtime rejection at **105**.

   **Recovery then becomes structurally impossible:** **114** requests direction through an amendment schema referring to draft nodes. Answer **122** proposes the correct missing bead, but the writer resolves amendment references against the persisted spine—where those drafts do not exist—yielding `content.re_112d1766c1: required field` at **123**. Retries end at **139–140**.

   The resumed attempt repeats the class: **196** rejects CSV setup path `items.csv`, but **197** permits editing only three `fields.execution` values. Answer **205** explicitly identifies the path as outside its schema. **222–223** pause again. Evidence: [run database, numbered events](C:/seldon/runs/fight-1/seldon/20261109T103417-a6d1a4-001-shelflife/.codex-harness/plan.sqlite3). Pinned `8dd872d`: `run_loop.py:55–70`, `run_content.py:78–85`.

3. **TRIAGE: DESIGN** — failure handling does not preserve a repairable contract for the artifact actually rejected. Draft references become canonical-reference requests; stale execution-field diagnostics exclude the newly rejected scenario path. **Siblings:** r25’s null-baseline producer/consumer contradiction; missing-bead coverage; repeated module→runtime correction cascades. Exporting `{data}/items.csv` repair wording to the user violates C16/C18/I10. The final explanation also misattributes the hold: **243** understands “yes” as continuation; **248** blocks unchanged facts.

4. **ONE simplest rule:**

   | Owner | Rule | Pros / cons |
   |---|---|---|
   | **CODE** | Every structural rejection returns a repair contract over the same retained artifact, permitting changes to the currently rejected fields or missing node kinds; its consumer uses that same artifact and contract. | Removes impossible repairs and user-facing internal chores; requires replacing stale diagnostic inheritance. LLM supplies meaning. |

5. **Improved versus r25:** the null-baseline contradiction no longer blocks this run; planning reaches compiler coverage and scenario validation. After continuation, outline **166** contains **two proposed beads**, versus zero initially—**not persisted or proven valid**. No completed product transition improved: **A remains the last proven transition; consumer-valid Spec is next.** Calls rose **9→20**, user decisions **1→2**, elapsed time **825→2,031 seconds**. [r25 diagnosis](r25-diagnosis.md).