P10 bird's-eye review of Seldon's M2 PLANNING design (ARCHITECT -> per-area DETAIL -> merge -> REVIEW -> B). Read-only. At most 30 lines, plain words. Three DESIGN faults in planning surfaced today from the first real runs; P10 (Blueprint v1.5 section 7) stops planning lanes until the shape is reviewed.

Read: ~/codex-harness/work/sprint-20261027/semantic-cc/CHARTER.md v1.7 (section 4 planning by area; C9; C12) and BLUEPRINT.md v1.5 (3.1 records; 3.3 planning fans out by area; R3; R4 contracts before parallel work: "Consumers receive its text in their brief. A unit never depends on another unit's files without a contract or a dependency edge"; R6 scopes; R10). Code on main 2073b1d: src/seldon/architecture.py, detail.py, plan.py (merge, prerequisites, validate), obligations.py, questions.py (architect_brief, detail_brief). Pending lane (not landed): ~/codex-harness/work/lanes/detail-repair-20261113 and its report detail-repair-report.md. Real recordings: C:/seldon/tests/m1/foundation-2073b1d-c01 and -c02 (calls/*/question.json, answer.txt: ARCHITECT and DETAIL).

Faults:
1. T-107: a merged-plan defect ended the run instead of being corrected (lane detail-repair makes it per-area exact-fix + one targeted re-ask).
2. All six recorded DETAIL answers put their checks (checks/...) outside ARCHITECT's literal area scopes; the scope rules reject them.
3. Both recordings have contract cycles (area A provides to B, B provides to A, e.g. page shell vs scripts). Lane 1 made a contract's provider a scheduling prerequisite (plan.prerequisites), so cycles cannot schedule.

Answer:
1. Root cause in one sentence: what about the planning shape produces these?
2. The simplest correct rules, holding at 100 units and 10 waves: (a) where check files live and who owns their scope (ARCHITECT areas include their check subtree? code-assigned per-area check scope? DETAIL may extend inside area?); (b) is a contract an ordering (provider first) or only a shared text agreement that enables parallel work, with real file dependencies as explicit edges; how cycles are handled; (c) what ARCHITECT must and must not decide vs DETAIL. Say what to delete.
3. Is the detail-repair lane's rule (per-area exact-fix + one targeted re-ask, then actionable stop) right?
4. Must not do.
