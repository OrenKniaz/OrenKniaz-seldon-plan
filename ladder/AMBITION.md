# Seldon ambition — what we are building and how far we push it

Oren, 2026-11-20: "push the envelope, be overly ambitious, overly creative, overly unreasonably motivated and ambitious about it and what it will do. but, remember to push most usage into codex."
This file is direction for the dev loop. CHARTER.md, CHARTER-LEAD.md and the BLUEPRINTs stay binding, and anything here that would change them goes under **For Oren** in AGENDA.md.

## The one goal (charter, plain words)
Seldon is the best way to use AI agents to turn a person's dream into a working product. Every dream we build is evidence for that, not the point.

## STRATEGY (Oren 11-22, binding): Lead first, Orchestrator paused
"focus on planner only mode, when that is perfect we can continue (if we want to) to planner+worker mode... until we can prove planner is basically 100% perfect, no reason to introduce other complexity like worker."
- All dev, cohorts and reviews go to Lead. No Orchestrator lanes, cohorts or fixes. Orchestrator code stays in the repo untouched, and a Lead change may delete shared code Lead no longer needs.
- Lead's shape (Oren 11-22): "planner should be so thin... no concurrency handled by us. it's just a beautiful process of expanding and crystallizing a dream, breaking it down into SW specs that are best fit for agentic development. of course I'm over simplifying... but you get it" Seldon owns expanding, crystallizing, specs, memory and proof. The builder owns execution, including any parallelism (native sub-agents). Seldon schedules no concurrency. Refined (Oren 11-22): "he still owns the results, he must be able to do those (to a degree or another), mainly be a subjective semantic guard... he should walk the user path" So Seldon's proof is to walk the person's path through the real product and judge, in meaning, whether the promises hold, not to negotiate check strength with the builder.
- "Perfect" = the micro ladder bar below with no Seldon bugs, then small: cost and time close to plain, proof better.

## Two shapes, one codebase, one shared core

**Seldon Lead (planner only): a staff-level tech lead in a box.**
- It grows the dream with the person (R18), writes each milestone as a mission brief in words, approves the spec at B, and never writes code or tests.
- It hands each milestone to one strong builder, which may use native sub-agents and skills, then proves the result itself, remembers everything across hundreds of context windows, and re-proves every earlier promise at every milestone.
- What it does that a plain agent can't: it never forgets a promise, never drifts, and never claims done without seeing it work.
- Target: the shape a person uses for a months-long dream they would never trust to a single chat.

**Seldon Orchestrator (planner + workers): a studio.**
- It splits a dream along its real seams (for example a DSP core in C, a Python simulator and a web front end), runs builders in parallel on disjoint scopes with contracts made just in time, and proves each wave.
- What it does that a plain agent can't: wall-clock speed through real concurrency, at the same proof standard. The person watches the dream converge on a board.
- Target: big dreams with real seams, where Lead would be correct but slow.

**The shared core is small and boring:** store, states, providers, proof runner, judges, grow/align, decisions, front door. Each shape stays thin on top of it. KPI: source lines reachable from each shape's entry point (Lead's target is about 2.5–3k).

## The ladder and the bars (both shapes, measured against plain on the same dream)

| Rung | Dreams | Bar to climb |
|---|---|---|
| Micro | hello → Foundation → ShelfLife → Quiet Bench | 5/5 C per dream, zero Seldon bugs (no stall, loop, false verification, needless question or desktop pop-up), oracle ≥ plain, code shape ≈ plain, cost ≤ 1.5× plain |
| Small (days) | briefs/S (door count, rehearsal keys, load-in) + one sealed held-out dream | 3/3 C, held-out passes first time, no promise lost between sessions |
| Medium (weeks, 10K+ LOC, real seams, many context windows) | a full-stack product with auth, SQL, front end and background jobs | Lead: zero earlier promises broken at C. Orchestrator: at least 2× faster wall time than Lead at equal quality |
| Big (months) | RNC/ANC on real demo-car data (C core, simulation, front end with parameter control and plots); Oren drives it himself | Oren wants to keep using it |

## Envelope-pushing ideas (try cheaply, keep what measures well)
1. **Promise board.** Every promise has a live state (proposed, approved, built, proved, regressed) with its evidence. It is the same data in both shapes, the convergence/kanban view Oren wants, in the read-only page (C20).
2. **Replay economy.** Every recorded question becomes an offline eval set. Prompt and judge changes are A/B'd offline on Terra before any real run. This is cheap, fast and blind-reviewed.
3. **Self-play dreams.** Terra writes new micro and small dreams plus sealed oracles nightly, so we never overfit to four fixtures.
4. **Builder tournament.** On a hard milestone, Lead hands the same brief to two builders (Codex and Claude, or two Codex sessions) and Seldon's proof picks the winner. Best-of-2 only where a failure is expensive.
5. **Lessons memory.** After each run a short debrief records what the planner and builders got wrong. The next brief for that person or kind of dream starts from those lessons (taste and habits).
6. **Proof as a product.** The retained checks, walkthrough and try-it guide ship with the product as a living test suite the person keeps.
7. **Cheaper by proof.** Where the runner proves something deterministically, skip the judge. The judge reads meaning only where meaning is the question. Aim for cost at or below plain on micro.
8. **Research spikes before B.** Planning may run throwaway experiments in scratch, such as algorithm trials on RNC data, so the spec is grounded in evidence. They never touch the product (C28).

## The rules that hold all of this (already binding; listed so nobody drifts)
- **Who does what:** the planner carries semantics only, in the schema, and never writes code or tests (10-27, restated 11-19). Spec before code (C28).
- **Coach, not referee:** set the model up to succeed. Normalise derivable things, never refuse. No caps (measure and route). A run never fails: it steers, asks the person (options + Other), or pauses and resumes.
- **One owner per thing:** one owner of proof (Seldon runs the checks; builders write them). Failures go to whoever can change the input, and nothing is resent unchanged.
- **Helpful failures:** what failed, expected versus got, what to do next.
- **Fault classes close only when the original user-visible failure is gone on the integrated code, with a real run** (Astra pattern 5). Scripted tests guard boundaries; they don't prove behaviour.
- **Every feature has a switch for A/B.** Hands-on review beside every oracle score. Prompts are the product.
- **Thin is the direction:** each lane removes something where it can, and src lines are reported at every landing.
- **The person's desktop is theirs:** no editors, browser windows or pop-ups from any run.

## Usage: push it into Codex
- A Codex Sol coordinator runs the loop: lanes, runs, censuses, landings and fault triage.
- **Models:** Terra 6.1 medium for simple lanes and all test cohorts. Sol 6.2 medium for new design and hard cross-module faults. Astra only for a must-have design review.
- **Claude Code** sets direction, reviews, pushes, and talks to Oren. Hourly check-ins only, reading one status file.
