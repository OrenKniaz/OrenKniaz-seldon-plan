CHARTER: serves C11/C16/C18/C23; identifies I5/I10 failures. Read-only; no tests or edits.

1. **Outcome / furthest phase:** `ERROR`, **10,901.672 seconds (~3h02m)**. **A accepted → Spec persisted/compiled → plan review → diagnostic Judge pending.** No B, Build, completed Steer, or C; no product delivered. The report’s top-level `phase=align` is stale: retained `meta` and later receipts show `roundtable`. **9 completed outer MCP calls**, plus **1 unresolved `harness_chat`**; **7 completed internal calls: 4 planner, 2 mechanical, 1 judge**, followed by another judge launch without completion. Zero reported MCP refusals; **2 internal answer rejections**. One simulated-user “yes” accepted A; `human_identity_verified=false`. The retained oracle reports startup failure; API/importer/UI remain unverified. [Report](C:/Users/oren/codex-harness/work/fight-1/fight-seldon-r28.json), [oracle](C:/Users/oren/codex-harness/work/fight-1/oracle-seldon-r28.json).

2. **First deviation:** **event 84**, repeating r27’s execution-contract detour: `unittest` descriptors are rejected; **92** rejects runtime `python`; **96** shows the planner discovering the installed interpreter through shell commands. CODE omitted setup facts the semantic call needed—I10. This recovers at **114**, and **119** compiles Spec.

   **The decisive review defect:** packets **123/133/136** say **“Full brief source unresolved”**, although the original brief exists at **5**. Reviews **140–144** find **no concrete plan defect**, but remain inconclusive over missing brief coverage and **pre-B absence of implementation/execution evidence**. That mixes plan sufficiency with later product validation.

   **The terminal stall:** **147** launches a semantic judge with deadline **10:47:20 UTC**; it is the last retained event. Later status receipts still expose that pending effect. No completion, ownership release, or steering is recorded. The final message calls this an expired *review*; the outstanding effect is actually **semantic**. Evidence: numbered events in [plan.sqlite3](C:/seldon/runs/fight-1/seldon/20261109T121252-904193-001-shelflife/.codex-harness/plan.sqlite3), [turn 2 receipt](C:/Users/oren/codex-harness/work/fight-1/receipts/20261109T121252-904193/20261109T121252-904193-001-shelflife/turn02.jsonl:28).

3. **TRIAGE: DESIGN** — semantic questions lack complete, phase-appropriate facts and obligations. **Siblings:** interpreter guessing here; r27’s unciteable review-attempt IDs and lost rejected response; r26’s draft/persisted-reference mismatch. Separately, the unretired expired semantic effect is a **bounded-recovery BUG** under I5/C18; transport failures occurred, but their precise causal role is unproven.

4. **ONE simplest rule:**

   | Owner | Rule | Pros / cons |
   |---|---|---|
   | **CODE** | Construct each question from canonical facts and obligations for its current phase; the LLM judges only that question. Before B, judge whether the plan can deliver the accepted dream; require delivery evidence after Build. | Removes missing-context and premature-proof barriers; requires correcting existing packet producers. |

5. **Improved versus r27:** Claude authentication failure now triggers a provider switch: **1 failed Claude launch → 2 successful Codex reviews**, replacing six authentication failures. Both reviews are retained as inconclusive with no positive credit; independence is labeled `single-provider`. **No further delivery transition:** B remains unproven, the interpreter detour persists, and elapsed time worsens **762→10,902 seconds**. R27’s reference-validation failure was bypassed, **not demonstrated fixed**. [r27 diagnosis](C:/Users/oren/codex-harness/work/fight-1/r27-diagnosis.md).

