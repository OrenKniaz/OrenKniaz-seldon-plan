LANE stage-eligible1. Worktree: ~/codex-harness/work/lanes/stage-eligible1. Temp files only under C:/seldon/tests/eligible1.
Read CHARTER.md first, then AGENTS.md. Rules: no unit tests (behaviour-only golden journeys); no lane-local SHAs; do not commit.

PROBLEM: real round 26. The LLM sized ShelfLife "medium" and wrote ordinary success measures into the vision's `metrics` and `stopConditions` (for example "exactly one of two concurrent consumes succeeds", "acceptance remains incomplete if ..."). `core/semantic_schema.py::small_plan` refuses any vision with those fields, so a normal closed-loop greenfield app took the old contract: 0 of 20 question schemas contained buildBead, and it stalled in trace. This is the third real run that never reached the five-kind plan. Run: C:/seldon/runs/fight-1/seldon/20261109T103417-a6d1a4-001-shelflife.

GOAL: a normal greenfield app reaches the five-kind plan even when its vision states success measures. Owner decision: the thin path must actually run. Earlier review constraint still stands: brownfield (baseline) and genuinely open-loop work (iterate toward a measured target) keep the fuller contract.

FIRST find out what makes work genuinely open-loop in this codebase: which consumer needs metric/stop-condition/iteration nodes, and how the vision question describes metrics/stopConditions. Then apply ONE rule at the existing owner. The likely shape: authored metric/iteration/stop-condition nodes or an existing explicit open-loop signal decide, and descriptive vision fields do not. If vision metrics/stopConditions then force a later consumer to demand nodes the five-kind schema cannot author, fix that consumer with the same rule so there is no dead end; the five-kind plan may carry them as vision meaning. Do not ask the LLM a new question unless no existing signal exists, and if you must, say so first in the report. Check the sizing/vision prompt: if it tells the LLM these fields imply iteration, make the wording match the rule.

Net src lines <=0 or very close. Time-box: if this needs more than about 40 net src lines, stop and explain in the report.

PROOF: make the `small_plan_golden(size="medium")` vision state metrics and stopConditions like ShelfLife's, still reaching the five-kind contract and B. One assertion that a dream with authored open-loop work or a baseline keeps the fuller contract, only if not already proven. Run only: bash ~/codex-harness/work/lanes/fast-gate.sh <this tree> eligible1

DELIVER in ~/codex-harness/work/lanes: stage-eligible1.patch (git diff against base, include new files), stage-eligible1.patch.sha256, stage-eligible1-report.md (at most 12 lines: TRIAGE BUG|DESIGN, siblings, the rule, net src/tests lines, fast-gate result with seconds).
