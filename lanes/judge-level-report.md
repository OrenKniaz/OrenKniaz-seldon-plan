Base fb74470 (same tree as lane HEAD 9df3379); no commit.
Source lines: judgment.py 191->180; plan.py 151->173; questions.py 246->255; schema.py 94->93; net +19.
Journey lines: tests/seldon/test_journey.py 835->858; no new modules or dependencies.
Removed quality judgment flag and code_quality auto-satisfaction; shared trace supplies final files; unit JUDGE stays local.
Golden: 1 test / 38 journeys vs base 1 / 38, PASS 165.89s; scale50 67.19s; timing assertions unchanged.
Largest question bytes, 1/50 units: WORK 3074/3074; JUDGE 5537/5537; DEMO 4347/4347; PRODUCT 4263/4263.
Other kinds, 1/50: ALIGN 3272/3272; PLAN 7208/7208; REVIEW 4979/39885 (existing whole-plan review).
Recorded-judgment size journey passed: DEMO 28306, PRODUCT 46711 bytes; file text supplied once.
Missing-owner criterion trace gets a REVIEW gap, repairs then scripted C; each criterion gets one initial PRODUCT question on the final candidate.
Rule: no flaw found; DEMO-FACTS/PRODUCT-FACTS preserved. No real provider calls or real-provider acceptance.
