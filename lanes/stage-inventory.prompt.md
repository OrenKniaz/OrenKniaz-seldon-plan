LANE stage-inventory. Worktree: C:/Users/oren/codex-harness/work/lanes/stage-inventory. Temp files only under C:/seldon/tests/inventory. This lane changes no product code: instrumentation only, and nothing from it lands.

The owner asked what 32,000 lines of Seldon do and whether they belong in charter v1.2. Answer with evidence, not impressions. Read CHARTER.md first.

1. Measure which functions in src/codex_harness/core actually execute on the thin path, by running small_plan_golden with function-level tracing (sys.setprofile or sys.monitoring, including child Python processes if it is cheap to do so; otherwise say so). Command shape: C:/Users/oren/codex-harness/.venv/Scripts/python.exe -B -c "import sys; from pathlib import Path; from tests.python.core.test_golden_path import small_plan_golden; small_plan_golden(Path(sys.argv[1]))" C:/seldon/tests/inventory/small-plan-1 with PYTHONPATH=<this tree>/src;<this tree> and TEMP/TMP=C:/seldon/tests/inventory.
2. For every module: lines of code, functions executed versus total, and lines inside executed versus never-executed functions.
3. Classify every module by the charter's core loop: KEEP (the A-to-C schema loop needs it: ask LLM with schema, validate, persist, launch worker, run tests, judge, approve), SHRINK, or DELETE (not needed by v1.2), with one-line reasoning and the charter clause it serves if any.
4. Totals: lines KEEP, SHRINK, DELETE, and an honest estimate of the smallest core that delivers charter v1.2 A to C. Name what a stub-run cannot see (crash recovery, real-provider paths).

Write C:/Users/oren/codex-harness/work/ladder/design-review/what-the-code-does.md: a one-paragraph verdict, the totals, then the module table sorted by lines. Plain language. No hedging filler.
