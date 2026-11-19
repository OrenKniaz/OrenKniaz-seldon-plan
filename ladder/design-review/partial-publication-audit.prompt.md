Read-only design audit (Sol high). Do not run tests or edit; final message = report. Do not run long commands.

Repo: C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc (Seldon main candidate e2daa3f = 4e2c055 + stage 2e). Charter: CHARTER.md.

Pattern (5 host reds in 2 days share it): a reader observes an owner's state between two writes that together mean one fact.
- Today: planner_candidate.py ~434-438 writes run record status=VALIDATED inside a transaction, THEN deliver() (candidate_delivery.py ~117) writes run["delivery"]; tests/python/core/acceptance_support.py:454 read VALIDATED without delivery -> KeyError 'delivery'.
- recov1 reds: monitor released quiescence before publishing outcome; launch certainty before entry marker; ordinal-shifted twin (work/ladder/design-review/recovery-flake-diagnosis.md, recov1-host4-diag.md, state-machines-audit.md, truth-dupes-audit.md).

Answer concisely:
1. Inventory every place one logical fact is published by 2+ separate writes that other readers (run_loop, planner status/views, cockpit/operator HTTP, MCP tools, acceptance, recovery, tests' observers) can observe in between. Table: fact | writes (file:line) | readers that can see the gap | consequence (product-visible wrong claim vs test-only).
2. TRIAGE BUG|DESIGN for the class.
3. The ONE simplest rule that removes the class (e.g. "a fact is visible only when its single terminal write lands; readers read only owner-published terminal facts") with LLM-or-CODE owner row, and where to apply it first (rank by product impact). Estimated line delta (aim net-negative).
4. Which instances are test observers reading raw intermediate records instead of the owner's published outcome (fix = read the owner), vs product gaps.
