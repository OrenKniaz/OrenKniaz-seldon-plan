LANE stage-core2: repair, and the LLM question rules. Worktree: ~/codex-harness/work/lanes/stage-core2 (Seldon main 2fd12fa). Temp files only under C:/seldon/tests/core2. You cannot delete folders, so use a new folder name for each retry.

Read CHARTER.md, ~/codex-harness/work/ladder/CLEAN-CORE-DESIGN.md sections 1, 3, 4, and ~/codex-harness/work/ladder/CLEAN-CORE-DECISION.md (LLM question rules). Behaviour-only tests; no unit tests; no lane-local SHAs; do not commit; touch nothing under src/codex_harness.

CONTEXT: first real run of the clean core: C:/seldon/tests/core1/real-lead-01 (recorded calls under calls/, output in C:/seldon/tests/core1/real-lead-01.out). In 2 minutes, real Codex accepted the strict schemas and went through ALIGN, approval A, PLAN and REVIEW. The reviewer found a gap and the run ended INCOMPLETE, as designed, because REPAIR does not exist yet.

BUILD:
1. REPAIR per design section 4: one EditBatch (Put, Retire, ReplaceLinks) applied atomically, validated as a whole graph, CODE binding the cause and revision, used for review gaps, RED/GREEN/demo judgment gaps, and a user's "revise" at a decision. The model proposes edits, never provenance. After a plan edit: fresh review. After B: within-scope edits proceed through a recorded semantic impact judgment, scope changes go to the user, per the design. Bound the cycle: at most three repairs for the same state before an explicit INCOMPLETE naming the unresolved gap. Unchanged inputs must never be re-asked.
2. `uncertain` handling: a review or judge that says uncertain names needed facts. CODE gathers what it can from the store and setup and asks once more with those facts; if nothing new can be supplied, INCOMPLETE with the question that remains. No holds.
3. Apply the LLM question rules:
   - Citations are an enum of this question's supplied fact handles in the schema. Every target and link field that refers to something existing is an enum of supplied handles too.
   - Replace generated shape examples with one short realistic valid example per state, plus the uncertain example. Keep them product-neutral.
   - One short guide per state, kept as data in one place, one decision each. Trim the PLAN guide hard: move mechanical rules into schema or CODE validation wherever possible.
   - Tell the reviewer that the wave check-in is a Seldon workflow step and not product work. The real reviewer's gap at C:/seldon/tests/core1/real-lead-01.out came from treating it as a plan dependency. Read that gap, decide whether the planner's guide or the plan shape caused it, and fix the cause. Guide work and the check-in should not need the model to express workflow at all if CODE can own that ordering.
4. Extend tests/seldon/test_journey.py with outcome-only variations: review gap then repair then B; RED or GREEN judgment gap then repair then C; uncertain then a fact supplied; repair bound exhausted to INCOMPLETE. Replay the recorded real answers from real-lead-01 if they still match, or say which no longer do.

Do NOT make real provider calls; the lead runs them. Stop and explain if production passes about 2,400 lines total.

DELIVER in ~/codex-harness/work/lanes: stage-core2.patch (git diff against base including new files), stage-core2.patch.sha256, stage-core2-report.md (at most 12 lines: changes, total production lines, journey result with seconds, what is unproven).
