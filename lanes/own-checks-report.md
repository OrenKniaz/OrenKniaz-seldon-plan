T-111: preserved the lead fix through shared plan.owned_scope in plan.merge and architecture.local_plan; area containment remains checked.
Removed planner scope-duplication guidance; kept worker instructions to write product and checks inside scope.
Added original UTF-8 ALIGN/ARCHITECT and four first DETAIL replies from foundation-5e3e40e-c01; both older recordings are unchanged.
All three replays reach REVIEW and approved B; scripted corrections address separate recorded defects, omit duplicate check scopes, and receive no correction for this defect; persisted units own every checkPath.
Gate: bash scripts/gate.sh owck-3, venv first on PATH: 14 passed in 223.94s (test count unchanged); owck-1/2 replay-response failures are recorded in T-111.
Delivered own-checks.patch (5 files, includes lead fix); tracking validated. No commit, dependencies or real provider calls; T-111 awaits lead landing and real-run qualification.
