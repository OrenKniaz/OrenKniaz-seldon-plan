# No hard caps (BLUEPRINT v1.8 draft) — Fable review, 2026-11-13

Verdict: **AGREE-WITH-CHANGES.** The draft matches Oren's words and the charter (C8 "No budget in v1", C12 "no arbitrary caps",
§5 "budgets in v1", §6 "measured here, not in the product"). No charter edit is needed. Four changes to the wording.
Read from text only; nothing was run.

## Reasons

1. **Terminal path is missing (the real gap).** "Nothing ends the dream on a count" plus "steering re-splits" can loop:
   unit -> 2 recoveries -> steer -> re-split -> children -> 2 recoveries -> steer -> ... The draft's "steering that cannot
   resolve it" has no test. Fix with one principle: **a count or a size may route (split, recover, steer, ask the user);
   it never refuses, fails or ends.** That is already the charter's shape (C4 "2 retries, then judge/steer", C11 "~3 rounds,
   then Seldon decides", C18 "2 recoveries, then steer"). The chain is then finite: recover twice -> steer once -> the same
   work back at steering goes to the user. The user's own answer is the only thing that drops a unit or ends a dream
   (I4 "the user said no", C21, C25). While the question is open, unrelated units keep running (R7), dependants wait with
   the reason shown (C12), and a run with nothing else runnable is *waiting for the user*: shown, resumable (C23), not
   INCOMPLETE. This is a real decision, so it waits even when check-ins were waived (C8 v1.8, same class as a scope change).
   I5 holds: every call still ends at its deadline; the only open-ended wait is a user gate, like A/B/C.
2. **Interim for T-133.** Unit steering is M3 (DV5). Until it lands, two recoveries go straight to the user question.
   Same path, one step shorter; no FAILED-ends-run stand-in.
3. **"Never enforced inside a run" is too strong.** R3 and my T-131 Fix B need a size to trigger a *split* inside a run.
   Say: a size may make code split a question; it never refuses one; an item that cannot be split is sent whole.
   A provider that itself rejects a question is an observed failure (I4) and recovers like any other.
4. **Debrief belongs in §7, not in an R rule.** R rules are the product's shape; charter §6 (line 80) puts efficiency
   metrics in the dev process, "never as product machinery". So: R15 says runs *record* the numbers and never act on
   them; new P11 holds the debrief. One sentence each, so P8 (no ceremony) holds.
5. **Add the T-131 lesson in plain words:** no brief asks a worker to make the product or its tests smaller to fit Seldon.

Kept, rightly: **provider deadlines** (they are what I5 requires and the only guard against a silent forever-run) and the
**1-vs-50 measurement** (a test on Seldon, R2/P2, not a limit on a dream). Note for the first debrief, not for the text:
3 of 10 WORK calls hit the 900 s wall while progressing; each hit spends a recovery, so with this rule a healthy big unit
reaches steering early. Raise `build` to 1800 s (already in Fix A) and consider an inactivity deadline as a ticket.

## Other text that states a count or size

BLUEPRINT.md
- L74 (§3.2) "Two recoveries (C18), then **unit steering** ... Other units keep running." Routing count, stays; needs the
  terminal sentence (edit below).
- L90 (R2) "*Check:* the largest question is the same size at 1 and at 50 units ..." Test measurement, stays unchanged.
- L92 (R3) "Any list an LLM must write is small and bounded; code splits ..." Stays; R15 states how to read "bounded".
- L112 (R13) "provider failures recover twice, then steer (C18)". Routing count, stays.
- L122 (§5 Drop) "the 64 KB error as a limit; repair counts by origin". Already there; widen (edit below).
- L1 title still says v1.7.

CHARTER.md (no edit proposed; all are routing counts or already forbid budgets)
- L35 C4 "2 exact-fix retries, then judge/steer"; L68 I10 the same. The code's 2x max_bytes re-ask *refusal* breaks this
  line as written: a re-ask that fails must steer, not refuse.
- L39 C8 "No budget in v1"; L43 C12 "no arbitrary caps"; L77 "budgets in v1 ... fixed ceremony counts as rules (counts
  are defaults)"; L80 "Budgets and efficiency metrics are measured here, not in the product."
- L42 C11 "~3 rounds, then Seldon decides"; L49 C18 "2 automatic recoveries of a bead, then steer"; L64 I5.
- L94 DV5 (no unit steering yet): add "interim: two recoveries raise the unit to the user (Blueprint R15)" when the
  register is next touched. Lead's call; it is a register note, not a rule change.

Code that must go with it (from the triage, for the lane brief): `questions.bounded_unit` 64 KB refusals (JUDGE, WORK,
ARCHITECT, DETAIL), `UnitTooLarge` arms in `units.run_unit` and `inference.call`, the 2x max_bytes re-ask refusal,
`refresh_units` uncaught `UnitTooLarge`, exhaustion -> FAILED -> dependants BLOCKED -> INCOMPLETE, JUDGE `ProviderFailure`
-> FAILED after 3 tries, and the `big-source` / `big-product` assertions that assert the defect.

## Proposed exact text

**Line 1:** `# SELDON BLUEPRINT v1.8 — how Seldon builds large dreams`

**Header line (after the v1.7 line):**

> **v1.8 (Oren, 2026-11-13, "no hard caps on budget anywhere, but later efficiency debrief"):** R15: no size, time or count limit refuses a question, fails a unit or ends a run; limits only route (split, recover, steer, ask the user). §3.2: the end of the steering chain is a user question. P11: efficiency debrief after each cohort or fight. §5: every hard cap dropped. Notes: `work/ladder/design-review/no-hard-caps-2026-11-13-fable.md`.

**§3.2, replace the last paragraph (L74):**

> A failure in PROVING, JUDGING or INTEGRATING returns the unit to its own worker with the exact failure. Two recoveries (C18), then **unit steering**: the planner re-splits it, changes approach, corrects a contract, or raises it to the user. Work that reaches steering a second time, as the same unit or as the units it was split into, goes to the user as one question: what was tried, what failed, and Seldon's recommendation. Only the user's answer drops a unit or ends the dream. Meanwhile other units keep running, dependants wait with the reason shown, and a run with nothing else to do waits for the user; it does not end.

**§4, new rule after R14:**

> **R15. No hard caps.** A size, time or count limit may only route work: split a question, recover a call, steer a unit, ask the user. It never refuses a question, fails a unit or ends a run. "Bounded" in R2 and R3 says how code builds questions: a subject too large for one question becomes several, and a piece that cannot be split is sent whole. No brief asks a worker to make the product or its tests smaller to fit Seldon. Provider deadlines stay as hang guards; a hit is a transient failure and recovers in the same session (R8). The chain always ends at the user (§3.2), never at a number. Each run records its largest question per kind, total calls and bytes, wall time and recoveries; nothing in a run acts on those numbers. Until unit steering lands (M3), two recoveries go straight to the user question. *Check:* a journey unit with a 150 KB patch reaches DONE with its files unchanged and no recovery spent; a unit that never passes ends in a user question while the other N−1 integrate and the run stays resumable. *Prevents:* T-131 (an 84 KB JUDGE refused; workers deleted tests and product to fit), T-133 (one unit's third failure ended a run with three healthy units waiting).

**§5 Drop row (L122), replace "the 64 KB error as a limit; repair counts by origin;" with:**

> every hard cap (R15): the 64 KB refusals on JUDGE, WORK, ARCHITECT and DETAIL questions, the 2x re-ask size refusal, repair counts by origin, retry counts that fail a unit or end a run;

**§7, new rule after P10:**

> **P11. Efficiency debrief.** After each cohort or fight the lead reads the recorded numbers (largest questions, slowest steps, repeated recoveries, deadline hits) and opens tickets for the biggest wins. Efficiency changes land through ordinary lanes; they never become limits inside a run (R15).

R2, R3, R13 and the charter: no change.
