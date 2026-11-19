LANE stage-bound1. Worktree: ~/codex-harness/work/lanes/stage-bound1 (Seldon at local 7273857, not yet on main). Temp files only under C:/seldon/tests/bound1. You cannot delete folders, so use a new folder name for each retry.
Read CHARTER.md first, then AGENTS.md. Rules: no unit tests (behaviour-only golden journeys); no lane-local SHAs; do not commit.

CONTEXT: real round 33 (run C:/seldon/runs/fight-1/seldon/20261109T190951-795786-001-shelflife, diagnosis ~/codex-harness/work/fight-1/r33-diagnosis.md). Ordinary test commands and CODE-bound repair sources now work on a real run. But the app worker has never launched in any real run. The tests-first stage is the bottleneck. In priority order:

0. The lead's fast gate is red on this tree: ~/codex-harness/work/sprint-20261027/golden-quiet6.log, `test_golden_path[web]`, `'validation' == 'contracts'`. Find out whether the assertion or the product is wrong after red1/m2 and fix the right one. Do not weaken what it protects.

1. BOUND THE TESTS-FIRST STAGE. The contracts bead failed on missing Playwright (284/302), browser startup (337), and LOCALAPPDATA (372), then replanning tried to consolidate beads and could not (398, 467/469). Delivery lead's decision, under the standing never-block-delivery rule: after the existing bound of two automatic contracts repairs, ANY still-unadmitted RED (not just inconclusive) releases the build bead with the honest weakRed label. No replanning of bead structure for this. Integrated GREEN and validation still gate C unchanged, so the build worker must still make the tests pass. All-skipped runs still do not count as RED; if the bound is exhausted on them, release with weakRed as well.

2. BOUNDED QUESTION PAYLOADS. At 691, context.observation.sourceRefs serialized to about 1.17M characters, and the provider refused 1,566,824 > 1,048,576 before the turn started. Rule: CODE gives each semantic call a bounded projection of current facts; historical evidence is carried by ID and revision, and its payload is never embedded recursively. Apply at the single packet owner, so every question is covered. Do not add per-question special cases.

3. NO EXTRA USER TOUCH BEFORE B. 160 -> 161: plan review found no material defect, findings [], but held on "unverified" browser availability, and Seldon asked the user for direction. Unverified feasibility with no finding does not hold the plan: it proceeds to B, with the uncertainty stated. Users are asked only A, B, C or a genuine scope decision.

4. Add to executionSetup in run_context.py the observed browser tooling on this machine (whether node and Playwright can actually run), so the planner does not write tests that cannot run. One observed fact, no new machinery.

Report only, do not fix: canonical bead restructuring during replan.

Prefer deleting. Stop and explain if this needs more than about 60 net src lines.

PROOF: extend existing journeys: contracts repairs exhausted, build bead still launches with weakRed and no user question; a question whose evidence history is huge stays under a fixed bound and still cites by ID. Outcome-only. Run ONLY: ~/codex-harness/.venv/Scripts/python.exe -B -c "import sys; from pathlib import Path; from tests.python.core.test_golden_path import small_plan_golden; small_plan_golden(Path(sys.argv[1]))" C:/seldon/tests/bound1/small-plan-1 with PYTHONPATH=<this tree>/src;<this tree> and TEMP/TMP=C:/seldon/tests/bound1. The lead runs the web leg.

DELIVER in ~/codex-harness/work/lanes: stage-bound1.patch (git diff against base, include new files), stage-bound1.patch.sha256, stage-bound1-report.md (at most 12 lines: TRIAGE BUG|DESIGN, siblings, the rules as applied, what was deleted, net src/tests lines, journey result with seconds).
