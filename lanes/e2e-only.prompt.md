Lane E2E-ONLY (Seldon; this folder = main 0cac4ef + own git). Owner decision (Oren, binding, repeated): NO unit tests. Proof = stub golden-path E2E, user journeys, and real farm runs.
Do:
1. Delete every test file under tests/python except: core/test_golden_path.py, core/test_approval_v2_journey.py, core/test_module_size.py and test_suite_budget.py (structural guards, <1s), plus conftest.py and support modules/fixtures that these still import. Delete support modules/fixtures nothing imports anymore.
2. Rewrite tests/python/test_suite_budget.py into one rule: only the allowed files above may contain tests; any new test_*.py file fails with the message "Seldon allows only golden-path/journey E2E tests (owner rule)". Ceilings = the new actual counts.
3. If a deleted test covered a real user-visible path the golden path does not exercise, do NOT port it; list it (<=10 lines) in the report as a candidate golden-path scenario.
4. Remove pytest markers/config that only served deleted tests (e.g. fast marker) from pyproject.toml if unused.
Do NOT run any test except: bash C:/Users/oren/codex-harness/work/lanes/golden-gate.sh <this folder> lane  (golden CLI+web, ~4 min), and python -m pytest tests/python/test_suite_budget.py tests/python/core/test_module_size.py -q (structural, seconds). No other pytest invocation at all. Timebox 45 min, effort medium.
Report <=12 lines ../e2e-only-report.md: files deleted (count), tests before/after, lines removed, golden result, candidate scenarios. Exact ../e2e-only.patch + sha256. No pushes. Write only here, C:\Users\oren\t\m, ../ report/patch.
