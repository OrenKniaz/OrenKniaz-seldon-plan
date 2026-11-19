TRIAGE FAULT SELDON DESIGN — Quiet Bench was estimated at weeks for one agent (T-227).
Root cause in `src/seldon/questions.py:56` and `:261` on 6433526. The scale lacked anchors and the local noise-filter example modeled Medium.
Fix the ALIGN coaching with plain single-agent effort anchors and ask what would increase the estimate. The owner still decides at A.
Files `src/seldon/questions.py`, `tests/seldon/test_journey.py`, `tests/seldon/fixtures/quietbench-q01-align.json`.
Tracked src/seldon lines 5,933 → 5,938. Patch applies to 6433526, whose tree matches the lane snapshot.
Strict recorded-facts journey failed on base and passed on the candidate. It displays Medium with its reason and carries the Micro override through reopen into ARCHITECT. All 27 cold imports passed.
Sole bare gate `bash scripts/gate.sh sizeCalib` passed 102 tests in 332.64 s with one added journey.
Real Terra estimation quality remains unverified. No provider calls or commit.
