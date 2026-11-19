LANE stage-core1: first real LLM path on the clean core. Worktree: C:/Users/oren/codex-harness/work/lanes/stage-core1 (Seldon main 5ee57f1). Temp files only under C:/seldon/tests/core1. You cannot delete folders, so use a new folder name for each retry.

Read CHARTER.md, then C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DESIGN.md (risk 2 especially: do the first native call early), then src/seldon. Behaviour-only tests; no unit tests; no lane-local SHAs; do not commit; touch nothing under src/codex_harness.

GOAL: the owner can launch a real run of the Plain Hello-world dream: "Build a tiny web page with one Play button. When I click Play, the page shows the text "Hello, world!". A single static HTML file is enough. No server, no accounts, no dependencies."

BUILD, smallest thing that works:
1. providers.py per the design: real Codex calls. Questions use `codex exec` with a strict --output-schema, read-only. Workers run `codex exec` with workspace-write inside their assigned worktree. Default model gpt-6.1-sol, medium effort. Reviewer is a separate fresh call, honestly labelled same-provider. Use hidden_process_kwargs on every launch. Capture and save the real question, schema and raw answer for each call so they can later replay as regression fixtures.
2. processes.py: bounded subprocess with deadline and cleanup. Lift from old audit_process.py only if plain subprocess is not enough for this milestone, and say which.
3. Setup facts given to the planner and workers, observed by CODE, not discovered by the LLM: Python path and version; node path; the Playwright install location and Chromium executable on this machine (Edge at C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe, Chrome at C:/Program Files/Google/Chrome/Application/chrome.exe, and Playwright browsers under %LOCALAPPDATA%/ms-playwright exist here; detect them, do not hard-code). Include how a test can drive a real browser with what is installed.
4. A small dev runner, tests/seldon/real_hello.py: runs the loop with real providers and a scripted user who says "yes" at each decision, writing everything under a slot folder given on the command line. A plain CLI entry for real users comes later.
5. Strict-schema reality: real providers reject schemas unless every property is required and additionalProperties is false. Make schema.py produce those for every question.
6. Malformed answer handling from the design: two exact-fix retries carrying every error, the rejected answer and the original facts, then an explicit INCOMPLETE outcome with the reason. Do not build REPAIR yet: a gap or failed judgment ends INCOMPLETE naming exactly where and why. The run must never hang or loop.

KEEP test: tests/seldon/test_journey.py still passes with scripted providers through the same provider function. Extend it only for the malformed-answer retry and INCOMPLETE outcome.

Do NOT make real provider calls yourself; you are inside a sandbox. The lead runs real_hello.py. Prove your side with the scripted journey plus a dry run that prints the exact codex command line and schema for one question.

Stay small. Stop and explain if production passes about 2,000 lines total.

DELIVER in C:/Users/oren/codex-harness/work/lanes: stage-core1.patch (git diff against base including new files), stage-core1.patch.sha256, stage-core1-report.md (at most 12 lines: new files and lines, total production lines, journey result with seconds, the exact command for the lead to launch the real run, what is unproven).
