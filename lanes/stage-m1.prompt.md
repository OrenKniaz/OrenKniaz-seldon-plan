LANE stage-m1: Blueprint milestone M1, the unit loop.
Worktree: C:/Users/oren/codex-harness/work/lanes/stage-m1 (Seldon main cdfa568). Temp files only under C:/seldon/tests/m1; you cannot delete folders, so use a new folder name per run.

Read CHARTER.md, then BLUEPRINT.md (binding; this lane builds M1 of section 6), then all of src/seldon and tests/seldon.
Rules: behaviour-only journeys, no unit tests. No real provider calls. Do not touch src/codex_harness or tests/python. No new dependencies. Do not commit.

GOAL
Replace the global phases with a per-unit lifecycle (Blueprint 3.2 unit table; R6, R7, R8, R9, R11, R14). Still one wave. No Area or Contract records yet (M2). The design test: it must hold at 100 units.

DESIGN (decided by the owner; if a point is wrong, stop and say exactly where instead of improvising)

1. Modules. Delete the Inference/Decisions/Verification/Execution mixins. No class shares state through `self` with another module; pass the store and ids explicitly. Lines at most 110 characters. Each module docstring names its charter clauses and blueprint rules.
   - states.py: the RUN and UNIT transition tables as data, `{state: {event: next}}`, and one `advance()` that refuses an illegal move. Every transition goes through it and is recorded.
   - store.py: keep. The run cursor and the unit rows become typed: fields declared once and checked on write. No free-form keys.
   - plan.py: a unit has `scope` (path patterns it may write), `checkPaths` (patterns inside its scope that hold its checks), `requirements`, `dependencies`. A check has `mode`: `establishes` or `preserves`. CODE assigns checks: a check belongs to the unit that owns all its requirements; a check whose requirements span units is a wave-level check. Remove exact productFiles/testFiles lists, the unit `tests` list, the wave node the LLM never wrote, and the hard-coded TRY.txt (one guide-path constant is fine).
   - proof.py (replaces evidence.py and verification.py). For a returned unit, by code only:
     a. diff the worktree against the unit's base commit; every changed path must match the unit's scope, else the failure names the paths;
     b. commit T = base + changed files matching checkPaths; commit P = base + all changed files;
     c. each `establishes` check must run at T and exit non-zero; every unit check must exit zero at P; a `preserves` check that exists at base must also pass at base; a run where nothing executed or everything skipped proves nothing;
     d. observations bind to commit ids and hold command, exit code, bounded output and evidence files.
     Delete input/obligation/scope hashing, checkGeneration and all evidence-reuse logic. When the commit changes, run again.
   - units.py: the unit loop as plain functions: READY, WORKING, PROVING, JUDGING, INTEGRATING, DONE, plus REWORK and FAILED. WORKING is one worker session that writes checks and product inside its scope and runs them. A failure in PROVING, JUDGING or INTEGRATING sends the exact failure back to the same worker: resume the provider session (`codex exec resume <thread id>`; the thread id is in the first JSON event, see a recorded stdout.bin under C:/seldon/tests/core1/real-lead-37/calls), and fall back to a fresh session with brief, patch and failure when resume is unavailable. Two recoveries, then FAILED. JUDGING is one question for this unit only: its requirements, its check sources, the failing output at T, the passing output at P, screenshots. It answers per requirement: is the check meaningful, is anything a stub, mock or missing.
   - scheduler.py: runs unit loops concurrently. A unit is READY when its dependencies are DONE and its scope overlaps no running unit's scope. Capacity is bounded. Every wait is recorded with its reason. A FAILED unit never stops others; its dependants become BLOCKED with the reason. The wave ends when no unit can progress.
   - gitwork.py (from work.py): one worktree per unit from the current wave candidate commit. Integration applies the unit's commit P onto the current candidate, then reruns that unit's checks on the new commit. Scopes are disjoint, so a conflict is a Seldon fault reported exactly. Keep crash-safe publication (intent, apply, confirm) and reopen.
   - run.py (from loop.py): ALIGN, A, PLAN, REVIEW, B, EXECUTE (scheduler), WAVE-VERIFY, CHECK-IN, DEMO-JUDGE, C. WAVE-VERIFY is code: run every check, unit and wave level, on the final candidate commit; a failing unit check returns to its unit as rework. If any unit is FAILED or BLOCKED, the run ends INCOMPLETE naming them, after every other unit finished. DEMO-JUDGE asks one bounded question per feature (the feature, its requirements, their final observations, screenshots); CODE combines the verdicts with "every requirement has a passing check on the final commit". The try-it guide is a CODE-created last unit that depends on all others.
   - decisions.py: keep explicit approvals and plan repair before B (review gap, plan edit, review again, at most 3). Remove plan repair after B, IMPACT and scope routing; they return in M3 as unit steering. Name this in the report as an open deviation.
   - inference.py and questions.py: keep strict schemas, exact-fix retries, provider retries and call recording. Facts for WORK and JUDGE come from one brief function per subject: plain labelled sections a person could read; no store ids except handles the answer must use; no digests or receipts (R12). Remove required `citations`; keep `why`.

2. Journeys in tests/seldon (scripted provider, real store, real git, real processes), proved by outcome:
   - a one-unit product reaches C;
   - three independent units overlap in time and integrate;
   - an out-of-scope write is refused and reworked;
   - an `establishes` check that passes without the product is refused and reworked;
   - rework resumes the same session and succeeds;
   - one unit fails three times: it is FAILED, its dependant BLOCKED, unrelated units DONE, the run INCOMPLETE naming them;
   - a kill during WORKING, PROVING and INTEGRATING, then reopen, completes without redoing DONE units;
   - a provider timeout recovers.
   - Scale journey (Blueprint P2): 50 units with chains and fan-in, a scripted worker writing one small file and one check per unit. All DONE; the largest WORK and JUDGE question at 50 units is no larger than at 1 unit; target under 60 seconds.
   Whole suite under 3 minutes. Delete journeys for removed machinery and say which.
   Adapt tests/seldon/real_hello.py and run_report.py to the new records so the lead can run hello-world and Foundation for real; keep the RUNS.md columns.

DELIVER in C:/Users/oren/codex-harness/work/lanes:
stage-m1.patch (git diff against base, with new and deleted files), stage-m1.patch.sha256, stage-m1-report.md of at most 15 lines: modules with line counts; what was deleted; journeys and seconds; the two state tables pasted; any point of this design you found wrong; what is unproven. Short, no boilerplate.
