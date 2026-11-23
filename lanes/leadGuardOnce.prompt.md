# Lane leadGuardOnce (Sol 6.2 medium), Lead only: one complete guard walk, one repair
Repo: this lane dir = main 80fad3b, which includes leadGuardOwner (the guard walks from the owner's own words). Binding: CHARTER-LEAD.md, BLUEPRINT-LEAD.md v0.5.
Facts, ShelfLife p01 on leadGuardOwner (C:/seldon/tests/leadGuardOwner-0/REPORT.md and its slot under C:/seldon/tests/m1):
- 14 calls, 495k tokens, 18 min. The order was ALIGN, REVIEW, WORK 357 s, then JUDGE, JUDGE, DECIDE, JUDGE, WORK, JUDGE, WORK, DECIDE, JUDGE, WORK, JUDGE.
- That is 1 first build, 3 repair builds, 6 guard calls and 2 recovery decisions.
- Cause: serial discovery. Each walk stopped at the first defect cluster, so the run went find, repair, re-walk, three times over.
- Most tokens ride on the guard calls, and each re-reads its full packet.
- The catches were real and must be kept: an oversized quantity disconnect plus a CSV abort, a huge DELETE id disconnect, and in S1 the cross-night uncertain-tap double count.
Design (lead, Claude):
1. The guard keeps walking after the first defect. It finishes the whole journey set from the owner's words and returns ALL reproduced defects in one verdict. Coach it: "a complete report saves a repair round".
2. One repair turn with the full list. The builder re-runs its own regression checks before returning.
3. The re-walk is scoped: it covers the repair diff plus the affected promises, reuses prior observations for everything else, and its packet carries only deltas, not the full history.
4. No caps. Measure.
Also fix this main bug: a UnicodeDecodeError ('utf-8' codec can't decode byte 0x92) when Seldon reads check output written in cp1252 on Windows. See C:/seldon/tests/m1 slot hc02 (leadHumanGuide race control) and its log. Decode output robustly at the one place it is read, and do not refuse.
Switch: SELDON_OFF=leadGuardOnce.
Tests: golden/journey only. Add one journey: a walk finds two defects, then one repair turn, one scoped re-walk, C. Run the journeys you touch plus cold imports. Do not run gate.sh or cohorts.
Report C:/seldon/tests/leadGuardOnce-0/REPORT.md (max 12 lines): net src, files touched, and cohort commands for ShelfLife ×2 and S1-doorcount ×1. Target: ShelfLife ≤1 repair cycle and ≤150k tokens, and S1 still catches the cross-night bug. Leave the diff, do not push. Temp files only under C:/seldon/tests/leadGuardOnce-0. Never open desktop windows. Never read C:/seldon/sealed/.
