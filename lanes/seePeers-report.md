TRIAGE FAULT SELDON
DESIGN: Consumers see every contract of consumed providers; the guide proves known contracts and leaves unseen forms to their owner.
removed: Named-contract-only visibility, blind walkthrough guessing, and machine-directed guide prose; no new state, labels, validators or caps.
files: src/seldon/architecture.py, src/seldon/plan.py, tests/seldon/test_journey.py.
src lines: all 4263 -> 4263; Python 4184 -> 4184 (net 0).
proof: Existing contract journey RED on missing sibling JSON agreement (7.04s), GREEN to scripted C without fixup/rework (9.58s); unrelated unit excludes provider contracts; test cases unchanged.
gate: bash scripts/gate.sh seePeers, venv first PATH, once: 39 passed/0 skipped in 466.71s; no post-gate edits or >5min test; judgeOnce gate overlapped after ours started.
base/next: snapshot25f2437 tree equals f69003d (e67ebce7521d14fc13fbd55f6614066d2ad1a1cc); T-192 awaits lead landing/native validation; no commit, real providers or .env reads.
