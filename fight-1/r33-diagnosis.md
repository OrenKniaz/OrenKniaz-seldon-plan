CHARTER: assesses C8/C14/C16/C18/C23 and I1/I2/I10. Read-only; no tests or edits.

1. **Outcome:** `BLOCKED-external` on **7273857**, after **48m41s**. Furthest path: **A → Spec/review → B → Build (tests only) → Judge → Steer → paused**. Application implementation never launched; no C or delivered product. **31 planner MCP calls**, 62 total MCP calls; 36 completed internal invocations: 12 planner, 21 judge, 3 mechanical. No reported MCP refusals; **six exact-fix rejections**. Three simulated “yes” replies covered A, an extra planning continuation, and B; then “Please continue.” Human identity remained unverified. The [oracle](~/codex-harness/work/fight-1/oracle-seldon-r33.json) records startup failure; API/importer/UI remain unverified. [Report](~/codex-harness/work/fight-1/fight-seldon-r33.json:18).

2. **First control-flow departure:** [event database](C:/seldon/runs/fight-1/seldon/20261109T190951-795786-001-shelflife/.codex-harness/plan.sqlite3), **160 → 161**: plan review explicitly establishes **no material design defect**, but holds on *unverified* browser availability/control feasibility, with `findings: []`. Instead of autonomously resolving or steering that uncertainty, Seldon requests more user direction—an extra touch outside A/B/C without an actual research question. The first Build defect follows at **284/302**: browser tests require unavailable Playwright despite the standard-library helper contract. Subsequent attempts fail on browser startup (**337**) and missing `LOCALAPPDATA` (**372**).

3. **TRIAGE: DESIGN — two distinct systemic failures.**
   - **Replanning cannot change its own structure.** The planner requests consolidation (**398**), but the outline requires separate contracts/build beads and cannot express supersession or dependency removal (**467/469**). Readback retains the build dependency and overlapping ownership; reviewers correctly block (**526/531/556**). Siblings: bead consolidation, ownership transfer, dependency removal, and acceptance-link transfer.
   - **Terminal context growth:** retained evidence is repeatedly embedded inside subsequent evidence. At **691**, `context.observation.sourceRefs` alone serializes to approximately **1.17 million characters**, including prior facts/current nodes. The provider rejects **1,566,824 > 1,048,576 characters** before starting the turn. Siblings: increasingly inflated requests at **449/630**, and steering results carrying earlier judgments and their facts. This is an internal design blocker despite the “external” outcome label.

4. **ONE simplest rule for the terminal class:**

   | Owner | Rule | Pros / cons |
   |---|---|---|
   | **CODE** | Give each semantic call a bounded projection of current facts; retain historical evidence by ID/revision, never recursively embed its payload. | Preserves provenance and stops recursive request growth; requires question-specific fact selection. |

   This removes the payload-growth class. Canonical structural replanning still needs repair before implementation can resume.

5. **Improved versus [r32](~/codex-harness/work/fight-1/r32-diagnosis.md):** the missing amendment-source contract is repaired: CODE creates a canonical `result` (**380**), and two sourced amendments are accepted (**393/394**). Test execution also gets beyond r32’s module/package binding failure, and Python **3.12.7** is observed. Steering now reaches substantive replanning and review—but cannot apply the requested graph changes. Delivery remains unproven; time increases **31m41s → 48m41s**, planner calls **23 → 31**.