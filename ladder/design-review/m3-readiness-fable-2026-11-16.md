# M3 readiness: from today's core to a dream 10-30x ShelfLife (Fable, 2026-11-16)
Read-only. Basis: CHARTER v1.8, BLUEPRINT (file header still says v1.10; R16 is in, the "R5 paused / one recovery" wording of
ab2ae1f is not in the file), `src/seldon` at 3c60cbf (4,179 lines), m3-design-2026-11-13, today's notes. Nothing was run; line
counts are estimates. Replaces the 11-13 M3 design where they differ: that one added four modules and a WaveRow to a 5k core.
## 0. Short answer
- What hurts first at size is not a crash. It is **big-bang integration** (every unit built blind, all proof at the end) and
  **the user being asked on every second failure**. Waves are the cure for the first, so M3 is the next step, not an extra.
- The simplest M3 is three reuses: a wave is an integer on the cursor; STEER is the ARCHITECT question asked again with what
  was built and what the user said; a path keeps one owner for the whole run. No new module, record kind or judge. About
  +120 src lines net, four parallel lanes. Prove it on "Quiet Bench" (ANC in simulation, 3 waves, ~12 units, Terra).
## 1. What works today only because ShelfLife is one wave and small
Ranked by how early it breaks as the dream grows.

| # | Where | What it assumes | At 10-30x |
|---|---|---|---|
| 1 | `questions.py:56-62`, `run.py:128-140` | One ARCHITECT answer holds every area and every contract in full | Hurts before B: 10+ areas and 30+ complete contracts in one answer; one schema error re-asks all of it (R3) |
| 2 | `questions.py:285-291`, `plan.py:82-89` | Every unit builds blind from contracts at once; proof waits for WAVE-VERIFY | Hurts most: 30+ units meet for the first time at the end; mismatches arrive in layers, each layer a full round |
| 3 | `recovery.py:23,27` | The second failure of a unit or gap goes straight to the user | At ~100 units nearly every run stops for the user several times; autonomy falls first here |
| 4 | `wave_verify.py:8-25`, `fixups.py:66-67`, `units.py:84-106` | Each fix round reruns every check of every unit; integration runs checks one unit at a time under one lock | Code time = product size x rounds: 38 s today, tens of minutes per round at size |
| 5 | `questions.py:205-207`, `:252`, `:269`; `plan.py:305` | Every DETAIL gets every contract; every WORK gets every quality line and every unit as an owner; the guide consumes every contract | Questions grow with the product (R2); the one guide session becomes the largest unit |
| 6 | `judgment.py:10-15`, `plan.py:158-168` | Final judging is per requirement and per area criterion; a feature never crosses areas | A promise dropped between areas is seen by nobody after REVIEW. Blind, not broken (C15, DV6) |
| 7 | `plan.py:56-69`, `detail.py:25`; `judgment.py:27-33`, `run.py:34` | Whole plan copied and all records scanned per call; every unit has a check and ends DONE | Slow code; a unit with no check, or a dropped unit, blocks C |

What stops the moment a second wave exists (all small): `states.py:17` CHECK-IN leads only to PRODUCT-JUDGE;
`questions.py:204` always `waves[0]`; `plan.py:118,133` every merge renumbers `n001/u001` and unit rows are keyed by those
names; `plan.py:313-318` + `run.py:148` + `fixups.py:40-42` B is "this exact document", so a new revision loses consent
(the Blueprint already says B binds commitments); `run.py:83` `waveStart` is set once; `plan_review.py:33` one review repair
per run; `decisions.py:29,90-91` revise and drop are refused "until M3".
## 2. The minimal M3 design
```
ALIGN -> A -> ARCHITECT -> DETAIL(wave 1) -> REVIEW -> B
wave k:  EXECUTE -> WAVE-VERIFY -> FLOW-JUDGE -> CHECK-IN
         more waves?  ARCHITECT(k+1, with results) -> DETAIL(k+1) -> REVIEW -> EXECUTE ...
         last wave?   VALIDATE (today's PRODUCT-JUDGE plus one question per commitment) -> C
```
**State, two additions.** The cursor gets `wave: int`, and `waveStart` moves to the candidate when a wave starts; each plan
unit carries the wave that last gave it work. The unit table gets `DONE --extend--> WAITING` (fresh session, new base), and
`ASKED --drop--> DROPPED` starts to work. No WaveRow: the cursor's per-wave fields are already rebuilt on every candidate change.
**Rules, each replacing something larger.**
1. **Waves carry commitments.** ARCHITECT's `waves` become `{goal, commitments}`; code puts an unassigned commitment in the
   last wave. DETAIL asks only areas that hold a commitment of this wave or consume a changed contract. Wave 1 is the skeleton
   because the architect is coached to put the thinnest end-to-end path there, not because code checks it.
2. **Contracts just in time.** ARCHITECT writes in full only the contracts wave 1 needs; a later one is a handle and one line
   until its wave is planned. Fixes row 1; a cross-wave contract is an ordinary plan node.
3. **STEER = ARCHITECT again.** After check-in the same question is asked with new facts: the previous architecture, one row
   per unit of the finished wave (worker summary, discoveries, open gaps, not judged), the user's check-in words, the
   remaining waves. The answer names only what changes; code merges by handle and validates the whole with
   `architecture.outline`. A changed contract already clears its consumers' judgments (`store.py:203`); now it also gets their
   area a DETAIL call. A change that needs a new or dropped commitment is answered `scope` and goes back to ALIGN and gate A,
   the existing "user approves scope" path. No STEER state, no amendment schema, no steer module.
4. **One owner per path for the whole run.** In a later wave, an answer that names an existing unit's scope is that unit
   continuing with more requirements (`extend`); a new scope is a new unit. Scope exclusivity, check ownership, fixup routing
   and verdict reuse by scope tree stay as they are. An earlier check broken by a later wave fails at WAVE-VERIFY and goes to
   its owner, who fixes it or hands it on (today's defect-to-owner rule).
5. **DETAIL from results.** The area brief gains "What exists here": its units (scope, acceptance sentences, last worker
   summary) beside the file list, and loses contracts the area does not touch. Handles are assigned once
   (`<wave>.<area>.<n>`); the plan accumulates and earlier waves are never re-merged.
6. **Unit steering = the coach, once.** On the second failure code asks COACH (planner model) with what was tried and sends
   the guidance to the worker. Only the next failure goes to the user. Re-split is not built: measure first.
7. **Check-in.** Approve goes on; revise carries the words into rule 3. DECIDE gains one choice, "approve and do not stop
   again": later check-ins are recorded and shown, not waited on (C8). Scope always waits (gate A).
8. **Placeholders need no record.** What the skeleton leaves out is a commitment of a later wave; units are judged only on
   their own wave's acceptance sentences; C needs every commitment validated.
9. **VALIDATE.** `judgment.subjects` adds one subject per scopeIn/improvement commitment: its text, the verdict rows of the
   features in its areas, the guide walkthrough evidence. Behaviour only (R2). This is the cross-area judge of row 6.
10. **Guide per wave.** The guide unit is extended each wave with that wave's contracts only: it is what the user tries at
    check-in and the wave's end-to-end smoke. B stays valid while the vision it approved is the current vision.

Deferred, measure on the test dream first: check reuse across rounds (row 4), read costs, splitting an over-grown unit.

**Lanes** (disjoint files; the lead first freezes `states.py`, `store.py`, `schema.py`, about +25):

| Lane | Files | Delivers | Src |
|---|---|---|---|
| W wave loop | `run.py`, `fixups.py`, `plan_review.py` | wave counter, CHECK-IN branches, waveStart, B bound to the vision, create/extend units per wave, dropped units at C, review repair per wave | +30 / -20 |
| P progressive plan | `plan.py`, `detail.py`, `architecture.py`, `questions.py` | rules 1, 2, 3, 5, 10; trims the product-sized facts of row 5 | +75 / -30 |
| S steer, check-in | `recovery.py`, `units.py`, `decisions.py`, `scheduler.py` | rules 6, 7; drop; deletes the "until M3" refusals | +35 / -10 |
| V validate | `judgment.py`, `flow_review.py` | rule 9; a unit without checks no longer blocks | +30 / -10 |
| R rig (no src) | `tests/seldon`, ladder oracle | scripted journey, 50 units / 5 waves, kill in wave 3 (P2); Quiet Bench brief, oracle, plain-Terra baseline | 0 |

Net about +120, main near 4.3k. All five start together after the freeze; one wiring landing by the lead. Each lane: one
golden journey with a fault twin, outcomes only; each new coaching sentence gets 5 Terra runs before a cohort (R16).
One line per lane for Oren: W, P, V coach (the model gets the product and its own results); S puts a coach's word before the whistle.
## 3. The intermediate test dream: "Quiet Bench" (ANC in simulation)
Step 0, nearly free: ShelfLife with the user dictating two waves, 1 Terra run, existing oracle. Proves the loop only.
Then Quiet Bench, in the user's words: *a noise-cancelling test bench on this PC, no hardware. Generate or import a noise
signal, simulate the acoustic path, run an adaptive canceller, save each session on a small local storage server, and show
in a page what was cancelled per frequency band. Three waves; first the thinnest thing that runs end to end.*
- 4 areas (signal + DSP core, session store, operator page, command line), 10-14 units, Python and Node only.
- Waves: 1 one tone through a fixed filter, saved and shown; 2 adaptive filter, band attenuation, browse and reload;
  3 compare runs, limiter and stop switch, WAV import. The session schema must grow in wave 2: the cross-wave contract change.
- Every run: one scripted steer at check-in 1 ("also export a session as CSV"), "do not stop again" at check-in 2, one kill
  inside wave 2. Expected 40-60 min on Terra. 1 run, fix, then 5. It is also the first slice of L3.
**Oracle (black box, same for plain Terra):** (1) follows the try-it guide from a fresh copy, and every wave's promises work
at the end through the real path (CLI, API, browser); (2) wave-1 behaviour still works after wave 3; (3) numbers on the
oracle's own hidden signal: attenuation per band above a floor a fixed filter cannot reach, so a left-over skeleton stub
fails, and the limiter holds when the filter is driven to diverge; (4) save, restart the server, reload, values equal, and
wave-1 sessions still load after the schema grew; (5) the steered CSV export exists and matches the session; (6) page craft,
scored as in ShelfLife. Run report, not oracle: 3 waves closed, the kill resumed without redoing a DONE unit, user questions
asked, largest question in wave 3 no larger than in wave 1, calls and fresh tokens per wave.
**Bar (lead's call): 4 of 5 reach C autonomously, each oracle score at least plain Terra's.** Then ANC proper.
## 4. BLUEPRINT changes for Oren to ratify
1. **§3.1 Unit, replace its last three sentences:** "A path has one owner for the whole run. A later wave gives the owner
   more work in the same scope; work in new paths is a new unit." *Why: one rule instead of owners changing hands and
   inherited checks; today's routing does not change.*
2. **§3.2 Run line:** "per wave [EXECUTE -> WAVE-VERIFY -> CHECK-IN -> STEER and DETAIL next wave]. STEER is the architecture
   question asked again with what was built and what the user said." *Why: one call sees results and the user's words
   together; Seldon's changes are still shown at the next check-in; a scope change still goes to the user first.*
3. **R5, replace the placeholder sentences:** "What the skeleton leaves out is a commitment given to a later wave. C cannot
   pass while a commitment is not validated." *Why: no separate placeholder record to keep true.*
4. **§3.3, add:** "ARCHITECT writes in full only the contracts the next wave needs. A later contract is one line until its
   wave is planned." *Why: a contract for wave 3 written before wave 1 exists is a guess.*
5. **R15, replace "Until unit steering lands..." with:** "After one recovery the planner is asked once for a new approach;
   the next failure goes to the user."
6. For information (lead's call): Quiet Bench 4 of 5 precedes the ANC cohort; at exit close DV3, DV5, DV6; fix the file header version.
## 5. Risks, stated plainly
- Rule 4 lets one unit grow over many waves until its judge question is large. R15 says send it whole; if Quiet Bench shows
  it, let the planner open a new unit in an empty sub-path. Do not bring back owner hand-over.
- Rule 3 asks for "only what changes"; a weak model may resend all or omit: merge by handle makes both harmless. Check on 5 Terra runs.
- Row 4 (full reruns) is not fixed here and will be the wall-time pole at ANC size. Any reuse keys on git tree ids only (R9).
