LANE stage-medium1. Worktree: C:/Users/oren/codex-harness/work/lanes/stage-medium1 (Seldon at 34d141e). Temp files only under C:/seldon/tests/medium1.
Read CHARTER.md first, then AGENTS.md. Rules: no unit tests (behaviour-only golden journeys); no lane-local SHAs; do not commit; do not run the slow suite.

OWNER DECISION (Oren, 2026-11-09): the five-kind plan (vision, feature, requirement, test, bead; one strict outline-and-fill question; contracts bead + build bead) also covers MEDIUM apps. Round 25 sized ShelfLife "medium", took the old contract, and stalled in trace; the thin path has never run for real.

CHANGE - one rule, one owner:
- `core/semantic_schema.py::small_plan` is the eligibility rule: size in tiny/small/medium, and still no metrics/stop conditions/baseline/iteration kinds. Keep large and brownfield/open-loop on the existing contract.
- `core/graph.py:246` duplicates the size test for the two-bead check. Make it consult the same rule instead of its own size set, so eligibility is stated once. Check for any other copy of this decision and fold it in.
- Review depth stays by size: DO NOT change `core/plan_reviews.py:468` (rounds) or `core/review_packets.py:185` unless you find medium would break there; if so, say so in the report.
- Rename `small_plan` only if it is cheap and clearly better; a misleading name is worse than a one-line rename, but do not widen the diff otherwise.
- Net src lines must be <=0 or very close. If other code becomes dead because medium no longer reaches it, delete it.

KNOWN LIMIT: one build bead for medium apps. Do not add more bead slots in this lane.

PROOF: `small_plan_golden` in tests/python/core/test_golden_path.py already takes size= and runs size="medium" as "shared-readiness" (line ~5461). Make the medium case prove the behaviour: a medium greenfield closed-loop dream gets the five-kind contract and reaches B, with medium's review depth. Add one assertion that a large dream or a baseline still takes the existing contract, only if not already proven. Run only: `bash C:/Users/oren/codex-harness/work/lanes/fast-gate.sh <this tree> medium1`.

DELIVER in C:/Users/oren/codex-harness/work/lanes: stage-medium1.patch (git diff against base, include new files), stage-medium1.patch.sha256, stage-medium1-report.md (at most 15 lines: TRIAGE BUG|DESIGN, sibling cases checked, what changed, net src/tests lines, fast-gate result).
