# Speed review (Opus) 2026-11-14 — why ShelfLife takes 40-92 min, and how to reach ~30

The brief's guess is wrong on one point. The "~16 min of wave-verify check runs" in g01 is not slow
checks. Real wave checks take under 1 min per pass; the slowest, n023 with Edge, takes 14 s. The 15.6 min
is three guide commands (`server.py --port 8000`) that never exit, each killed at the 300 s check timeout.
This happens in every run: 1-7 such timeouts (g01 3, g04 2, g05 2, h02 4, h04 1, h05 2, h01 3, h03 7 = 35 min).

## 1. Critical paths (minutes from the first call; timeline from question.json/stdout.bin mtimes)
g01 (60):  0-6.4 planning (ALIGN, ARCH, review gap, ARCH again, 4 DETAIL in parallel, 4 REVIEW)
  | 6.4-21.9 UI unit u003 d1c0db2d 14.8 min of WORK + judge (pantry, server and delivery all finish earlier)
  | 21.9-23.5 the delivery unit u004 tail: 2 judge gaps (b25b11f8, 0c2e5b75), 2 reworks
  | 23.6-28.1 guide WORK 0bbd9506 | wave verify: guide:format refusal (r315, URL link) | guide 0.7
  | wave verify: guide:format refusal (r348, non-argv fence) | guide 2.1
  | 32.1-47.7 IDLE, no LLM call: tryItGuide:001/002/004 each timed out at 300 s (r389, r390, r392)
  | 47.7-56.1 guide rework 809c3738 (8.3 min to fix those commands) | 56.5-60.2 6 FLOW + 8 PRODUCT calls, one at a time
h02 (76):  0-8.5 planning (one area: DETAIL/REVIEW gap loop 3x, 4.7-8.5)
  | 8.5-18.8 UI unit 9.7 min of WORK + judge | 18.9-25.8 import unit (it depends on u001+u002), 1 judge gap
  ("importer missing at T", r268) | 25.9-39.4 delivery unit d4e3ded8 12.9 min (depends on all three: a 4-deep chain)
  | 39.5-45.3 guide 3.1, format refusal, 0.7, format refusal, 1.2
  | 45.3-65.8 IDLE: 4 server commands x 300 s (r422, r423, r426, r427) | 65.8-70.6 guide rework 4.8
  | 71.1-75.8 14 FLOW/PRODUCT calls, one at a time (4.7 min)
g04 (92):  0-4.6 planning | 4.6-20.7 UI unit 14.6 min of WORK | 14.3-27.5 delivery u003: 1 judge gap, blocked, rework
  | 27.6-30.1 guide | wave verify: guide:format refusal + delivery n024 fail (r247), so u003 reworks 30.8-40.1 (2 more
  judge gaps) while the guide waits | 40.2-42.3 guide, format refusal | 42.3-52.6 IDLE: 2 x 300 s timeouts | guide 2.6
  | 55.6-86.1 THREE flow-gap rounds (23629908, a8ea9f9a, 8acf76fb) on the same n014 empty-state bug. Each round sends
  the fix to u001, u002 and u003; u001 answers "blocked: belongs to u002" (f12f2dae); u002 reports "fixed" twice
  but tested its own fixture, not the integrated screenshot case (9c7942d3, cc9b91d7). Each round: about 6 WORK +
  4 JUDGE + wave verify + flows rerun = 6-13 min | 86.1-91.8 14 FLOW/PRODUCT calls, one at a time

## 2. Top causes, ranked by minutes
1. Guide commands that never finish (a server start) are run as checks and killed at 300 s. 10-20 min per run
   (h03 35), plus the guide rework that follows (3-8 min). That makes roughly 15-25 min per run. Cause:
   guide.py turns every argv block into a check that must exit. The work text in plan.py ("commands ... that
   finish on their own") still leaves the worker no honest way to write "start the server", which the user needs.
2. Guide format refusals are identical in every run. Each run has 2 of them: the URL link becomes
   `docs/http:/127.0.0.1:8000`, and a non-argv fence (e.g. bash/text) gets "must be an argv fenced block".
   Each costs one wave verify plus a guide call. That is 2.5-4 min per run, on the critical path every time.
   The guide also has no unit proof: its PROVING cause is [] (g01 r308), so it learns these rules only at wave verify.
3. FLOW and PRODUCT calls run one at a time (the flow_review.step loop L184; PRODUCT the same). Each call takes
   0.2-0.5 min, so 14 calls take 4-6 min for every final pass (g04 had 4 passes).
4. Delivery units are judged on the wave outcome before they can reach it. g01 u004: 2 gaps say "run n029
   against the integrated product". n029 is in "Wave checks to write, not run here", and the UI unit had not
   landed yet. The same happens in h02 r268 and g04 (6 gaps). Cost: 2-7 min on the critical path plus ~25% of
   WORK tokens. This conflicts with BLUEPRINT ("flow review is the only cross-unit judge").
5. A flow gap goes to every traced unit, without the failing evidence (flow_review.review L116-119:
   units = traced_units). g04 lost about 30 min. 0 in typical runs, but it makes the rework-heavy tail.
6. Build calls are long and serial: the UI unit takes 10-15 min at Sol high. The native run took 10 min
   in total at medium. Some plans chain units 4 deep (h02: UI, then import, then delivery, then guide).
   We could not tell how much is effort and how much is unit size; it needs a measured A/B.

## 3. Smallest changes, ranked by minutes saved per unit of risk
A. Guide service step (cause 1). Allow one ```argv-service fence: Seldon starts it, waits for the declared
   URL or port, runs the following argv blocks against it, then tears it down in the existing job object.
   Other argv blocks must exit. Saves 15-25 min per run. Proof gets stronger: the guide's real server flow
   is now walked. Files: guide.py, proof.observe (keep one live process across steps), plan.GUIDE_WORK text.
B. Normalise the guide instead of refusing it (cause 2). Ignore http(s) links in the path check (or check
   them against the started service). Treat non-argv fences as prose. Run guide.checks as the guide unit's
   proof at PROVING, so any leftover failure returns to the worker before the whole wave verify.
   Saves 3-4 min per run, near zero risk: every argv command still runs. Files: guide.py, wave_verify.py
   L18-30 (move to unit proof), units.py.
C. Run FLOW and PRODUCT calls in parallel (cause 3). Same ThreadPool and capacity as wave_verify; apply all
   gaps together. Saves 3.5-5 min per final pass. No change to proof. Extra tokens only when there is a gap.
   Files: flow_review.step, the PRODUCT step.
D. The unit judge ignores wave-only commitments (cause 4). A commitment whose only proof is a "wave check to
   write, not run here" is judged by FLOW, not at unit JUDGING. Saves 2-7 min on the critical path and
   many WORK tokens. Low-medium risk: FLOW still judges it on the integrated commit.
   Files: judgment.py brief/validate.
E. Send a flow gap to one owner, with its evidence (cause 5). Send it to the unit whose scope holds the
   failing behaviour (the architect's correction owner for the crossed contract). Attach the failing
   observation and screenshot refs, so the worker reproduces the integrated case. Other units are not
   touched; a wrong owner answers "blocked" plus a discovery, which already re-routes. Saves 0-25 min.
   Medium risk. Files: flow_review.review, fixups.
Then, measured rather than designed: run build at medium (and Terra 6.1 for the guide and small fixups) on
half the cohort. It changes only providers.ROLES/role_for. Expected 20-35% off WORK minutes if the oracle
score holds.
Projection: A+B+C+D bring g01 from 60 to about 30 min and h02 from 76 to about 42. To reach 30 for h02-shaped
plans, add medium effort and shallower dependency chains: delivery should depend on contracts, not on finished units.

## 4. What to measure in the next cohort (timeline.py + the counts query used here)
- tryItGuide timeouts per run (target 0); guide:format refusals (target 0); number of wave verifies (target 1-2).
- Minutes from the first FLOW call to the last PRODUCT call (target under 1.5).
- Unit-judge gaps whose correction names a wave check (target 0), and WORK minutes on the delivery unit.
- Flow-gap rounds per run, and the units touched per round (target 1).
- For the medium A/B: WORK minutes per unit, the UI unit's minutes, and the oracle score. Keep medium only
  if the score is not lower.
- Wall time per run against the ~30 min target: measured and reported, never enforced.
