LANE stage-red1. Worktree: C:/Users/oren/codex-harness/work/lanes/stage-red1. Temp files only under C:/seldon/tests/red1. You cannot delete folders, so use a new folder name for each retry.
Read CHARTER.md first, then AGENTS.md. Rules: no unit tests (behaviour-only golden journeys); no lane-local SHAs; do not commit.

CONTEXT: real round 31 (run C:/seldon/runs/fight-1/seldon/20261109T171636-f1497a-001-shelflife, diagnosis C:/Users/oren/codex-harness/work/fight-1/r31-diagnosis.md). First real run past B: B committed, publication ran, the contracts worker wrote four test files. Then it stopped. Ten tests skipped because prerequisites were absent, yet exit-code observations gave four raw PASS (184). After readmission (208) all four checks exited 2 before any product assertion (219), because the app does not exist yet. An inconclusive judgment became semanticHeld=true, repairRequired=false, resumeRun=null (237-238). The build bead depends on the contracts bead, so implementation never launched: the tests need the app, and the app waits on the tests. Then Seldon asked the user for help.

ONE RULE: CODE consumes every execution judgment as a phase-specific transition; none ends in a hold with no next step.
- Contracts phase: the purpose is meaningful RED, tests that exist and do not pass because the product is missing. Failing because the product files are absent IS valid RED on greenfield work and releases the build bead. A skipped test is never PASS and never RED by itself: a run where everything skips is not RED.
- Blocked or invalid RED (tests broken for reasons other than the missing product) schedules bounded same-scope repair of the contracts bead, then replan. No user question.
- If the judge stays inconclusive on RED after that bound, standing owner rule applies: never block delivery. Release the build bead with an honestly labelled weak RED.
- Integrated GREEN still gates later validation exactly as today. Do not weaken acceptance.
- Give the judge what it needs: which product files are absent, and each check's actual failure. Do not rejudge unchanged evidence (262/280-281, 307/325-326); same evidence should reuse the same judgment or move on.

Siblings: name in the report anything left from "browser verification requires interactive operation its invocation never supplies" and the file-citation exact-fix rejections at 193/228/271/316. Fix them only if they fall out of the same owner.

Prefer deleting the hold state over adding branches. Aim for net src <= 0; stop and explain if it needs more than about 40 net lines.

PROOF: in an existing golden journey, the contracts bead's checks fail because the product is absent; the build bead launches with no user question; a run where everything skips is not accepted as RED. Outcome-only assertions. Run ONLY: C:/Users/oren/codex-harness/.venv/Scripts/python.exe -B -c "import sys; from pathlib import Path; from tests.python.core.test_golden_path import small_plan_golden; small_plan_golden(Path(sys.argv[1]))" C:/seldon/tests/red1/small-plan-1 with PYTHONPATH=<this tree>/src;<this tree> and TEMP/TMP=C:/seldon/tests/red1. If the behaviour lives only on the A-to-C path, add the proof where the lead's fast gate (web leg) reaches it, and say so; do not run that leg.

DELIVER in C:/Users/oren/codex-harness/work/lanes: stage-red1.patch (git diff against base, include new files), stage-red1.patch.sha256, stage-red1-report.md (at most 12 lines: TRIAGE BUG|DESIGN, siblings, the rule as applied, what was deleted, net src/tests lines, journey result with seconds).
