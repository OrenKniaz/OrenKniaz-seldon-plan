LANE stage-core6: audit change 3, one scoped durable work unit. Worktree: ~/codex-harness/work/lanes/stage-core6 (Seldon main f465f9c). Temp files only under C:/seldon/tests/core6. You cannot delete folders, so use a new folder name for each retry.

Read CHARTER.md (C12, C13, C17, C18, C23, I9), ~/codex-harness/work/ladder/CLEAN-CORE-DECISION.md, ~/codex-harness/work/ladder/CLEAN-CORE-DESIGN.md, and ~/codex-harness/work/ladder/design-review/clean-core-scaling-audit.md section 3 and change 3. Behaviour-only tests; no unit tests; do not commit; touch nothing under src/codex_harness. No prompt sentence may patch one observed answer.

GOAL: make one scoped, durable work contract the unit of the loop. Tiny work is one serial unit. A larger app is many units, with no second execution model. CODE owns identities, dependencies, attempts, integration and invalidation; the LLM owns semantic decomposition only when there is more than one unit.

CHANGE THE SHAPE, per the audit:
- Each unit records its own requirements, tests, owned files, dependencies, attempts, and results. Delete blanket every-bead-to-every-requirement links, global latest-result assumptions, and the in-memory `task`/`bead`/`assignment`/`changed` globals. Assignment authority lives in the store, so a re-opened run can tell what is finished.
- Requirement and test links stay local, so a change invalidates only what depends on it, and unaffected evidence stays valid.
- Run ready units concurrently when they do not share files, using a small bounded pool. Conflicting ownership waits with a recorded reason. Integrate each finished unit with real base revisions and changed-file patches, at a recoverable publication boundary, so a crash cannot leave half a candidate.
- A run can be reopened from the store: finished work is retained, and an uncertain writer is not relaunched. Keep this minimal: one reopen path, proved once by a killed run.
- REPO HYGIENE, owner's instruction: no god files. loop.py is 534 lines and is about to grow; split it along real responsibilities (state transitions, work execution, decisions/repair routing) so each module has one job and reads in one sitting. Every module's docstring names its charter clause. Remove anything dead.

PROVE by outcome in tests/seldon/test_journey.py, in the same journey style with scripted LLM replies and real processes:
- The existing single-unit journey is unchanged in outcome.
- A plan with three independent units, for example three buttons in three files plus a shared integration, runs units concurrently, with measured overlap in time asserted from recorded attempts, no file conflicts, each unit having its own checks, integrating to one working product through C.
- Two units claiming one file do not overlap and record why.
- Changing one unit's requirement invalidates only that unit's evidence.
- A run killed mid-work reopens, keeps finished units, and completes.

Keep hello-world's prompts and costs the same or smaller. Do NOT make real provider calls. Say the production line total and per-module sizes.

DELIVER in ~/codex-harness/work/lanes: stage-core6.patch (git diff against base including new files; the lead will rebase if needed), stage-core6.patch.sha256, stage-core6-report.md (at most 14 lines: what changed, module sizes, total lines, journey results with seconds, what is not proven).
