Base f8c8081; A+C: 10 files, +399/-120, net +279; no commit.
Files: src/seldon/{architecture,fixups,plan,plan_review,questions,schema,units}.py; tests/seldon/{test_architect,test_fixups,test_journey}.py.
Deleted: path/matches handoff lookup, one-handoff cap, coverage-derived check repair, checks_for mode flip, recovery charge on fixup admission, duplicated dependency instructions in owner lookup.
Repair consumes owner handles, waits for the DONE owner, resets fixup recoveries, proves local GREEN at P and reruns the failing wave check at INTEGRATING; oversized WORK/JUDGE failures include exact bytes and retry.
Journeys: blocked sibling owner -> scoped repair -> blocked unit C; own/repeated handoffs bounded; three-unit wave reopens only owner; two-spent-recovery owner completes fresh fixup; strengthened check completes on integrated product; passing fault twins.
Golden/FLOW/crash-reopen/recorded B-C replays and original 1/50 size/timing assertions passed; 14 passed vs base 14; no skips.
Gate: bash scripts/gate.sh orep-6, venv Scripts first on PATH; 296.55s suite / 297.82s wall.
Earlier REDs: stale admission-count expectations, invalid overlap fixture and T-123 WORK growth corrected; orep-5 hit a nonstarted 350ms bootstrap fault (138 receipts cleanup verified); unchanged orep-6 passed.
Protected source, CHARTER/BLUEPRINT and raw replay JSON unchanged; no dependencies or real providers. Hermetic observer lane remains separate; live acceptance unperformed.
