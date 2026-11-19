CHARTER: serves C13/C14/C18/C26 — violates no I#. Read-only diagnosis; no changes, tests, or provider launches.

1. **Execute failed inside Seldon.** Turn 6 called `harness_worker_start` for publication `328e924f…`; `harness_worker_status` reported **`IndexError: tuple index out of range`**. Supported readmission created successor `5ad74f49…`, which failed identically.
The source-localized raise is [dispatch.py:2588](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/dispatch.py:2588): `records[plan.beads[bead_id].depends_on[0]]["integrated"]["semantic"]`. Published B1 has `semanticPhase="build"` and `dependsOn=[]`, loaded as an empty tuple.
Terminal receipts retain exception type/message but discard the traceback at [planner_jobs.py:451](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_jobs.py:451); attribution is from source plus saved input, without reproduction.

2. **TRIAGE: DESIGN — canonical producer/consumer mismatch — sibling cases:** dependency-free build beads, arbitrary first dependencies, and downstream Contracts-RED validation.
The compiler accepts the current trace, while dispatch still assumes the older contracts→build topology. This is a **Seldon defect**, not provider/environment failure or invalid worker-start arguments.
**No model worker launched:** two controllers/worktrees started; both run receipts say `didExecuteRealProvider=false`, B1 `attempt=null`. Recovery verified zero active children.

3. **The five generic errors represent three causes**, confirmed by `planner-refusal` events:
- **#53 / turn 4:** `harness_record_chat_confirmation` returned `state="stale"` after D1 changed the revision; expected stale-subject protection, not an exception.
- **#135 / turn 6:** `harness_worker_status(328e924f…)` reported the first controller’s `IndexError`.
- **#138 / turn 6:** `harness_worker_status(5ad74f49…)` reported the successor’s identical `IndexError`.
- **#140 / turn 7:** status reread of that same successor; **no third crash or launch**.
- **#141 / turn 11:** `harness_packet_view(B1)` raised **“No current compiled or published manifest”** at [mcp_planner.py:893](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/mcp_planner.py:893), after D2 changed the revision; compile followed by packet-view succeeded.

4. **Lane overlap:** 2b removes budgets and preserves launch authority, but retains the crashing access (`dispatch.py:2583`); 2d improves recovery/lifetimes but also retains it (`:2412`). **Neither fixes this execution mismatch.**
2a2 addresses pending findings permitting publication; it does not repair execution or stale reads. R4 recorded finding dispositions before publication (event #105); this diagnosis does not establish a DV10 escape.
Round 3 stopped earlier at scenario coverage. R4’s placeholder scenarios/empty targets are not the cause of this prelaunch crash.

5. **Concrete remedies per cause:**
- **Execution — owner `dispatch.py`:** replace the mandatory first-dependency Contracts lookup with trace-bound RED evidence handling; update its consumer in `planner_candidate.py:102`, which otherwise rejects missing Contracts RED. Merely guarding the index leaves the next blocker.
- **Stale confirmation — caller / `planner_confirmations.py`, `approvals.py`:** prepare a fresh B after revision-changing writes, then bind the reply to that subject; preserve stale rejection.
- **Stale packet — caller / `mcp_planner.packet_view`:** compile the changed current plan before reading its packet—the run already demonstrated this supported remedy; no additional code fix is established.