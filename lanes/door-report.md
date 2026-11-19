TRIAGE FAULT SELDON
DESIGN: C20/R17 file-only atomic answers preserve live work; ask shows question, label/means options and Other.
Removed: pause-on-answer, stdin response delivery, misleading WAITING for a live controller with a request.
Files: src/seldon/frontdoor.py; tests/seldon/test_front_door.py; post-gate stale assertion only in test_journey.py.
Src Python: 4199 -> 4215; frontdoor 239 -> 255; cases 44 -> 46. Base d17135f; named 2946398 unavailable.
Gate door ONCE: 45 passed/1 stale-status failure, 605.08s; test-only fix then affected journey 1 passed/16.84s; no re-gate.
Evidence: base RED; live worker finishes without reopen, stale ID refused, crash replay applies once, legacy requests pass; composite final, longest gate test 125.87s.
Next: lead landing and sibling R17 producer/polling integration; framed ask uses handoff fixture. No real providers, commit or .env reads.
