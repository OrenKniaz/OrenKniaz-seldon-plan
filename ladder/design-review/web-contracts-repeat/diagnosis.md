CHARTER: serves C2/C18/C23 — violates no I#.

**TRIAGE: DESIGN — controller recovery discards retained semantic progress. The repeated Contracts phase is proven; why the controller disappeared remains unresolved.** Verified HEAD `97d059b`. No tests or edits.

1. **Why `deadOwner` became true**

   [launch.json](~/codex-harness/work/ladder/design-review/web-contracts-repeat/dead-segment/launch.json:1) records:

   ```text
   pid:             48100
   at:              2026-11-08T11:51:49.956175+00:00
   processIdentity: 134386123099467748
   ```

   [`segment_status()`](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_jobs.py:718) probes **that PID**. Identity equality controls `launched`; **only `observed["running"] is False` controls `deadOwner`**. An identity mismatch or unknown observation cannot directly produce this recovery reason.

   On Windows, [`process_observation()`](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/audit_process.py:41) returns false through either:

   - `OpenProcess` failing with error **87**, or
   - successful queries returning an exit code other than **259**.

   The deadline was still nearly nine minutes away. Therefore event 192 implies one of those false-liveness observations. **The raw probe, error and exit code were not retained, so these artifacts cannot establish which—or the cause of death.**

   The receipt captures identity after `Popen` and contains a nonempty identity ([launcher](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_jobs.py:669)). There is no evidence establishing a creation-time race, inherited Job termination or a bad fresh-process probe. Job membership is not consulted by this check. Missing `started.json` establishes no recorded payload entry, not the reason for disappearance. The supplied quiescence receipt belongs to **previous segment `70c813…`**, not `e58c37cb`.

2. **What activates recovery so soon; why web**

   Activation here does not necessarily mean reconnect. [`wait_for_question()`](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_loop.py:1373) polls every **50 ms** and calls `run_loop()` when it observes `deadOwner`; `_step()` then reconciles. The MCP request waits through this path ([caller](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/mcp_planner.py:153)). The 3.3-second wake-gap event merely logs elapsed time.

   There are two normal loop entrants: MCP waiting and the completed controller’s [`monitor()` callback](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_recovery.py:433). Events show original effect owner **3688**, controller **48100**, then successor effect owner **9956**. The event does not retain the recovery caller, but a different caller PID cannot itself make `deadOwner` true: the check still probes 48100.

   **Nothing in this recovery path is web-specific.** Both golden surfaces use stdio MCP. The `d381` sibling shows CLI exposure too; differing timing is plausible, not proven causality.

3. **Real-run impact and exhaustion**

   [`_recover()`](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_loop.py:672) explicitly sets `resumeRun=None`. BUILD consequently republishes and selects a successor job ([BUILD branch](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_loop.py:800)).

   Worse, [`segment_outcomes()`](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_jobs.py:485) rejects the previous run’s different effect ID, finds no current beads, and marks **both Contracts and Build** as faults with “not launched.” Event 193 charges their stable work identities.

   **Yes:** two such readmissions consume the allowance; the next matching fault selects `steer` ([bound](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_recovery.py:328)). Healthy product work can therefore be interrupted for planner direction because of controller failures. This is STEER, not necessarily literal `PAUSED`.

   A real provider run can incur repeated Contracts work and judgment cost. This dump uses scripted providers and proves a **second judgment request/semantic effect**, not an actual paid charge or completed second verdict.

4. **Should Contracts rerun?**

   **No, provided its retained binding remains current.** Events 184/194 have the same plan revision; observations 173/205 have identical contract revision, candidate tree and observation-file hashes. The new Contracts execution creates a different commit and evidence binding.

   The positive judgment belongs to the original evidence; preserve that evidence and continue Build. Do not attach its verdict to the newly generated evidence. The existing successful continuation already selects the retained run ([continuation](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/run_loop.py:1196)); recovery loses that selection.

5. **One simplest rule; PUB1**

   **Controller replacement resumes the earliest unfinished admitted work; it never invalidates current completed work merely because the controller changed.**

   | Owner | Implementation and tradeoff | Approximate delta |
   |---|---|---|
   | **CODE** | Preserve the bound progress through recovery and derive fault work from unfinished work. Deterministic scheduling/provenance, not LLM judgment. Requires a valid handoff across quarantine. | **40–80 production lines**, estimated |

   Simply retaining `resumeRun` is insufficient: real-attempt confinement requires the run to belong to its admitted job ([guard](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/attempt_provenance.py:300)). Genuine repeated controller failures may still exhaust recovery; this rule removes semantic rewind and incorrect Contracts charging.

   **PUB1 does not remove this class.** It changes outcome publication and interrupted-admission handling, but retains the same false-liveness predicate ([patch:695](~/codex-harness/work/lanes/stage-pub1-9ea08e87.patch:695)) and recovery branch for this existing request ([patch:948](~/codex-harness/work/lanes/stage-pub1-9ea08e87.patch:948)). It does not change `_recover()` clearing `resumeRun` or the recovery bound.

**Last proven outcome:** Contracts received positive credit; Build was admitted but has no recorded payload entry. **Remaining blocker:** the controller-exit cause needs the contemporaneous process-probe result or retained process exit evidence; this dump cannot supply it.