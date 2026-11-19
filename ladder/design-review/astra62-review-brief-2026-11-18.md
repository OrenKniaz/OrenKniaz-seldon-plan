# Astra 6.2 deep review brief (2026-11-18) — read only, write one file

You are reviewing Seldon from the outside, as the most skeptical and most inventive senior engineer in the room. You are not here to approve or to polish. You are here to find what is wrong, what is missing and what would be much better, in the idea, the binding documents and the code, and especially in how the three connect.

## What Seldon is (owner's words, Charter v1.4)
Seldon should be the best way to use AI agents to build "dreams": real, large apps a person describes in their own words. Every app it builds is only a confirmation of that goal. Seldon wraps provider agents (Codex, Claude); it plans, coordinates, proves and re-plans; it calls the LLM through schema-bound headless questions. The owner's direction since 11-16: Seldon is the head coach of the model, not its referee ("thin": least structure the model needs, code derives the rest, never refuse, a run never fails, it pauses or asks).

## Read (paths relative to C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc unless absolute)
- `CHARTER.md` (the what; C1-C26, I1-I9, deviation register) and `BLUEPRINT.md` v1.12 (the shape; R1-R17, §3 records/loops, §6 milestones M1-M4).
- `src/seldon/` (~4.8k lines) — the implementation. Read it as an architect: flows, state, where the LLM is asked what, where code decides.
- Evidence of how it behaves for real:
  - Design notes and reviews: `C:/Users/oren/codex-harness/work/ladder/design-review/` (start with `*-2026-11-16.md`: thin-shackles, effic-fable, effic-astra, m3-readiness-fable, m3-lanes-fable, wave2-fable).
  - Real runs: `C:/seldon/tests/m1/shelflife-main-*` (each has `calls/call-*/{question.json,prompt.txt,answer.txt}` and `product/.seldon/state.sqlite3`); logs in `C:/seldon/tests/m3*/` and `C:/seldon/tests/m2*/`. M2 (one wave) reached 20/20 apps scoring 36-39 on a blind oracle (plain Codex: 34-36). Since M3 (waves) landed on 11-17, five real runs in a row each hit a different new bug (strict schema loop, STEER replacing wave history, git cwd, check misrouted to an owner who cannot fix it, cross-unit contract mismatch looping on one worker).
  - Judge evaluation: `C:/Users/oren/codex-harness/work/ladder/judge-eval/report.md` (0 false alarms, 0/3 recall on known real defects).
  - Our process: `C:/Users/oren/codex-harness/work/ladder/LANDING-CHECKLIST.md`, `DEV-VERIFICATION.md`, `TICKETS.json`.
- Do not read any `.env` file. Do not edit anything except your output file. Do not run Seldon or call providers.

## How to think (please follow this order)
1. **Before reading the code, write down from the Charter alone** how you would design Seldon if starting today: 5-10 lines. Keep it; you will compare against it.
2. **Find contradictions and gaps between the three layers**: a Charter promise the Blueprint does not carry, a Blueprint rule the code does not follow (or follows in letter only), code that exists for no rule, a rule that exists for no failure. Name file:line or rule ids.
3. **Find the pattern behind the M3 bugs.** Five different symptoms in five runs is a signal about the design, not bad luck. What single idea is wrong or missing? (Hint we suspect but want challenged: scripted test stubs are more convenient than real models, and code trusts answer shapes it never told the model about.)
4. **Steelman, then attack, the core bets**: LLM-calls-as-schema-bound-questions; contracts first; waves; code-observed RED/GREEN; separate judges; planner-first questions to the user; "never fail, only pause". For each: keep, change or drop, and why.
5. **Be creative.** Propose at least three ideas we have not considered that could make Seldon 3-10x better (quality, speed, cost or autonomy) on large dreams. Bold is welcome; say what evidence would prove or kill each one cheaply.
6. **Kill list**: what should be deleted from the code or the documents because it no longer pays.
7. **Compare with your step-1 design**: where is ours better than yours, and where is yours better?

## Output
Write at most 220 lines to `C:/Users/oren/codex-harness/work/ladder/design-review/astra62-review-2026-11-18.md`, plain words, in this order:
- **The one thing** (3 lines): the single most important change.
- Contradictions/gaps between Charter ↔ Blueprint ↔ code (ranked, each with evidence).
- The M3 bug pattern and its root idea.
- Core bets: keep / change / drop.
- New ideas (≥3), each with a cheap test.
- Kill list.
- Your design vs ours.
- What you are least sure about.
No praise, no summary of what Seldon is. Short sentences. Evidence over opinion.
