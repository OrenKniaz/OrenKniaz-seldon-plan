LANE stage-core10b: per-unit judgment, redone so it cannot regress real runs. Worktree: ~/codex-harness/work/lanes/stage-core10b (Seldon main e4024b6, where the first attempt was reverted). Temp files only under C:/seldon/tests/core10b. You cannot delete folders, so use new names.

Read CHARTER.md (C9, C11, C12, I1, I9, I10), ~/codex-harness/work/ladder/CLEAN-CORE-DECISION.md, and the first attempt: ~/codex-harness/work/lanes/stage-core10.patch and stage-core10-report.md. Behaviour-only tests; do not commit; touch nothing under src/codex_harness or tests/python.

WHAT WENT WRONG WITH THE FIRST ATTEMPT (scripted journeys passed, real runs fell from 6 of 6 to 0 of 5):
- Hello-world runs C:/seldon/tests/core1/real-lead-34 and -35: the judge answered uncertain, asking for "the remaining r17 content, including the complete n3 obligation, check assertions, observed execution results". Paging split one obligation's evidence across questions, so no question held enough to decide.
- Foundation runs C:/seldon/tests/core1/real-f11 and -f12: "No dependency-ready unit" after the tests phase: deriving tests from requirements left a unit or the integration step with nothing schedulable.
- Earlier failures it was meant to fix: real-f7 and -f9 (JUDGE question over 64 KiB) and real-f8 (planner unable to keep unit test lists consistent).

THE MAIN TEST THIS TIME IS REAL RECORDED ANSWERS. Every real call is saved under calls/call-*/ (question.json, answer.txt). Build a replay journey that feeds the recorded real ALIGN/PLAN answers of f7, f9, f11, f12 and lead-34 through the current code and runs to the point each one failed, with scripted replies after that. It must fail on today's main the same way the real runs did, and pass after your change. Say which recordings no longer match the schema.

DESIGN:
1. A judge question never splits a single obligation's evidence. The unit of judgment is one unit (or the integration step) with its complete obligations, check source, observed results and evidence references. Bound it by removing duplication at the producer (repeated sources, all-unit inventories, embedded artifacts), not by paging. If a single unit genuinely cannot fit, say so plainly as a planning signal to split the unit; do not truncate.
2. Code derives unit tests from requirement ownership, and every derived assignment is schedulable: a test covering several units belongs to an integration step that depends on them, and the scheduler can always progress. Prove no unit or step is left without a runnable phase.
3. Keep hello-world's largest question no larger than today and its outcome one unit.

Report hello-world and Foundation largest question bytes before and after, and net production lines (aim flat or lower; the first attempt was +92).

Do NOT make real provider calls.

DELIVER in ~/codex-harness/work/lanes: stage-core10b.patch (git diff against base including new files), stage-core10b.patch.sha256, stage-core10b-report.md (at most 10 lines).
