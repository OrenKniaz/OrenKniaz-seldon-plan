# Efficiency review (Fable) 2026-11-16 — cohort m2twenty3, main e57b218, 20 ShelfLife runs on Terra
Read-only. Measured from `calls/*` and `state.sqlite3` of z01..z20 (835 calls). Mean run: 41.8 calls, 11.5 min.
Cost weight used (my assumption, not a price list): uncached input 1, cached input 0.1, output 8.
## Short answer
- Wall time: about 30% is there (11.5 -> ~8 min), from deleting serial steps. Cost: no 30-50% without touching
  the first WORK calls; safe cuts give ~10%, up to ~25% if fix rounds halve.
- Bigger finding than either: the judges are mostly blind today. At C, 98 of 206 requirement verdicts (48%) and
  66 of 119 quality verdicts (55%) are "not judged", and 37 of 57 final unit verdicts stand as an open gap.
  The oracle 36-39 was reached with half of the final judgment missing. The waste and this hole have one cause.
## 1. Where it goes (per run, mean of 20)
| part | calls | cost | wall on the path |
|---|---|---|---|
| first WORK (3 units + guide) | 4.1 | 29% | 252 s (37%), longest unit ~200 s, then guide |
| fix WORK (resumed session) | 1.6 | 21% | 63 s (9%) |
| FLOW + PRODUCT first asks | 13.5 | 19% | 41 s (6%), FLOW then PRODUCT, serial states |
| FLOW + PRODUCT re-asks | 5.4 | 6% | 55 s (8%), one subject per step, serial |
| unit JUDGE first / after fix | 3.0 / 1.4 | 5% / 5% | 15 s / 14 s |
| plan (ALIGN, ARCHITECT, DETAIL, REVIEW) | 12.7 | 15% | 124 s (18%) |
| code only (proofs, WAVE-VERIFY, git) | - | - | 98 s (14%) |
Cost is 51% uncached input, 35% output, 14% cached input.
Critical path: plan 2.1 min -> longest unit ~3.3 -> unit JUDGE 0.25 -> wait 21 s -> guide WORK 69 s -> guide proof +
WAVE-VERIFY 38 s -> (65% of runs) fix round ~1.5 min -> FLOW 0.2 -> FLOW re-asks -> PRODUCT 0.25 -> PRODUCT re-asks.
Serial steps that could overlap: the guide (needs only contracts), FLOW with PRODUCT, FLOW-gap and PRODUCT-gap fix rounds.
## 2. Calls that change no outcome (measured)
- **Re-asks: 107 of 107 stay "uncertain".** A re-ask carries no new fact (`Requested facts` only lists the same
  observations and screenshots again). Every one ends as "not judged", which is what the first answer already said.
- **First unit JUDGE: 0 of 60 satisfied (54 gap, 6 uncertain).** In all 60 the only observations supplied were the
  RED runs at T. `plan.assigned(local=True)` drops every check of a unit that has wave requirements, and in ShelfLife
  that is every unit, so no GREEN run at P exists when the judge is asked. Its gaps say so: "both observations ran at
  T", "run the check against the delivered candidate". 68 of 68 `unit_gap` records became `open_gap`: none caused
  rework.
- **That verdict then blinds the final judges.** FLOW and PRODUCT get `Source judgment: allSatisfied false` with no
  finding. 114 of 147 first-ask "uncertain" answers name exactly that ("the finding behind the source judgment is
  unavailable"). z19 is the only run where all three units ended satisfied after fixes: 11 of 11 requirements judged.
- Unit JUDGE after a fix (it sees GREEN): 20 satisfied, 6 gap, 2 uncertain. It works; keep it. Plan REVIEW finds
  37 gaps in round 1 and still 23 in round 2, then B proceeds; no cut proposed.
## 3. Facts repeated or too big
- Every non-WORK call pays ~7-9k input tokens of Codex preamble beyond Seldon's prompt (a FLOW prompt is ~2k
  tokens), mostly uncached. For small questions the cost lever is call count, not fact size.
- JUDGE (43 kB): `Proof execution` 11 kB repeats `Observations` 4 kB, with processControl, pids, cwd per row.
- Fix WORK: median 352k input tokens (30k uncached) for 3 commands and 38 s; a whole first build is 121k (11k).
  The resumed thread holds the brief, yet the 37 kB prompt sends it again, with 11.7 kB of `Execution facts`.
- 18 of 37 fix rounds are check failures at WAVE-VERIFY: the first time the check ever ran against real peers
  (answer shape `{"items": [...]}` vs list x4, Windows temp-file locks x3, kit browser/serve deadline x6).
## 4. Ranked cuts
1. **Delete the re-ask.** "uncertain" becomes "not judged" at once (today's outcome, 107/107). Removes FLOW-FACTS
   and PRODUCT-FACTS, `pendingJudge`, `judge_uncertain`, `resolve=`. flow_review.py L78-80, 88-95, 161-169,
   183-186; judgment.py L93-95, 135-139, 160-164, 177-180; states. About -40 src lines. Removes a referee loop.
   **Cost -6%, wall -8 to -9%.** Grows with size: today it is one serial step per uncertain subject.
2. **Judge the source where the proof is.** For a unit whose proof owner is WAVE-VERIFY, skip the JUDGE at the unit
   and ask it after WAVE-VERIFY passes, with that unit's final observations (`judge_brief` already takes `commit`
   and `observations`), in the same parallel batch as FLOW and PRODUCT (one judging step, one fix round for all
   gaps). Drop the `Source judgment` fact from FLOW and PRODUCT; code already ANDs unit verdicts (R2). Drop
   `Proof execution.Evidence` from JUDGE. units.py JUDGING branch (~L131-152), judgment.py L50-56, 65-69,
   flow_review.py L64-65, questions.py L277-294, 309-343, run.py L158-169. Net about -20 lines. Coaching: the judge
   gets evidence it can use, no new rule. C14/C15 keep their reading: one unit verdict bound to the commit.
   **Cost -2 to -4%, wall -4 to -6%** (FLOW and PRODUCT overlap; one round fewer when both find gaps).
   Warning: judges that can see may find real gaps, so fix rounds may rise at first. Check on 5 runs first (R16).
3. **Guide leaves the critical path** (S1 of 11-14, still open). The guide is a unit with no dependencies, written
   from contracts beside the product units; its walkthrough is proven at WAVE-VERIFY like every other blind check.
   Deletes `dependencies: all` in plan.add_guide. Measured tail today: 21 s wait + 69 s WORK + 38 s proof.
   **Cost 0 (+1% if guide fixes rise), wall -12 to -18%.**
4. **Lean fix brief.** When the session resumes, send only the correction and the failing observation rows (check,
   exit code, last output); the thread has the rest. A fresh session still gets the full brief (R8). Strip
   processControl/cwd/pids from `Execution facts` everywhere. questions.py work_brief, execution_facts,
   repair_facts. Fewer lines. Coaching. **Cost -3 to -5%, wall ~0.** Then measure 10 fix rounds resumed vs fresh:
   if a fresh fix costs about one first call, R8's "resume is cheaper" fails for small fixes (a further -8 to -10%).
5. **Fewer blind-check fix rounds** (18 of 37). No new rule: with cut 3, WAVE-VERIFY starts when the last product
   unit integrates, so the round overlaps nothing serial. Next, in `units.integrate`, run a unit's own checks when
   every provider it consumes is already in the candidate (drop the `local=True` filter in that case); a failure
   returns to the still-warm session. ~+5 lines. **Cost -3 to -6%, wall -5 to -8%** if half of those rounds go.
## 5. Combined, and what grows
- Cuts 1-3 (deletions, low risk): **cost -8 to -10%, wall -25 to -30%** (11.5 -> ~8.3 min).
- All five: **cost -15 to -25%, wall -30 to -40%** (~7-8 min). First WORK (29% cost, the 3.3 min pole) is the
  product itself; plain Codex spends the same 3-4 min there. A 50% cost cut is not available at equal quality.
- What scales worst for a larger dream: serial re-asks (linear in subjects), fix rounds that each rerun every check
  of every unit, resumed-session input (grows with unit size), ~8k fixed tokens per call. Cuts 1, 2, 5 and 4 hit these.
- Order: 1 and 2 in one lane (2 makes 1 honest), 5-run check, then 3, then 4 and 5. No cap, no cheaper judge model.
