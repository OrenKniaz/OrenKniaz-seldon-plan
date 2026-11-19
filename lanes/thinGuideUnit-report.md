TRIAGE FAULT SELDON, DESIGN — the reader guide is now an ordinary last unit; its declared checks own walkthrough execution.
DESIGN: work/ladder/design-review/guide-walkthrough-fable-2026-11-16.md (Fable 11-16), implemented on base 149f7ea100659b535e5c9ea6553a7c498ccb90a2.
Removed guide.py, prose fence/path parsing, format refusals and guide-specific proof/trace/owner branches; kept WAVE-VERIFY unchanged and GUIDE_WORK verbatim.
Files: src/seldon/{guide,proof,judgment,run,plan,fixups}.py; tests/seldon/{test_journey,kit_journey,test_proof}.py (last fixes inherited screenshot wiring).
Src/seldon lines: 4316 -> 4269 (-47); journey cases: 24 -> 23 (duplicate server case consolidated). Server fence reaches SCRIPTED_C; ordering, sources, screenshots and guide failure owner proven.
Env: .venv/Scripts first PATH; PYTHONPATH="src;tests/seldon". Full: python -m pytest -x -q tests/seldon -p no:cacheprovider --basetemp=C:/seldon/tests/thinGuideUnit-7/pytest: 19 passed, 1 stale-test failure, 418.62s.
After test-only fix, same flags with tests/seldon/test_journey.py -k "hermetic or guide_walkthrough or check_kit_golden", basetemp thinGuideUnit-8/pytest: 4 passed, 80.03s; base -5 guide journey RED 16.83s at ordering. Composite proof; full suite not rerun.
T-185 row updated; tracking validator, Python parse, diff and reverse-apply checks pass. Lead review/landing + real cohort pending; no providers, gate.sh, commit, .env reads or >5min hang.
