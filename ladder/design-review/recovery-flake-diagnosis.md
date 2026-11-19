CHARTER: serves C18/C23/C25 — violates no I#.
Read-only diagnosis at `semantic-cc` **676e26b966a7cfcc9271a991151ad884684e598a**; no edits or tests.
**Several distinct windows exist; the logs do not establish one common race.** Incident attribution remains unproved: the assertion output truncates the cursor, and retained `C:\seldon\tests\…` workspaces deny access.
References below use `src/codex_harness/core/` in that checkout.

1. **Orderings that produce the symptoms**
   
   Pause already writes a legitimate **non-exhaustion** steering event: `run_loop.py:528` → `planner_recovery.py:395`.
   Resume explicitly readmits that job; its `steeringJudgmentId` excludes it from automatic-recovery counting (`planner_recovery.py:393`, `:370`).
   
   **fix16, one recovery:** C fails → automatic readmission #1 → successor fails **before its attempt exists**.
   Dispatch records that failure (`dispatch.py:625–681`), but recovery excludes beads without `attempt` (`planner_recovery.py:212–223`).
   `_recover` interprets the empty set as denied/uncertain and **abandons**, producing `STEER` with no effect (`run_loop.py:717–741`).
   The old golden accepts that state as exhaustion and then finds only one readmission. This is a concrete source-supported ordering, not confirmed incident causality.
   
   **fix17, two recoveries but false flag:** the same pre-attempt failure occurs **after readmission #2**.
   Abandonment emits no new `worker-recovery-steering-required` event; `faults[0]` can therefore still be the pause’s false event.
   `approvals.records` sorts **newest first** (`approvals.py:39–44`): this is an event-selection assumption, not evidence that the exhaustion calculation returned false for the same work.
   
   **sweep1, no question:** that abandonment produces “Permission/uncertain launch held,” so the exhaustion-specific question never appears.
   Polling `harness_plan_status` cannot repair or advance it: status only reads (`mcp_planner.py:104–114`).
   A scheduling delay exceeding 45 seconds is another possible explanation; the truncated cursor cannot distinguish it from a durable hold.
   
   **Separate mirror race:** worker writes segment terminal (`planner_jobs.py:703`); monitor writes segment quiescence (`planner_recovery.py:452`), then root terminal (`:467`).
   Between those writes, loop reconciliation reads the completed segment (`run_loop.py:594–602`), while `worker_job_status` reads missing/older root terminal (`planner_jobs.py:384–429`).
   That disagreement is real. **I found no demonstrated path making it the cause of these recovery-count assertions.**

2. **Product defect versus test assumption**
   
   **Both.** Real prelaunch failures/dead controllers can lose fault identity and enter a terminal abandonment instead of ordinary recovery: a product recovery defect.
   Root/segment status disagreement also affects real readers and reconnects.
   Conversely, “any STEER means exhaustion,” an unbound `faults[0]`, and an unestablished 45-second bound are test assumptions.
   Increasing the wait does not resolve a persistent permission/uncertainty hold.

3. **TRIAGE: DESIGN — outcome identity disappears before recovery; siblings: prelaunch failure, dead controller, interrupted launch.**
   
   **One owner rule:** the admitted segment publishes its outcome **with canonical work identity and launch certainty**, including failure before an attempt.
   Recovery alone calculates allowance and disposition from that outcome and its existing lineage; loop and views consume the decision.
   Preserve genuine denied/unknown-launch holds; distinguish them from an observed failure before launch.
   The allowance calculation is already transaction-serialized (`plan_store.py:146`; `planner_recovery.py:318,367–401`).
   **No lost-counter-update race is established; adding another counter would worsen ownership.**

4. **Deterministic fault twin — proposed, not executed**
   
   Reuse the real pause→reattach→resume journey and canonical dispatch/recovery producers.
   Use acknowledged pipe/Event barriers to select the successor after automatic readmission #1 or #2.
   At C’s packet-building boundary (`dispatch.py:640`), inject `OSError` **before** assignment of `current["attempt"]` (`:651`); let normal failure handling continue.
   After producer completion, observe respectively: **one readmission**, or **two readmissions plus the retained false steering event**, and a held question rather than exhaustion.
   No sleeps or fabricated recovery records are needed. Existing `fault-contracts` raises only after attempt creation (`test_golden_path.py:387`), missing this boundary.
   Separately, gate the monitor immediately before root-terminal mirroring to reproduce segment/root disagreement; that twin must not be presented as reproducing the count failures.

5. **Stage 2e overlap**
   
   Addendum 2 **item 5** owns control/exhaustion scheduling and presenting the correct outstanding question.
   Its **line 107 explicitly defers job-status precedence**; TD#6 is not implicitly included.
   Keep segment-outcome/work-identity repair as a **small separate Tier 2 lane**, with 2e consuming its result and preserving one writer per shared file.
   Sweep1’s job→publication repair addresses TD#5; it does not establish closure of SM#7/8 or TD#6/8.
   **Next unproven step:** execute the forced twin and obtain the failing job’s bound disposition/outcome before assigning these historical gates a definitive cause.