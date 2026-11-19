LANE stage-snapshot1. Worktree: C:/Users/oren/codex-harness/work/lanes/stage-snapshot1. Temp files only under C:/seldon/tests/snapshot1. You cannot delete folders, so use a new folder name for each retry.
Read CHARTER.md first, then AGENTS.md. Rules: no unit tests (behaviour-only golden journeys); no lane-local SHAs; do not commit.

CONTEXT: real round 30 (run C:/seldon/runs/fight-1/seldon/20261109T163744-35c37c-001-shelflife, diagnosis C:/Users/oren/codex-harness/work/fight-1/r30-diagnosis.md). Both plan reviewers finished positive with zero findings and B was displayed and answered, for the first time ever. Then B became stale (160-161) although 159 judged continuity positive (impact=HOW). Reviewer fallback at 115 changed the reviewer node, and reviews 125/130/131 bound node revisions alongside an outdated generated VISION.md. Snapshots 137/145 prove every canonical node unchanged; only the generated document revision and reviewer-node hash differ. Then both positive reviews became review-reuse questions (240/243), which supply hashes without before/after content, go inconclusive (269/318) and hold (270/319).

ONE RULE: gates and reviews bind to one immutable canonical semantic snapshot: the plan's meaning nodes. Generated Markdown projections and reviewer-selection/bookkeeping nodes cannot invalidate that snapshot. If the snapshot is unchanged, reviews and B stand: no staleness, and no reuse question at all. If it changed, a fresh review runs. Prefer deleting the review-reuse question and hash comparison over repairing them.

Siblings to close under the same rule if they fall out: 164 requests a review verdict while 172/181/190 demand content.nodes; valid file references rejected at 251/260/300/309. Name anything left over in the report.

Do not change what approval B means: a real meaning change must still invalidate it. Name the interrupted-effect quarantine at 150 in the report only.

Aim for net src <= 0, and this one should genuinely delete code. Stop and explain if it needs more than about 40 net lines.

PROOF: in the existing small journey, a reviewer provider falls back (changing the reviewer node) and generated docs regenerate; reviews stay valid and B commits with no extra question and no staleness. Also one outcome assertion that a real meaning edit after review does invalidate. Run ONLY: C:/Users/oren/codex-harness/.venv/Scripts/python.exe -B -c "import sys; from pathlib import Path; from tests.python.core.test_golden_path import small_plan_golden; small_plan_golden(Path(sys.argv[1]))" C:/seldon/tests/snapshot1/small-plan-1 with PYTHONPATH=<this tree>/src;<this tree> and TEMP/TMP=C:/seldon/tests/snapshot1.

DELIVER in C:/Users/oren/codex-harness/work/lanes: stage-snapshot1.patch (git diff against base, include new files), stage-snapshot1.patch.sha256, stage-snapshot1-report.md (at most 12 lines: TRIAGE BUG|DESIGN, siblings, the rule as applied, what was deleted, net src/tests lines, journey result with seconds).
