# Clean core decision (Oren, 2026-11-09)

Oren: "why keep useless code that makes a mess when 1.2 idea should be omarchy style clean". Supersedes the 2026-11-08 "thin path inside the repo, delete afterward, no restart" direction in THIN-PATH-DECISION.md. Charter v1.2 itself is unchanged.

Direction: build the charter 1.2 loop as a clean new core. Reuse an old part only when the inventory (design-review/what-the-code-does.md) shows it earns its place. Everything else goes. No compatibility with the old core.

Style rules:
1. One way to do each thing: one loop, one plan format, one test route (ordinary commands), one question builder, one review path.
2. The loop is: ask the LLM with a strict schema, validate, save, launch worker, run tests, judge, approve.
3. Stub A-to-C from the first commit, replaying real recorded LLM answers. Hello-world is the first real target, ShelfLife after.
4. Every module states its charter clause. No clause, no module.
5. Patches to the old core stop now. stage-bound1 is not landed. Local commits 838cdd7 and 7273857 stay unpushed.

Size target: a few thousand lines. A target, not an estimate; the inventory informs it.

## LLM question rules (Oren, 2026-11-09)

1. Structured answers wherever possible: strict schemas, enums for every choice, no free text where a choice will do.
2. Prompts have a valid example and a short, clean guide. One state, one short guide, kept as data in one place.

Added by the delivery lead:
3. One decision per question. If a guide needs "also", split the question.
4. `uncertain` is always a legal answer and names the fact it needs, so the model never has to guess to fill a field.
5. CODE supplies every ID, path and revision. The model picks from enums of supplied handles and never types one.
6. Refusals list every error at once, with the rejected answer and the original facts.
7. Every call is fresh and stateless, built from bounded facts; nothing relies on a provider session.
8. Every real question and answer is recorded. A prompt or schema change is checked by replaying recorded answers.
9. Model by role: strongest for judgment and planning, cheaper for mechanical work.

## The plan holds product meaning only (Oren's question, 2026-11-09: "why on a simple app, a repair was even needed?")

The first real hello-world plan was 9.4 KB: 3 requirements, 2 tests, 3 beads, 2 waves. One requirement was about Seldon's evidence folder and review process. The reviewer's only gap was Seldon's own check-in leaking into the plan. Our PLAN prompt told the model to express that workflow.

Rule: the LLM plans the product (features, requirements, tests with ordinary commands). CODE owns the workflow: tests-first ordering, beads for small work, waves, check-ins, guide work, evidence folders.
Acceptance: real hello-world reaches C with zero repairs. A repair on a tiny app is a Seldon defect until shown otherwise.

## Dev-run findings (Oren, 2026-11-09): repairs are red flags; review issues get logged during dev testing

Every real dev run produces one report and one row in work/ladder/RUNS.md. These are dev tools, not product features.
- Red flags: repairs and their causes, exact-fix retries by schema field, refusals, uncertain answers, repeated questions, blocked workers, INCOMPLETE.
- Review log: every reviewer and judge gap, with target and correction, tagged product issue or Seldon leak.
- Schema: fields the model got wrong, fields never used by the model or by code.
- Semantic: facts supplied but never cited, tests that pass while the verdict is a gap, RED reasons.
- Efficiency: time, tokens, prompt and answer size per state; calls per state; plan size against app size.

## Fast and magic (Oren, 2026-11-09: "be omarchy, strive for fast efficient and clean")

The bar is high-end craft: clean, efficient, nothing wasted, nothing to configure. Numbers below are examples of that bar, not the goal, and giant apps will rightly take longer:
- `pip install` under 10 seconds, no build step, no native dependencies.
- `seldon` starts in under 200 ms. Imports stay lazy.
- Zero setup: one command with the dream. Seldon detects providers, tools, browser and git. It asks nothing it can detect; defaults are opinionated and changeable afterward.
- First useful response to the user within seconds, with live progress during every long step.
- Scripted full journey under 60 seconds. Real hello-world, dream to C, under 10 minutes.
- Short prompts, cheap models for mechanical work, reviews in parallel: LLM latency is the only wait.
- Errors say the one next thing to do.

## Hello-world bar (Oren, 2026-11-09): "keep at hello world until we are truly in awe of how well it works"

ShelfLife waits. Hello-world moves on only when real runs are repeatedly excellent: zero repairs, zero retries, a short plan, tight prompts, a page that is really clicked in a real browser, and a clean walkthrough at C. One lucky pass does not count.

## Seldon's taste (Oren, 2026-11-09): "max efficient, max cool, max simple, max beautiful. Everything!"

This is how Seldon thinks, for every product including hello-world. It serves C6's quality bar.
- ALIGN: every Vision Lock carries a taste bar. Improve the dream toward the most beautiful, simplest, most delightful version of what was asked, within scope.
- PLAN and REVIEW: the simplest design that achieves it; a plan that is merely correct is a gap.
- WORK: workers build it beautifully the first time, with no dependencies or code that do not earn their place.
- JUDGE(demo): judges real screenshots against the taste bar. Functional but plain does not pass.
One short sentence in each guide, not a checklist. A plain page reaching C counts as a Seldon defect.

## No patching bad design (Oren, 2026-11-09): "If something fails at this simple app at times, it would be a shit show on mega app."

Any hello-world failure, even once in many runs, is treated as a design defect until shown otherwise. Before a fix: name the class, the shared rule that removes it, and how it would appear on a very large app. A prompt sentence that patches one observed answer is not a fix. Hello-world moves on only when real runs pass repeatedly, at a rate we would trust at a thousand times the size.

## Leeway for unrequested additions (Oren and Astra, 2026-11-09; design-review/scope-leeway.md)

Allow unrequested improvements that support the accepted experience and preserve its meaning, constraints and commitments. Changes to what the product promises, asks of users, or requires to operate need user agreement. The line is changed commitments, not added pixels, words or lines of code. LLM owns the judgment, CODE owns records and routing, the user owns scope and acceptance. No classifier, permission matrix or new gate. At C, mention noteworthy discretionary choices in one line. Judges rejecting an addition must cite the accepted obligation or material consequence.

## Ladder (Oren, 2026-11-09)

1. Hello-world: keep hitting until repeatedly excellent.
2. Foundation (new rung): a small multi-button app, each button its own independent piece ("Hello, world!", "My name is Seldon", "This is the Foundation"), built by workers running concurrently. Proves the scoped work unit and real parallel execution: measured overlap, no file conflicts, separate checks, one integration.
3. ShelfLife.

## Repo hygiene (Oren, 2026-11-09)

Clean, tight, maintainable. No god files; everything in the right place. Each src/seldon module keeps one job and stays small enough to read in one sitting; split a growing responsibility before it becomes a god file. No stray scripts, dead code, or dev artifacts in the product tree. Old core removal stays scheduled for the cutover.
