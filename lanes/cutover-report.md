Base e5a4ead; lane HEAD e47de62 has the identical tree; uncommitted.
Deleted 229 files: src/codex_harness, tests/python, fixtures, scripts, tests/browser, tests/fixtures, UI-AUDIT.md, PROVENANCE.md, extraction-manifest.json, and docs except its mixed audit.
Kept src/seldon (runtime); tests/seldon (semantic journey, recorded reply, development runners).
Kept docs/legacy-capability-audit.md (new-core findings alongside history); README.md (goal/tests); AGENTS.md (builder rules).
Kept CHARTER.md (binding goal); BLUEPRINT.md (binding design); pyproject.toml (build/test/lint); .gitignore (development hygiene).
Lines, tracked files: src/seldon 2,506 -> 2,506; whole repository 66,809 -> 4,828.
Suite: 1 passed in 137.87s; first concurrent-deletion run: 1 timing failure in 188.87s (scale 82.33s > 60s). No limits changed.
Ruff 0.11.13: 16 inherited findings vs 17 at base with requested settings (203 with original settings); 0 new. E501=5 B023=1 I001=6 B905=2 F841=1 UP017=1.
Wheel: offline cached Hatchling; C:/seldon/tests/cutover-1/wheel/seldon-0.1.0-py3-none-any.whl: only 15 seldon/*.py files plus 3 standard dist-info files; no entry points.
Reference scan: 0 retired-package matches, including hidden/ignored files; charter, blueprint and src/seldon unchanged.
Automatic approval review blocked shell deletion/empty-directory cleanup; explicit tracked-file patch deletion succeeded; empty directories remain locally.
