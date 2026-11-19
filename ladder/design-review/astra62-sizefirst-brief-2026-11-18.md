# Astra 6.2 design brief: "size first" (2026-11-18) — read only, write one file

## Facts
- Owner's size scale (by single-agent effort): **micro** = minutes for one plain session; **small** = days; **medium** = weeks, drifts across sessions, 10K+ LOC with real seams (DB, front, back, auth); **big** = months, always drifts.
- Owner's binding test ladder: micro (hello-world CLI → multi-CLI Foundation → ShelfLife → Quiet Bench) until "happy", then small (min→max), then medium (min→max); big is built by the owner himself. "Happy" = boring execution (4/5 reach C with no unit/step questions, oracle score ≥ plain) AND cost/time near plain for that size.
- Today Seldon splits every dream into areas, contracts, waves and many units. On micro dreams this is pure overhead and creates seam bugs:
  - Quiet Bench: plain Codex Terra 1 session, ~3 min, ~225 LOC, calibrated oracle 10 pass/0 fail/4 unverified; Seldon 176 calls, ~40 min, ~2.6M fresh tokens, 7/2/5, 11 user questions about missing peer agreements (now fixed).
  - ShelfLife (2 waves): Seldon 79 calls, 39/40; plain 3-4 min, 34-36.
- Seldon's value should be keeping medium/big dreams from drifting. It must never lose badly to plain on micro/small.

## Read
`C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/` CHARTER.md (C5 size, C13 separate sessions, C14/C15 proof, C26), BLUEPRINT.md v1.14 (R1-R18, §3, §6), and `src/seldon/` (vision size, architecture, detail, plan, units, judgment, run). Earlier reviews in `C:/Users/oren/codex-harness/work/ladder/design-review/` (astra62-review, effic-*, speed-design). Never read .env. Edit only your output file. No provider calls.

## Design questions
1. **Sizing.** How Seldon decides micro/small/medium/big at A (who decides, on what evidence, shown to the user as a choice per R17/R18, overridable), using the owner's scale.
2. **The micro/small path.** What the thinnest Seldon run looks like for a dream one session can do: e.g. one area, one unit (one worker session) building the whole product, with Seldon still adding its value (grown and aligned vision, code-observed proof on the real path, one judge, the try-it guide, C). What can be skipped or folded (contracts, REVIEW, FLOW, per-area PRODUCT, waves). Target cost: within ~1.5-2x plain. Which charter rules (e.g. C13 tests in a separate session) bind here, and how to honour them cheaply, or which should be re-worded for micro (for the owner to ratify).
3. **Testing the wave machinery on micro dreams.** The owner allows splitting micro dreams into waves for testing. Design a switch (e.g. `SELDON_SPLIT=force`) that keeps today's full path available for micro dreams without making it the default.
4. **The boundaries.** When does a dream graduate to the full path (small→medium), and how does a dream that turns out bigger mid-run move up (STEER) without restarting?
5. **Measure.** What each rung reports so "happy" is checkable: autonomous C, oracle vs plain, calls, fresh tokens, wall time, ratio to plain.
6. **Lanes.** Sol 6.2 lanes with disjoint files, each with a ready-to-paste brief (PROBLEM, DESIGN, do-not-touch, fault twin from recorded data, PROOF/DELIVER like `C:/Users/oren/codex-harness/work/lanes/askContracts.prompt.md`), a feature switch, and one plain line for the owner (coaching or refereeing). Prefer deleting and folding over adding.

## Output
At most 160 lines to `C:/Users/oren/codex-harness/work/ladder/design-review/astra62-sizefirst-2026-11-18.md`: the one-paragraph answer first, then the design, any charter/blueprint wording for the owner to ratify, the measure, the lanes, and what you are least sure about.
