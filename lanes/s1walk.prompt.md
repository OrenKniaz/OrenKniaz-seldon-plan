# Lane s1walk (Sol 6.2 medium): hands-on blind review of two products built from one brief
Brief: ~/codex-harness/work/ladder/briefs/S/S1-doorcount.md (Mara's venue door counter).
Products: C:/seldon/tests/s1walk-0/A and C:/seldon/tests/s1walk-0/B. They are disposable copies, and you may run them freely.
Walk each one as Mara, Jo and Ben would, on the real product. Use the server, the API and a headless browser where available (never a visible window).
Cover every part of the brief:
- one-hand big number and places left
- the no-night-open state
- Out at zero
- two doors at 119 competing for the last place, done truly concurrently
- uncertain tap retry with no double count
- correction with reason, who, and history
- first-full time and peak
- last four Fridays and CSV export
- restart mid-night
- offline, with no network assets
Record what you did and what you saw.
Then review the code as a maintainer who must change it next month: readability, line length, structure, error handling, and how safe it is to change.
Output C:/seldon/tests/s1walk-0/REPORT.md, max 35 lines, containing:
- a table of brief items × A/B: works, partly, broken or missing, each with a one-line evidence pointer
- code-quality verdicts and scores out of 10 for A and B
- human UI/UX feedback for each
- an overall winner, with reasons
Do not guess which builder made which product. Temp files only under C:/seldon/tests/s1walk-0. Never open desktop windows. Never read C:/seldon/sealed/.
