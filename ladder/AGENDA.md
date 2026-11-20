# Seldon autonomous agenda (lead: Claude; Oren 2026-11-19: "loop yourself and keep pushing the envelope ... improve Seldon from every direction")

Rules for every loop: launch what is decided in the same turn; every real run gets a 10-min check; land only on a gate green with NO env vars + cold imports; hands-on review (code, commands, page) beside every oracle score, both arms; lanes code on Sol 6.2 medium, deep design/review on Astra 6.2 high; tests on Terra; watch Codex usage; log each loop in HANDOVER.md; anything that changes CHARTER/BLUEPRINT goes to "For Oren" below, never applied without his word.

## Now
0. **Oren 11-19 binding: zero Seldon bugs on micro before any bigger dream.** Bar: 5 runs each of hello, Foundation, ShelfLife, Quiet Bench; all reach C; zero step failures, zero stall-alarm loops, zero bookkeeping refusals, zero Seldon-fault questions. Every fault found -> root-cause lane -> rerun that dream. Small/medium/RNC and the "Seldon as lead" architecture question are parked until the bar is met.
1. ~~microLean~~ LANDED 6beb500 (gate 104/104 no env).
2. prompts2 LANDED 21b6381 (trial, OFF by default; SELDON_ON=prompts2). replayAB lane RUNNING (offline prep + explicit Terra generation + blinded packets). Then: rewrite prompts behind `SELDON_OFF=prompts2` + offline replay A/B on recorded questions (blind code-quality/fidelity comparison).
3. Re-run the micro ladder (hello, Foundation, ShelfLife, Quiet Bench) with new prompts; oracle + hands-on review; paired with plain.

## Next
3c. **Code-quality severity:** with judgeEvidence on, the Terra judge found the golfed source in Quiet Bench but filed it as a NIT (no fix round), and passed ShelfLife's one-line web/app.js as satisfied. Coach the code-quality rubric: code a maintainer would struggle to change safely (compressed multi-statement lines hiding logic, one-line pages) is must-fix; style preferences are nits. Then re-run ShelfLife + Quiet Bench with judgeEvidence and compare readability by hand.
3b. **Evidence lane (before any judge-model change):** make the judge's packet contain the answer: browser console errors and failed requests captured in observations; a real Stop/progress observation on runs; resource cleanup (open file/DB handles) observed after the walkthrough; a code-quality subject with the actual source excerpt and a rubric (readable, changeable). Then re-run the judge cases (Terra) and re-grade blind.
4. 5-run micro cohort: "happy" = 4/5 autonomous C, quality >= plain (oracle AND hands-on), time/cost <= 2x plain.
5. Small rung: pick/write small dreams (days of single-agent work; e.g. a Gantt-planner-class app), owner-voice briefs, sealed oracles by Astra, plain baseline.
6. Judge quality: grow judge-eval with real defects from current runs (Stop-not-observable, golfed code, missing guide examples); add code-quality subject; measure recall.
7. Efficiency: cost per call, fixed overhead on micro, builder speed.
8. Growth coaching (R18): expansions offered as options; less passive persona; count owner-endorsed new behaviours.

## Ideas to try (creative, from every direction)
- Astra review ideas: both ends of a disputed contract predict one observation before coding; "does the evidence contain the answer?" paired good/broken test; one worker owning both endpoints for a disputed boundary.
- Prompt library as a first-class artifact with versions, replay scores and switches.
- Builder self-review pass with a senior-engineer rubric before returning (cheap, same session).
- Use plain Codex as a fallback/peer: on micro, run plain + Seldon proof around it.
- Learn from each run: auto-extract "lesson" lines into coaching candidates, gated by replay A/B.
- Read-only Prime Radiant page (M4) once medium is reached.

## For Oren (needs his word; collected, not blocking)
- **Ratify the Lead lane's 3 charter changes** (drafts in design-review/CHARTER-LEAD-draft-2026-11-19.md, BLUEPRINT-LEAD-draft, lead-design): (1) delegate implementation — one builder per milestone may use native sub-agents/skills, Seldon keeps transitions, the owner keeps scope and acceptance (replaces C1 for Lead mode); (2) the milestone is the unit of delivery; (3) cumulative proof — every milestone re-proves earlier promises on the integrated product. Plus C27: mode chosen at kickoff.
- **Switch on the new prompts (prompts2) by default?** Blind A/B round 2 (2 reviewers, 5 builder pairs): new prompts win code quality 4/5 with both reviewers agreeing, incl. both whole products; fidelity fixed (user labels kept); but 3 split single-reviewer losses on component pairs (page: fewer assigned checks + generic error text; guide: one check less). Strict precommitted rule = fail, so it stays OFF. Options: (a) switch on now, (b) one more round targeting component completeness, (c) keep off. **Lead recommendation 11-19 after real both-trials runs: keep OFF for now** — in real runs prompts2's richer answers trip Seldon's strict bookkeeping checks (ALIGN constraint quoting, source handles, value shapes; ShelfLife looped at DETAIL to the stall alarm). alignNormalise lane (normalise, don't refuse) running; re-run both-trials after it.
- **Judge model in test runs.** Evidence 11-19: the same recorded Quiet Bench final judgment, replayed: Terra flagged the Stop defect 2/6 times (in the real run it said satisfied), Sol 6.2 flagged it 2/2 with more real findings. Judging on Terra is a coin toss. Options: (a) Sol 6.2 for the JUDGE role only in test runs (cost: a few Sol calls per run); (b) two Terra judge samples, union of must-fix gaps; (c) keep Terra and accept misses. **Lead recommendation 11-19: keep Terra** — evidence + code-quality severity moved judging more than Sol did (Sol caught 1/7 vs Terra 1/14 strict). Rule today: test env Terra, never Sol. **Update 11-19 (strict blind grading, 42 answers):** real defects caught: Terra-old 0/14, Terra-new 1/14, Sol-old 1/7, Sol-new 1/7 (all the Stop case); nobody caught favicon 404s, open SQLite handles or golfed code. A stronger judge alone won't fix it; evidence first (lane below), then decide the model.
- **Hello greeting fixture**. The kickoff reads “hello world, I'm Seldon.” and a Lead run locked the full stop. The exact oracle expects “hello world, I'm Seldon” without it. Which bytes should the ladder require? Round 3 keeps the raw oracle score and the accepted-vision result.
