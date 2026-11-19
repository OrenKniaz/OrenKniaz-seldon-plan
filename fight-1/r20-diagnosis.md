CHARTER: serves C1/C8/C18/C23; isolates a transport bug. No tests or edits. **The supplied artifacts identify r20 at `f965c26`; r19 is the comparator.**

1. **Outcome:** `ERROR`, 139.109 seconds, one turn. Furthest: **A presented, awaiting approval**; Spec/B/Build/Steer/C never reached. Two outer planner MCP calls: status and chat. Three internal provider calls completed: understanding (`gpt-6-astra`), expansion judgment (`gpt-6-astra`), size assessment (`gpt-6.1-sol`, **medium**). This includes an Align judgment, not post-build Judge. **Zero refusals, zero user decisions, no product delivered.** The oracle reports server exit 2; API/importer/UI remain unverified. [Report](/~/codex-harness/work/fight-1/fight-seldon-r20.json:11), [oracle](/~/codex-harness/work/fight-1/oracle-seldon-r20.json).

2. **First demonstrated break in the forward path:** after successful turn 1, **status readback aborts before the simulated user can answer A**. Database event **25** requests `align+vision-lock`; event **47** retains `WAIT_USER` with that request. The status subprocess exits **0**, but its output contains Windows-1252 byte **`0x96` at offset 7511**, representing the en dash in `1–80`. Reading those retained bytes as UTF-8 reproduces the reported exception. At `f965c26`, `plan_cli.py:25` emits `ensure_ascii=False` through locale-dependent stdout; [farm.py:323](/~/codex-harness/work/run-farm/farm.py:323) assumes UTF-8. This is a producer/consumer encoding mismatch, not a semantic refusal. [Raw status](/~/codex-harness/work/fight-1/receipts/20261108T094116-8f5f14/20261108T094116-8f5f14-001-shelflife/status01.jsonl), [database](/C:/seldon/runs/fight-1/seldon/20261108T094116-8f5f14-001-shelflife/.codex-harness/plan.sqlite3).

3. **TRIAGE: BUG** — the deterministic JSON transport has inconsistent encodings; the planning design need not change. Siblings: curly quotes, accented names, non-Latin text, Unicode paths and diagnostics crossing any redirected CLI JSON boundary. ASCII-only initial status concealed the defect.

4. **ONE simplest rule:**

   | Owner | Rule | Tradeoff |
   |---|---|---|
   | **CODE** | Machine JSON producers explicitly emit UTF-8 bytes; consumers decode UTF-8, independent of Windows locale. | Small transport fix; preserves arbitrary user text without encoding guesses or LLM intervention. |

5. **Improved versus r19:** the extra **P permission gate is gone**. Instead of stopping before any internal invocation, Seldon completes understanding, expansion assessment and size routing, then presents the charter’s A decision. Refusals fall **1 → 0**; outer planner calls **4 → 2**. **A acceptance and subsequent delivery remain unproven** because readback failed before any reply. [r19 diagnosis](/~/codex-harness/work/fight-1/r19-diagnosis.md).