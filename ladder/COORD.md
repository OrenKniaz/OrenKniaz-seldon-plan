# Coordination: two Claude sessions on Seldon (Oren 11-22: "you drive ... both can work, but be coordinated")

Lead: original session (owns AGENDA priorities, design, "For Oren"). Fork: "Seldon delivery lead Nov 04 (fork)".

## Tracks
- A (fork): guard/walk + micro proof — T-290, Quiet Bench x5 census, leadGuard* follow-ups. Sole runner of cohorts and full gates.
- B (lead): Astra 5 (one promise history for C + handoff, two-milestone regression journey), Astra 6 (narrow Lead imports), judge-input token cut.

## Rules
1. One lander at a time: fetch, rebase on origin/main, cold-import, push; tell the other session sha + net src lines.
2. Every lane lists its files below before launch; overlapping files -> second lane waits or rebases.
3. Gates/cohorts run by the fork (ask it to queue), or by lead when the fork says it is idle.
4. AGENDA.md = lead; findings -> HANDOVER.md.

## Active lanes (name | owner | files | status)
- leadImports | lead (Sol) | lane copy work/lanes/leadImports @34d9378; touches many modules (architecture, plan, questions, decisions, frontdoor, new small modules); in lead.py/judgment.py/proof.py/providers.py ONLY import lines + call sites | running 11-22 ~20:00, no gate (fork queues it)
- leadJudgeTokens | lead (Sol) | lane copy work/lanes/leadJudgeTokens @34d9378; new src/seldon/evidence.py + one-line call sites in judgment.py/lead.py; switch SELDON_OFF=leadLeanJudge | running 11-22 ~20:00, offline Terra replay only
5. Shared semantic-cc checkout stays on main: no branch switches or rebases there (coord lands from it). Rebase in a `git worktree` under work/lanes; land by fetch + cherry-pick onto main.
- leadPlanOne | lead (Sol) | lane on leadCarryR tree; planning region only (ALIGN/MILESTONES/REVIEW, size routing, planning prompts in questions.py) | running 11-22 late
- leadGuardReuse | fork (Sol) | lane on main 441c0d2; guard question/prompt + guard walk path: judgment.py guard prompt, lead.py prove/guard call site only, proof.py witness replay for the guard, questions.py guard text (NOT planning prompts), test_journey.py guard cases | running 11-22 22:05
- leadLeanBuilder | lead (Sol) | lane on leadPlanOne tree; builder brief and receipt in lead.py, empty pre-run observations on micro path | journeys passed, diff ready for lead review
- leadSizeByBuilder | lead (Sol) | lane on 943def4; planning/size routing + planning prompts only | running 11-22 night
- leadLeanBuilder | REJECTED by race 11-22 22:06 (see HANDOVER)
- leadGuardR2 | fork | STOPPED 11-22 23:0x, replaced by leadGuardOwner (Astra macro)
- leadHumanGuide | lead (Sol) | lane on d822514; B/plan templates, WORK brief, receipt (planning+builder prompts), guard input paths only | running 11-23
- leadGuardOwner | fork (Sol) | lane on main d822514; guard question/prompt + guard call site (judgment.py, questions.py guard text, lead.py prove guard call only, proof.py witness replay), test_journey.py guard cases; NOT planning, NOT B template, NOT receipt | running 11-22 23:05
- leadAskWell | lead (Sol) | lane on d822514; ALIGN prompt + example only (questions.py ALIGN text) | running 11-23
- leadKeepBuilding | fork (Sol) | lane on main d822514; build-return routing only: lead.py build/fail path (where a WORK return without a complete candidate is classified and routed), decisions.py route for that case, test_journey.py build-continuation cases; NOT guard prompt, NOT B template/receipt fields, NOT planning | running 11-22 23:35
- leadGuardOnce | lead (Sol) | lane on 80fad3b; guard walk completeness, repair, scoped re-walk (judgment.py, lead.py prove) + cp1252 decode fix | running 11-23
- leadSeldonOwns | lead (Sol) | on fd6dc6f+guardOnce; PROVE/decisions routing of Seldon/builder-owned failures | running 11-23
- leadNoFalseAmend | lead (Sol) | on 4f71b6d; judge amend normalisation, guard/builder boundary coaching, receipt path normalisation | running 11-23
- leadThinBrief | lead (Sol, detached) | on e4802dc; WORK prompt structure (lead.py render_builder, questions.py WORK) | running 11-23
- leadPlausibleGuard | lead (Sol, detached) | on 989c515; guard must-fix plausibility + local normalisation of judge/receipt bookkeeping (judgment.py, lead.py, proof.py) | running 11-23
