TRIAGE FAULT SELDON + BUG — T-208, checkIdentity on fd51495.
Root cause in src/seldon/plan.py:56–70. The latest WORK list replaced prior checks, reassigned their IDs and linked each check to every unit requirement.
Fix. Persist check IDs and declared requirement links across WORK reports. Named updates and retirements apply explicitly. WAVE-VERIFY and C use the active declarations.
Files. src/seldon/{plan,questions,run,schema,units}.py and tests/seldon/test_journey.py.
Source lines. src/seldon 4,898 → 4,946 (+48). Python 4,819 → 4,867.
Proof. Base RED for missing interface evidence. Both strict-schema journeys GREEN through scripted C. All 27 cold imports passed.
Gate. bash scripts/gate.sh checkIdentity once with venv first on PATH: 74 passed, 4 stale test assertions failed in 329.37s. Test-only correction: all 4 passed in 40.43s, no re-gate.
Patch applies to fd51495. Legacy records retain positional IDs and inferred links. Main landing and real-provider validation remain pending.
