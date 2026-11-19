# Speed design (Fable) 2026-11-14 — one shape for ShelfLife in 20-30 min and for large dreams
Read-only review. Basis: CHARTER v1.8, BLUEPRINT v1.9, src/seldon at b2f0f13, round-1/2 reviews, slot i01 product tree (m2i, ef048d4), the coordinator's check-duplication
measurement. No provider runs. Estimates are mine; measured numbers are cited.

## 1. The irreducible critical path
A run cannot be shorter than: PLAN (ALIGN, ARCHITECT, DETAIL fan-out, REVIEW: ~4.5 min clean) + W (the longest single writer) + PROVE/JUDGE (~0.7) + WAVE-VERIFY (~0.7) +
FLOW and PRODUCT in parallel (~1) = **~7 min + W**. W is output-bound (35-40 tok/s; commands are not the cost). Today W = 10-11 min (UI unit, 24-27k tokens). Everything
else on today's paths is waste of four kinds:
1. A serial tail that needs nothing it waits for: the guide (4.5-7.5 min every run; 25.7k chars in i01, larger than the UI).
2. Tokens that prove the same behaviour again: each unit writes a behaviour as a unit check against a fake peer AND as an integrated check (i01: server local.py 15.1k +
  inventory_double + integrated.py 15.3k; page local.cjs 12.5k + fixtures + integrated.cjs 9.9k; delivery fresh_folder.cjs 9.8k re-walks it; the guide walks it again;
  FLOW judges it again). i01 holds ~41k chars of product, ~110k of checks, 25.7k of guide.
3. Loops that do not converge or wait for no reason (plan repair on a contract gap, a unit question held until all units end).
4. Reasoning effort and user-config reading that buy nothing on reworks and prose.
Target arithmetic: 7 + W<=8 + one real fixup (~4) = ~19-20 min; no fixup ~15. So the design goal is W <= ~8 min, nothing serial after the units, and at most real-bug reworks.

## 2. The design: three rules, each a deletion
**S1. Only a local read makes anything wait.** b2f0f13 made this true for product units. Finish it: the guide is an ordinary unit with no dependencies that consumes the
contracts (commands, routes, labels are already contract text). Its walkthrough is a wave-level check: RED at wave start, GREEN at WAVE-VERIFY; a failure is a fixup owned
by the guide scope, whose worker then sees the integrated product. This deletes `dependencies: all` in plan.add_guide and needs no draft/resume machinery (I prefer it to
round-2 cut A: zero added cost when the guide is right, ~3 min when wrong; fall back to A only if a cohort shows guide fixups in more than half the runs). The same rule
covers "ask a stalled unit at once" (a question waits for the user, never for sibling units).
**S2. Every behaviour is proven once, by the unit whose code implements it; a wave check proves only the join.** What each level must prove (this answers the
coordinator's question):
- **unit check**: the behaviours this unit's code implements, exercised on the real surface (C26), fed at its boundary by contract-shaped *data* (canned responses or
  inputs copied from contract text). It never re-tests a peer's behaviour and never contains a peer with logic or state (i01 inventory_double.py, i02's fake API peer
  inside ledger.cjs 30.8k are a second implementation: waste now, drift later). Edge cases, states, errors and visual evidence live here, once.
- **contract check** (provider-owned): the provider's real product honours the contract text. Run locally. The fixture data consumers use and this check read the same
  contract text, which is what keeps fixtures honest.
- **wave check**: one real path per contract crossing, asserting agreement only (what one side wrote, the other side shows). It re-asserts no state or edge case a unit
  check owns. i01 integrated.py re-proves ordering, unicode search, concurrent consumes and restart persistence that inventory's own checks already prove: all of that
  goes.
- **walkthrough**: the guide's commands run and its paths exist. Nothing else. So do unit checks shrink to what is genuinely local? Half yes. The fake peer and any
  assertion about the peer go; the unit's own behaviours stay local, because the worker's run-and-refine loop is where first-time quality comes from (R8) and it is what
  keeps units parallel. The level that shrinks most is the *integrated* one: from a second full suite to a join. RED/GREEN is unchanged (C14, R9, v1.9 Rule 3): a
  requirement new in a unit has a unit check that failed at T; a cross-area requirement has its join check, RED at wave start, GREEN at WAVE-VERIFY; WAVE-VERIFY still
  runs every check on the integrated commit (C15), so nothing is proven on less than today. FLOW review remains the semantic cross-unit judge. How to land it within R12
  (no patch sentence): (a) replace the level sentences in DETAIL with these four definitions; (b) code computes a **proof map** (requirement -> checks with level and
  owner) from the plan and gives it as a fact to REVIEW (which names any requirement proven twice or a join that re-asserts unit cases) and to the unit JUDGE (so it stops
  asking a unit to prove a peer's behaviour locally: i01 r192, r235 were exactly that). No refusal, no cap.
**Ratification: yes, one sentence in BLUEPRINT 3.1 (Check record)**, because it fixes how C14/C15 are read: "A behaviour is proven once, at the unit that implements it,
against contract-shaped data; a wave check proves one real path per contract it crosses and repeats no unit case; no check contains a second implementation of a peer."
**S3. Mechanics are shipped once; meaning is written per unit.** The check kit, and the same idea for effort: roles pick the cheapest setting that the oracle cannot tell
apart (reworks and the guide at medium now; first WORK by A/B).

## 3. The check kit, judged
Weight: hand-written machinery is 15-25% of check code (coordinator), so on the UI pole ~6-8k of ~58k chars: **~1-1.5 min**, about half of what S2 saves there (~7-10k
chars, 1.5-2.5 min) and far less than S2 saves in total output (roughly a third of all check code, plus the judge gaps and reworks that code attracts). Build it second,
small. It is still right, for two reasons beyond minutes: i01 helpers.cjs hard-codes this PC's playwright-core and Edge paths into the delivered product (a real defect:
the user's checks run nowhere else), and at 100 units it is 100 copies.
- **Contents (two files, ~150 lines, no more):** `browser`: open a URL in the real browser found at run time, return the real Playwright `page`, `shot(name)` at the
  agreed viewports into SELDON_EVIDENCE_DIR, console-error capture, a deadline, guaranteed close. `serve` (node and python twins): start the product's real argv on a free
  port with a temp data dir, wait until ready, kill the tree. Nothing else.
- **Proof-strong:** the kit never asserts, never fakes, never substitutes a server ("no Seldon stub magic", C14). Pass or fail is still the worker's assertion and the
  exit code; the JUDGE reads shorter steps; the kit is covered once by Seldon's golden gate. No step DSL: workers write ordinary Playwright against the open `page` (I3).
- **Contender-neutral / product-neutral:** it knows no product, language of the product, or provider (I7); it is surface mechanics chosen by the setup facts, and it
  replaces the `browserHowTo` prose (R12: fix in code, not in a prompt). Code vendors it into the product's check tree on the wave start commit with code as its owner
  (R6), so the delivered checks run without Seldon. A worker that ignores it is not refused; usage is measured. In the fight the oracle is black-box on the product, so
  the kit cannot move the score; offer the plain contender the same folder if wanted.
- Later surfaces (API, CLI, HW) add a kit file only when a cohort shows repeated machinery. No ratification needed.

## 4. The parallel check writer, judged
**Not now, and not as product-vs-checks.** Reasons: (1) it removes the worker's run-and-refine loop: a product writer with nothing to run delivers worse, and the first
proof moves to WAVE-VERIFY where a miss costs a 2.5-6 min fixup; i04 (r417, r447: selectors written against an unseen UI, ~5 min) is the measured price of blind checks.
(2) It is R8's "two cold sessions per unit" again, in parallel instead of serial. (3) After S2 + kit the UI unit's checks fall from ~34k to ~18-20k chars, so the split
would save ~2 min at best and needs one clean agreement to break even. How it would work if a later cohort earns it (no new mechanism, R1): the check writer is an
ordinary unit whose scope is the area's check subtree and whose checks are wave-level; both units get the same requirements and the same contract text (the UI-structure
contract carries every role/name/label the checks use: round-2 cut E is the precondition, not an option); nobody waits. RED = each check fails on the wave start commit
(true tests-first, C14); GREEN = WAVE-VERIFY on the integrated commit; a disagreement is a fixup to the check owner, who fixes the check or names the product unit as
correction owner with the evidence (ef048d4). Trigger: after S1-S3, a unit whose checks are still more than half of W in two cohorts. Even then, first split the *unit*
along a contract seam (next section); that keeps each writer whole.

## 5. When to split a UI
One screen is one unit, always: components of one screen share state, layout and taste, and an integrator costs more than it saves. Split when ARCHITECT can state a
**UI-structure contract** (shell slots, routes, navigation names, design token names) such that each screen's requirements touch the others only through it. Then: a
shell+tokens unit provides that contract (skeleton wave, BLUEPRINT 3.3: screens really read its files, so this is a true dependency), screen units run in parallel after
it, the shell owner owns the one navigation join check, and PRODUCT judges coherence per area on screenshots (already so). ShelfLife (one page) is never split; a
12-screen app is 1 + 12 units over two waves. This is ARCHITECT's judgement by seams, not a size branch (R1), and uses the existing Contract kind: no ratification. This
is also how W stays bounded at size: the planner sizes a unit as one writer's few minutes and splits along contracts; nothing caps a worker (R15).
## 6. Smaller items
- **Effort:** reasoning is 40-50% of output on reworks, 15-25% on first attempts. Reworks (attempt > 1) and the guide at medium now; all first WORK at medium on half a
  cohort, kept only if the oracle and C rate hold. Judges stay Sol (terraReplay). R13 binds the strongest model to architecture, planning and judgment only: no
  ratification.
- **WORK with --ignore-user-config** (round-2 item 6): workers read ~/.codex memories and skills (32k chars in one guide call) and import audit ceremony into checks
  (`BEHAVIOR / Realistic bug / Coverage gap` lines in i01). REC-14 hermetic.
- **Plan repair converges** (round-2 C) and the loop lanes now landing: keep; they remove the 5-12 min tails (i02, i04).
- **Guide scope:** the guide is the walkthrough; reference material belongs to the one documentation owner (README). State it as the guide's principle, not a size limit.
- **At 100 units:** WAVE-VERIFY runs every check so far; S2 halves that suite, and check runs are already hermetic, so run them in parallel up to machine capacity. Track
  "check seconds per wave" in the P11 debrief.
## 7. Ranking (critical-path minutes saved per run / risk) and ratification
| # | Change | Saves | Risk | Oren |
|---|---|---|---|---|
| 1 | S1 guide = ordinary no-dependency unit, walkthrough proven at WAVE-VERIFY | 4-6 (every run) | low-medium (blind guide -> one fixup) | no |
| 2 | S2 proven once + proof map fact to REVIEW and JUDGE | 1.5-2.5 on W; ~1/3 of check output; 0-4 fewer rework min | medium | **yes, one sentence in 3.1** |
| 3 | WORK ignores user config; reworks + guide at medium | 1-3 | low | no |
| 4 | Ask a stalled unit at once; contract gap -> the one-question contract fix | 0-5 (the slow runs) | low | no |
| 5 | Check kit (browser + serve), vendored, replaces browserHowTo | 1-1.5 on W; fewer environment reworks; fixes hard-coded paths | low | no |
| 6 | First WORK at medium, A/B on half a cohort | 1-2 | quality, measured | no |
| 7 | UI split by contract seams (ARCHITECT principle) | 0 on ShelfLife; bounds W on large UIs | low for large, never applied to one screen | no |
| 8 | Parallel check writer | <= 2 | high (blind checks, lost refine loop) | would need R8 wording; **defer** |
Projection with 1-5: i01 23 -> ~15-16; i03 30 -> ~21 (its real flow bug stays); i02 38 -> ~23; i04 42 -> ~24. Nothing here drops a C#: proof still runs on the integrated
commit, RED is still observed by code, judges are unchanged.
## 8. Lane order (disjoint file groups; rebase on the loop lanes first)
Round 1, in parallel:
- **L-A guide unit (S1):** plan.py (add_guide), guide.py, wave_verify.py, proof.py (walkthrough purpose).
- **L-B hermetic + effort (#3):** providers.py only (role_for reads the attempt from context).
- **L-C ask at once (#4a):** scheduler.py, run.py.
- **L-D repair converge (#4b):** plan_review.py, detail.py — only after the loop lanes have landed there.
Round 2, in parallel, after one cohort measures round 1:
- **L-E proven once (S2):** questions.py (DETAIL level definitions replaced, proof map built there from plan.assigned, fed to REVIEW and judge_brief), judgment.py. Brief
  can be written now; lands on Oren's sentence.
- **L-F kit (#5):** new src/seldon/kit/ (browser.cjs, serve.cjs, serve.py), gitwork.py (vendor on the wave start commit), providers.setup_facts (drop browserHowTo) —
  after L-B, same file.
Round 3: the medium A/B (#6) as a cohort arm, no code beyond L-B's table. #7 is one ARCHITECT principle, landed with the first large-UI dream (L3), not before. #8 stays a ticket (type idea) with its trigger from section 4. Gate note: one gate per loop; each round is judged by one cohort's timeline.py numbers and the same oracle score.
## 9. Not verified
The 15-25% machinery share and the i02/i03 sizes are the coordinator's; I inspected i01 only. Minute figures for S2 and the kit come from character shares at
35-40 tok/s, not from a run. Whether a guide written from contracts alone passes its walkthrough first time is unknown until L-A's cohort.

## 10. Cohort m2j wall: "blocked" units whose proof is a wave check (Fable, 2026-11-14, main 03694dc)
**TRIAGE: DESIGN.** Same family as T-150, third appearance (judge gap -> judge gap after prose fix -> worker "blocked"). Sibling cases: j05 u001/u003/u004, j02 u001/u004 (wave-check
evidence), and the worker-side echo j05 r225/r280, j02 r329/r349/r370.

### 10.1 Root cause (from the stores)
The worker is not the origin. In every case the first WORK answer was **done** (j05 r187 u003, r287 u001, r307 u004; j02 r208, r238). The wall starts at the unit JUDGE:
- j05 r217 u003: `meaningful: False` on n033, "n035 has only a failing wave-start observation; no passing integrated ... evidence"; gap: "Supply passing P evidence for n035
  against the integrated product ... No passing n043 evidence substitutes". Same shape: j05 r262, r316 (u001/n012), r336 (u004/n043); j02 r230 (u001/n012), r273 (u004/n038).
- That gap becomes the rework brief's "Exact failure". The worker is now ordered to produce something its worktree cannot produce, while "Unit evidence" says the opposite.
  It answers truthfully: `blocked`, owner = itself ("Run check_inventory_path.py at WAVE-VERIFY", r225) or the absent peer ("Provide the assembled inventory.py and
  server.py", r280 -> fixups.handoff ValueError "files are not in this unit's base by design ... return done" -> charged recovery -> ASKED). Two workers instead built a
  fake integrated layout to satisfy the judge (j05 r344, j02 r291): slower, and weaker proof than WAVE-VERIFY.
- Why the judge does it: 9a5d6c0 put the unit's owned wave checks into JUDGE "Checks" and their wave-start RED into "Observations"; `plan.proof_map` (provenOnce) lists
  **every** wave check tracing a requirement, including other units' (n043 is in u001's and u003's map). The judge sees a named prover with RED and no GREEN and a prompt
  asking for "passing P output". 3c56782 removed the `exercisedAtP` field and added one sentence; the judge moved the same true objection into `meaningful` and `gaps`.
- The judge and the worker are both stating a true fact: "the rest of this proof belongs to WAVE-VERIFY". JUDGE has only satisfied/gap and WORK only done/blocked, so the
  truth can only be expressed as a failure. Code already knows this fact (check level + owner). A prose sentence cannot hold what the question's structure contradicts.

### 10.2 The one rule
**A call is asked only about proof that exists at its stage. What a later stage proves is a code fact, never a question, a check row, or a failure text.**
At unit level that means: the unit JUDGE's subject is unit-level checks plus the unit's source; a wave check appears there only as source text. Its RED is recorded by code at
wave start (kept, proof.py), its GREEN by code at WAVE-VERIFY, and its meaning is judged once, by flow review, which already receives the wave checks and their final
observations. Proof is not weakened: nothing leaves the run that proves; one premature question leaves. It holds at 100 units (proof map per unit shrinks to its own rows).

### 10.3 Exact changes (delete first; net negative in src)
1. `questions.judge_brief` — delete the 9a5d6c0 widening: `"Checks"` back to `plan.assigned(document)[ref]` (unit level only); `"Proof map"` rows filtered to
   `level == "unit"`; drop observations whose purpose is `wave-start` for a wave-level check (wave-start rows of *unit* checks that passed at T stay, v1.5). Add one code fact
   `"Proven by code at WAVE-VERIFY (not judged here)"`: `{check: owner}` for the wave checks tracing these requirements. Delete the 3c56782 sentence ("An owned wave check shows its RED here ...").
2. `questions.build` / `schema` JUDGE — a requirement with no unit-level check owned by this unit gets the source-style assessment (no `baselineDemonstrated`); code
   decides from the proof map. This is the original T-150 case, closed by structure; provenOnce makes it rare (every m2j requirement has a unit check).
3. `flow_review` — add the wave-start rows of the flow's wave checks beside the final rows (same `observed` shape). The only judge that can see RED and GREEN together
   now judges the wave check's baseline. (About 3 lines; if flow facts grow measurably, drop this and rely on code RED.)
4. `fixups.handoff` — delete the `raise ValueError("...not in this unit's base by design...")`. Normalise instead: a discovery naming a unit whose product is not in this
   unit's base is not a blocker by construction; record it (`disposition: "wave verify"`), charge nothing, and continue to PROVING as done. Code proves done-ness there
   anyway; `outcome` is derivable for this case. If every discovery is of this kind the unit proceeds; a DONE-owner or contract discovery keeps today's path.
5. `questions.UNIT_EVIDENCE` — cut to the screenshot sentence plus "Wave checks are written here and run by Seldon at WAVE-VERIFY." (the fact key "Wave checks to write, not run here" already says it).
6. `recovery`/`units.work` — unchanged. `tests/seldon/wave_red_journey.py` + `recorded_f04_delivery.json`: re-point to the new outcome (10.5) rather than keep the judge-sees-wave-RED assertion.

### 10.4 "Self-owned blocked asks at once": keep
It is the right rule for a worker that truly cannot do its own work, and it saved the retries it was built to save. In m2j it fired on a contradiction Seldon created
(judge demand vs brief); after 10.3 that source is gone. No carve-out, no cap. Note only: j05 u002 ASKED is a different thing (two real product gaps found by the judge in
two rounds, r400/r438, then R15's interim 2-recoveries question) and is not part of this wall.

### 10.5 Outcome journeys (behaviour only, scripted provider)
- **J1 wave-proved unit finishes:** unit owns one unit check and one wave check whose scenario needs a sibling. WORK done -> JUDGE question contains no wave check row and no
  wave-level observation -> DONE; WAVE-VERIFY records the wave check GREEN; flow review question holds its wave-start RED and final GREEN.
- **J2 peer discovery is not a blocker:** WORK answers blocked naming a not-yet-integrated sibling -> unit reaches DONE with 0 recoveries, discovery recorded; no ASKED.
- **J3 real wave failure still bites:** wave check fails at WAVE-VERIFY -> fixup lands on the check's owner (unchanged path); the run does not reach C without GREEN.
- **J4 genuine self-block still asks:** WORK blocked naming itself -> one user question at once (lineage journey, unchanged).
- **Real-run signal:** next cohort has zero JUDGE gaps and zero WORK failures whose text names a wave check or WAVE-VERIFY; u001-style "temporary integrated layout" reworks disappear.

### 10.6 Not verified
Read j05 and j02 stores only (not the logs, not the worker stdout). Did not confirm flow review's question size after step 3, nor that R2's "source judged once" reviewers
accept the wave check source staying in the unit JUDGE's "Check sources" (it must: the unit owns that file). No code was run.
