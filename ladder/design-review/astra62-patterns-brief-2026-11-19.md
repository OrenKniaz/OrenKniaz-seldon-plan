# Astra 6.2 high: find the recurring design patterns behind Seldon's micro-ladder failures (read only)

You are reviewing Seldon. Seldon is a platform where AI agents build a person's "dream" (an app) from their words. It comes in two shapes in one codebase: **Orchestrator** (planner + units/contracts/waves + workers + judges) and **Lead** (planner + memory + proof, one builder session per milestone). The owner wants an honest, independent view. Nobody is steering you toward any answer. Form your own.

## The situation
The owner's binding bar: zero Seldon bugs on micro dreams (hello CLI, Foundation page, ShelfLife small full-stack app, Quiet Bench) before any bigger dream. Plain Codex, given the same dream, delivers working products without Seldon's machinery. Over the last day the bar has not been met in either shape, despite a steady stream of root-cause fix lanes. Each fix passes its gate and the next batch shows new faults. Source has grown from about 4,200 to about 7,500 lines.

## Read
- Binding docs (Seldon repo ~/codex-harness/work/sprint-20261027/semantic-cc): CHARTER.md, BLUEPRINT.md, CHARTER-LEAD.md, BLUEPRINT-LEAD.md, AGENTS.md, and src/seldon/ (read what you need).
- Evidence (~/codex-harness/work): ladder/census-batch2.md, ladder/census-batch3.md, ladder/census-ab.md, ladder/ab-triage.md, ladder/HANDOVER.md (the last ~80 lines), ladder/TICKETS.json (recent tickets), and the lane reports lanes/*-report.md from 2026-11-19 (quietDesktop, trialFidelity, guideEvidenceScope, workerQuestionLoop, leadThin, guideCommand, firstPathProof, detailOwner, nextWave, browserProof, plannerBrief, codeShape, productLoop, refuseSweep, alignNormalise, featureReq). Read the matching lanes/*.prompt.md where you need to see what was asked.
- Lead batch on 1531a71 (hello 3/5 C, Foundation 2/5 C): run stores at C:/seldon/tests/m1/{hello-1531a71-lh0*,foundation-1531a71-lf0*}/product/.seldon/state.sqlite3 (records, questions, cursor) and each slot's call logs.
- Never read .env files or anything under C:/seldon/sealed. Edit nothing except your output file. No provider calls, and never open desktop applications.

## Questions
1. What recurring patterns do you see across the failures and the fixes, in both shapes? Name each pattern, with the evidence (ticket, run or report) behind it.
2. For each pattern: is it a bug, or does it come from the design (a part that should be simpler, owned differently, or not exist)? Say which part of the charter, blueprint or code it traces to.
3. Do the two shapes share these patterns or differ? What does that tell you?
4. What should change, if anything: keep, simplify, replace or delete. Prefer the smallest change that removes a whole class of failures, and say what it removes from src.
5. What would you measure to know the change worked on the micro ladder?

## Deliver
Write ~/codex-harness/work/ladder/design-review/astra62-patterns-2026-11-19.md (at most 150 lines). Reply with a 10-line summary: the 3 strongest patterns and your top recommendation. Mark anything that would need a charter or blueprint change as **FOR OREN**.
