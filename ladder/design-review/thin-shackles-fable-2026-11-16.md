# Thin: remaining shackles, parallel build, T-184 (Fable, 2026-11-16)

Read-only. Basis: CHARTER v1.8, BLUEPRINT v1.10, thin tree `work/lanes/guideEvidence/src/seldon` (4,429 lines; line numbers below
are that tree), the five stores `C:/seldon/tests/m1/shelflife-thin2-f2ffb6e-t01..t05` (540 recorded replies, read with mode=ro).
No provider calls, no tests run. Estimates of lines removed are estimates.

## 0. Three facts from the stores that change the brief
1. **The build is serial because of code, not because the architect makes few units.** Every run has 2 areas and 2-4 units, with
   5-6 contracts between them. `plan.py:235-245` then turns every `reads` path into a dependency edge. Result in all five runs:
   one chain. t03 and t05: the backend waits for the page (it "reads" `static/index.html`). t01, t02: a unit waits for the owner
   of `checks/kit/**`, files Seldon itself supplies and that are already in every worktree. First-pass WORK calls in t01 were
   7.2 + 2.6 + 6.0 + 8.6 min in a row (24 min); side by side that is 9 min.
2. **The unit judge is asked about peers that are not there.** 20 unit JUDGE gaps in t01-t04; 17 say a peer file is absent or
   integration was not exercised ("import_items.py is absent", "server.py was absent"). Each costs one rework, then the unit
   integrates anyway as an "open gap". Nearly every unit pays this once.
3. **T-184 is not a check failing locally.** t05 u002: the worker returned `done` correctly on call 1 ("static checks pass;
   real-server integration remains unproven"). The unit judge gapped all 5 requirements because the backend was absent (and the
   backend was waiting for this unit, fact 1). Sent back, the worker asked the right question: "May u002 hand off with integrated
   acceptance pending WAVE-VERIFY?" `units.py:73-78` matched the words "wave-verify"/"handoff" and answered with a dump of
   execution facts instead of "yes". The worker asked again; the answer is cached (`units.py:70-72, 86-87`) and the path back to
   the worker is not counted (`units.py:88-90`). 294 times. Plain worker was right every time: FAULT SELDON, DESIGN.

Other code refusals of model answers in the same runs: "reads and file prerequisites must name a concrete file" x14 (DETAIL),
"Discoveries must name an approved unit or contract" x10 (each re-asks a whole WORK session), "name one existing provider area
and distinct existing consumer areas" x5 (each re-asks ARCHITECT, ~1 min of the strongest model; t01, t02, t04 ran it twice).

## 1. SHACKLES, ranked by measured cost
Lane letters: A and B touch disjoint files and can run together. C runs after both land.

| # | Where | Forces / forbids | Why not needed, or the coaching replacement | Lines | Lane |
|---|---|---|---|---|---|
| 1 | `plan.py:235-245`, `plan.py:84-85, 190-192`; `schema.py:39, 51` (`reads`); `architecture.py:77-80, 183-187` | Planner must list files each unit reads; code makes each a dependency; wildcard reads refused (x14) | A contract is the agreement that lets both sides build at once (R4). Delete the `reads` field and the derivation. `dependencies` stays: local unit positions only, for "cannot be written until the other's files exist" | -30 | A |
| 2 | `units.py:70-78, 86-87` | Code answers a worker's question by keyword match, with a fact dump, and caches it | Meaning judged by pattern-matching (I1). Every worker question goes to the planner (COACH), who answers in words | -12 | B |
| 3 | `units.py:164-172` | Unit JUDGE gap sends a unit back even when its proof belongs to WAVE-VERIFY | See section 3. One condition; removes ~1 rework per unit per run | +1 | B |
| 4 | `questions.py:281-284`, `inference.py:60-61`, `units.py:31` | A worker discovery must name a unit or contract node or the whole WORK answer is refused (x10) | A discovery is a note for check-in. Accept any owner text; delete the validator | -9 | B (calls), A (dead def) |
| 5 | `architecture.py:116-120, 63-65` | Contract naming its provider among consumers, or a duplicate consumer, is refused (x5) | Derivable: code drops the provider and duplicates from consumers (normalise, T-111 rule). Refuse only an unknown area name | -2 | A |
| 6 | `schema.py:17-18, 21, 72-85, 114, 142` | Every planning list <= 12 items, contract and requirement text <= 2,048 chars, all text <= 8,192; over = refused | R15: limits route, never refuse. The 2,048 cap pushes contracts to be thin, which is the opposite of what parallel building needs. Delete `bounded()` and `maxLength`; sizes are already recorded per call | -14 | A |
| 7 | `schema.py:31` | Contract `kind` is a closed list of six | I3: closed lists of what a product may be are forbidden (a data rule, a visual style, a protocol fail today). Make it free text | 0 | A |
| 8 | `schema.py:101`; `questions.py:60-62` | Worker must list requirement handles per check | Code overwrites them (`plan.py:65`). Drop the field and the prompt words | -1 | A |
| 9 | `questions.py:167-168`, `schema.py:55-57` | Architect must place "check subtrees" and "shared check helpers" in area scopes | In thin, workers write their own checks. This text produced checks-only units (t02 u003, t04 u002), a "check-helpers" contract (t05) and kit ownership. Replace with the kit sentence in section 2 | 0 | A |
| 10 | `questions.py:112` | UI craft rules (8 lines) appended to every WORK prompt, backend included | Noise for a weaker model. Supply as a labelled fact only when the unit's area carries the visual-direction commitment | 0 | A |
| 11 | `schema.py:89-92`; `questions.py:355-356, 373-378`; `inference.py:62-67`; uses in `judgment.py`, `flow_review.py:85-91` | Judge fills 2-3 booleans per requirement plus verdict plus gaps; code refuses answers where they disagree | Redundant: a requirement is negative exactly when a gap names it. Keep verdict, gaps (target, correction), why. "RED enough" (v1.9) is a gap like any other | -25 | C |
| 12 | `schema.py:38-39, 49-51`; `architecture.py:30-33, 66-76, 159-165`; `plan.py:193-200, 214-222` | Each unit must restate which contracts it provides and consumes; mismatches refused or sent back as corrections | Consumers are derivable (every unit of a consuming area gets the text). Only `provides` is needed, and only when an area has several units | -15 | C |

Not in a lane, needs Oren's word because R5 names it: **skeleton obligations** (`obligations.py` 30 lines, plus about 20 in
`architecture.py:140-144, 179-182`, `plan.py:128-131, 181-183`, `run.py:45-46`, `schema.py:35, 63`). The core runs one wave, so a
"placeholder to close later" cannot exist, yet the schema offers it and the planner used it in 4 of 5 runs (2, 1, 3, 0, 3). Proposal:
stop offering it until waves land in M3 (about -50 lines). Also free: the no-op ARCH-REVIEW state (`plan_review.py:7-8`, -6).

Checked and kept (structure, not shackles): disjoint scopes, `safe_path`, one unit per requirement, exact-fix retries (C4),
scope enforced from the diff, the vision `size` enum (C5).

## 2. PARALLEL BUILD: coach the split, delete the serializer
No new rule or validator. Four changes, all in lane A.

**a. Code stops serializing (shackle 1).** Units that share only a contract start together. `plan.wave_requirements` already
names WAVE-VERIFY as proof owner for a unit that consumes a peer's contract, so nothing new is needed there.

**b. ARCHITECT prompt (`questions.py:47-50`), replacing "Prefer the fewest units ... parallel work pays":**
> What areas, agreements and wave goals deliver the accepted vision? Split it the way a small team would start on the same
> morning: each area is work one builder finishes alone, at the same time as the others, from the contract text. Put into
> contracts everything two areas must agree on (routes and payloads, data rules, file names, commands, page structure), complete
> enough that neither side needs to see the other's files. A session-sized app is usually 2-4 areas; a truly tiny one is 1.
> Give every commitment handle to one area, and give areas disjoint path scopes.

Ownership fact (`questions.py:167-168`): "Each area owns disjoint paths, with room for its own checks. `checks/kit` is supplied
by Seldon in every worktree; nobody owns or builds it." The ARCHITECT example (`questions.py:137-141`) is one area with zero
contracts, and a weaker model copies the example: make it two areas (a small API and its page) with one full contract.

**c. DETAIL prompt (`questions.py:51-54`), add:** "Normally the area is one unit. Use more only when they can be built at the
same time. Name a dependency only when a unit cannot be written until another unit's files exist."

**d. What the worker, the unit judge and COACH see** (`questions.py:277-278`, the `Execution` fact, replacing the current text):
> Your peers are building their units right now from the same contracts; their files are not in this worktree. Build to the
> contract text. Run what you can here. A check that needs a peer's files fails here, and that is expected: write it, declare
> it, say so in your summary and return done. Seldon runs every check on the integrated product and comes back to you only if
> one fails there.

COACH prompt (`questions.py:57-58`), add: "Answer yes or no first when the question allows it."

Expected wall, from t01-t04 timings: planning 4-6 min; build = longest first-pass unit 7-9 min plus prove, judge, integrate 2;
WAVE-VERIFY 1-2; one parallel fixup round 3-5; FLOW and PRODUCT (already batched) 3-4; one gap round 4-6. **About 24-30 min**
against 39-58 today. Not proven: needs the cohort. Risk to watch: contract mismatches found at integration instead of earlier;
t03 and t05 already built the page before the backend from contract text alone, and t03 reached C at oracle 37.

## 3. T-184: one rule
**A unit goes back to its worker only for something its own worktree can show, and there is one counted way back.**

- *Only what its worktree can show.* When the unit's proof owner is WAVE-VERIFY (`plan.wave_requirements(document, ref)` is not
  empty), a unit JUDGE gap never reworks the unit. The verdict is recorded on the commit (C15 reading, Blueprint 8.4), the unit
  integrates, and WAVE-VERIFY plus flow review judge the real thing on the integrated commit, where a failure becomes a fixup
  for its owner. In `units.py:169`: `if not prior and not plan.wave_requirements(document, ref)`. Units with no peer keep
  today's single local rework. This removes the cause of the loop and fact 2's wasted rework.
- *One counted way back.* A worker question is answered by COACH (shackle 2), and the return uses `recovery.recover` like every
  other return, replacing the bare `advance(... "recover")` at `units.py:88-90`. Then the existing chain (two recoveries, then
  the user, R15) bounds every loop of this kind with no progress check, no cache and no new state. The 294 repeats become one
  planner answer; a second identical question becomes one user question while other units keep running.

No answer-comparison code, no "unchanged answer" detector: those would be patches on a path that should not exist.

## 4. Lane plan
Proof for every lane: golden and journey only, one gate run, no unit tests, timing never asserted. Report src lines before/after.

**Lane A `thinParallel` (Sol 6.1 medium). Files: `plan.py`, `architecture.py`, `schema.py`, `questions.py` only.**
Shackles 1, 5, 6, 7, 8, 9, 10 and section 2 b-d, word for word. Delete the `reads` field everywhere and `plan.py:235-245`;
`dependencies` in DETAIL become local positions only. Normalise contract consumers. Delete `bounded()` and text `maxLength`.
Free-text contract kind. New ARCHITECT/DETAIL/COACH prompt text, Ownership fact, two-area example, `Execution` fact, CRAFT as a
conditional fact. Delete `validate_discoveries` only if lane B has landed; otherwise leave it. Proof: a scripted journey with
two areas joined by one contract shows both units WORKING at the same time and reaching DONE with no dependency wait recorded;
an ARCHITECT answer listing the provider among consumers is accepted; a 3,000-character contract is accepted. Net src target:
-40 or better. Then a 5-run Sol ShelfLife cohort: wall, max parallel WORK, oracle >= 36.

**Lane B `thinOneWayBack` (Sol 6.1 medium). Files: `units.py`, `inference.py` only.** Closes T-184. Shackles 2, 3, 4 and
section 3. Delete the keyword lookup and the guidance cache; every question goes to COACH; return through `recovery.recover`.
Add the proof-owner condition at the JUDGE gap. Remove the two `validate_discoveries` calls. Proof: a scripted journey where a
wave-owned unit's judge returns a gap integrates without rework and the gap is repaired after WAVE-VERIFY; a fault twin whose
worker returns the same question forever ends in one user question with the other units DONE and the run resumable. Net src
target: -15 or better.

**Lane C `thinJudgePlain` (Sol 6.1 medium), after A and B land. Files: `schema.py`, `questions.py`, `inference.py`,
`judgment.py`, `flow_review.py`, `run.py`.** Shackles 11 and 12. Judges answer verdict, gaps, why; code derives per-requirement
status from the gaps; delete the consistency refusals. Units stop restating consumed contracts. Proof: existing golden judge
journeys green with the smaller schema; recorded-answer replay updated once. Net src target: -35 or better. Because Terra
missed real gaps in the judge replay (11-14), run that replay against the new judge schema before any Terra cohort.

Expected total after A+B+C: about 4,340 src lines. With the obligations proposal, about 4,290.
