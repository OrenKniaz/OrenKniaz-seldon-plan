LANE stage-nowin2. Worktree: ~/codex-harness/work/lanes/stage-nowin2. Temp files only under C:/seldon/tests/nowin2.
Read CHARTER.md first, then AGENTS.md. No unit tests, no lane-local SHAs, do not commit.

PROBLEM: console windows pop up and steal focus on the owner's Windows machine during runs. Seldon's controller starts with DETACHED_PROCESS (core/planner_jobs.py:588), so it has no console, and every console tool launched beneath it without CREATE_NO_WINDOW opens a visible window. `core/audit_process.py` already passes creationflags=subprocess.CREATE_NO_WINDOW.

ALREADY TRIED AND FAILED: changing the controller itself to CREATE_NO_WINDOW turned the web gate red three times. Do NOT change the controller's flags. Do not change how audit_process launches.

CHANGE - one rule, one owner: every subprocess launch in src/ of a console tool (git, python, npm, shells, providers) is window-hidden on Windows, using one small shared helper that returns the right kwargs (nothing on other platforms). Sites to cover include runners.py, package_provenance.py, acceptance_revision.py, test_audit.py, wave_refine.py, supervision.py, steering.py, project_init.py, dispatch_repository.py; find any others by grep, including asyncio.create_subprocess_*, os.system and os.startfile. Merge with any creationflags a site already passes rather than overwriting it. Keep the diff mechanical and do not refactor these call sites otherwise.

Do NOT run the gate or the test suite: a real run is using this machine and the lead gates it after. Do a static check only: compile the changed files and grep that no src launch is left without the helper, and list any deliberate exception.

DELIVER in ~/codex-harness/work/lanes: stage-nowin2.patch (git diff against base, include new files), stage-nowin2.patch.sha256, stage-nowin2-report.md (at most 10 lines: TRIAGE BUG|DESIGN, sites changed, exceptions, net src lines).
