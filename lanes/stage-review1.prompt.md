LANE stage-review1. Worktree: ~/codex-harness/work/lanes/stage-review1. Temp files only under C:/seldon/tests/review1.
Read CHARTER.md first, then AGENTS.md. Rules: no unit tests (behaviour-only golden journeys); no lane-local SHAs; do not commit.

CONTEXT: real round 27 (run C:/seldon/runs/fight-1/seldon/20261109T113826-5f0c19-001-shelflife, diagnosis ~/codex-harness/work/fight-1/r27-diagnosis.md) is the first run on the five-kind plan. Spec persisted and compiled and reached roundtable, then paused. Both reviewers were Claude and the Claude CLI was not logged in. The run must not stop for that.

FIX TWO THINGS, ONE RULE EACH, AT THE EXISTING OWNERS:

1. A reviewer that cannot authenticate is an unavailable reviewer. Standing owner rules: a missing verifier degrades to a labelled tier and never blocks delivery; same-provider reviewers are acceptable if only one provider works. So when a launched reviewer fails on authentication, the review reselects from the remaining working providers, labels the tier honestly, and continues without a STEER or any user question. Recognise authentication failure from what the provider actually emitted in this run. See `review_provider.py` (selection near line 38, `review_tier`) and `review_rounds.py` (which already classifies some provider failures). Prefer finding this at selection or the first failure, and do not spend three rounds on it. If no provider works, follow the existing labelled-tier behaviour.

2. A question may be answered by citing anything CODE supplied in that question's facts. Event 196 correctly cited the six review-attempt IDs supplied in facts 187; `run_questions.py:62` refused them because it accepts only subjectRefs/evidenceRefs, and evidenceRefs was empty. Derive the citeable set from the supplied facts at one place. Then keep the rejected response through retry and steering: `plan_judgments.py:236` retained it conditionally, and steering 214 carried rejectedResponseEventId=null, so the planner could not recover. Event 187 also reported convergence=true with zero review credits; fix that if it falls out of the same owner, otherwise name it in the report.

Do not fix the interpreter-discovery detour (events 84-114) here.

Time-box: about 60 net src lines. Prefer deleting. If it needs more, stop and explain.

PROOF: extend an existing golden journey with one fault twin: the first reviewer's provider fails with the authentication error seen in this run; the journey still reaches B with an honest tier and no user question. Use outcome-only assertions. Run ONLY the small journey, not the fast gate, because the lead is gating on this machine:
  python -B -c "import sys; from pathlib import Path; from tests.python.core.test_golden_path import small_plan_golden; small_plan_golden(Path(sys.argv[1]))" C:/seldon/tests/review1/small-plan
using ~/codex-harness/.venv/Scripts/python.exe, with PYTHONPATH=<this tree>/src;<this tree> and TEMP/TMP set to C:/seldon/tests/review1. Remove that small-plan folder before each attempt. Put the journey wherever it is reached by this command.

DELIVER in ~/codex-harness/work/lanes: stage-review1.patch (git diff against base, include new files), stage-review1.patch.sha256, stage-review1-report.md (at most 12 lines: TRIAGE BUG|DESIGN, siblings, the two rules, net src/tests lines, journey result with seconds).
