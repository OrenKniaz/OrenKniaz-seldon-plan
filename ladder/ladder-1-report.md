TRIAGE: DESIGN — farm coupled scheduling, paths, verification and fake outcomes to one fixed suite; sibling cases are every smaller cohort and server-backed brief. Shared hooks now live in farm/verify.
Files: ladder.py, oracle.py, README.md, STATE.json, BLOCKERS.md, PROMOTIONS.md, five dry-fixtures, and 30 briefs (L0/L1/L2/L3 = 5/14/8/3).
Farm changes: dynamic brief rotation, injectable run/slot/evidence roots, bounded dispatch callbacks/STOP, run budgets, selectable fake scenarios/artifacts; verify.py adds scored external Python oracles.
Reuses farm cohort/run_one/install_build/product verification/failure_code; existing run-farm briefs unchanged; ShelfLife imports fight-1/oracle.py unchanged with a >=36/40 gate and redirected evidence roots.
Farm smoke ONCE: farm.py run --dry-run --briefs 5 --parallel 2 — SELF-TEST PASS; receipts ../run-farm/dry-runs/20261104T123445Z-398948/.
Ladder smoke: ladder.py run --dry-run — DRY-RUN PASS; evidence dry-runs/dry-03133e94d81e/dry-run-evidence.json.
Proved real fake-artifact verification, SHA A->B resetting window 1->0, blocker 20261104T123756Z-8182e8-001-hello with receipts, then two full 5/5 clean cohorts promoting L0->L1.
Real STATE remains L0/0/no installed SHA; dry STATE/BLOCKERS/PROMOTIONS are isolated; run receipts C:/seldon/runs/ladder/L0/dry-03133e94d81e/; temp C:/seldon/tests/ladder-1/.
Real start: `& '~/codex-harness/.venv/Scripts/python.exe' '~/codex-harness/work/ladder/ladder.py' run --parallel 4`
STOP drains started jobs; lock excludes concurrent ladder runs; new SHAs reset the window and require a preceding-level spot gate above L0; Codex usage-limit errors remain reruns.
Next unproven transition: real L0; HTTP/UI/ShelfLife oracles are wired but unexecuted. No pytest, unit tests, real Codex, installation, farm loop start, or pushes.
