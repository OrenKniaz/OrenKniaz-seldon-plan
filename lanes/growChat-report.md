TRIAGE FAULT SELDON + DESIGN · T-214
Root cause `src/seldon/frontdoor.py:64,136` reads one menu and redelivers the same carrier while its request stays open.
Saved round groups expose delta, defaults, size override and Other. Request and reply IDs carry exact picks or words through reconnect.
Lines `src/seldon/frontdoor.py` 255 → 334, `tests/seldon/test_front_door.py` 294 → 444. Patch applies to `0bf6cb9`.
RED public MCP state failed on a grouped request. GREEN the r10/r170 controls and counterfactual grouped reply passed with a loop contract twin.
Lane gate `bash scripts/gate.sh growChat` passed 84 tests in 337.43 s with strict stubs. All 27 modules cold-imported. Formatting reflow preserved both ASTs.
Next proof is growLoop's real producer/consumer journey and merged gate. T-214 records the receipt contract and fresh-ALIGN switch ownership.
