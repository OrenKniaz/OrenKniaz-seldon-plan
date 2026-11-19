LANE stage-core7: redesign RED so it cannot veto valid work. Worktree: ~/codex-harness/work/lanes/stage-core7 (Seldon main 6156fce). Temp files only under C:/seldon/tests/core7. You cannot delete folders, so use new names.

Read CHARTER.md (C14, I1, I2, I7, I9), ~/codex-harness/work/ladder/CLEAN-CORE-DECISION.md, and the audit's RED section in ~/codex-harness/work/ladder/design-review/clean-core-scaling-audit.md. Evidence: real runs C:/seldon/tests/core1/real-lead-09, -22 and -24 (.out reports and calls/). Behaviour-only tests; do not commit; touch nothing under src/codex_harness. The owner's rule: a failure on hello-world is a design defect; no prompt sentence that patches one observed answer. Delete wherever possible.

THE DEFECT: twice now a judge rejected missing-product RED ("rerun against the loadable page"), and in run 22 a worker was blocked by a test that deliberately skipped a visual review and exited 1. Two causes are structural:

1. RED asks the judge to interpret a run that cannot reach any behaviour, because the product does not exist. Change the question. CODE establishes: the baseline contains none of the declared product files, the command really executed, its exit code, and the bounded output. The judge then reviews the TEST ITSELF: given its actual source text, does this check exercise the accepted obligations, and is its failure attributable to the absent product rather than to broken tooling? It no longer asks for evidence of behaviour on a page that does not exist. Give the judge the test source as a fact. A test that would pass with no product, or that asserts nothing about the obligation, is the gap RED exists to catch. Keep the rule general enough that existing-product work can later say which obligations must already be green.

2. execution.json makes every product's tests write a Seldon-specific report, which leaks Seldon into products (I7) and invites self-inflicted skip logic. Remove the report contract, its guide sentence, REPORT, toolReady and the worker's duty to write it. CODE observes exit codes and output. Tooling failure and all-skipped are recognised by the judge from the actual output and test source, and all-skipped must still not count as RED or GREEN. A check is automated: it never waits on a manual or visual review. Visual quality is judged by Seldon from real screenshots at demo; say that once, in the structure of the task, not as a patch.

Also make the 36-journey suite fast: it now takes nearly 8 minutes. Share expensive setup, run journeys in parallel where they are independent, and remove duplicate paths, keeping every behaviour proved. Target under 2 minutes, and say the result.

Prove by outcome: a greenfield test that fails on absence passes RED with no behaviour evidence; a test that asserts nothing, passes with no product, or only reports tooling failure does not; products contain no Seldon report file; a worker is never blocked by its own skip.

Do NOT make real provider calls. Net production lines should fall.

DELIVER in ~/codex-harness/work/lanes: stage-core7.patch (git diff against base including new files), stage-core7.patch.sha256, stage-core7-report.md (at most 12 lines: what changed, what was deleted, module sizes, total lines, journey count and seconds).
