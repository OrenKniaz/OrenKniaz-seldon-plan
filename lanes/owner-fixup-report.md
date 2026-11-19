T-118 owner-fixup; clean base 548086a (9eddbb9 golden-only); uncommitted.
Source net lines: src/seldon/fixups.py +30; units.py +2; scheduler.py +1; states.py 0 (+1/-1); store.py +3.
Journey net lines: tests/seldon/test_fixups.py +53; test_journey.py +2. Total: 7 files, +102/-11 (net +91).
DONE sibling discovery -> owned_scope fixup -> fresh-candidate guide -> SCRIPTED_C, guide recoveries 0; own-scope discovery -> FAILED/INCOMPLETE, recoveries 2.
Gate: bash scripts/gate.sh ofix-4: 14 passed in 234.95s (base 14; two added golden journey cases); retained timing assertions and recorded replays unchanged.
RED ofix-2: base reproduces guide exhaustion, 13 passed/1 failed in 65.65s. ofix-3: owner routed but strengthened check wrongly preserved, 13/1 in 117.99s; fixed by existing flow reproof rule.
Typed owner waits persist; pre-handoff saved units default to no owner wait. Existing owner recovery limits bound exhaustion.
Lead decisions touched: none. No CHARTER/BLUEPRINT edits, dependencies, commits or real provider calls; diff check and patch reverse-apply check passed.
Remaining: lead review/landing and authorized real cohort qualification; T-118 stays in_progress, no product acceptance claimed.
