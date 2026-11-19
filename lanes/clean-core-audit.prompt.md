Read-only design audit: no edits, no tests, no provider launches. Output one document.

Owner's instruction: "Make sure we are not patching shit design. If something fails at this simple app at times, it would be a shit show on mega app."

Read: CHARTER.md; C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DECISION.md; C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DESIGN.md; all of src/seldon; tests/seldon/test_journey.py; C:/Users/oren/codex-harness/work/ladder/RUNS.md; and the real runs C:/seldon/tests/core1/real-lead-01 through -12 that exist, with their .out reports and calls/ folders (runs 03, 04 and 09 failed in instructive ways). git log -12 shows the sequence of fixes.

Answer plainly:
1. Which landed fixes are real design rules, and which are prompt sentences patching one observed answer? Be blunt. For each patch, name the design that would remove the need for it.
2. Variance. The same dream gives different plans, tests and verdicts between runs. Where can a single LLM's judgment flip the whole run, and how does the design contain that? Run 09's RED dispute is the example: is our RED concept itself sound, or should code establish more of it?
3. Scale. Imagine this exact loop on an app a thousand times larger, with many workers and waves. For each state and module: what breaks first, what must change in shape now because it would be expensive later, and what is correctly deferred. Do not recommend building features early; identify only shape mistakes.
4. Efficiency: the wasted LLM work, ranked, with the simplest structural removal for each. Note the observation that workers are told "Report, do not prove" and so never run or look at their own work; and that every decision uses an LLM to read "yes".
5. The three changes that most raise reliability, simplicity and beauty together, in order. Each with its owner (CODE or LLM), what gets deleted, and how we would measure it in RUNS.md.

Be concrete, cite files and run events, and keep it under 200 lines. Decide; do not list options.
