# Deep design review: why is Seldon Lead (planner only) far from plain? (Astra 6.2 high, READ-ONLY)

You are reviewing, not building. Do not edit Seldon source, do not run cohorts. You may read anything under the paths below and run read-only queries on run stores (sqlite) and logs. Never read C:/seldon/sealed/ or any .env file.

## The owner's words (Oren, 11-22)
"so far I'm disappointed by our only planner mode... there is no reason it won't be very close to plain... that's the whole idea... before we said our workers were the buggy inefficient bug.. I'm not sure anymore.."

Oren, later the same day: "planner should be so thin... no concurrency handled by us. it's just a beautiful process of expanding and crystallizing a dream, breaking it down into SW specs that are best fit for agentic development. of course I'm over simplifying... but you get it" Refined (Oren 11-22): "he still owns the results, he must be able to do those (to a degree or another), mainly be a subjective semantic guard... he should walk the user path" So Seldon's proof is to walk the person's path through the real product and judge, in meaning, whether the promises hold, not to negotiate check strength with the builder.

## What Lead is supposed to be (binding)
Repo ~/codex-harness/work/sprint-20261027/semantic-cc (main 6419fc5): CHARTER.md, CHARTER-LEAD.md v1.1, BLUEPRINT-LEAD.md v0.3. Plain words: Seldon grows the dream with the person, writes each milestone as a brief in words, approves the spec at B, hands the milestone to ONE strong builder (who may use native sub-agents), then proves the result itself and remembers every promise. The planner writes no code or tests. On a micro dream, a builder plus a light planner should cost and take about what plain Codex does, with better proof.

## Facts (verify them, do not trust them)
- Plain Codex Terra on ShelfLife: about 3.9 min, ~1,041 product lines (work/fight-1/, work/ladder/census-*.md).
- Lead ShelfLife, main 6419fc5 (bound proof): 4/5 C, 14–22 min wall, 16–20 provider calls per run, 2 recovery rows EVERY run. Runs: C:/seldon/tests/bpShelf/*.log, slots C:/seldon/tests/m1/shelflife-bp-6419fc5-bs0N/ (product/.seldon/state.sqlite3).
- Earlier Lead history: work/ladder/census-lead-1.md (rounds on 54c774c and 6ea9aa3: 32 of 33 failures came after green checks; 11.4 MB judge prompt), work/ladder/design-review/astra62-patterns-2026-11-19.md (your earlier patterns).
- Foundation x5 (bpFound) on 6419fc5: 5/5 C, 8-14 calls, 1-2 recovery rows each. hello x5 (bpHello): 5/5 C, 7-9 calls, 1-2 recovery rows each. Even hello needs 7 calls and a recovery row; plain needs 1 call. Cohorts ran overnight 23:20-10:40 (host likely slept): use per-call durations from logs and stores, not cohort wall.
- Orchestrator (planner + workers) reference: census-batch3.md (ShelfLife about 7 min, 6–8 calls).
- Lead source: src/seldon/lead.py, judgment.py, proof.py, plan.py and what they import. Reachable lines: Lead ~6.5k vs a 2.5–3k target.

## Questions (answer from evidence; name files and lines)
1. Where does Lead's time and token cost go, per call kind (ALIGN, MILESTONES, REVIEW, WORK, JUDGE, proof runner, idle), compared with plain on the same dream? Which part of the gap is planning overhead, which is proof, which is rework, which is Seldon waiting?
2. Why does every run need recoveries? Is the builder wrong, or is Seldon creating the failure (brief, receipt format, proof runner, judge, routing)?
3. Is the problem the shape itself or its implementation? What is the SIMPLEST Lead design that would land within about 1.5x plain on micro dreams without losing what Lead promises (memory, cumulative proof, no false done)? What should be deleted rather than fixed?
4. Was the "workers were the bug" conclusion right? What do Lead and Orchestrator share that is slow or buggy in both (the shared core: store, proof runner, judges, grow/align)?
5. Anything else you see that the owner should know.

No direction bias is intended: if the evidence says the charter or blueprint is wrong, say so plainly.

## Output
~/codex-harness/work/ladder/design-review/astra62-lead-vs-plain-2026-11-22.md
Start with a 10-line summary in plain words for the owner. Then findings with evidence, then a ranked list of at most 6 changes (each: what, why, expected effect, lines removed/added). Keep it under 250 lines.
