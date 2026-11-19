# Never fail (R15 addendum, T-133, T-134) — Fable design, 2026-11-13

Read on main 5868df7. Nothing here is built. TRIAGE T-133: DESIGN — every `except` in the core funnels into one sink (`fail → INCOMPLETE`, `exhausted → FAILED`); siblings are every row below. TRIAGE T-134: DESIGN — see §3.

## 1. Inventory: what ends a unit or run today, and what it becomes
(a) steer [until M3: user question] · (b) user question · (c) pause · DEL = delete, nothing replaces it.

| Path today | file:line | Becomes |
|---|---|---|
| Run-level catch-all → `incomplete()` → INCOMPLETE; 21 `"fail"` rows | run.py:215, 69-79; states.py:8-29 | (b) the catch-all asks the user at the step where it happened; rows DEL |
| Units not DONE after scheduler → `incomplete("Units incomplete")` (f02) | run.py:177-180 | (a) run stays in EXECUTE with the unit's question displayed |
| `recover()` exhausted (`recoveries>=2`) → FAILED | units.py:16-25 | (a) unit → ASKED, question displayed, others keep running |
| `block_dependants` + scheduler failed-dependency → BLOCKED | units.py:28-40; scheduler.py:22-27, 47-48 | DEL. Dependants stay WAITING; the existing "Dependencies not DONE" reason shows the asked unit |
| JUDGE ProviderFailure → non-retryable FAILED | units.py:218-219 | (c) not the unit's failure; special case DEL |
| WORK ProviderFailure, denied or unverified → FAILED; transient → spends a unit recovery | units.py:221-222; inference.py:53 | (c) for every provider failure except the unit's own deadline; a deadline still spends a recovery (R15) |
| `MissingFacts` non-retryable; `UnitTooLarge`; 64 KB and 2x refusals | units.py:223-226; questions.py:110-116; inference.py:19-20; judgment.py:102; flow_review.py:79 | DEL (R15 hard caps; same deletion as the no-hard-caps note). `inference.py:83` DEMO-uncertain raise is dead with DEMO: DEL |
| `proof.UncertainCleanup` → non-retryable FAILED | units.py:227-228; proof.py:61 | (c) pause, user resume only (a process may still be alive; no auto-retry) |
| Reopen: interrupted WORKING spends a recovery, third → FAILED | run.py:116-118 | DEL the count: an interruption is the machine's, never the unit's. `reopen` event only |
| "Three pre-B plan repairs exhausted" (g04) | plan_review.py:150-151 | DEL. After 3 repair rounds REVIEW advances to B with the open gaps shown in the review the user already sees (C11: ~3 rounds, then decide) |
| "Post-B plan steering is deferred to M3" | plan_review.py:148-149 | DEL (unreachable: REPAIR is only entered before B) |
| DETAIL / ARCHITECT "after one re-ask, planning stopped" + `planning_stop`, `planning_resume`, `Run.resume_planning`, `resume-*` rows | detail.py:14-19, 27-28, 143; run.py:197-209; states.py:29 | (a) the same catch-all question at DETAIL/ARCHITECT; the special resume door DEL (answering is the resume) |
| "exact-fix retries exhausted" `AnswerRejected` outside DETAIL | questions.py:420 | (a) catch-all question (C4: retries, then steer). The count stays: it routes |
| Decline at any gate; revise at CHECK-IN or C → raise → INCOMPLETE | decisions.py:38-39 | decline = the user ends the dream → STOPPED (the only non-accepted end). revise after B: request stays displayed with "changes after B arrive with steering (M3); approve or stop" |
| Bound-response mismatch, "Decision changed" | decisions.py:27, 34 | request stays displayed (catch-all never asks over an open request) |
| "No unit can progress"; "Execution requires B"; `eligible()` raises; fixups, gitwork, judgment, flow_review, wave_verify invariants | scheduler.py:50; run.py:170; run.py:36-66; others | (b) catch-all question (approve = try the step again). These are Seldon faults; each opens a ticket (P9) but the run stays resumable |
| Provider denial (logged out), usage limit, offline, Codex missing (`prepare` RuntimeError) | providers.py:116, 199-219 | (c) |
| Non-unit call: 2 transport recoveries then raise | inference.py:53 | (c) after the retries |
| User `stop` → `incomplete()`; "Run is INCOMPLETE; use start" | frontdoor.py:184-186, 215 | STOPPED by the user's words; kept |
| Controller crash on an uncaught bug (KeyError…) | frontdoor.py:94 | already a pause: state untouched, idle, `resume` works. Keep |

## 2. The one rule and the mechanism
**Rule: an exception never moves the run or a unit to an end state. Three sinks, one handler each: the provider did not answer → pause; a unit's own work failed twice → the unit asks; anything else → the step asks. Only the user's words end a dream (STOPPED) or drop a unit.**

- **Waiting for the user = the existing `decision_request` + `cursor.decision` + `decisions.decide` + front door `answer`.** No new record kind. Gate is `UNIT` or the run state's name. Subject: `{unit|step, tried: the recorded unit_failure / error texts, affects: waiting dependants, options}`. The DECIDE question and its three choices are reused unchanged: approve = try again (unit: fresh session, recoveries 0), revise = try again with the user's words (unit: appended to `unit.failure`, which is already "Exact failure" in the brief; planning: via `questions.user_words`, which now reads every revise answer, not only A/B), decline = drop the unit (below) or, at a step, stop. The recommendation line is empty until M3: STEER then sits between ASKED and the question and fills it. The `approval` record gains `choice`.
- **Unit states:** FAILED and BLOCKED go; `ASKED` (`again → REWORK`, `drop → DROPPED`) and terminal `DROPPED` come. `recover()` on the third failure moves the unit to ASKED and, in the same transaction, displays its request if no request is open (a second asking unit waits its turn; no clobber).
- **Others keep running:** the scheduler already does this once BLOCKED is gone; it returns when nothing can run. `Run.step` in EXECUTE then decides the open request; `user()` raises `Waiting` (moved from frontdoor to decisions.py), `Run.run` catches it and returns with the state unchanged. `answer` while the controller is running pauses it first instead of refusing (workers resume their sessions, R8; no recovery spent).
- **Drop** = `plan.without(document, closure)` (the unit, its dependants, consumers of contracts it provides) stored as a new revision, with the user's answer recorded as the B approval of that revision (C21: narrowing the user approved). Everything downstream reads the revision as today; no special cases in `eligible`, judgment or wave verify. Offered only when the reduced plan validates and no closure unit is DONE; otherwise the options are again / direction / stop (true replanning is M3).
- **Pause is not a state.** The run stays where it is; `cursor.failure` (free once the repair raise is gone) holds the reason, taken from the existing `provider_failure` record. `Run.run`: `except ProviderFailure` → set reason, wait (60 s doubling to 15 min, no count), run the same step again; the step is the probe, and unit loops are re-entrant (`recovered_report`, session resume). Unverified cleanup (provider or `UncertainCleanup`) sets the reason and returns instead of waiting: only `resume` continues. `resume` during a wait restarts the controller at once.
- **Outcome reads:** front door `state()` derives one `status` (I6, never stored): `ACCEPTED`, `STOPPED`, `WAITING` (a request is displayed), `PAUSED` (reason set, shown verbatim), else `RUNNING`. The runner prints status, reason and next sentence. RUN table: INCOMPLETE → STOPPED, entered only from decide/stop.
- **Recognising unavailable (T-132 rule kept):** only the provider's own `turn.failed` / `error` events are read, never stderr. The word list adds usage (`usage limit`, `usage_limit_reached`, `rate limit`, `insufficient_quota`, `hit your`) to denial; a match means "pause now, skip retries" and labels the reason with the provider's message. **The list can no longer cause a failure:** any other provider failure is retried twice (unit calls too) and then pauses anyway, so a missed word costs two calls, not a run. A new `Deadline(ProviderFailure)` marks a timeout Seldon enforced; it is the only provider failure `run_unit` turns into a unit recovery.
- **Scripted dev user** answers only A, B, CHECK-IN and C; any other request ends the scripted run as WAITING with the question printed (an honest non-C result; no fake user, no loop). Farm slots keep their own wall clock for PAUSED.
- Check-in waiver (C8) names CHECK-IN only; UNIT and step requests always wait by construction.

## 3. T-134: TRIAGE DESIGN
Cause: `plan.merge` (plan.py:275-278) appends the provider's requirement ids to every cross-area check, as DETAIL was told ("code links those contracts' provider requirements"). The area REVIEW brief (plan_review.py:19-22) then shows that check with the appended ids but only the area's own nodes, so the reviewer sees ids it cannot resolve and calls them foreign. DETAIL cannot remove them (code adds them again on every merge), so the repair loop was unwinnable: 3 repairs, INCOMPLETE. Siblings: any code-derived link shown in a per-area brief (unit `dependencies` from file prerequisites, `level` promoted to wave).
**Rule: a reviewer is shown what the planner wrote, in the planner's terms; a link code derived is shown as the agreement it came from, never as planner text (I1, R12, normalise-not-refuse).**
Change (plan_review.briefs, ~6 lines, no prompt sentence): in the brief's copy of each owned check, `requirements` keeps only the area's own ids and a new `integrates` lists the contract handles whose provider requirements code linked (derived: contracts whose provider unit owns a removed id). The canonical plan is untouched. With §1, a reviewer that still objects costs 3 rounds and then shows at B; it can no longer end a run.

## 4. Delete-list and files (net lines fall)
- states.py: 21 `fail` rows, `INCOMPLETE` + 2 resume rows, 8 `exhausted`/`blocked` rows → `asked`; +ASKED, DROPPED, STOPPED. ≈ −8
- units.py: `block_dependants` (−13), four except arms (−8), `retryable`; `recover` asks. ≈ −18
- scheduler.py: failed-dependency branch, `blocked_any` (−9). run.py: `incomplete` (−11), `resume_planning` (−14), reopen count (−3), units-incomplete (−4); + pause/ask handlers (+16), decide-first in step (+4). ≈ −12
- detail.py: `stop`, `planning_stop`; `resume_id` reads the last answered request. ≈ −8. plan_review.py: two raises (−4), 3-round route (+1), T-134 (+6).
- questions.py / inference.py / judgment.py / flow_review.py: caps, `UnitTooLarge`, `MissingFacts` (≈ −22). providers.py: `Deadline`, words, `prepare` raises ProviderFailure (+6).
- decisions.py: `Waiting`, choice handling for UNIT/step gates, stop on decline (+18). plan.py: `without` (+18). frontdoor.py: `status`, answer/resume pause first; `except Waiting` and the two refusals go (≈ 0).
- Estimate: src about −40 net. Tests: every `== "INCOMPLETE"` / FAILED / BLOCKED assertion (test_journey 872-908, test_fixups 48-49, 368-370, test_architect 158, 492-617, test_review 117, test_front_door 141-158) is replaced by the journeys below; `!= "INCOMPLETE"` guards become `status != PAUSED/WAITING`.

## 5. Journeys (stubs, outcome assertions only)
1. **Twin, never passes.** 4 units + guide, u002 fails proof every time, u003 depends on it. Assert: u001 and u004 integrate; status WAITING; the request names u002, three failures, u003 as affected; no outcome record; reopen shows the same request. Answer "drop it" → reduced revision, run reaches SCRIPTED_C, C subject shows the drop. Same start, answer "use the items route, not a fixture" → the next WORK brief carries those words, stub passes, reaches C with all units DONE.
2. **Fault twin, usage limit mid-run.** Stub provider emits a native `turn.failed` usage-limit event from call N for K calls (one WORK, one JUDGE in flight, one planner-side variant at DETAIL). Assert: status PAUSED with the provider's message; no unit state changed, no recovery spent, no unit_failure record; "usage back" → the same controller (injected wait) and, separately, kill + `resume`, both reach C; every unit DONE once; no finished unit re-ran. Variant: logged-out event, and an unknown native error (two retries, then PAUSED).
3. **Fault twin, unverified cleanup.** PAUSED with the receipt path; no auto-retry; `resume` continues.
4. **T-134 twin.** Recorded g04 DETAIL (consumer-area wave check on http-items, http-errors): the REVIEW brief for `interface` contains no id absent from its nodes and lists `integrates`; stub reviewer that flags any unresolvable id answers adequate; run reaches B. Second twin: reviewer returns a gap 4 times → B is displayed with the gap; state never STOPPED.
5. **Stuck step.** ARCHITECT answers invalid 3 times → WAITING at ARCHITECT; answer with direction → next ARCHITECT question carries it → continues. Decline → STOPPED with the user's words.
6. The 50-unit journey (P2) with one never-passing unit: 49 integrate, status WAITING.

## 6. Lanes (disjoint files; order)
- **Lane A first (small, unblocks the fight): T-134 + plan repairs.** plan_review.py only + journey 4.
- **Lane B: pause.** providers.py, inference.py, the provider/cleanup arms of units.py `run_unit`, the `Run.run` loop in run.py, journey 2-3. Lands alone.
- **Lane C: ask.** states.py, units.py `recover`, scheduler.py, decisions.py, plan.py `without`, detail.py, run.py (`incomplete`, step, reopen), frontdoor.py, questions.py `user_words`, journeys 1, 5, 6. After B (shares units.py, run.py). If C grows, drop (`plan.without` + DROPPED) splits off as C2; until then decline on a UNIT request offers again / direction / stop.
- Cap deletions (questions.py `bounded_unit`, 2x refusals) ride with the no-hard-caps lane if it is open, else with C.
Open risk, stated: `plan.without` on a compiled plan (handles must not renumber; contracts, obligations and quality traces must stay valid) is the one piece I have not traced line by line.
