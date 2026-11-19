T-126: base-only rule; uncommitted on d8083bc (base e699ff8 golden-only).
Files: src/seldon/{questions,fixups,gitwork}.py; tests/seldon/test_fixups.py; +98/-5, net +93.
Journey: python -m pytest -x -q tests/seldon -k test_blocked_owner_journeys -p no:cacheprovider --basetemp=C:/seldon/tests/bonly-2/pytest
Result: 1 passed, 14 deselected in 51.23s; .venv/Scripts first on PATH; all temp under bonly-1/bonly-2.
RED bonly-1: 48.78s, false u001 DONE->REWORK; GREEN preserves sibling repair and reaches SCRIPTED_C without false fixup.
Wrong: golden parallel stub (tests/seldon/test_journey.py) reads the old wave-fact label; lead must rename to "Wave checks to write, not run here" (outside four-file scope).
No gate.sh, real providers, commits or dependencies; T-126 remains in_progress until lead landing/validation; tracking validator passes.
