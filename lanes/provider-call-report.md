Base 6bf515c6ba6dc4e8bab3f9da92d2f50d68a2be3d; 4 files +39/-56, net -17 (source -21); 14 collected unchanged.
Files: src/seldon/providers.py, src/seldon/inference.py, tests/seldon/test_journey.py, tests/seldon/test_flow.py.
Deleted unused worker role, context/retries arguments, callable fallback/alias, duplicate command construction and broad denial-substring scan.
Search confirmed unused names; callable-only protocol was test-only in ask_flow, whose existing journey now follows invoke/timeout_for. No journey assertions changed.
Kept the reachable native app-server access-denied refusal permanent; arbitrary login/forbidden diagnostics no longer establish denial.
more_facts(neededFacts) supplies Requested facts for one bounded inline re-ask, then not judged; batch E caller migration and callback integration remain unproven.
bash scripts/gate.sh pcall-2: RED, 13 passed/1 failed, 191.35s pytest / 193.92s wall.
Unchanged timing rerun pcall-3: RED, 13 passed/1 failed, 247.23s pytest / 248.99s wall; no further rerun.
Both hit existing T-99: 350ms timeout twin missed bootstrap gate (executionStarted=false, timedOut=false, cleanupVerified=true), recovered, failed expected reason; load cause unproven. Full golden/scale unproven.
Patch whitespace/reverse-apply checks pass; T-99/T-124 and lane tracking updated. Next: process owner resolves startup deadline; E adopts callback. No commits, dependencies or real providers.
