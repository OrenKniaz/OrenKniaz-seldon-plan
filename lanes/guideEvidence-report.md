TRIAGE: FAULT SELDON | BUG | guide execution evidence wiring.
Mis-trace: guide.py ignored retained JSON-fenced argv; judgment.trace(tryItGuide) supplied the resulting [] wrapper/path probe as PRODUCT behaviour (confirmed read-only main m01 and thin c01).
Fix: one parser for json/argv; WAVE-VERIFY records each real argv directly, retaining exit/output/artifacts/images; guide:paths remains a code check excluded from PRODUCT. No prompt rules, new validators or caps.
Siblings: ordinary PRODUCT criteria and FLOW trace canonical plan checks, not this guide parser; no matching mis-trace found there.
Src lines thin f2ffb6e: 4430 -> 4429; main b95331c: 4943 -> 4942 (both +12/-13, net -1).
Journeys: extended existing check-kit guide/WAVE-VERIFY flow; scripted PRODUCT requires actual argv, successful exit/output/artifacts plus browser images to reach C; broken guide yields a real check gap. Collections thin 19 -> 20, main 119 -> 120.
Evidence: relevant base RED 1 failed/13.01s; narrow check_kit_golden 3 passed/42.77s (guideEvidence-5), main check_kit_journey 3 passed/46.10s (-7); thin golden once 20 passed/307.63s (-8), responsive throughout.
Delivery: guideEvidence.patch is diff against thin base; it does NOT apply to main. guideEvidence-main.patch was made against fresh git archive b95331c at C:/seldon/tests/guideEvidence-main; main apply --check passes, thin reverse-check passes; changed Python parses.
Limits: no real providers, commits or new dependencies; main full golden unrun. Ruff reports inherited B905 in judgment.py, reproduced on base and recorded in T-183; no unrelated lint fix.
Next: lead reviews/lands the appropriate patch and validates real ShelfLife runs; T-183 stays in_progress pending landing and validation.
