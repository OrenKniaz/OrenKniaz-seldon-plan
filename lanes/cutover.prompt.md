LANE cutover (ticket T-24): Seldon becomes only the new core. Worktree C:/Users/oren/codex-harness/work/lanes/cutover-20261112 (main e5a4ead). Temp only under C:/seldon/tests/cutover-<n>. Do not commit. No new dependencies. Do not edit CHARTER.md or BLUEPRINT.md.

Read CHARTER.md, BLUEPRINT.md, AGENTS.md, then src/seldon and tests/seldon.

DO
1. Delete src/codex_harness and tests/python.
2. For every other top-level path (docs, fixtures, scripts, tests/browser, tests/fixtures, UI-AUDIT.md, PROVENANCE.md, extraction-manifest.json, README.md, AGENTS.md): if nothing in src/seldon or tests/seldon uses it and it describes or serves only the old core, delete it. If it is still used, keep it. README.md and AGENTS.md stay but drop text about the old core; README says in a few lines what Seldon is (CHARTER.md section 1) and how to run tests/seldon. Do not invent features.
3. pyproject.toml: wheel packages only src/seldon; remove every old [project.scripts] entry. Do not add a new CLI (the front door is milestone M4); say so in one README line. pytest testpaths = tests/seldon. Ruff: src = ["src","tests/seldon"], line-length 110.
4. tests/seldon/test_journey.py: remove the dead `if mode == "legacy-approved":` blocks.
5. Check: `grep -r codex_harness` over the tree finds nothing; `ruff check src/seldon tests/seldon` (report counts, fix only what this cutover caused); tests/seldon passes:
   PYTHONPATH="<lane>\src;<lane>\tests\seldon" python -B -m pytest tests/seldon -q -p no:cacheprovider --basetemp=C:/seldon/tests/cutover-<n>/bt   (mkdir the parent first)
   Build the wheel offline (`python -m pip wheel . --no-deps --no-build-isolation -w C:/seldon/tests/cutover-<n>/wheel` or hatchling if available) and list that it contains only seldon/.

DELIVER in C:/Users/oren/codex-harness/work/lanes: cutover.patch (git diff --binary against base, including deletions), cutover-report.md at most 12 lines: paths deleted and kept with one reason each for kept; lines before/after (src/seldon, whole repo); suite result and seconds; ruff result; wheel contents. No boilerplate.
