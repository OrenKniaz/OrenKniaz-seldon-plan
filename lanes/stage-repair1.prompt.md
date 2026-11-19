LANE stage-repair1. Worktree: C:/Users/oren/codex-harness/work/lanes/stage-repair1. Temp files only under C:/seldon/tests/repair1. You cannot delete folders, so use a new folder name for each retry.
Read CHARTER.md first, then AGENTS.md. Rules: no unit tests (behaviour-only golden journeys); no lane-local SHAs; do not commit.

CONTEXT: real round 29 (run C:/seldon/runs/fight-1/seldon/20261109T153444-ad0e9a-001-shelflife, diagnosis C:/Users/oren/codex-harness/work/fight-1/r29-diagnosis.md). The five-kind plan compiled, reviewers got the brief and found one real defect (no explicit Python 3.12 verification). The run then stalled and never reached B: the planner proposed the right repair, but it went through the amendment path, which demands provenance the LLM cannot supply (183/191/199 required field; 222 sources must be discovery|research|result). 230/233 then asked the USER for an ID and SHA-256, nine times.

ONE RULE: before B nothing is locked beyond the accepted vision, so a plan-review finding is repaired with the same confined typed edits as any other plan repair (the trace1 `edits` contract and CODE-owned handles). CODE binds the repair to its triggering finding and revision; the LLM supplies only the semantic change and targets. Amendments are for changing something already approved at B or later, and must not be offered before B. The user is asked only for a genuine scope decision. Never expose an ID, SHA or provenance chore to the user.

Also fix the sibling: finding disposition requires a nonempty answer but offers no `open` choice, which produced repeated rejection and judgment cycles and 14 finding members for one gap (event 244 onward). One finding stays one finding across rounds.

Prefer deleting pre-B amendment routing over adding a branch. Aim for net src <= 0; stop and explain if it needs more than about 40 net lines.

Name in the report, but do not fix, the interrupted-effect quarantine at 548/690 unless it blocks this path.

PROOF: in the existing small journey, a reviewer reports one concrete plan defect; the planner repairs it with typed edits; review passes; the run reaches B with no user question and no amendment. Outcome-only assertions. Run ONLY: C:/Users/oren/codex-harness/.venv/Scripts/python.exe -B -c "import sys; from pathlib import Path; from tests.python.core.test_golden_path import small_plan_golden; small_plan_golden(Path(sys.argv[1]))" C:/seldon/tests/repair1/small-plan-1 with PYTHONPATH=<this tree>/src;<this tree> and TEMP/TMP=C:/seldon/tests/repair1.

DELIVER in C:/Users/oren/codex-harness/work/lanes: stage-repair1.patch (git diff against base, include new files), stage-repair1.patch.sha256, stage-repair1-report.md (at most 12 lines: TRIAGE BUG|DESIGN, siblings, the rule as applied, net src/tests lines, journey result with seconds).
