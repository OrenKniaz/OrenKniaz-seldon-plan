LANE stage-core5: the audit's changes 1 and 2. Worktree: C:/Users/oren/codex-harness/work/lanes/stage-core5 (Seldon main d4cb94c). Temp files only under C:/seldon/tests/core5. You cannot delete folders, so use a new folder name for each retry.

Read CHARTER.md, C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DECISION.md, and all of C:/Users/oren/codex-harness/work/ladder/design-review/clean-core-scaling-audit.md. The audit is your spec. Behaviour-only tests; no unit tests; do not commit; touch nothing under src/codex_harness. No prompt sentence may patch one observed answer: if the fix is a sentence, find the structure that removes the need for it.

CHANGE 1: evidence applicability and execution facts are authoritative in CODE.
- One owner establishes candidate/test/input identity, execution status, coverage, and whether earlier evidence still applies because its inputs are byte-identical (run 12: only TRY.txt changed, and the judge refused valid evidence for lack of that fact; `_eligible()` already knows how). Judges receive those facts as established and are not asked about them. Do not duplicate functional checks at walkthrough; `plan.create()` must stop cloning a verification command into a walkthrough.
- RED: CODE establishes the baseline, the declared product outputs, tool readiness (the test tooling really ran), the command's execution and test inventory. All-skipped or tool failure is not RED. The judge is asked only whether the attempted check meaningfully challenges the obligation. No stderr keyword matching. Replace the missing-product sentence added in d4cb94c with this structure.
- `shutil.which()` at PLAN rejects legitimate not-yet-built product executables. Separate installed verification tools from product outputs.
- ALIGN must receive the setup capabilities that its "observable with the supplied setup" guide refers to.
- A real user's decision: an explicit approve/revise response bound to the displayed subject is consumed by CODE with no LLM call; the scripted dev reply is consumed the same way and stays labelled scripted. The LLM reads only free-form or qualified words. Delete the "scripted approval is interpretable" sentence and any question this makes unnecessary.

CHANGE 2: each worker finishes a locally checked result; repairs route by cause.
- Delete "Report, do not prove". Workers run their assigned checks, and on a UI look at their own real screenshots, and refine before returning. Seldon's independent observation stays the only proof.
- The build worker writes the guide in the same delivery, with CODE still scheduling acceptance; remove the separate guide worker call. Keep the demo judgment.
- Repairs route by cause: a missing fact gathers evidence and never forces a file edit; an implementation fault goes back to its writer with the actual failure; a plan defect goes to plan edits. Delete forced changed-byte progress, guide rewrites for evidence defects, and empty REPAIR calls that just reschedule the same task (run 09 spent four test-worker calls this way). A discovery receives a disposition instead of being dropped.
- Role config: give the invocation an explicit per-role model and effort from one table, recorded in provenance. Keep the same model for now, except build worker and demo judge high effort, and free-form DECIDE low effort.

Also: real_hello.py records the source commit in RUNS.md (it says unknown today), plus the question-contract digest. Do change 3 only where it falls out of these; say what remains.

Prove by outcome in tests/seldon/test_journey.py: unchanged-input evidence is reused at demo with no gap; a broken-tool failure is not RED while a real run against a missing product can be; an evidence gap triggers no product edit; an implementation fault reaches its writer with its failure; explicit approve uses no LLM call; there is no guide worker call. Remove journey branches that manufacture gaps from packet shape.

Do NOT make real provider calls. Net production lines should fall or stay flat; say which went.

DELIVER in C:/Users/oren/codex-harness/work/lanes: stage-core5.patch (git diff against base including new files), stage-core5.patch.sha256, stage-core5-report.md (at most 14 lines: what changed against each audit item, what was deleted, total production lines, journey result with seconds, what remains from change 3).
