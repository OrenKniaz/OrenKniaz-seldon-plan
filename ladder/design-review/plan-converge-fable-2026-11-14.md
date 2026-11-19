# Planning convergence bird's-eye (Fable, 2026-11-14)

Read-only review of cohort m2k on 54eaab4 (k02, k04, k05 stores) and plan_review.py, detail.py,
architecture.py, recovery.py, questions.py, decisions.py. No provider runs. Astra's note not read.

## 1. Why each run cannot converge

**Shared blocking cause (all three, a BUG in today's lineage landing, recovery.py).**
`recovery.planning` asks the owner *instead of* routing: when `failed()` returns asked, the
`advance(event)` is skipped, so the state does not move. After the owner answers, the same step runs
again, records a new cause, and `failed()` asks again at once because of
`asked = ... or bool(state["answer"])` (recovery.py line 28 of the module). The owner's direction is
never given to any planner. Proof in the stores:
- k02: r188 direction -> r196 review_repair -> r197 question; r198 -> r206 -> r207. No DETAIL call after r174.
- k04: r274 -> r282 -> r283; r284 -> r292 -> r293. No DETAIL call after r244.
- k05: after r168 and r186 only `REVIEW architecture` questions ran (r176, r194). ARCHITECT never ran again.
So "6 attempts and 2 owner directions" is really 3 review rounds, then two directions that were dropped.

**Second shared cause: progress was charged as failure.** A verdict with an architecture-target gap
is charged twice (review_repair, then architecture_gap: k02 r94+r96, k04 r116+r118). The owner was asked
after 3 rounds while gaps were shrinking and different each round (k02 3 -> 1 -> 1, k04 7 -> 3 -> 1).
That is not a fixed point.

**The gap each run would hit next, even with routing fixed:**
- **k02 (BUG, guideUnit).** `questions.build` tells DETAIL that Seldon's guide unit owns `docs/try-it.md`,
  but REVIEW is not told. Delivery correctly refers to the guide; the reviewer sees an unagreed file and
  demands a contract for it (r182). The reviewer lacks a fact the planner had. Also its target
  "architecture: contract_gap ..." is not exactly "architecture", so plan_review.step sent it to delivery.
- **k04 (DESIGN, provenOnce).** Round 2 told server to move the validation matrix to the HTTP boundary.
  Server did. Round 3 (r268) then said persistence checks n008/n010/n011 now overlap and "server cannot
  perform that cleanup outside its scope". A REVIEW gap is `{target, correction}` with no owner;
  plan_review.step labels it with the reviewed area; REPAIR re-asks only server, which cannot edit a
  peer's records. The gap is true under v1.10 but nobody it is sent to can fix it. It is surplus proof,
  not a missing promise.
- **k05 (DESIGN, provenOnce).** The interface reviewer (r82) asked that quality:5 trace to the backend's
  query check. `architecture.local_plan` refuses any non-local check in quality coverage, so interface
  DETAIL can only answer `contract_gap: supply the backend check handle` (r97, r132). ARCHITECT is
  forbidden to write checks, so it records a deferring decision; ARCH-REVIEW rejects the deferral (r164,
  r182, r200). The needed fact (a peer's check proves part of my criterion) cannot be written at any level.

Hypothesis verdict: half right. Reviewers do see real cross-area proof facts and no move can act on
them (k04, k05). But the fix is not a new cross-area restructure move. Who proves what across areas is
structure that code can derive from the contract graph; the reviewer was asked to police it and to
have areas restate it. And the wall that actually stopped all three is the dropped owner answer.

## 2. The one rule

**A plan gap is sent only to someone who can fix it, and every answer is tried before anyone is asked again.**

What follows from it, nothing more:
- An owner answer always reaches a planner call (DETAIL or ARCHITECT) before the next question.
- One review verdict is one charge. A question means "the same subject came back after a real try".
- The reviewer gets the same facts the planner got, plus the peers' proof as code-derived facts.
- Before B a reviewer raises only a missing promise or an unagreed shared value. Where proof sits
  across areas (overlap, reuse, which boundary) is derived by code and is never a plan-review gap.
  "Proven once" stays a planner instruction and a P11 measurement; it is not a gate (R15, P11).

## 3. Revert or narrow

| Landing | Verdict |
|---|---|
| lineage (recovery.py) | NARROW. One shared history is right. Fix the dropped answer and the double charge. |
| provenOnce (level text + proof map to REVIEW/JUDGE) | NARROW. Keep level definitions in DETAIL and the map for JUDGE. In REVIEW the map is a fact, peers' rows count as proof, overlap and cross-area tracing are not gaps. |
| guideUnit | KEEP the unit. NARROW: REVIEW gets the same guide fact as DETAIL. |
| repairConverge c486ed0 | KEEP. Normalise the target match (starts with "architecture"), do not require exact text. |
| depGraph b2f0f13 | KEEP. No evidence against it in these runs. |

## 4. Smallest change list (delete first)

1. `recovery.py failed()`: delete `bool(state["answer"])` from the planning ask (when `shape` is given).
   `answered()`: set `rounds = 0, stage = 0`. An answer is new information and gets its own tries.
   The unit path (`recover`, no shape) is unchanged.
2. `detail.gap()`: when called for a forwarded repair (detail.collect, "architecture" in the correction),
   charge under that repair's ref, not a new one. `failed()` already ignores a cause it has seen.
3. `plan_review.repair()`: owner words are added to each area's review gaps, not put in their place
   (today `corrections = {...words}` throws the reviewer's gap away).
4. `plan_review.step()`: `g["target"].lower().startswith("architecture")` instead of `== "architecture"`.
5. `questions.build()`: add the guide fact for REVIEW as well as DETAIL (one condition).
6. `plan.proof_map()`: for each wave-level row, add the provider-side checks of the requirements it
   integrates, marked `peer` (the links already exist from `deferred_checks`). About 4 lines.
7. `questions.PROMPTS["REVIEW"]`: one sentence: "Peer rows are proof already planned by their owner;
   never ask this area to repeat, trace or change them; overlap with a peer is not a gap." Delete nothing
   else; add no new state, no new record kind, no cross-area repair step.
Not now: routing a gap to the owner of a handle it names (n008 -> persistence). Add only if a real
peer-record gap survives 6 and 7.

Outcome journeys (extend `tests/seldon/lineage_journey.py` and `gap_owner_journey.py`, no new suites):
- **k02-shape:** review returns a gap for three rounds, owner gives a direction. Outcome: the next
  provider call is a DETAIL question that carries both the gap and the words; the run reaches B; there is
  never a second decision_request without a planner call between.
- **k05-shape:** the question is raised at ARCH-REVIEW; owner gives a direction. Outcome: the next
  planner call is ARCHITECT with the words; the run reaches B.
- **k04-shape:** a recorded two-area plan where a consumer wave check crosses a provider contract.
  Outcome: the consumer's REVIEW question shows the provider's checks as peer rows and the guide fact;
  one verdict with an architecture gap plus an area gap moves the recovery round count by one.
Stubs cannot prove that a real reviewer stops asking for overlap cleanup. That part is proven only by
real planning-only runs (see 5).

## 5. Before the next cohort

- The three journeys pass in the fast gate, once (no test tuning).
- Three real ShelfLife runs stopped at B (planning only, about 10 minutes each): at least 2 reach B with
  no owner question. Read every REVIEW gap from them: zero gaps about overlap or cross-area tracing,
  zero gaps about the guide file. If one appears, fix the prompt sentence, do not add a mechanism.
- In any run where the simulated owner answers, the record after the answer is a DETAIL or ARCHITECT
  question, and the report's planning rounds equal the number of review verdicts with gaps.
- The cohort report labels a run "owner fixed point" only when the same subject returned after an
  answered direction was tried. k02/k04/k05 would not have earned that label.
