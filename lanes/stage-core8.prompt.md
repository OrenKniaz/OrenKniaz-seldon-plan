LANE stage-core8: one plan shape for every size, so independent pieces become concurrent units. Worktree: ~/codex-harness/work/lanes/stage-core8 (Seldon main 64cc377). Temp files only under C:/seldon/tests/core8. You cannot delete folders, so use new names.

Read CHARTER.md (C5, C12, I9), ~/codex-harness/work/ladder/CLEAN-CORE-DECISION.md. Behaviour-only tests; do not commit; touch nothing under src/codex_harness.

EVIDENCE: two real runs of the Foundation dream (C:/seldon/tests/core1/real-f1 and real-f2; dream at ~/codex-harness/work/foundation/dream.txt) reached scripted C with zero red flags, but ran as a single unit with no concurrency. The dream asked for three independent pieces in separate files. The LLM sized it "tiny", and schema.py offers `units` only when size is not tiny, so the planner could not express what the dream asked for.

FIX THE SHAPE: the plan answer has one shape for every size. `units` is always offered; a tiny product is simply one unit. Delete the size branches in schema.py and questions.py (PLAN example) and anything else that keys structure on size. Size stays a judgment that informs review depth only. Each unit owns its requirements, its tests, its files and its dependencies, so independent pieces can carry their own checks. The guide for PLAN says once, plainly, that each independently buildable piece is its own unit; do not add size rules.

Keep hello-world's prompts no larger than now and its plan one unit. Update the journeys so the fixtures use the one shape, and prove by outcome that: hello-world is one unit; a three-piece plan with per-unit tests runs concurrently through C. Keep the suite under 2 minutes.

Do NOT make real provider calls. Net production lines should fall.

DELIVER in ~/codex-harness/work/lanes: stage-core8.patch (git diff against base including new files), stage-core8.patch.sha256, stage-core8-report.md (at most 8 lines: what changed, what was deleted, total lines, journey count and seconds).
