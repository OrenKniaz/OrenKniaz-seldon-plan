LANE detail-repair (tickets T-107 and T-105). Worktree ~/codex-harness/work/lanes/detail-repair-20261113 (Seldon main 2073b1d). Temp only under C:/seldon/tests/drep-<n>. Do not commit. No new dependencies. Do not edit CHARTER.md or BLUEPRINT.md. Behaviour-only journeys. No real provider calls. Tickets per work/ladder/TRACKING.md.
Read CHARTER.md v1.7 (section 4 planning by area; I2/I4 never refuse what can be repaired), BLUEPRINT.md v1.5 (3.3; R3; R4; R12), then src/seldon (detail.py, architecture.py, plan.py, run.py, questions.py) and tests/seldon.

FAILURE (both first real runs of ARCHITECT/DETAIL ended INCOMPLETE before execution, no repair attempted):
- C:/seldon/tests/m1/foundation-2073b1d-c01: merge refused "hello.js: a file prerequisite needs one other planned writer" (a unit listed a cross-unit read of a file no other unit writes).
- C:/seldon/tests/m1/foundation-2073b1d-c02: merge refused "Unit judgment needs a local semantic check for [an integration requirement]" (a requirement assigned to a unit that owns no local check for it).
Read their calls (ARCHITECT, DETAIL question.json/answer.txt) first and say for each which area produced the defect.

RULE (decided by the lead; if wrong, stop and say where): a merge-time defect is a correction, not a stop.
1. Every validation that concerns only one area's own units, requirements, checks, reads and scopes runs inside that area's DETAIL answer check, so the existing exact-fix retry corrects it there (e.g. a read must name another unit's planned file; every requirement a unit owns has a local check in that unit's checkPaths unless it is explicitly a cross-unit requirement owned at wave level per the existing assigned() rule).
2. A validation that needs several areas (cross-area reads, contract endpoints, scope overlaps between areas) names the areas owning the offending records; code re-asks only those DETAIL questions once with the exact error and the minimal facts of the other side (its contract text or the owning unit's planned path), then merges again.
3. A cross-area need no contract covers is the existing contract gap to ARCHITECT (once).
4. Only after these bounded steps does the run stop, naming the defect and the area (INCOMPLETE with an actionable reason).
5. T-105: add one gate script scripts/gate.sh in the repo (PYTHONPATH=src;tests/seldon with Windows separators as the landing chain uses, TEMP/TMP under C:/seldon/tests/<tag>, pytest tests/seldon -q -p no:cacheprovider --basetemp=...), use it for your own gate, and replace remaining "from tests.seldon..." imports with plain module imports (test_fixups.py, test_journey.py) so lane and landing gates are identical.
JOURNEYS (outcome only): replay both recorded failures (their recorded DETAIL answers as scripted answers) and show each is corrected by one re-ask and reaches B; a defect that persists after the re-ask stops with an actionable reason naming the area; an in-area defect is fixed by the exact-fix retry without a re-ask; question sizes unchanged.
LEAD DECISIONS THAT MUST SURVIVE: everything on main; timing asserts unchanged; suite under 180 s quiet if achievable (report).
DELIVER in ~/codex-harness/work/lanes: detail-repair.patch (all new files), detail-repair-report.md at most 10 lines: which area produced each defect; what moved into per-area validation; journeys and seconds; gate script; anything wrong.
