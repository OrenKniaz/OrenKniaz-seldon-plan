# Zero-bug micro census — batch 3

Integrated candidate `7e547433ad3f0c98059993121ccb94d284a45e20`. Terra medium, trials off. Five ShelfLife and five Quiet Bench slots. SQLite supplies the final state and guide verification. Wall time is approximate elapsed time from slot creation to log completion.

| Run | Final state | Fault records | Recovery rows | Refusals | Fault questions | Alarm | Calls | Wall min | Oracle P/F/U | Main HTTP | Lines / longest / >160 |
| --- | --- | --- | ---: | --- | ---: | --- | ---: | ---: | --- | ---: | --- |
| s01 | SCRIPTED_C | None | 0 | None | 0 | None | 8 | 7 | 39/0/1 | 200 | 255 / 3553 / 34 |
| s02 | SCRIPTED_C | None | 0 | None | 0 | None | 8 | 8 | 38/1/1 | 200 | 244 / 3366 / 27 |
| s03 | SCRIPTED_C | None | 0 | None | 0 | None | 6 | 6 | 38/1/1 | 200 | 187 / 3547 / 29 |
| s04 | SCRIPTED_C | None | 0 | None | 0 | None | 6 | 7 | 38/1/1 | 200 | 288 / 3639 / 27 |
| s05 | SCRIPTED_C | unit_failure 1 | 1 | None | 0 | None | 7 | 7 | 38/1/1 | 200 | 261 / 3986 / 39 |
| q01 | WORKING | None | 1 | None | 0 | Yes | 37 | 11 | — | — | — |
| q02 | WORKING | None | 1 | None | 0 | Yes | 39 | 10 | — | — | — |
| q03 | SCRIPTED_C | unit_failure 1 | 2 | None | 0 | None | 16 | 18 | 8/1/5 | 200 | 446 / 4061 / 50 |
| q04 | SCRIPTED_C | unit_failure 1 | 2 | None | 0 | None | 18 | 24 | 7/3/4 | 200 | 226 / 3144 / 30 |
| q05 | SCRIPTED_C | None | 1 | None | 0 | None | 14 | 16 | 7/3/4 | 200 | 353 / 3037 / 36 |

## Decision

8/10 scripted C, 8/10 verified guides, 3 fault records, 8 recovery rows, 0 refusals, 0 literal fault questions, 2 stall alarms and 0 slots with a call kind over 30. Raw oracle failures 11, missing oracle outputs 2.

## Per-product evidence

Shape counts UTF-8 product text and excludes checks, state, caches, dependencies and binary files. ShelfLife plain Terra reference was 1,041 lines, longest line 337.

- **s01** `docs/try-it/walkthrough.cjs` 36/284/8, `docs/try-it.md` 14/453/2, `import_items.py` 28/140/0, `pantry.py` 39/199/1, `README.md` 10/196/1, `server.py` 81/241/7, `static/app.js` 39/716/8, `static/index.html` 7/898/6, `static/style.css` 1/3553/1. Oracle UI readable contrast and calm design (unverified). Receipt `C:/seldon/tests/zbRound3/s01/summary.json`.
- **s02** `docs/try-it/walkthrough.py` 50/188/1, `docs/try-it.md` 22/279/2, `import_items.py` 24/183/2, `pantry.py` 37/199/2, `README.md` 10/167/1, `server.py` 81/289/6, `static/app.js` 18/885/11, `static/index.html` 1/2150/1, `static/style.css` 1/3366/1. Oracle UI expiring soon and expired marking (fail), UI readable contrast and calm design (unverified). Receipt `C:/seldon/tests/zbRound3/s02/summary.json`.
- **s03** `docs/try-it/walkthrough.cjs` 29/1080/10, `docs/try-it.md` 19/368/2, `import_items.py` 19/159/0, `pantry.py` 33/199/2, `README.md` 9/174/1, `server.py` 65/290/7, `web/app.js` 11/1256/5, `web/index.html` 1/2552/1, `web/style.css` 1/3547/1. Oracle UI expiring soon and expired marking (fail), UI readable contrast and calm design (unverified). Receipt `C:/seldon/tests/zbRound3/s03/summary.json`.
- **s04** `docs/try-it/walkthrough.py` 71/212/1, `docs/try-it.md` 23/588/2, `import_items.py` 20/165/1, `pantry.py` 25/225/4, `README.md` 9/252/1, `server.py` 80/199/5, `static/app.js` 51/292/6, `static/index.html` 8/773/6, `static/style.css` 1/3639/1. Oracle UI expiring soon and expired marking (fail), UI readable contrast and calm design (unverified). Receipt `C:/seldon/tests/zbRound3/s04/summary.json`.
- **s05** `docs/try-it/walkthrough.cjs` 36/484/14, `docs/try-it.md` 14/348/2, `import_items.py` 25/172/1, `README.md` 8/230/1, `server.py` 82/292/4, `shelflife/store.py` 37/239/2, `static/app.js` 51/299/8, `static/index.html` 7/1024/6, `static/style.css` 1/3986/1. Oracle UI expiring soon and expired marking (fail), UI readable contrast and calm design (unverified). Receipt `C:/seldon/tests/zbRound3/s05/summary.json`.
- **q01** No measured files. Oracle unavailable. No product files to run Receipt `C:/seldon/tests/zbRound3/q01/summary.json`.
- **q02** No measured files. Oracle unavailable. No product files to run Receipt `C:/seldon/tests/zbRound3/q02/summary.json`.
- **q03** `bench.py` 20/98/0, `docs/try-it/guide.ps1` 80/330/5, `docs/try-it/page.cjs` 37/411/4, `docs/try-it/walkthrough.py` 52/356/13, `docs/try-it.md` 61/665/10, `quiet_bench/__init__.py` 0/0/0, `quiet_bench/core.py` 131/191/4, `server.py` 52/342/5, `static/app.js` 7/757/7, `static/index.html` 1/2733/1, `static/style.css` 5/4061/1. Oracle wave-1 fixed-filter run preserved (unverified), limiter holds during divergence (unverified), stop within one block (fail), fresh-copy guide commands start and stop (unverified), wave-1 saved shape loads after schema growth (unverified), page craft (ShelfLife rubric) (unverified). Receipt `C:/seldon/tests/zbRound3/q03/summary.json`.
- **q04** `bench.py` 19/113/0, `docs/try-it/walkthrough.cjs` 30/333/3, `docs/try-it.md` 21/661/4, `quiet_bench/__init__.py` 1/0/0, `quiet_bench/core.py` 105/286/9, `server.py` 38/288/4, `web/app.js` 8/1003/7, `web/index.html` 1/2255/1, `web/style.css` 3/3144/2. Oracle wave-1 fixed-filter run preserved (unverified), limiter holds during divergence (unverified), stop within one block (fail), CSV rows and invalid WAV atomicity (fail), fresh-copy guide commands start and stop (fail), wave-1 saved shape loads after schema growth (unverified), page craft (ShelfLife rubric) (unverified). Receipt `C:/seldon/tests/zbRound3/q04/summary.json`.
- **q05** `bench.py` 22/135/0, `docs/try-it/walkthrough.py` 96/370/13, `docs/try-it.md` 44/516/6, `quiet_bench/core.py` 112/217/3, `quiet_bench/export.py` 17/117/0, `server.py` 47/356/3, `web/app.js` 12/746/8, `web/index.html` 1/1900/1, `web/style.css` 2/3037/2. Oracle wave-1 fixed-filter run preserved (unverified), limiter holds during divergence (unverified), stop within one block (fail), CSV rows and invalid WAV atomicity (fail), fresh-copy guide commands start and stop (fail), wave-1 saved shape loads after schema growth (unverified), page craft (ShelfLife rubric) (unverified). Receipt `C:/seldon/tests/zbRound3/q05/summary.json`.

Raw slot census and exact fault and recovery bodies are in `C:/seldon/tests/zbRound3/slots.json` and `C:/seldon/tests/zbRound3/faults.json`.

## Decision and triage

**The zero-bug bar failed.** ShelfLife reached 5/5 scripted C and Quiet Bench reached 3/5. All eight completed products returned HTTP 200 on their main command and stored verification_complete=true. The independent oracle scored ShelfLife 191/4/5 and the three delivered Quiet Bench products 22/7/13. The two stalled workers published no product for oracle scoring. The raw oracle includes checker-side guide parsing failures described below. Exact Node 20 compatibility remains open.

| Evidence | Cause and impact | Owner or next evidence |
| --- | --- | --- |
| s02–s05 browser receipts | The literal “Expiring soon” heading was absent with both trials off. All five ShelfLife products passed the three healthy-console assertions. The exact-literal gap crosses both renderers. | trialFidelity, canonical WORK and folded judgment in questions.py and judgment.py |
| q01 r55/r63/r65, q02 r53/r61/r63 | WORK used outcome=question for a status and unresolved evidence. The COACH request omitted the substantive findings and asked for the original question. The simulator supplied an acknowledgement that made no progress. q01 was stopped by the coordinator and q02 by the watchdog. | workerQuestionLoop, units.py:76 and decisions.py:48. Patch passed focused scripted routing. The same live analogue and paraphrased recurrence remain open. |
| s05 r62, q03 r58 | Workers reset SELDON_EVIDENCE_DIR to a product-local evidence directory, then scope enforcement rejected its artifacts. Enforcement correctly protected product scope. | guideEvidenceScope, plan.py:13–23 and proof.py:58. Preserve external evidence ownership during local probes. |
| q03 r49/r53/r58 | The approved scope string included prose, “checks/** excluding checks/kit/**”. The matcher evaluated it literally and rejected the declared checks/page.cjs. | scopeExpression, plan.py:27–38 and ARCHITECT/DETAIL scope prompts. Preserve existing authority. |
| q03 r93 | GUIDE proof first omitted actual PowerShell commands and observations. Recovery produced a runnable walkthrough and final checks r219–r221 passed. The independent guide recognizer could not derive commands from assignments. | guideCommand follow-through. Exact Node 20 remains open. |
| q04 r78/r105/r148, q05 r155 | q04 initially omitted saved settings restore and later hit two browser failures. The passing feature repair preserves keyboard focus across list refresh. q05 final page proof timed out amid session polling, then passed after stale selection responses were gated and assertions tied to the new run ID. Both recovered. The browser kit reported phase and URL on the final deadlines. The exact pending await is still unproven. | Retain browserProof instrumentation and firstPathProof follow-through. No common kit fault was established. |
| q03–q05 Stop | Direct loopback replays in all three products returned a zero cursor on a running Stop acknowledgement and later terminal counts of 32,768 / 28,382 / 26,924. That count difference reproduces the raw oracle failure. The handlers return the persisted starting checkpoint, so these receipts cannot measure post-ack block progress. | Product Stop and existing firstPathProof follow-through. Prove the bound from the actual acknowledged cursor. |
| q04/q05 CSV and guide | PowerShell run/list/show/export succeeded. The produced CSV widths varied across record types under the first header, which the generated proof accepted and DictReader rejected. The guide oracle skipped the assignment that invokes run. Its raw “guide lacks examples” failure applies to the recognizer. | csvExportProof queued. Replay a rectangular CSV consumer and preserve records, values and counts. |
| q04 progress text | cohort2.sh printed ASKED, while final SQLite records SCRIPTED_C with verification_complete=true. The report keeps the cohort log as raw evidence and uses the durable transition. | Existing rig status parsing issue in cohort2.sh:33, also seen in batch 2. |

All three Quiet Bench completions accepted the scripted CSV check-in and reached wave 2 without a consumption refusal. This cohort produced no new native overlap refusal for the detail-owner repair. Direct product smoke, oracle details, and Stop and PowerShell CLI receipts are under C:/seldon/tests/zbRound3.
