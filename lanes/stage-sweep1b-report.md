CHARTER: serves C11/C14/C18/C26 — violates no I#; mechanical port onto Seldon a3f1e2e, no new behavior.
TRIAGE: BUG — port the independently approved owner fixes unchanged — siblings: SM#4, SM#5, SM#7, TD#4, TD#5.
CONFLICTS: keep fix17's planner_views.py deletions (file unchanged); retain lower ceilings TOTAL=32264, mcp_planner=286, planner_views=51, execution_assessments=557. run_setup.py/run_loop.py unchanged.
SIMPLEST: same consolidated selector/fact reads and golden twins; no new machinery. LLM-or-CODE: retained CODE (+canonical recorded facts; −semantic meaning remains with existing 1j).
PROD: +101/-143 (net -42) · TEST: +154/-2 (net +152); suite nodes 19→19; no new test files/nodes, raised caps or lane-local SHA pins.
GATE: bash ../golden-gate.sh . stage-sweep1b exit 0: 18 passed in 572.64s (9m32s); web 1 skipped/4.81s, UNVERIFIED in sandbox. Process-local read-only Git alternate supplies canonical historical objects; no trust/global changes.
REVIEW: mechanical port APPROVE, exact patch SHA256 7322e47e206bc36f066a11cc11690deec1d2a5553d2b40954c4a7b2b1ade1f13; original independent approval retained in stage-sweep1-reviewH.md.
ARTIFACTS: stage-sweep1b.patch vs lane base + stage-sweep1b.patch.sha256; no shared install/lane commit/push/screen control; CC host gate remains web/publication authority.
