T-78; base 9437ec377837e6e958c51c690981aefe8b66b08b; uncommitted binary patch, including new judgment.py.
Source lines before/after: gitwork 175/144; inference 69/69; plan 139/151; questions 349/246.
Source lines before/after: run 244/208; schema 94/94; states 53/57; store 210/213; judgment 0/186.
Journey module lines 739/771; source total across changed modules 1333/1368. Owner guide constants unchanged.
Removed reviewer integratedWalkthrough/inspections, selection validators/catalog, 64 KiB inspection errors, feature-wide DEMO and product-wide PRODUCT; retained unit brief cap.
State rows: DEMO/PRODUCT-JUDGE uncertain -> respective FACTS; FACTS resolved -> respective JUDGE; JUDGE/FACTS gap (including repeated uncertainty) -> EXECUTE.
Golden gate: 1 pytest PASS, 37 journeys vs base 33; 169.14 s (pytest 169.28), base 154.17 s; scale50 70.94 s; no skips.
New cases seconds: DEMO/PRODUCT fact+reopen 7.44/7.23; named gap 13.22/13.83; repeated uncertainty 13.52/13.83; traced helper/artifact 9.05.
Largest question bytes at 1/50 units: WORK 3067/3067; JUDGE 5523/5523; DEMO 4753/4753; PRODUCT 4664/4664.
Rule disagreements: none. Fixups reopen the existing owning unit, preserving its session and the approved plan; code ANDs requirement/criterion verdicts.
Unproven: real-provider/browser behavior, replay of the failed Foundation run, historical-store migration, owner/full-vision acceptance; ruff unavailable (no install).
Next: lead integration and authorized real replay. No commit, real provider call, new dependency, charter/blueprint edit or size-cap increase.
