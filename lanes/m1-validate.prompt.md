LANE m1-validate: validate M1 on Seldon main e5a4ead with real runs. No code changes, no commits.
Worktree: ~/codex-harness/work/lanes/m1-validate-20261112. Temp only under C:/seldon/tests/m1val-<n> (new folder per run).
Python for real runs: ~/AppData/Local/Programs/Python/Python312/python.exe. Use tests/seldon/real_hello.py the way earlier cohorts did (see work/ladder/RUNS.md rows hello-ef91dd7-*).
1. Real hello-world 10 times, one after another. 2. Real Foundation (three buttons) 2 times.
Append one RUNS.md row per run in ~/codex-harness/work/ladder/RUNS.md, ids hello-e5a4ead-01..10 and foundation-e5a4ead-01..02, same columns.
If a run fails or needs a repair: do not fix anything; record the exact failure, the call recording path, and your reading BUG or DESIGN with one reason.
DELIVER ~/codex-harness/work/lanes/m1-validate-report.md, at most 12 lines: clean count per dream, every failure with path and reading. No boilerplate.
