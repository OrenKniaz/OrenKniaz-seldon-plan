# M3 steering: one door, one comparison (Fable, 2026-11-15)

Read-only design review. Basis: CHARTER v1.8, BLUEPRINT v1.10, `src/seldon` at 683d19b (run.py, plan.py, decisions.py, wave_verify.py, recovery.py, scheduler.py,
states.py, detail.py, plan_review.py, store.py), TICKETS T-17/18/20/49/121/122, plan-cost-astra-2026-11-15, plan-converge-fable, loop-hunt-astra, speed-design-fable,
m3-design-2026-11-13. No provider calls, no tests. Nothing here is built; every scale number is an estimate until the journeys in §6 run.
TRIAGE: DESIGN. All six tickets are one missing rule: the plan can change in only one direction (forward to B) and consent is bound to a whole document.

## 1. The one rule
**Every plan change takes one door, and one comparison decides what it touches.**
- **One door.** A review gap, a merge correction, a stuck unit, a worker's contract discovery, the owner's words at any gate or mid-run, and "the next wave" are the
  same event: a recorded *change* with a source and a target. The planner that owns the target answers it (ALIGN for commitments, ARCHITECT for the outline, DETAIL
  for one area) and code compiles the next plan revision. This is today's pre-B REPAIR path, kept and allowed after B. No new question kind, no STEER schema.
- **One comparison.** An approval, a verdict or a unit's DONE stands while the canonical facts its subject consumes are equal in the new revision (the plan-cost
  rule, extended from questions to consent and done work). Nothing else invalidates anything. Compared as structured content; no hashes, counters or text heuristics.
- **Done work is never undone.** A change produces new units on top of the product as it exists (R10). Nothing integrated is reverted or re-judged because the plan moved.
Consequence: a run has no state where the owner's "no" or "change this" has nowhere to go (R15), and cost follows the size of the change, never the size of the plan.

## 2. What each record consumes (the whole comparison table)
| Record | Consumes | So it is asked or done again only when |
|---|---|---|
| A approval | the vision (commitments: scopeIn, improvements, quality) | the vision changes |
| B approval | the vision it displayed | a commitment changes (ratified v1.7: B binds the commitments) |
| CHECK-IN approval | that wave's end commit | never again; a new wave has a new one |
| DETAIL answer of (wave, area) | the area record, its contract texts, its decisions, its wave goal, changes aimed at it | one of those differs (detail.ask already reuses by `basis`) |
| REVIEW verdict of (wave, area) | the area's own plan content and the peer proof it consumes | per plan-cost landing item 3 |
| Unit DONE | its scope, instructions, requirement texts, check bodies, consumed and provided contract texts | no equal unit exists in its (wave, area) after the change |
| Unit / flow / quality verdict | git trees of the owning scopes (existing `judgment.current`, R9) | those trees change |

## 3. State and records it changes
- **`change` record (new, immutable; the only writer of a post-ALIGN revision):** `{source: review|merge|unit|discovery|owner|wave, cause, words, targets, before,
  after, kept, added, dropped}`. Folds `review_repair`, `detail_correction`, `architecture_gap`, `contract_revision` (four kinds become one) and
  `RunRow.requestedChange`. `targets` are handles: `vision`, `architecture`, or area handles. The page and the check-in card read these rows.
- **Who names the target.** CODE for every Seldon-made change (a gap carries its owner; a merge correction its participating areas; a unit its area; a contract
  discovery its contract). LLM only for the owner's words: DECIDE, already called at every gate, gains `targets` chosen from the handles in the displayed subject.
  Zero extra calls. A mis-aimed area change escalates by the existing `contract_gap` → ARCHITECT path.
- **B validity:** `plan.approved` becomes `B.subject.vision == cursor.vision`. Delete `contract_descendant` and the whole-document equality (B stores the plan and
  review inside the approval today and `run.py` compares them before EXECUTE).
- **Stable handles (also closes T-72):** `plan.merge` stops renumbering `n001/u001` globally. A node is `<wave>/<area>/<local handle>`, a unit `<wave>/<area>/u<k>`,
  with `k` never reused. Areas not re-asked keep their nodes byte for byte. `areaDetails` is keyed by (wave, area).
- **Adoption (`plan.adopt`, CODE):** in each re-asked (wave, area), a new unit whose consumed facts equal an old unit's takes that unit's handle and row (DONE stays
  DONE, no call). Any other new unit is new work based on the current candidate. An old unit left unmatched: never started → row removed; DONE → kept as history,
  state DONE, its commits stay; WORKING → the change to that area waits for it to return (R8), reason shown.
- **Unit node gains `wave`** (set by code). `RunRow` gains `wave: int`; `waveStart` moves at wave open. No WaveRow: the per-wave fields on RunRow are already keyed
  by `candidate` and are simply rewritten each wave. Outline `waves[i]` gains `commitments`; code checks the union equals the vision's.
- **Run table:** `REPAIR` is renamed `STEER` (the door) and gains entries from `B`, `CHECK-IN`, `C`, `EXECUTE`; exits to `ALIGN`, `ARCHITECT` or `DETAIL` by target.
  `REVIEW.reviewed` goes to `B` only when the B approval is not current, else to `EXECUTE`. `CHECK-IN.approve` goes to `DETAIL` while a wave with open commitments
  remains, else onward. `decline` no longer calls `stop()`: DECIDE's choices become `approve | change | stop | unclear`. A "no" without direction leaves the
  same question open (parked, resumable). Only the owner's explicit stop ends a run. Net: zero run states added.
- **Deleted:** the hold "Changes after B arrive with steering (M3)"; "Dropping is not available yet" (a drop is a commitment change through the door);
  `decline → stop`; plan-wide scope disjointness; whole-plan B subject.

## 4. Waves and scopes
- **A wave is the units of one `wave` index.** It ends where it does today: all its units integrated and WAVE-VERIFY green on one commit, then flow review, then
  CHECK-IN. Opening wave w+1 is a `change` with source `wave`, aimed at the areas holding a commitment of that wave, an open placeholder or a stale contract
  endpoint. Other areas get no call. The loop body is unchanged; hello-world is wave 0 with one area and takes the same path (R1).
- **DETAIL(w)** writes only wave w's units for one area. Added facts: the wave's goal and this area's commitments in it; "what exists here" (one row per DONE unit
  of the area: scope, obligations, worker summary) beside today's file listing. It never re-emits earlier waves (R3).
- **Scopes are exclusive within a wave only** (BLUEPRINT §3.1, already ratified). `plan.validate`, `validate_owned_work` and `merge` compare units of the same wave.
  The owner of a path, and so of a check file, a fixup and a gap, is the latest unit whose scope holds it: `plan.owners` picks the highest wave among candidates.
  The scheduler's running-overlap wait stays as the runtime guard. Changing behaviour delivered in an earlier wave is a new unit over those paths, which must
  name the inherited checks it revises (§3.1). WAVE-VERIFY keeps running every accumulated check.
- **Mid-wave steering.** A unit that spent two recoveries becomes a `change` aimed at its area (facts: failure history, previous area plan, sibling claims). The
  scheduler calls the door inline, as it already calls `decisions.decide` inline: one DETAIL and one REVIEW for that area while running workers continue; only new
  starts wait (about 2-4 min). The scheduler reloads the plan and creates rows each loop instead of once. Work that comes back a second time (same recovery
  lineage, already tracked) is one owner question; the owner's direction goes through the same door.

## 5. Owner experience at 100 units (chat acts, the page shows; C20)
| Gate | Chat card, built by code, same size at 3 and 300 units | The owner can say |
|---|---|---|
| **A** | Understanding, commitments, quality bar, size. Unchanged. | approve; change (→ ALIGN) |
| **B** | Commitments by handle; areas (one row: responsibility); wave outline (one row: goal, commitments closed); wave 1 as unit counts per area and its goal; review result per area (adequate, not judged, open gap). About 40-60 lines. Every unit, check and contract is on the read-only page. | approve; change X (→ door, returns to B only if a commitment moved, else shown at next check-in); a "no" alone keeps the question open |
| **Scope change after B** | One question, not two: commitments added, removed or reworded, then the impact computed by adoption (units kept, new, dropped, per wave; areas re-planned). Approval rebinds A and B together. Until it is answered the run continues on the approved plan; declining discards the proposal and nothing stops. | approve; change; keep the current plan |
| **CHECK-IN** | Wave goal and result; commitments closed with their flow verdicts; the `change` rows since the last card (source, what, kept/new/dropped counts); not judged; next wave's goal and commitments. Recorded and shown even when waived (C8 v1.8). | approve; change X (→ door, built in the next wave or as new units now) |
| **C** | Per commitment: delivered verdict, evidence link, try-it guide, not judged. | accept; change X (→ door → a further wave → CHECK-IN → C) |
| **Unit question** | What was tried, what failed, who waits, recommendation (exists). | direction (→ door); drop the commitment (→ scope question) |
Units are never listed in chat, only counted. The scripted response binds `{request, subject, choice}` to the small card subject, not to a plan document.

## 6. Cost at scale (estimates; planning rates from plan-cost b01-b03 and i01)
- Per (wave, area): 1 DETAIL (+ about 0.4 exact-fix retry until reference normalisation lands) + 1 REVIEW, in parallel across areas, 1.5-2.5 min wall each.
- 100 units, 10 areas, 6 waves, capacity 8: before B = ALIGN + ARCHITECT + architecture review + about 6 areas of wave 1 ≈ 16-20 calls, 6-8 min. Each later wave
  ≈ 10-15 calls, 3-5 min. Whole-run planning ≈ 80-90 calls, 25-30 min wall, against roughly 100 × 8 min / 8 ≈ 100+ min of unit work plus proof.
- One-area steer: 2-5 calls (the area, plus consumer reviews whose peer proof really changed), 2-4 min, no running worker interrupted, zero owner questions.
- Outline steer: + ARCHITECT + its review + DETAIL only for areas whose consumed facts differ. Scope steer: + ALIGN + one owner question.
- Never paid: re-plan of untouched areas, re-review of unchanged subjects, re-judging or re-running DONE units, a second B for a non-scope change.
- Not solved here: WAVE-VERIFY reruns every check each wave (linear, code time); T-32 integration lock. Each run reports calls and minutes per change (P11).

## 7. Tickets
| Ticket | Outcome |
|---|---|
| T-17 one wave, no steering | Closed by slices 3-4: the wave index, DETAIL(w) as a `wave` change, CHECK-IN → DETAIL. DV3 and DV5 close at the M3 exit cohort. |
| T-18 no plan repair after B | Closed by slices 2 and 4: the door is legal after B; a stuck unit is an area change; B stays valid by comparison. |
| T-121 decline or revise ends the run | Closed by slice 2: every gate's "change" enters the door; "no" parks; only explicit stop ends. Nothing reaches INCOMPLETE. |
| T-122 B subject too large | Closed by slice 2: B consumes the vision; the card is a bounded code projection; detail is on the page. |
| T-20 plan-wide disjoint scopes | Closed by slice 3: exclusivity per wave, latest owner by path. |
| T-49 repair cannot name the units behind competing claims | Moot as a separate fix: a merge correction is a `change` whose targets are the participating areas and whose facts are their conflicting claims (merge already computes both for cycles and provider counts); only when no area can fix it does it go to ARCHITECT with the previous outline. Close on the slice 4 replay. |
| T-72 obsolete handles (bonus) | Closed by slice 1: handles are stable and area-local. |

## 8. Build order (serial; each lands alone on the fast gate; behaviour-only journeys with a fault twin)
Prerequisite: the plan-cost first landing (canonical-content review basis). Slice 1 reuses its comparison rather than adding a second one.
| Slice | Files | Net lines (est.) | Proof journey |
|---|---|---|---|
| **1 Stable plan, adoption** | `plan.py` (handles, `consumed`, `adopt`), `detail.py` (areaDetails by wave/area), `store.py` (`change` kind) | +50 (+110 / −60) | Five areas, three units DONE; one area re-detailed before B and again after: untouched areas keep every handle, row and verdict with no call; an equal unit stays DONE; a changed one is new work on the candidate; an unstarted orphan row is gone. Twin: kill during adoption, reopen, same result. |
| **2 One door at every gate** | `decisions.py`, `states.py`, `run.py`, `plan_review.py` (repair → steer), `questions.py`/`schema.py` (DECIDE targets, B card) | +10 (+90 / −80) | Owner changes at B twice then approves; changes at CHECK-IN and at C and receives a changed product and a fresh gate each time; a scope change is one question with its impact, and declining it keeps the run going; a bare "no" parks and resumes; B card bytes equal at 3 and 100 synthetic units. Twin: change words aimed at the wrong area still reach the right planner. |
| **3 Waves** | `run.py`/`states.py` (CHECK-IN → DETAIL), `detail.py`/`questions.py` (wave goal, areas with work, what exists), `architecture.py` (wave commitments), `plan.py` (per-wave scopes, latest owner), `obligations.py` | +70 | Extend P2: 50 units in 5 waves reach scripted C; an area with no work in a wave gets no call; a wave-2 unit takes a wave-1 path and the wave-1 check runs under its new owner; kill in each run state of wave 3 resumes without redoing a DONE unit; largest question equal in waves 1 and 5. |
| **4 Mid-wave steering** | `scheduler.py` (reload per loop, inline door), `recovery.py`, `units.py`, `fixups.py` | +30 | One unit of N fails a third time: its area is re-planned and the wave completes while N−1 siblings never stopped; its successor failing reaches one owner question whose direction is tried; T-49 replay (reciprocal dependency, then duplicate provider) reaches B with the participants named. Twin: the re-plan returns the same plan → owner question, not a loop. |
Total about +160 net in `src`, no new module, one state renamed. Before the L3 cohort: recorded real answers for DECIDE-with-targets and DETAIL-on-existing-product
join the replay set (P3); scripted journeys prove routing only (P2).

## 9. Risks, stated plainly
1. **Unit matching by equal content.** A planner that rewords an unchanged unit creates duplicate work (a worker then finds it done: minutes, not corruption).
   Supply the previous area plan and ask for unchanged units verbatim; report "reworded" counts per change. Do not add text-equivalence heuristics (I1).
2. **ARCHITECT churn.** In b01 each ARCHITECT round changed every area's inputs (wave and decision text). At 10 areas an outline steer then costs a full wave
   re-detail. Area facts must carry only that area's decisions and wave commitments so the comparison stays local; measure before tuning.
3. **DECIDE targeting** is the one new LLM-written field. A wrong target wastes one DETAIL call and escalates; it cannot change scope, because only ALIGN writes the vision.
4. **Post-B plan drift is not owner-approved** between check-ins. This is the ratified v1.7 trade (B binds commitments); the `change` rows on the card and page are the control.
5. **History units.** Code from a DONE unit whose plan was replaced stays in the product. Its paths belong to the latest owning unit; a path no live unit owns must
   appear as a fact in that area's next DETAIL. Until VALIDATE lands (DV6) a narrowed commitment under green checks is caught only by flow review.
6. **Start stall** during an inline steer (2-4 min for new starts). Accept, measure; move planning off the control thread only if P11 shows it matters.
7. Out of scope and still per m3-design-2026-11-13: typed discovery kinds, per-area quality, VALIDATE per commitment, one judge loop. This design replaces that
   note's STEER question, `steer.py`, `checkin.py`, `waves.py`, WaveRow, envelope record and REPLACED state; it does not conflict with its ratified wording.

## 10. Draft text for Oren (BLUEPRINT only; no charter change needed)
**§4, new R16. One door, one comparison.** "Every change to the plan, before or after B, is recorded with its source and target and answered by the planner that
owns the target: ALIGN for commitments, ARCHITECT for the outline, DETAIL for one area. Code adopts the new revision. An approval, a verdict or a finished unit
stands while the canonical facts it consumes are equal in the new revision; nothing else invalidates it. Finished work is never undone: a change adds units on top
of the product as it exists. *Check:* in a journey with one area changed after B, every other area keeps its units, verdicts and approvals with no call.
*Prevents:* T-18, T-121 (a change after B had nowhere to go), whole-plan consent (T-122)."
**§3.2 Run, after "any change to the commitments goes to the user first", add:** "At B and at every check-in the chat shows commitments, areas, the wave outline
and counts; units are shown on the read-only page. A changed commitment is one question that shows the change and its impact; until the user answers, the run
continues on the approved plan. Declining without direction leaves the question open; only the user's explicit stop ends a run."
**§3.1 Unit row, add:** "A record's handle is assigned once and never renumbered."
