LANE stage-core9: make concurrent units and provider calls robust. Worktree: C:/Users/oren/codex-harness/work/lanes/stage-core9 (Seldon main 8ddd8bc). Temp files only under C:/seldon/tests/core9. You cannot delete folders, so use new names.

Read CHARTER.md (C12, C18, C20, I2, I9), C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DECISION.md, C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DESIGN.md section 1 (universal exits). Behaviour-only tests; do not commit; touch nothing under src/codex_harness or tests/python. No prompt sentence may patch one observed answer.

EVIDENCE:
- Real Foundation run C:/seldon/tests/core1/real-f3 (report: real-f3.out): real concurrency worked, with four test workers and then four build workers in parallel. It stalled because unit checks for each button opened index.html, which another unit (the composer) owned and had not built yet. Workers reported "blocked: the composition owner must supply index.html" and the run ended INCOMPLETE.
- Real run C:/seldon/tests/core1/real-f4: a PLAN provider call hung and timed out after 600 seconds (calls/call-2f3718b6ac684f4caad0f949325ded8d/result.json, timedOut true), and the whole run ended INCOMPLETE. The design promises at most two recoveries for transient provider failure; it was never built.

FIX BY RULE:
1. A unit's checks may depend only on its own files and the files of units it depends on. Make that true structurally: CODE knows which unit owns each file. When planning, the plan states dependencies; when a worker is blocked on a file owned by another unit, CODE recognises the owner from the plan, records a missing dependency as a plan defect, adds it through the existing repair route, and reschedules, bounded like other repairs. Also tell the planner once, in the PLAN guide's existing sentence about units, that a unit's checks use only its own and its dependencies' files.
2. Transient provider failure (timeout, crash, non-zero exit without a schema answer) gets at most two fresh retries of the same question with the same facts, recorded as attempts, then the existing INCOMPLETE with the exact reason. Authentication and permission failures are not retried. A worker retry never runs while a previous writer for the same unit could still be alive.
3. Provider timeout: 600 seconds is one fixed number for every call. Make it per role from the existing role table (short for questions, longer for workers), and record it.

Prove by outcome: a unit whose check needs another unit's file gets that dependency and reaches C without a user question; a provider call that times out once then succeeds continues the run; one that always fails ends INCOMPLETE after two retries; an auth failure is not retried. Keep the suite under 2 minutes and hello-world's prompts unchanged.

Do NOT make real provider calls. Keep net production lines low.

DELIVER in C:/Users/oren/codex-harness/work/lanes: stage-core9.patch (git diff against base including new files), stage-core9.patch.sha256, stage-core9-report.md (at most 8 lines).
