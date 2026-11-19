TRIAGE FAULT TEST + BUG
Root cause: outside-contract moves the consumer to area-3; the native stub hardcoded unit-002 as consumer and unit-003 as unrelated, so both assert before emitting a terminal answer.
Fix: select the native consumer from Contracts consumed; remove stale fresh-brief contract-presence assertion; require the named contract to remain outside Crossed contracts. Provider-routing and outcome assertions retained; no source changes.
Files: tests/seldon/test_journey.py (+3/-2); mergeFix.patch.
Proof: focused judge_once (all 5) + thin_plan (all 19): 24 passed/8 deselected, 256.46s; sole bash scripts/gate.sh mergeFix: 44 passed, 374.09s, exit0 (case count unchanged).
Base: snapshot36bba61 tree d34889b95c72c6b38995b81fcd9b8bde9413cd78 equals canonical915cb06. No real providers, commits, .env reads or >5min hang; temp under mergeFix-1/-2 (gate root junction).
