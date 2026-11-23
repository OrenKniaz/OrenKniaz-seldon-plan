# Lane timeWhy (Terra 6.1 medium): analysis only, no code changes
Oren 11-22: "How hello is faster but ShelfLife slower? Let's learn from abnormalities."
Lone runs, timed by call-directory mtimes (each call dir is written when that call ends):
- Lead hello ih01 (C:/seldon/tests/m1/hello-imp2-91643a4-ih01): 2.2 min total. Calls: 3 planning calls at about 13-17 s each, WORK about 41 s, GUARD about 44 s.
- Lead ShelfLife is01 (C:/seldon/tests/m1/shelf-imp2-91643a4-is01): 7.8 min total. Calls: 3 planning calls at about 20 s each, WORK about 232 s, GUARD about 164 s.
- Plain (C:/seldon/tests/plainBase/*/events.jsonl, run.json): hello took 223/258/93 s with only 2-5 shell commands. ShelfLife took 200/233/356 s.
The lead's hypothesis: plain hello time is model deliberation on an under-specified dream, and Lead's exact spec removes it. ShelfLife's time is real build work, which the spec doesn't shrink, so Lead pays build + guard + planning on top.
Test the hypothesis with data:
1. Timeline per run. For every plain run and every Lead slot with usable timestamps, find the time between events: model reasoning/latency vs command execution vs waiting. Lead slots: m1/hello-coord4r-*-chr0*, found-coord4r-*-cfr0*, shelf-coord4b-*-csb0*, shelf-witnesscarry4-*, *-imp2-*; find the exact dir names. Use events.jsonl timestamps if present; otherwise use per-call files and the codex session logs under ~/.codex/sessions/2026/11/22 that match the run's cwd.
2. Hello: what did plain spend 93-258 s on? Quote the reasoning or decision points, e.g. the greeting text, argument handling, tests. Did Lead's WORK skip them because the brief already decided them?
3. ShelfLife: Lead WORK vs plain build. Same amount of work? Where does the guard's 164 s go: product launch, browser kit, screenshots, model time? Which of it is repeated or idle?
4. Variance: plain ShelfLife ranges 200-356 s, and plain hello ranges 93-258 s. Which runs are outliers, and why?
5. Conclusions for Seldon:
   (a) where the spec saves builder time, and how to get that on bigger dreams;
   (b) the top 2 guard or planning time sinks, with a fix proposal for each;
   (c) does Lead's overhead look fixed or growing with dream size? Use hello vs Foundation vs ShelfLife: minutes for planning, WORK and guard vs number of promises.
Write C:/seldon/tests/timeWhy-0/REPORT.md, max 30 lines, with a table per run. Do not edit any repo. Temp files only under C:/seldon/tests/timeWhy-0. Never read C:/seldon/sealed/. Never open desktop windows.
