# Lead micro ladder census — round 3

Real Codex Terra medium provider calls with scripted user decisions. SQLite supplies the durable run outcome and verification.
Independent evidence is scored from a disposable product copy. Lines / longest / >160 count UTF-8 product text excluding checks and dependencies.

| Cohort / slot | State | C verified | Owner accepted | Fault records | Recoveries | Refusals | Fault questions | Alarm | Calls | Wall min | Oracle P/F/U | Lines / longest / >160 |
| --- | --- | --- | --- | --- | ---: | --- | ---: | --- | ---: | ---: | --- | --- |
| leadRedCoord3Real / red01 | WAITING | — | — | lead_failure 1 | 1 | None | 1 | None | 5 | 1.7 | — | — |
| leadGuideReplayReal / lg01 | SCRIPTED_C | true | false | lead_failure 1 | 1 | None | 0 | None | 7 | 2.7 | 2/1/0 | 82 / 135 / 0 |
| leadHello7 / lh01 | SCRIPTED_C | true | false | lead_failure 2 | 1 | None | 0 | None | 9 | 3.6 | 2/1/0 | 59 / 228 / 1 |
| leadHello7 / lh02 | SCRIPTED_C | true | false | lead_failure 3 | 1 | None | 0 | None | 11 | 5.0 | 2/1/0 | 110 / 357 / 5 |
| leadHello7 / lh03 | SCRIPTED_C | true | false | lead_failure 1 | 1 | None | 0 | None | 7 | 3.0 | 2/1/0 | 74 / 156 / 0 |
| leadHello7 / lh04 | SCRIPTED_C | true | false | lead_failure 1 | 1 | None | 0 | None | 7 | 3.0 | 2/1/0 | 46 / 291 / 2 |
| leadHello7 / lh05 | SCRIPTED_C | true | false | lead_failure 1 | 1 | None | 0 | None | 7 | 2.5 | 2/1/0 | 45 / 275 / 2 |
| leadFound7 / lf01 | SCRIPTED_C | true | false | lead_failure 1 | 1 | None | 0 | None | 7 | 14.0 | 7/0/0 | 68 / 394 / 12 |
| leadFound7 / lf02 | SCRIPTED_C | true | false | lead_failure 1 | 1 | None | 0 | None | 7 | 13.1 | 7/0/0 | 124 / 515 / 16 |
| leadFound7 / lf03 | SCRIPTED_C | true | false | lead_failure 1 | 1 | None | 0 | None | 7 | 24.0 | 7/0/0 | 172 / 452 / 18 |
| leadFound7 / lf04 | SCRIPTED_C | true | false | lead_failure 1 | 1 | None | 0 | None | 7 | 15.1 | 7/0/0 | 122 / 292 / 4 |
| leadFound7 / lf05 | SCRIPTED_C | true | false | lead_failure 2 | 1 | None | 0 | None | 9 | 30.5 | 7/0/0 | 126 / 526 / 23 |

## Durable outcome

- **leadRedCoord3Real** 0/1 scripted C, 0/1 verification complete. Source 33046e1273e15be2c1967258d7513490a97ed410+worktree:99cf044a76aa.
- **leadGuideReplayReal** 1/1 scripted C, 1/1 verification complete. Source 8434139ac2ceb1f6e065114f072a9ca26aff4f9b+worktree:3b21c164fcbc.
- **leadHello7** 5/5 scripted C, 5/5 verification complete. Source 54c774c6dd55c98e4c52744885144f59f1f21176.
- **leadFound7** 5/5 scripted C, 5/5 verification complete. Source 54c774c6dd55c98e4c52744885144f59f1f21176.

## Per-product evidence

- **leadRedCoord3Real/red01** No measured product files. hello.py absent. Receipt `C:/seldon/tests/coord3-20261120/leadRedCoord3Real/red01/summary.json`.
- **leadGuideReplayReal/lg01** `docs/try-it/check.py` 48/99/0, `docs/try-it.md` 27/135/0, `hello.py` 7/71/0. Raw oracle exact-greeting fail. Period-bearing kickoff reading matches direct CLI stdout = true. Receipt `C:/seldon/tests/coord3-20261120/leadGuideReplayReal/lg01/summary.json`.
- **leadHello7/lh01** `docs/try-it/walkthrough.py` 28/131/0, `docs/try-it.md` 23/228/1, `hello.py` 8/67/0. Raw oracle exact-greeting fail. Period-bearing kickoff reading matches direct CLI stdout = true. Receipt `C:/seldon/tests/coord3-20261120/leadHello7/lh01/summary.json`.
- **leadHello7/lh02** `docs/try-it/walkthrough.ps1` 43/292/2, `docs/try-it/walkthrough.py` 27/129/0, `docs/try-it.md` 32/357/3, `hello.py` 8/71/0. Raw oracle exact-greeting fail. Period-bearing kickoff reading matches direct CLI stdout = true. Receipt `C:/seldon/tests/coord3-20261120/leadHello7/lh02/summary.json`.
- **leadHello7/lh03** `docs/try-it/walkthrough.py` 41/108/0, `docs/try-it.md` 26/156/0, `hello.py` 7/71/0. Raw oracle exact-greeting fail. Period-bearing kickoff reading matches direct CLI stdout = true. Receipt `C:/seldon/tests/coord3-20261120/leadHello7/lh03/summary.json`.
- **leadHello7/lh04** `docs/try-it/walkthrough.py` 27/107/0, `docs/try-it.md` 13/291/2, `hello.py` 6/71/0. Raw oracle exact-greeting fail. Period-bearing kickoff reading matches direct CLI stdout = true. Receipt `C:/seldon/tests/coord3-20261120/leadHello7/lh04/summary.json`.
- **leadHello7/lh05** `docs/try-it/walkthrough.py` 25/108/0, `docs/try-it.md` 13/275/2, `hello.py` 7/71/0. Raw oracle exact-greeting fail. Period-bearing kickoff reading matches direct CLI stdout = true. Receipt `C:/seldon/tests/coord3-20261120/leadHello7/lh05/summary.json`.
- **leadFound7/lf01** `docs/try-it/walkthrough.cjs` 2/66/0, `docs/try-it.md` 15/394/3, `foundation.js` 1/161/1, `hello.js` 1/142/0, `index.html` 23/388/4, `name.js` 1/144/0, `style.css` 25/280/4. Oracle passed all reported checks. Receipt `C:/seldon/tests/coord3-20261120/leadFound7/lf01/summary.json`.
- **leadFound7/lf02** `docs/try-it/walkthrough.cjs` 49/515/9, `docs/try-it.md` 19/215/3, `index.html` 25/278/3, `scripts/foundation.js` 3/86/0, `scripts/hello.js` 3/72/0, `scripts/name.js` 3/75/0, `style.css` 22/343/1. Oracle passed all reported checks. Receipt `C:/seldon/tests/coord3-20261120/leadFound7/lf02/summary.json`.
- **leadFound7/lf03** `docs/try-it/walkthrough.cjs` 101/452/7, `docs/try-it.md` 16/359/4, `first.js` 3/72/0, `index.html` 21/349/4, `second.js` 3/77/0, `style.css` 25/372/3, `third.js` 3/81/0. Oracle passed all reported checks. Receipt `C:/seldon/tests/coord3-20261120/leadFound7/lf03/summary.json`.
- **leadFound7/lf04** `docs/try-it/walkthrough.cjs` 1/109/0, `docs/try-it.md` 16/292/2, `index.html` 24/88/0, `scripts/foundation.js` 22/61/0, `scripts/hello.js` 22/56/0, `scripts/seldon.js` 22/57/0, `style.css` 15/224/2. Oracle passed all reported checks. Receipt `C:/seldon/tests/coord3-20261120/leadFound7/lf04/summary.json`.
- **leadFound7/lf05** `docs/try-it/walkthrough.cjs` 92/333/8, `docs/try-it.md` 11/403/2, `index.html` 9/408/5, `scripts/foundation.js` 1/166/1, `scripts/hello.js` 1/147/0, `scripts/name.js` 1/149/0, `style.css` 11/526/7. Oracle passed all reported checks. Receipt `C:/seldon/tests/coord3-20261120/leadFound7/lf05/summary.json`.

Raw records and per-slot files are under `C:/seldon/tests/coord3-20261120`.


## Triage and comparison

- Lane red01 on the revised T-256 source proved all CLI subjects, then paused on T-258. Independent replay of the candidate's actual documented PowerShell commands returned 0, 2, 2. The builder's own walkthrough omitted shell status inspection. Manual receipt at `C:/seldon/tests/coord3-20261120/red01-11201120-manual/guide-manual.json`.
- Combined lg01 reached scripted C in seven calls with verification complete. The judge routed weak assertions and a missing optional guide action to the same builder. The repair strengthened assertions and removed the optional unexercised shell instruction while keeping all three approved scenarios.
- Main leadHello7 delivered 5/5 verified scripted C, 41 provider calls, all Terra medium. No stall, refusal or fault question. Eight Builder recovery records were ordinary judge-driven corrections to diagnostic assertions or guide coverage. Per-slot calls 9 / 11 / 7 / 7 / 7. Independent CLI replay observed the accepted greeting, exit 0 and empty stderr, plus exit 2, empty stdout and a useful stderr diagnostic for an extra argument and unknown flag, in all five delivered candidates.
- T-257 fixture conflict applies to all five raw hello scores (each 2/1/0). The locked greeting includes the period and matches product output. The canonical JSON oracle expects the same words without it. This prevents treating the raw scores as five accepted-behavior failures.

- Main leadFound7 delivered 5/5 verified scripted C. All 37 provider calls were Terra medium. Zero refusal, stall alarm or operator fault question. Six Builder corrections improved exact offline page, keyboard, fresh open, visual or guide checks before C. Final per-slot calls 7 / 7 / 7 / 7 / 9.
- The independent Foundation oracle passed 35/35. Each copied page opened directly from file, rendered three adjacent controls, used three separate local scripts, displayed only the corresponding message for each interaction, and emitted no browser errors or network requests. The desk-size captures show legible output and obvious Play controls in all five. Median longest measured product line 452 characters, range 292–526, and 4–23 lines over 160 per slot. The prior Orchestrator trial-off and trial-on samples both scored 35/35. The trial-on samples had a shorter median maximum of 100. The five Lead products meet the runtime path with room for code readability improvements.

## Plain comparison controls

- Matched plain ShelfLife built with one direct Terra-medium call from the same dream in 236.8 seconds. It used 34,306 fresh-plus-output tokens per native usage receipt. Independent oracle 35/4/1. The exact heading appeared at both widths and the controls loaded over HTTP 200. A favicon 404 accounts for three raw console failures and a Windows file lock accounts for the database cleanup failure. Shape 342 lines, longest 4,581, 22 over 160. Current plain compresses substantially more than the retained 1,041-line/337-character reference. Raw receipt `C:/seldon/tests/coord3-20261120/plain-shelf-review/summary.json`.
- Retained plain Quiet Bench was independently rescored at 9/1/4 using the current oracle, with HTTP 200 and a usable settings/action page. The failing guide path returned 404 during saved-session readback. Shape 249 lines, longest 1,408, 21 over 160. The older calibrated design-review score was 10/0/4. Raw current receipt `C:/seldon/tests/coord3-20261120/plain-qb-review/summary.json`.
