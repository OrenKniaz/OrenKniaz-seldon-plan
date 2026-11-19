TRIAGE FAULT SELDON — dropped defect handoff charged the finder.
DESIGN: Fable 11-16 defect-to-owner implemented, including the exact shared WORK/COACH/refusal sentence; no new state, questions, validators or caps.
Removed: wait-owner/UnitRow.waitingFor, forced writer routing, fixups seen/charged bookkeeping, write-only discovery record, free-text owners and discovery-question COACH detour.
Files: src/seldon/{plan,units,proof,fixups,questions,schema,gitwork,states,store,scheduler,decisions}.py; tests/seldon/test_journey.py.
Src lines: 4193 -> 4196 (+3, about flat); journey cases: 34 -> 37.
Gate: bash scripts/gate.sh defectOwner; .venv/Scripts first on PATH; 37 passed in 492.22s, exit 0; run once, no post-gate fixes.
Proof: new journey reproduces base finder wait (RED); done/question handoffs reach scripted C via B; ineffective B fix reaches WAITING and reopens/resumes; A files preserved. Focused 3 passed; full gate includes all three.
Base: clean snapshot 53e7cd9 titled base main 1f2d6df (original object unavailable). No commits, real providers or .env reads; T-187 stays in_progress pending lead landing and authorized Terra ShelfLife validation.
