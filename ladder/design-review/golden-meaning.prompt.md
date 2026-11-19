READ-ONLY AUDIT (Sol HIGH) of Seldon's golden gate: ~/codex-harness/work/sprint-20261027/semantic-cc tests/python/core (test_golden_path.py, acceptance_support.py, mcp_planner_support.py, other test_*.py) and work/lanes/golden-gate.sh. Charter CHARTER.md v1.2; rules: no unit tests, outcome-only assertions, never delete coverage, never raise caps.
Context: the gate is our only automated gate and is now the delivery bottleneck: full CLI ~535-870s on host (target ≤600s), `shelflife-scenarios` journey 440-550s quiet and times out at its 600s cap under load; web ~180-280s. Logs: work/sprint-20261027/golden-*.log (timings print "golden <name>: seconds=").
Answer:
1) Per journey/case: what it uniquely proves (protected behavior + realistic regression it catches), wall time, and which other journey proves the same thing (overlap).
2) Assertions that would still pass if the feature were broken (tautological/weak) — file:line, why, and the outcome assertion that would replace it.
3) Where the time goes in shelflife-scenarios and the CLI gate: provider-boundary stub rounds, venv/wheel builds, HTTP servers, waits/polls, repeated setup. Rank by seconds saved.
4) A concrete plan to reach shelflife-scenarios ≤300s and full CLI ≤600s with ZERO lost unique coverage: shared fixtures, reuse of built wheels/venvs across journeys, merging overlapping journeys, removing duplicated proof. For each: seconds saved, coverage risk, files.
5) Note what Stage 2e (in flight: provider-boundary stubs, harness_chat ingress) will change in these journeys, so the gate-speed lane sequences after it.
Final message = full report, markdown, ≤120 lines. No edits/tests.
