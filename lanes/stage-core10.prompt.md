LANE stage-core10: bounded judgment per unit, and code-derived unit tests. Worktree: ~/codex-harness/work/lanes/stage-core10 (Seldon main c5ab470). Temp files only under C:/seldon/tests/core10. You cannot delete folders, so use new names.

Read CHARTER.md (C9, C11, C12, I1, I9, I10), ~/codex-harness/work/ladder/CLEAN-CORE-DECISION.md, ~/codex-harness/work/ladder/CLEAN-CORE-DESIGN.md (section 3, question construction: CODE pages oversized subjects into bounded questions with explicit coverage; never silently truncates), and the audit's JUDGE row in ~/codex-harness/work/ladder/design-review/clean-core-scaling-audit.md. Behaviour-only tests; do not commit; touch nothing under src/codex_harness or tests/python. No prompt sentence may patch one observed answer.

EVIDENCE: real Foundation runs C:/seldon/tests/core1/real-f7, -f8, -f9 (reports in .out files, calls/ folders).
- f7 and f9 built the whole three-button product with real parallel workers, then died at JUDGE: "Question exceeds 64 KiB; split its coverage before asking". Paging was designed and never built. One three-button app should be nowhere near a limit.
- f8 failed PLAN three times on "Unit checks must refer to its own obligations": the planner must list each unit's tests and keep them consistent with requirement links by hand.

FIX BY RULE:
1. JUDGE is per unit, with complete bounded evidence for exactly that unit's obligations, and an integration judgment only for obligations that span units, from its own bounded facts. Each question carries explicit coverage: which obligations it judges. A subject too large for one question is split by CODE with recorded coverage, never truncated. Also find why one JUDGE question got this big for three buttons (repeated sources, full screenshots, all units at once) and remove the duplication at its producer.
2. A unit's tests are derived by CODE: a test belongs to the unit that owns the requirements it covers. Remove the `tests` field from the planner's unit shape, delete the rule that refused f8's plan, and let CODE compute it. A test that covers requirements in several units belongs to the integration step.
3. Report the largest question in bytes for hello-world and for the scripted three-unit journey, before and after.

Prove by outcome: the three-unit journey reaches C with per-unit judgments and every question under a fixed bound well below 64 KiB; a plan without per-unit test lists is accepted; hello-world prompts do not grow. Keep the suite under 2 minutes.

Do NOT make real provider calls. Net production lines should fall or stay flat.

DELIVER in ~/codex-harness/work/lanes: stage-core10.patch (git diff against base including new files), stage-core10.patch.sha256, stage-core10-report.md (at most 8 lines).
