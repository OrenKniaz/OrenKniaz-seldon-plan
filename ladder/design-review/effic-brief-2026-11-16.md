# Efficiency review brief (2026-11-16) — READ ONLY, write one file

Oren asks: is there room for another **30-50% cut in cost or wall time** per run, without losing quality?
Next step after this is a much larger dream, so prefer cuts that grow with app size.

## Facts
- Code: `work/sprint-20261027/semantic-cc` (main; src/seldon ~4.2k lines). Binding: `CHARTER.md`, `BLUEPRINT.md` v1.11
  (read R2, R9, R15 no hard caps, R16 thin: coach, don't shackle).
- Cohort: 20 ShelfLife runs on main e57b218, every role on Terra 6.1 medium. 19 finished on their own and 1 with one
  simulated-user answer; all scored oracle 36-39 (plain Codex Terra: 34-36).
- Per-run calls, tokens and wall time by question kind: `work/ladder/design-review/effic-data-2026-11-16.txt`.
  Typical run: 35-62 calls, 8-17 min, 1.1-4.3M input tokens (~75% cached), 30-80k output.
- Plain Codex on Terra: one exec, 3-4 min, oracle 34-36 (no token log).
- Raw run stores (questions, prompts, answers, stdout with usage): `C:/seldon/tests/m1/shelflife-main-e57b218-z01` … `-z20`,
  each with `calls/call-*/{question.json,prompt.txt,stdout.bin}`. Timestamps give the critical path.
- Earlier speed work (do not repeat; build on it): `speed-design-fable-2026-11-14.md`, `speed-astra-2026-11-14.md`,
  `speed2-opus-2026-11-14.md` in this folder.

## Questions
1. Where do the tokens and the wall time go? Name the critical path: which steps run serially that could overlap.
2. Which calls change no outcome (a judge that always says satisfied, a FLOW/PRODUCT question repeated per item, a review that
   never finds anything)? Measure it from the answers, don't guess.
3. Which facts are repeated across calls or bigger than the decision needs (uncached tokens)?
4. Rank the 3-6 best cuts by expected saving (% cost, % wall time), with evidence and the src lines touched. Say for each one
   whether it is coaching or refereeing, and whether it makes src smaller.

## Rules
- No hard caps, no limits that refuse or fail (R15). Measure; never cap.
- Keep independent proof (C14, C15) and the M2 bar (oracle >= 36). Removing a call is fine if the evidence shows it never
  changes an outcome, or if its job can fold into another call.
- Test runs stay on Terra or Luna, never Sol. A cheaper model per role is allowed only with replay evidence (see memory: the
  Terra judge replay showed Terra misses real gaps on JUDGE/FLOW/REVIEW).
- Simple and small. Prefer deleting over adding.
- Read only: write nothing except your one output file, at most 80 lines, plain words.
