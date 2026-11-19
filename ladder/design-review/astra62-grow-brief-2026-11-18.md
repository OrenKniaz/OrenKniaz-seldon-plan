# Astra 6.2 design brief: the first stage, "grow, then align" (2026-11-18) — read only, write one file

You are designing the heart of Seldon. Be inventive and concrete. The owner's words, now BLUEPRINT R18:
> "Macro idea from user, expand and improve, align using multi ask questions tool until user agrees align and expansion done."

## What happens today (the gap)
- ALIGN is one schema-bound call; its answer becomes the vision; the user approves it at gate A (options + Other, R17). Then ARCHITECT plans areas, contracts and waves.
- On Quiet Bench (a "large" dream), ALIGN's 7 scope items were the user's paragraphs nearly word for word, plus 3 small "improvements". The plan had 5 units. The 3 waves were dictated by the user's own text. ~460 lines of product. Seldon acted as a careful executor of a pre-chewed spec, not a planner growing a dream.
- Suspected causes in the coaching: ALIGN is told to keep every exact user value verbatim in its scope item (good for values, but it drives copying), and planning is coached toward the thinnest plan.

## Read
- `~/codex-harness/work/sprint-20261027/semantic-cc/CHARTER.md` (C5 size, C8 gates, C9 V-model trace, C20 chat acts) and `BLUEPRINT.md` v1.14 (R17 asking the user, R18, §3.3 progressive planning).
- `src/seldon/` especially the ALIGN/vision path: `questions.py` (ALIGN prompt + facts), `schema.py` (VISION), `run.py` (ALIGN/A states), `decisions.py` (gate A, options), `frontdoor.py` (how chat shows a question).
- The Quiet Bench run: `C:/seldon/tests/m1/quietbench-d56dc7b-b01*/calls/` (the ALIGN question and answer) and the dream `~/codex-harness/work/ladder/briefs/L3/4-quietbench.json`.
- Your own review `astra62-review-2026-11-18.md` in this folder.
Do not read any `.env` file. Edit nothing except your output file. No provider calls.

## Design questions
1. **The loop.** Rounds of: expand + improve the dream → ask the open choices as several questions at once (2-4 options each, recommendation first, Other) → fold the answers in → repeat, until the user says alignment and expansion are done. What does one round's question and answer look like (schema in plain words)? What does the planner show the user each round (the grown product in a few lines, what changed since last round)? How does the loop end (an explicit "this is it" option every round)? How does it avoid endless rounds without caps (R15: no hard limits; coaching and the user's choice end it)?
2. **What "expand and improve" means** so a weak model (Terra) does it well: features, the people and stories behind them, quality bar, the size of the whole product, order of value, what to leave out. How to keep the user's exact values without copying their prose as the plan. How the grown vision feeds ARCHITECT so the split and waves are sized to the dream, not the thinnest path.
3. **Questions that matter.** How the planner picks the 2-6 questions per round that most change the product (not trivia), and how answers stay traceable into the plan (C9).
4. **Chat and the simulated user.** How the front door shows a multi-question round in chat (C20) and maps answers back. How the test simulated user answers realistically (picks the recommendation, sometimes Other, says "done" when the vision covers the dream), so cohorts stay autonomous.
5. **How we measure it.** A test dream written the way a real person writes (short, no waves, no interface spec), and a cheap measure of growth: features/stories/parts per dream vs what the dream implies, before any app is built. What would show this stage is working.
6. **Lanes.** Split into Sol 6.2 lanes with disjoint files, each with a ready-to-paste brief (PROBLEM, DESIGN, do-not-touch, fault twin built from recorded data, PROOF/DELIVER as in `~/codex-harness/work/lanes/checkContract.prompt.md`), a feature switch name (`SELDON_OFF=<name>`), and one plain line for the owner: coaching or refereeing.
Rules: coach not referee; no caps; delete what this makes dead; helpful failures; strict schemas.

## Output
At most 180 lines to `~/codex-harness/work/ladder/design-review/astra62-grow-2026-11-18.md`: the design first (plain words), then the test dream + measure, then lanes with briefs, then what you are least sure about.
