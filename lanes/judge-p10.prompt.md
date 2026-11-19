P10 bird's-eye review of Seldon's JUDGMENT design. Read-only. At most 30 lines, plain words. Two DESIGN faults in the judgment module landed today after this morning's review; P10 (Blueprint v1.5 section 7) stops lanes there until the shape is reviewed.

Read: C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/CHARTER.md and BLUEPRINT.md (R2: source judged once at the unit, behaviour after integration; R7, R9, R12; section 3.2 flow review; 8.4 reading of C15; section 6 M2 row). Code on main 59d3a56: src/seldon/judgment.py, questions.py (judge_brief, PROMPTS), plan.py (criterion level, unit_criteria, coverage), units.py. Tickets T-78..T-93 in C:/Users/oren/codex-harness/work/ladder/TICKETS.json (evidence fields). Morning review result: C:/Users/oren/codex-harness/work/ladder/RECOMMENDATIONS.json.

Today's chain, each from one real canonical Foundation run (3 buttons + shared page): T-78 one subject per question; T-81 judge at the owning level, no judgment flag; T-82 final judges see behaviour only; T-83/T-84 code walks the guide; T-85 planner marks each QUALITY CRITERION unit or product (unit criteria asked in each reached unit JUDGE with its source; product at PRODUCT); T-86/T-87 bugs. Now:
- T-92: real criteria mix both (e.g. "each script owns only its button" = source, AND "page works with a script missing" = behaviour). REVIEW loops asking to split the criterion; the planner cannot split it because criteria come from the Vision Lock accepted at A. foundation-59d3a56-c02: 3 REVIEW gaps, 4 REPAIRs pre-B. C:/seldon/tests/m1/foundation-59d3a56-c02/calls.
- T-93: a visual criterion marked unit reached a unit JUDGE without the screenshots; uncertain -> unit FAILED -> run INCOMPLETE. C:/seldon/tests/m1/foundation-59d3a56-c01/calls.
Real Foundation results today: 9 runs since the first judge fix, 6 reached C, repairs 0-8, flags 0-14, not improving.

Answer:
1. Root cause in one sentence: what about the shape keeps producing these? (Is it that quality criteria from the Vision Lock are product-level prose that we keep trying to route by evidence type?)
2. The simplest correct shape for quality judgment in M1 now, that holds at 100 units and does not need the planner or reviewer to classify criteria. Consider, e.g.: quality criteria judged only as behaviour at PRODUCT with per-unit verdict rows; source-related quality folded into the unit JUDGE's standing obligations (CRAFT/JUDGMENT_LEEWAY: no stubs, stays in scope, owns its responsibility) for every unit always; ALIGN writing criteria that are observable; or something better. Say what to DELETE.
3. Does M2 (contracts + flow review) remove this class by construction, so the M1 stand-in should be made minimal rather than perfected? If so, what is the minimal M1 stand-in?
4. Must not do.
