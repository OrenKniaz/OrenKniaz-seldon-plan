LANE stage-packets1. Worktree: ~/codex-harness/work/lanes/stage-packets1. Temp files only under C:/seldon/tests/packets1. You cannot delete folders, so use a new folder name for each retry.
Read CHARTER.md first, then AGENTS.md. Rules: no unit tests (behaviour-only golden journeys); no lane-local SHAs; do not commit.

CONTEXT: real round 28 (run C:/seldon/runs/fight-1/seldon/20261109T121252-904193-001-shelflife, diagnosis ~/codex-harness/work/fight-1/r28-diagnosis.md). The five-kind plan saved and compiled, and two Codex reviews ran, but the run did not reach B.

ONE RULE: CODE builds each semantic question from the canonical facts and obligations of its current phase; the LLM judges only that question. Apply it to the three concrete cases, at the existing packet producers:
1. Review packets 123/133/136 said "Full brief source unresolved" although the original brief exists at event 5. Reviewers must receive the actual brief, or the accepted vision that canonically carries it.
2. Plan review before B asks whether this plan can deliver the accepted dream. Reviews 140-144 found no concrete plan defect but stayed inconclusive over absent implementation and execution evidence. That evidence belongs after Build; a pre-B review must not ask for it or be inconclusive for lacking it.
3. Events 84-114: the planner guessed execution descriptors (`unittest`, runtime `python`) and hunted for the interpreter with shell commands. CODE should supply the observed setup facts and allowed descriptor forms in the plan question.

Name in the report, but do not fix, the unretired semantic effect at event 147 unless it is clearly a real bug rather than the PC sleeping (the machine slept through this run).

Time-box: about 40 net src lines. Prefer deleting. If it needs more, stop and explain.

PROOF: assertions in an existing golden journey that the plan-review packet contains the brief text, does not request implementation evidence, and that the plan question supplies the setup facts. Outcome-only. Run ONLY: ~/codex-harness/.venv/Scripts/python.exe -B -c "import sys; from pathlib import Path; from tests.python.core.test_golden_path import small_plan_golden; small_plan_golden(Path(sys.argv[1]))" C:/seldon/tests/packets1/small-plan-1 with PYTHONPATH=<this tree>/src;<this tree> and TEMP/TMP=C:/seldon/tests/packets1.

DELIVER in ~/codex-harness/work/lanes: stage-packets1.patch (git diff against base, include new files), stage-packets1.patch.sha256, stage-packets1-report.md (at most 12 lines: TRIAGE BUG|DESIGN, siblings, the rule as applied, net src/tests lines, journey result with seconds).
