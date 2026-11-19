# Seldon code quality A/B

Arm A uses Terra medium with trials off on `a4204ec`. Arm B uses Terra medium with `judgeEvidence,plannerBrief` enabled on `513de6a`. Both trials changed together, so any difference applies to that combined configuration.

Foundation was opened directly as a file. The same brief-derived browser check measures title, three side-by-side controls, three local scripts, each exact message independently, and offline/browser errors in both arms. ShelfLife uses the same 40-item oracle in both arms and a separate main-server startup check.

| Product | Arm | Slot | C? | Recovery rows | Oracle P/F/U | Lines / longest / >160 |
| --- | --- | --- | --- | ---: | --- | --- |
| Foundation | A | `foundation-a4204ec-f01` | SCRIPTED_C | 0 | 7/0/0 | 64 / 379 / 9 |
| Foundation | A | `foundation-a4204ec-f02` | SCRIPTED_C | 0 | 7/0/0 | 56 / 304 / 7 |
| Foundation | A | `foundation-a4204ec-f03` | SCRIPTED_C | 0 | 7/0/0 | 125 / 322 / 8 |
| Foundation | A | `foundation-a4204ec-f04` | SCRIPTED_C | 0 | 7/0/0 | 113 / 523 / 9 |
| Foundation | A | `foundation-a4204ec-f05` | SCRIPTED_C | 0 | 7/0/0 | 41 / 1916 / 6 |
| Foundation | B | `foundation-513de6a-fb01` | SCRIPTED_C | 0 | 7/0/0 | 167 / 98 / 0 |
| Foundation | B | `foundation-513de6a-fb02` | SCRIPTED_C | 0 | 7/0/0 | 188 / 93 / 0 |
| Foundation | B | `foundation-513de6a-fb03` | SCRIPTED_C | 0 | 7/0/0 | 142 / 100 / 0 |
| Foundation | B | `foundation-513de6a-fb04` | SCRIPTED_C | 0 | 7/0/0 | 75 / 138 / 0 |
| Foundation | B | `foundation-513de6a-fb05` | SCRIPTED_C | 0 | 7/0/0 | 166 / 104 / 0 |
| ShelfLife | A | `shelflife-main-a4204ec-s01` | SCRIPTED_C | 1 | 39/0/1 | 234 / 3433 / 29 |
| ShelfLife | A | `shelflife-main-a4204ec-s02` | SCRIPTED_C | 0 | 39/0/1 | 258 / 3481 / 30 |
| ShelfLife | A | `shelflife-main-a4204ec-s03` | SCRIPTED_C | 1 | 39/0/1 | 254 / 3357 / 20 |
| ShelfLife | A | `shelflife-main-a4204ec-s04` | SCRIPTED_C | 0 | 39/0/1 | 186 / 4294 / 26 |
| ShelfLife | A | `shelflife-main-a4204ec-s05` | SCRIPTED_C | 1 | 39/0/1 | 275 / 3467 / 35 |
| ShelfLife | B | `shelflife-main-513de6a-sb01` | SCRIPTED_C | 0 | 35/4/1 | 510 / 655 / 16 |
| ShelfLife | B | `shelflife-main-513de6a-sb02` | SCRIPTED_C | 1 | 36/3/1 | 970 / 135 / 0 |
| ShelfLife | B | `shelflife-main-513de6a-sb03` | SCRIPTED_C | 1 | 35/4/1 | 988 / 492 / 8 |
| ShelfLife | B | `shelflife-main-513de6a-sb04` | SCRIPTED_C | 1 | 36/3/1 | 932 / 617 / 9 |
| ShelfLife | B | `shelflife-main-513de6a-sb05` | SCRIPTED_C | 1 | 35/4/1 | 864 / 602 / 15 |

## Code shape and oracle comparison

- Foundation median lines / longest / >160 changed from `(64, 379, 8)` to `(166, 100, 0)`. Aggregate P/F/U changed from `(35, 0, 0)` to `(35, 0, 0)`.
- ShelfLife median lines / longest / >160 changed from `(254, 3467, 29)` to `(932, 602, 9)`. Aggregate P/F/U changed from `(195, 0, 5)` to `(177, 18, 5)`.
- ShelfLife plain Terra reference was 1,041 lines with a 337-character maximum. There is no matched plain oracle receipt in this comparison. No matched plain Foundation reference was supplied.

## Evidence

- foundation-a4204ec-f01 — `C:/seldon/tests/zbCoord-0/foundation-a4204ec-f01/foundation-oracle.json`.
- foundation-a4204ec-f02 — `C:/seldon/tests/zbCoord-0/foundation-a4204ec-f02/foundation-oracle.json`.
- foundation-a4204ec-f03 — `C:/seldon/tests/zbCoord-0/foundation-a4204ec-f03/foundation-oracle.json`.
- foundation-a4204ec-f04 — `C:/seldon/tests/zbCoord-0/foundation-a4204ec-f04/foundation-oracle.json`.
- foundation-a4204ec-f05 — `C:/seldon/tests/zbCoord-0/foundation-a4204ec-f05/foundation-oracle.json`.
- foundation-513de6a-fb01 — `C:/seldon/tests/zbCoord-0/foundation-513de6a-fb01/foundation-oracle.json`.
- foundation-513de6a-fb02 — `C:/seldon/tests/zbCoord-0/foundation-513de6a-fb02/foundation-oracle.json`.
- foundation-513de6a-fb03 — `C:/seldon/tests/zbCoord-0/foundation-513de6a-fb03/foundation-oracle.json`.
- foundation-513de6a-fb04 — `C:/seldon/tests/zbCoord-0/foundation-513de6a-fb04/foundation-oracle.json`.
- foundation-513de6a-fb05 — `C:/seldon/tests/zbCoord-0/foundation-513de6a-fb05/foundation-oracle.json`.
- shelflife-main-a4204ec-s01 — `C:/seldon/tests/zbCoord-0/zbs01/summary.json`.
- shelflife-main-a4204ec-s02 — `C:/seldon/tests/zbCoord-0/zbs02/summary.json`.
- shelflife-main-a4204ec-s03 — `C:/seldon/tests/zbCoord-0/zbs03/summary.json`.
- shelflife-main-a4204ec-s04 — `C:/seldon/tests/zbCoord-0/zbs04/summary.json`.
- shelflife-main-a4204ec-s05 — `C:/seldon/tests/zbCoord-0/zbs05/summary.json`.
- shelflife-main-513de6a-sb01 — `C:/seldon/tests/zbCoord-0/zbsb01/summary.json`.
- shelflife-main-513de6a-sb02 — `C:/seldon/tests/zbCoord-0/zbsb02/summary.json`.
- shelflife-main-513de6a-sb03 — `C:/seldon/tests/zbCoord-0/zbsb03/summary.json`.
- shelflife-main-513de6a-sb04 — `C:/seldon/tests/zbCoord-0/zbsb04/summary.json`.
- shelflife-main-513de6a-sb05 — `C:/seldon/tests/zbCoord-0/zbsb05/summary.json`.

## Outcome and hands-on review

**Readability improved in the combined arm. Product parity did not pass.** All ten B slots reached scripted C. All five Foundation slots and four ShelfLife slots (sb01, sb02, sb03, sb05) recorded `verification_complete=false`, principally because the judge could not establish that the delivered guide's actual steps were exercised from a fresh checkout. The independent Foundation browser check proves its scoped behaviors separately.

- Foundation A and B each passed 35/35 direct-file browser checks. All five B products have zero measured lines over 160 characters. Visual inspection found three aligned play panels with all three outputs legible in each B capture. The B products used six provider calls each and wrote no recovery rows.
- ShelfLife A scored 195 pass, 0 fail, 5 unverified. B scored 177 pass, 18 fail, 5 unverified. Fifteen failures were three console assertions per run for one missing favicon in each of the five B products. The other three were explicit heading misses. sb01 and sb05 say **Needs attention**, and sb03 says **Use these soon**, where the brief requests **Expiring soon**. Those products still rendered an expiry section. The raw outcome captures both the heading fidelity gap and the console problem.
- All five ShelfLife B server commands returned HTTP 200 in isolated scratch directories. Visual review of retained 1280px walkthrough captures found the same expiry, inventory and add-form hierarchy in both arms, and verified the three renamed headings. Subjective visual quality remains unscored.
- Trial activation is confirmed in all ten B slots by WORK questions with a `plannerBrief` and JUDGE questions with `Code shape (measured)`. Build, planner, reviewer and judge were configured Terra medium, first WORK medium. The existing scripted decider remained Terra low. Four ShelfLife B runs needed fixup recovery, versus three ShelfLife A runs. The four B fixups all included formatting repairs, providing direct evidence that the judge sometimes turned measured source shape into action.
- Every ShelfLife B judge packet contained `favicon.ico` in its observations. The defect still shipped through scripted C. In the affected heading samples, the original exact heading was present in the fresh WORK user-words appendix, but absent from the planner-authored brief. The evidence establishes fidelity and judgment misses even though it does not isolate the effect of either trial.
- Keep both trials off by default pending lead review of the fidelity, console, and fresh-checkout guide gaps. The next decision is whether these issues require a focused trial revision before another paired ShelfLife run.

Raw B usage and SQLite census are under `C:/seldon/tests/zbCoord-0/ab-b-usage.txt` and `ab-b-census.txt`. The sb03 progress row said ASKED, while transition r272 records `SCRIPTED_C`. Its outcome r271 retains incomplete verification.
