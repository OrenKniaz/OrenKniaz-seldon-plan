# Lane leadPlausibleGuard (Sol 6.2 medium), Lead only: the guard judges as the owner's real users, and Seldon never re-asks to fix bookkeeping
Repo: this lane dir = main 989c515. Binding: CHARTER-LEAD.md, BLUEPRINT-LEAD.md v0.5 (bound proof: a must-fix quotes the B line it violates; anything else is a note). Rule: normalise, not refuse.
Read C:/seldon/tests/costWhy-0/REPORT.md first. ShelfLife s01 (C:/seldon/tests/m1/shelf-989c-*-s01) took 20 calls and 1.24M fresh tokens; plain takes 24k.
Two design causes:
1. **Gold-plating became must-fix.** The guard turned implausible extremes into a six-cycle repair chain: a 131,073-character name, 9,223,372,036,854,775,807 units, then the display, then precision. Real catches to keep:
   - a short malformed CSV row that aborts valid rows (the brief says "skipping invalid rows");
   - clipped text a household would see;
   - a delayed retry that deletes replacement stock.

   Rule: a must-fix is a failure that a person in the owner's story would plausibly hit, or that loses or corrupts their data, and it quotes B or the owner's words. An implausible extreme is a note, shown to the owner as an advisory ("no limit on name length; suggest 200"). It never starts a repair.

   Coach the guard as "the owner's real users on a normal week, plus the interruptions they would really cause", not as a fuzzer. Keep one end-to-end boundary check for each real input class.
2. **Bookkeeping re-asks.** Five repeated JUDGE calls followed "Credit only promises declared for this observation" validation errors. Each resubmitted the whole packet, costing 278k fresh tokens and producing no new findings. Rule: Seldon normalises the judge's answer locally. Drop the credits for undeclared promises with a visible note and keep the rest. Never re-ask the judge for a bookkeeping correction. Apply the same rule to any other schema-correction re-ask in JUDGE or RECEIPT that code can normalise: find them all, and delete the re-ask paths.
Switch: SELDON_OFF=leadPlausibleGuard.
Tests: golden/journey only. Add journeys for:
- an extreme-input finding that becomes a note, with no repair;
- an undeclared-credit answer that is normalised, with no second JUDGE.

Run the journeys you touch plus cold imports. Do not run gate.sh or cohorts.
Report C:/seldon/tests/leadPlausibleGuard-0/REPORT.md, max 12 lines: file:line for each fix, every re-ask path removed, net src (aim ≤ 0), and cohort commands for ShelfLife ×2 and S1-doorcount ×1. Target: ShelfLife ≤150k and ≤1 repair cycle, with the real catches kept. Leave the diff, do not push. Temp files only under C:/seldon/tests/leadPlausibleGuard-0. Never open desktop windows. Never read C:/seldon/sealed/.
