# Design review (Astra 6.2 high, READ-ONLY): Lead across milestones — memory, regression, re-proof
Do not edit Seldon source or run cohorts. Read anything below; read-only queries on stores/logs are fine. Never read C:/seldon/sealed/ or any .env.

## Context
Repo ~/codex-harness/work/sprint-20261027/semantic-cc, main 8c9ccdc. Binding: CHARTER-LEAD.md v1.1, BLUEPRINT-LEAD.md v0.4 (section 2a: Seldon's guard walks the user path itself, human UI/UX feedback, the builder returns only for a B-quoted demonstrated defect). Owner's shape (11-22): "planner should be so thin... a beautiful process of expanding and crystallizing a dream, breaking it down into SW specs best fit for agentic development"; "he still owns the results... a subjective semantic guard... he should walk the user path".
Today, single-milestone micro dreams: hello 5/5, Foundation 5/5, ShelfLife 3/3 fully verified C. 5 calls, 1 WORK per clean run; the guard catches and routes real defects. Your previous review: work/ladder/design-review/astra62-lead-vs-plain-2026-11-22.md (changes 5 and 6 still unbuilt).
NOTHING has tested Lead's core promise: across milestones it never forgets a promise, never drifts, and re-proves every earlier promise at every milestone. You noted that approval advances the next milestone straight to BUILD, that there is no HANDOVER/AGENDA renderer, and that C reads only partial promise history.

## Questions
1. Trace what happens today on a 2-3 milestone dream, from code (lead.py, plan.py, proof.py, judgment.py, decisions.py, states.py): what the milestone-2 builder brief contains about milestone 1, what the guard re-walks, what C reads, what survives a crash/reopen between milestones. Where would a regression of a milestone-1 promise slip through?
2. The simplest design that keeps the promise (thin planner, guard walks): promise history as one record; the milestone-2 guard re-walks earlier promises (all, or those touched by the diff plus a cheap smoke of the rest?); a check-in between milestones that can revise the next brief from observations; human-readable memory files rendered from the store. What to delete rather than add.
3. A concrete test dream for this (micro-sized, 2-3 milestones), designed so milestone 2 plausibly breaks a milestone-1 promise (e.g. ShelfLife then categories plus shopping list touching the same table and page). Give the brief text and what a correct Seldon run must show.
4. Anything in Lead's state or plan model that blocks multi-milestone growth on small (days) and medium (weeks) dreams.

## Output
~/codex-harness/work/ladder/design-review/astra62-lead-memory-2026-11-22.md: a 10-line plain-words summary for the owner, findings with file:line evidence, the ranked minimal changes (lines removed/added), and the test dream brief. Under 220 lines.
