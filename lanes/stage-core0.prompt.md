LANE stage-core0: the clean core, day-one stub spine. Worktree: C:/Users/oren/codex-harness/work/lanes/stage-core0. Temp files only under C:/seldon/tests/core0. You cannot delete folders, so use a new folder name for each retry.

Read, in order: CHARTER.md (v1.3, especially I9), C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DECISION.md, C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DESIGN.md. The design is your spec. Rules: behaviour-only tests, no unit tests; no lane-local SHAs; do not commit.

BUILD ONLY the design's "Day one: complete stub spine" milestone: new package src/seldon/, importing nothing from codex_harness. Stdlib only for now.
- loop.py, schema.py, store.py, plan.py, questions.py, evidence.py and work.py as far as the spine needs them. Every module's docstring names its charter clause. One way to do each thing. Keep each module well under its design target; less is better. Do not add anything the journey does not exercise: no milestone-1a repair, recovery, MCP, or real providers yet. Leave a one-line extension note only where the design names one.
- Lift `hidden_process_kwargs` only if you launch a process and need it. Do not lift audit_process yet; a plain bounded subprocess is enough for day one.
- Providers sit behind one small function so a scripted reply and a later real call are interchangeable.

THE TEST (the only test): tests/seldon/test_journey.py, one scripted journey through the real loop: ALIGN -> DECIDE(A) -> PLAN -> REVIEW -> DECIDE(B) -> WORK(tests) -> OBSERVE(RED) -> JUDGE -> WORK(build) -> INTEGRATE -> OBSERVE(GREEN) -> JUDGE -> WORK(guide) -> OBSERVE(demo) -> JUDGE -> DECIDE(C) -> ACCEPTED, on a small command-line product. Real SQLite, real temporary worktrees, real subprocesses, a real failing test then a real passing test. Only LLM replies and user words are scripted, by question kind and occurrence. Scripted workers only write product and test files. Never seed the store to skip a state. Assert outcomes a user would care about: the delivered product actually runs and gives the promised output, RED was observed before GREEN and failed because the product was missing, C binds the delivered candidate, approvals were asked only at A, B and C (a wave check-in only if your spine has one wave end; follow the design and say what you did).

Run: C:/Users/oren/codex-harness/.venv/Scripts/python.exe -B -m pytest tests/seldon/test_journey.py -q -p no:cacheprovider --basetemp=C:/seldon/tests/core0/run-1 with PYTHONPATH=<this tree>/src and TEMP/TMP=C:/seldon/tests/core0. Target about 60 seconds or less.

Do not touch src/codex_harness or tests/python. If an existing size guard or suite budget counts the new files, say so in the report instead of changing it.

If the design is wrong or unbuildable somewhere, stop at that point and say exactly where; do not improvise a second mechanism.

DELIVER in C:/Users/oren/codex-harness/work/lanes: stage-core0.patch (git diff against base including new files; use git add -N first), stage-core0.patch.sha256, stage-core0-report.md (at most 12 lines: modules and line counts, total lines, journey result with seconds, where you departed from the design and why, what the journey does not prove).
