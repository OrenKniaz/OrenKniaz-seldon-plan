# M3 + R17: final design and lanes (Fable, 2026-11-16)
Basis: BLUEPRINT v1.12 (R15, R16, R17, §3), CHARTER v1.8 (C8, C20), `src/seldon` at f69003d (4,468 lines), m3-readiness-fable-2026-11-16. Nothing was run; line counts are estimates. Lanes start after seePeers and judgeOnce land, on main after those landings.

## 1. R17 design
**Where the user is reached today** (all through `decisions.request` -> one slot `cursor.decision` -> `frontdoor.state.waitingFor` -> chat
relays words with `answer` -> `DECIDE` maps them to approve / revise / decline):
- Gates A, B, CHECK-IN, C: `run.py:137-147`. Unit question: second failure, `recovery.py:27` -> `decisions.ask_unit` (three fixed strings).
- Step question: repeated planning gap `recovery.planning` (`detail.py:15,101,128`); any code fault `run.py:201-207`.
- A worker's own question already goes to COACH (`units.py:67-75`). ALIGN asks nothing: its `unknowns` are only listed at A.

**(c) One question shape.** Every request carries `ask = {question, options: [{label, means}]}`: 2-4 options, the recommendation first.
Chat adds "Other". In the store each option also has an `effect` that code set; the model never writes effects.

| Touch | Who writes the options | Options (first = recommended) | Other = own words |
|---|---|---|---|
| A, alignment and expansion | ALIGN: `alternatives` replace `unknowns` (smaller, bigger, a different answer to what the words leave open) | "Build this" (approve); each alternative (direct) | revise -> ALIGN |
| B | code (the decision is fixed) | "Build this plan" (approve); "Build it and do not stop at check-ins" (waive) | revise -> REPAIR |
| CHECK-IN k | code, with the next wave's goal in the label | "Go on to wave k+1: goal" (approve); "Go on and do not stop again" (waive); last wave: "Finish and validate"; "Stop here" | steer |
| C | code | "Accept"; "Stop without accepting" | steer: a fix wave |
| Unit or step question | planner (COACH `ask`) | the planner's 2-3 approaches (direct); units also get "Leave this out" (drop) | direction |
| Code fault | code | "Try again"; "Stop" | direction |

Effects: approve, waive (approve and set `cursor.waived`), direct (the label and its meaning become the user's direction), drop, stop.
- **Chat shows it:** `state.waitingFor.ask` = question, options, "Other". The front door's instruction says: show them as written, with
  your own ask-user tool when you have one; relay the picked label or the user's own words with `answer`; never pick for the user (C20).
- **Code maps it back:** words equal to a label (case and spaces ignored) select that option with no model call. Anything else goes to
  DECIDE, whose answer is one of this request's labels, or Other, Stop, Unclear. Unclear keeps the same request shown with one line why.
  Today `unclear` falls through `decisions.py:105` and approves the gate; this removes that.
- Reading for Oren to confirm: at B, check-in and C the option words are fixed in code because the decision is fixed; the planner writes options wherever the content is open (A, unit and step questions).

**(a) Planner first.** `ASKED` now means "needs an answer", from the planner and then the user. Chain per unit or gap (R15, no numbers
end it): failure 1 recovers in the same session (today); failure 2 asks COACH with what was tried, the requirements, contracts,
decisions and earlier user answers. COACH returns `guidance` (applied at once, recorded as the planner's answer, the user is not
asked) or `ask` (the user question with its options). On the next failure the user is asked and the planner's new proposal is
option 1. A user answer resets the chain. A step question takes the same path inside `decisions.decide`: a request without `ask`
is first given to COACH. A worker's own question keeps today's path; when COACH returns `ask` it becomes the unit question.
A code fault is not a meaning question, so it skips the planner. State added: one key `coached` in the recovery record.

**(b) Non-blocking.** One rule, `decisions.holds(store)`: a shown request holds only what depends on it.

| Request | Waits | Keeps going |
|---|---|---|
| Unit question | that unit and the units that depend on it (already true in `scheduler.py`) | every other unit of the wave |
| Check-in k | the start of wave k+1 work, and C | STEER, DETAIL and REVIEW of wave k+1 on the recommendation; VALIDATE on the last wave |
| A, B, step question, code fault | its own step: nothing else exists to do | - |

- Check-in stops being a waiting state: `CHECK-IN` posts the request and moves on at once. Wave k+1 work and C need its answer or the
  waiver. An "Other" answer steers: ARCHITECT is asked again with the words, and merge by handle keeps what still fits.
- A waived check-in is recorded with its approval ("waived by the user") and never takes the slot. Scope changes still go to gate A.
- **The run pauses only when nothing can move**: no unit running and a shown request holds the next step (`Waiting`, as today).
- **Answering must not stop work.** Today `answer` pauses the controller (SIGTERM), which kills running workers. New: `answer` writes
  `answer.json` beside the run; a live controller reads it at its next loop turn, an idle one is spawned as today. The scheduler polls
  on every turn (today it stops polling after the first miss, `scheduler.py:24`).
- One request is shown at a time; other ASKED units queue and are asked next. No queue record, no new state machine.

## 2. What may break out of the gate
Rows of m3-readiness §1. Rows 1, 2, 3, 6 and the "second wave" list are cured by lanes P, W, S, V below.

| # | Break | Now or measure | Signal on Quiet Bench (run report) |
|---|---|---|---|
| 4 | Every fix round reruns every check | Measure. WAVE-VERIFY already runs units in parallel; honest reuse needs the same product tree (R9), which a fix changes | WAVE-VERIFY seconds per round and rounds per wave. Act when it passes 15% of wall time or 5 min a round |
| 5 | Questions grow with the product | P trims DETAIL and guide. WORK still lists every unit as an owner: measure | largest DETAIL, WORK, JUDGE question in wave 3 against wave 1; act at 1.5x |
| 7a | Whole plan copied, all records scanned per call | Measure | longest controller stretch with no provider call or check running; act above 2 s |
| 7b | A unit with no check, or a dropped unit, blocks C | Design now: V and W | journey twins |
| new | `unclear` words approve a gate, C included | Design now: S | twin: unclear words leave the request shown |
| new | An answer kills running workers | Design now: D | twin: answer mid-wave, the running unit finishes in its own session |
| new | Scheduler asks the user once, then never again in that wave | Design now: S | twin: answer arrives while others run |
| new | Plan merge renumbers units, unit rows are keyed by those names | Design now: P (handles assigned once) | twin: wave 2 keeps wave-1 rows and commits |
| new | Next wave planned ahead, then the user steers | Accept: one planning round is redone | planning calls spent before a steer; steers per run |
| new | One unit grows over many waves | Measure (m3-readiness §5) | largest unit's JUDGE question per wave |
| new | STEER answer resends all or omits parts | Merge by handle makes both harmless; 5 Terra runs before the cohort (R16) | steers that changed an untouched area |
| new | Second question waits unseen behind the shown one | Measure | time a unit sat ASKED before it was shown |

## 3. Lanes
**Lead freeze** (one small landing, gate green, before any lane is cut; then these three files are closed to lanes):
- `states.py` RUN: `"ARCHITECT": {"outlined": "DETAIL", "scope": "ALIGN"}`; `"REVIEW": {"reviewed": "B", "planned": "EXECUTE", "gap": "REPAIR"}`;
  `"CHECK-IN": {"next": "ARCHITECT", "last": "PRODUCT-JUDGE"}`. In `advance`: `steer` from ARCHITECT, DETAIL, REVIEW, REPAIR,
  PRODUCT-JUDGE or C goes to ARCHITECT (one line beside the `stop` rule). UNIT: `"DONE"` gains `"extend": "WAITING"`.
- `store.py`: RunRow gains `wave: int = 1`, `waived: bool = False`; UnitRow gains `wave: int = 0`; the recovery default gains `coached=False`.
- `schema.py`: `OPTION = obj(label=TEXT, means=TEXT)`; `ASK = obj(question=TEXT, options=array(OPTION, 2))`. VISION: `unknowns=REFS`
  becomes `alternatives=array(OPTION, 1)`. ARCHITECT: `waves=array(obj(goal=TEXT, commitments=REFS), 1)`, `areas=array(AREA)`, and a
  second alternative `obj(scope=TEXT)`. COACH: alternatives `obj(guidance=TEXT)` or `obj(ask=ASK)`. DECIDE:
  `choice("approve", "revise", "decline", "unclear", *targets, "Other", "Stop", "Unclear")`; the lead deletes the four old values at wiring.
- `questions.py`, three spots, then lane P owns the file. ALIGN example: `alternatives` with one option; ALIGN prompt gains "Name 1-3
  alternatives the user may prefer to this vision: smaller, bigger, or another answer to what their words leave open." COACH prompt
  gains "If the vision, decisions and results do not settle it, return ask: one question, 2-4 options, your recommendation first."
  DECIDE prompt becomes "Which displayed option do the user's verbatim words choose? Other for their own direction, Stop to end the
  dream, Unclear when you cannot tell." `example_architecture` waves gain `commitments`. Test stubs and recordings updated to match.
- Interfaces lanes rely on: `decisions.holds(store) -> bool` (S); `decisions.request(store, gate, subject)` unchanged (S);
  `plan.built(store)` = one row per unit of the finished wave, and `architecture.merge(previous, answer)` (P); B's subject carries
  `"vision": cursor.vision` (W) and `plan.approved` compares only that (P).

| Lane | Files (disjoint) | Delivers | Src |
|---|---|---|---|
| P wavePlan | `plan.py`, `detail.py`, `architecture.py`, `questions.py` | M3 rules 1, 2, 3, 5, 10 | +75 / -30 |
| S askUser | `decisions.py`, `recovery.py`, `scheduler.py`, `units.py` | R17 a, b, c; drop; waive | +60 / -30 |
| D door | `frontdoor.py` | options in chat; answer without stopping work | +15 / -10 |
| V validate | `judgment.py`, `flow_review.py` | M3 rule 9; no-check and dropped units | +30 / -10 |
| W waveLoop | `run.py`, `fixups.py`, `plan_review.py` | wave counter, pass-through check-in, extend, B bound to the vision | +35 / -20 |
| R rig | `tests/seldon`, ladder | 50 units / 5 waves journey, Quiet Bench brief, oracle, baseline | 0 |

P, S, D, V, R start together after the freeze. W starts on freeze + `wavePlan.patch`, because a second wave cannot be planned without P. The lead lands P, S, D, V, then W, then one wiring pass. Net about +145, main near 4.6k; the lead reports src lines per landing.

**One line per lane for Oren:** P coaching (the planner sees what was built and plans only the next wave). S coaching (the planner's
word comes before the user's time, and the user picks instead of composing). D coaching (the chat gets a ready question; answering
no longer stops work). V the one referee we keep (a promise is checked once, at the end, on behaviour). W neither: plumbing for
waves, with one waiting state removed. R measurement only.

**Shared boilerplate, the last two lines of every brief (replace `<lane>`):**
PROOF: golden/journey only (behaviour, never timing/counts). Full gate once at the end: bash scripts/gate.sh <lane> with ~/codex-harness/.venv/Scripts first on PATH. Test-only failures after the gate: fix without re-gating, report. No real provider calls, no commit, never read any .env file. Temp only under C:/seldon/tests/<lane>-<n>. Hang >5 min on one test = stop and report. Direction (BLUEPRINT R16 thin): coach not referee; simple and clean; no new state, question kinds, validators or caps (R15); delete what your change makes dead.
DELIVER in ~/codex-harness/work/lanes: <lane>.patch (diff vs base) and <lane>-report.md <= 8 lines starting with TRIAGE FAULT SELDON + DESIGN line, removed, files, src lines before/after, gate result.

### wavePlan
LANE wavePlan (open a ticket in ~/codex-harness/work/ladder/TICKETS.json via tracking rules if no row exists). Worktree ~/codex-harness/work/lanes/wavePlan = Seldon main <freeze commit>. Read AGENTS.md, BLUEPRINT.md §3, R5, R10, R16 first.
PROBLEM (by reading, m3-readiness §1 rows 1, 2, 5): one ARCHITECT answer must hold every area and every contract in full; DETAIL always plans `waves[0]` (questions.py:204) and gets every contract; every merge renumbers units (plan.py:118,133) while unit rows are keyed by those names; B is "this exact document" (plan.py:313-318). A second wave cannot be planned.
DESIGN: read ~/codex-harness/work/ladder/design-review/m3-readiness-fable-2026-11-16.md §2 rules 1, 2, 3, 5, 10. Implement:
1. Waves carry commitments (`waves[k].commitments`); code puts an unassigned commitment in the last wave. DETAIL for wave k asks only areas that hold a commitment of wave k or consume a contract that changed. ARCHITECT prompt: wave 1 is the thinnest path that runs end to end; write in full only the contracts the next wave needs, a later contract is a handle and one line.
2. Handles are assigned once (`<wave>.<area>.<n>`); the plan accumulates; earlier waves are never re-merged or renumbered. An answer that names an existing unit's scope is that unit with more requirements; a new scope is a new unit.
3. STEER is ARCHITECT again: `architect_brief(..., built=plan.built(store))` adds the previous architecture, one row per unit of the finished wave (worker summary, discoveries, open gaps, not judged), the user's check-in words and the remaining waves. The answer names only what changes; `architecture.merge(previous, answer)` merges by handle and `architecture.outline` validates the whole. A resent or partial answer is normalised, never refused. An answer `scope` is returned to the caller unchanged.
4. DETAIL's area brief gains "What exists here" (its units: scope, acceptance sentences, last worker summary) and loses contracts the area does not touch. The guide unit is extended each wave with that wave's contracts only.
5. `plan.approved`: B holds while the vision it approved is the current vision.
Do not touch run.py, fixups.py, plan_review.py, decisions.py, recovery.py, scheduler.py, units.py, frontdoor.py, judgment.py, flow_review.py, states.py, store.py, schema.py: other lanes and the lead own them.
Fault twin: a two-wave plan built through stub answers: wave 2 keeps every wave-1 unit name and requirement, extends one unit and adds one; a STEER answer that resends everything and one that names a single changed contract both give the same merged architecture, and only the changed contract's consumers are detailed again; a contract first written as one line is complete in the plan before the wave that needs it is detailed.

### askUser
LANE askUser (open a ticket ... as above). Worktree ~/codex-harness/work/lanes/askUser = Seldon main <freeze commit>. Read AGENTS.md, BLUEPRINT.md R15, R16, R17, CHARTER.md C8, C20 first.
PROBLEM (by reading): the second failure of a unit goes straight to the user with three fixed strings (recovery.py:27, decisions.py:29-31); the planner is never asked. The user composes every answer from scratch. DECIDE's `unclear` falls through decisions.py:105 and approves the gate. The scheduler asks the user once per wave and then sets `user = None` (scheduler.py:24). Drop and revise are refused "until M3" (decisions.py:29, 90-91).
DESIGN: read ~/codex-harness/work/ladder/design-review/m3-lanes-fable-2026-11-16.md §1. Implement:
1. `decisions.request` stores `ask = {question, options: [{label, means, effect}]}` on every request, built per gate from the §1 table. For A the options are "Build this" plus the vision's `alternatives`.
2. Planner first: an ASKED unit, or a step request without `ask`, is given to COACH with what was tried, the failure, requirements, agreements, decisions and earlier user answers. `guidance` and not yet coached: record it as the planner's answer, mark `coached`, move the unit `again` with the guidance; the user is not asked. Otherwise post the request: COACH's `ask`, or its guidance as option 1 "Try the planner's new approach". Units also get "Leave this out". `recovery.answered` clears `coached`. A code fault gets "Try again" / "Stop" with no COACH call. The COACH call for a unit runs as a pool job, never under the integration lock.
3. `decide`: words equal to a label (case and spaces ignored) select it with no model call; else DECIDE with `targets` = this request's labels. Apply the effect: approve (today's path per gate); waive (approve and `waived=True`); direct (unit: `again` with the direction; A: revise; B: revise; CHECK-IN and C: `requestedChange` and `steer`; step: `requestedChange`); drop (the unit and every unit that depends on it go ASKED/WAITING -> DROPPED, recorded); stop. Other = direct with the user's words. Unclear: keep the request, say why in `failure`, raise Waiting. The scripted dict path stays as it is. Delete `hold` and both "until M3" texts.
4. `decisions.holds(store)`: a unit request never holds the run; a check-in holds only the start of the next wave's work and C; any other request holds its step. A CHECK-IN request when `cursor.waived` is recorded with an approval "waived by the user" and does not take the slot.
5. Scheduler: try `decide` on every loop turn (wake at least every 2 s; this is a poll, not a limit); DROPPED and ASKED units never count as "no unit can progress"; raise Waiting only when nothing runs and a request is shown.
Do not touch run.py, fixups.py, plan_review.py, plan.py, detail.py, architecture.py, questions.py, frontdoor.py, judgment.py, flow_review.py, states.py, store.py, schema.py.
Fault twin: a unit that fails twice gets planner guidance and reaches DONE with no user request recorded; when it fails again the user sees a request whose first option is the planner's proposal, and answering with that label resumes it under a stub that has no DECIDE answer. While unit A waits on the user, independent units reach DONE and a dependent one waits; the answer resumes A and the run reaches C. Words that fit no option leave the same request shown and approve nothing (gate C included). "Leave this out" drops A and its dependents and the rest finish. Kill while a request is shown: reopen shows the same request.

### door
LANE door (open a ticket ... as above). Worktree ~/codex-harness/work/lanes/door = Seldon main <freeze commit>. Read AGENTS.md, BLUEPRINT.md R17, CHARTER.md C20 first.
PROBLEM (by reading): `answer` always calls `pause` first (frontdoor.py:192), which ends the controller and every running worker; with R17 questions arrive while work continues, so each answer would cost the running sessions. `state` shows the raw subject and tells the chat only "relay your words"; the chat has no options to show.
DESIGN: read m3-lanes-fable-2026-11-16.md §1 (c) and (b). Implement:
1. `state.waitingFor` gains `ask`: the question and its options as `{label, means}` (never `effect`), then "Other". A request without `ask` is shown as today. The `next` sentence and the MCP instructions say: show the question and options as written, recommendation first, with your own ask-user tool when you have one; relay the picked label or the user's own words through answer; never pick for the user.
2. `answer` writes `{request, words}` to `answer.json` in the side folder (temp file, then replace) and does not pause. A running controller's `user()` reads it when the request matches and removes a file for any other request; an idle controller is spawned as today. The file is the only carrier: delete the stdin response path.
3. `state` while a request is shown and the controller runs: status RUNNING with `waitingFor` present.
Do not touch any other src file. Tests: tests/seldon/test_front_door.py only.
Fault twin: an answer given while a unit is WORKING leaves the controller process the same and that unit finishes without a `reopen` transition; an answer for an old request id is refused with the current id; a controller killed after the answer file is written applies the answer once on resume; a request without `ask` still shows and answers as today.

### validate
LANE validate (open a ticket ... as above). Worktree ~/codex-harness/work/lanes/validate = Seldon main <freeze commit>. Read AGENTS.md, BLUEPRINT.md R2, R5, R9, C15 reading in §8.4 first.
PROBLEM (m3-readiness §1 rows 6, 7): final judging is per requirement and per area criterion, so a promise that crosses areas is seen by nobody after REVIEW; a unit with no check, or a dropped unit, blocks C.
DESIGN: m3-readiness §2 rules 8, 9. Implement:
1. `judgment.subjects` adds one subject per scopeIn and improvement commitment: its text, the verdict rows of the features in its areas, the guide walkthrough evidence. Behaviour only; reuse by scope tree as for other subjects. Its gap routes to the owner as today.
2. A unit is judged only on the acceptance sentences of the wave that last gave it work; earlier verdicts are reused while its scope tree is unchanged.
3. A unit without checks keeps its local judgment and does not block. A DROPPED unit's requirements and commitments are recorded "left out by the user" and do not block; C shows them.
Do not touch run.py, units.py, fixups.py, plan.py, architecture.py, questions.py, schema.py, states.py, store.py, decisions.py.
Fault twin: every feature passes but a commitment that crosses two areas is not carried end to end (planted): VALIDATE names the gap and its owner reworks, then C; with the path carried, C with one verdict per commitment. A run with one dropped unit reaches C and shows what was left out; a planted gap in a kept unit still reworks.

### waveLoop
LANE waveLoop (open a ticket ... as above). Worktree ~/codex-harness/work/lanes/waveLoop = freeze commit + wavePlan.patch (base). Read AGENTS.md, BLUEPRINT.md §3.2, R10, R11, R17 first.
PROBLEM (by reading): the run is one wave: CHECK-IN leads only to PRODUCT-JUDGE and waits; `waveStart` is set once (run.py:83); units are created once from B; one review repair per run (plan_review.py:33); fixups require the exact B revision (fixups.py:40-42); C requires every unit DONE (run.py:34).
DESIGN: m3-readiness §2 (state and rules 4, 7) and m3-lanes §1 (b). Implement:
1. ARCHITECT step: in wave > 1 pass `built=plan.built(store)` and merge with `architecture.merge`; an answer `scope` advances `scope` (to ALIGN and gate A).
2. REVIEW ends `reviewed` in wave 1 and `planned` later; review repair is per wave. B's subject carries `vision`.
3. EXECUTE start for the wave: a new unit is created; an existing DONE unit with new requirements is extended (fresh session, base = candidate, `wave` = k). This step, and C, need the last check-in's answer or the waiver; without it: Waiting.
4. CHECK-IN: post the request (commit, wave, what was built, open gaps, next wave goal) and move on at once: `next` (wave + 1, `waveStart` = candidate) or `last`.
5. `step`: when a request is shown, try `decide`; on Waiting go on with the step unless `decisions.holds(store)`.
6. `eligible`: units DONE or DROPPED; fixups bind to B, not to the revision number.
Do not touch decisions.py, recovery.py, scheduler.py, units.py, plan.py, detail.py, architecture.py, questions.py, frontdoor.py, judgment.py, flow_review.py, states.py, store.py, schema.py.
Fault twin: a two-wave scripted journey reaches C; wave 2 extends one wave-1 unit and adds one. With check-in 1 unanswered the wave-2 plan exists and no wave-2 unit has started; the answer starts them. After "do not stop again" the run never waits at a check-in and each check-in has its request and approval records. Killed inside wave 2, the reopened run finishes and wave-1 DONE units keep their commits. A wave-1 check broken by wave 2 fails WAVE-VERIFY and reworks its owner. A steer at C adds a wave instead of refusing.

### rig
LANE rig (no src). Worktree ~/codex-harness/work/lanes/rig = freeze commit. Deliver (a) tests/seldon scale journey with a stub provider: 50 units, 5 waves, one steer, one planner-answered failure, one user question answered by label while others run, a kill in wave 3; it reaches C and no DONE unit is redone. (b) ~/codex-harness/work/ladder/briefs/L3/4-quietbench.json and an `oracle.py` case `quietbench` from §4. (c) the sim user answers by option label (first option unless the script says otherwise); the run report adds the §2 signals, user questions shown, and questions the planner answered. (d) the plain-Terra baseline command for the same brief. Same PROOF and DELIVER lines; gate.sh rig.

## 4. Quiet Bench: dream brief and oracle
**Message (the user's words, save as `message`):**
Build Quiet Bench, a noise-cancelling test bench that runs on this PC with no audio hardware. Python 3.12 standard library plus Node 20
for the page checks; no third-party runtime packages, no network. I can generate a noise signal (tones, band noise) or import a WAV
file; the bench simulates the acoustic path from the noise source to the ear, runs an adaptive canceller (LMS family) against it and
tells me how much was cancelled in each frequency band. Every session is saved on a small local storage server
(`python server.py --port PORT --data DIR`) with its settings and results, and a web page on that server lets me start a run, browse
saved sessions, reload one and compare two. A command line (`python bench.py run|list|show|export`) does the same without the page.
A limiter must hold the output inside a safe level when the filter diverges, and a stop switch ends a run at once.
Build it in three waves and show me each one. Wave 1: the thinnest thing that runs end to end, one tone through a fixed filter,
saved and shown. Wave 2: the adaptive filter, attenuation per band, browse and reload. Wave 3: compare runs, limiter and stop
switch, WAV import.
**Profile:** audience "an audio engineer trying ideas before buying hardware"; care "numbers I can trust and a bench that never blasts"; tone "calm, exact, instrument-like"; platform "local Windows, Python 3.12 stdlib, modern desktop browser"; defaults "no
accounts, network, deployment or paid assets; ask before scope changes".
**Scripted user, every run:** A, B: first option. Check-in 1: Other, "also let me export a session as CSV". Check-in 2: "Go on and do not stop again". C: first option. One kill inside wave 2, then resume. Unit questions: sim user, counted apart (dual metric).
**Oracle (black box, the same for plain Terra):**
1. Guide: from a fresh copy, `docs/try-it.md` works as written; server, page and CLI start and stop.
2. End to end: one generated run through CLI, API and page gives the same session and the same band numbers.
3. Wave 1 still works after wave 3: the fixed-filter tone run saves and shows.
4. Numbers on the oracle's own hidden signals (two tones, band noise): attenuation per band above a floor a fixed filter cannot reach; a skeleton stub fails here. Residual energy falls over the run.
5. Limiter: with a step size that makes the filter diverge, output stays inside the stated level and the session records that it limited. Stop switch: a long run ends within one block and is saved as stopped.
6. Storage: save, restart the server, reload: values equal. A session written in wave-1 shape still loads after the schema grew.
7. Steer: `export` gives a CSV whose rows match the session's band results. WAV import: a 16-bit mono file runs; a bad file is a clear error and nothing is saved.
8. Compare: two sessions side by side, per-band difference correct. Page craft scored as in ShelfLife.
**Run report, not oracle:** 3 waves closed; the kill resumed without redoing a DONE unit; user questions shown and planner-answered questions; work done while a question was open; the §2 signals; calls and fresh tokens per wave.
**Bar (lead's call): 4 of 5 reach C autonomously, each oracle score at least plain Terra's.** Order: ShelfLife with two dictated waves once (proves the loop), Quiet Bench once, fix, then five.
