# Seldon study, 2026-11-10 (Fable)

> **Correction, 2026-11-11 (Oren):** hello-world is a test fixture, not the product target. The target is the large dream, where a single worker does not give a good result. The comparison against plain Codex in sections "Verdict" and "1" measured the fixture, and the "acceptance loop around one agent build" recommendation in section 5 is withdrawn. Sections 2 to 4 (design faults, repeated mistakes, repo state) stand. The direction is now `BLUEPRINT.md` beside the charter.

Scope: charter v1.3, the clean-core decision and design, all of `src/seldon` at `e4024b6` (2,330 lines), the scripted journeys, the 48 real runs in `RUNS.md`, the ShelfLife fight record, and one new experiment (plain Codex on the hello-world dream). Read-only except for that experiment, which wrote only under `C:/seldon/tests/study`.

## Verdict in five lines

1. The goal is right. Half of the mechanism is right. The other half is the reason nothing ships.
2. The right half: Seldon agrees a vision with the user, fixes what "done" means, and proves it independently on the real product. No coding agent does that by itself.
3. The wrong half: Seldon also acts as the scheduler that cuts work into small pieces and runs a worker for each. The coding agent already does that job better alone, at every size we have tested.
4. The new core is cleaner than the old one, but in one day it started repeating the old pattern: grow, patch, regress.
5. Recommendation: keep the outer loop (vision, contract, independent proof, user gates). Give the whole build to one agent session. Add decomposition only when a measured size needs it.

## 1. The macro idea

### What the evidence says

| Dream | Who | Result | Time | Input tokens |
|---|---|---|---|---|
| ShelfLife | Plain Codex, 1 call (11-01) | Delivered, 36 of 40 oracle checks | 6 min | 0.44M |
| ShelfLife | Seldon old core, 33 real rounds | Never delivered | 13 to 49 min each | up to 20M |
| Hello-world | Plain Codex, bare dream (today) | Working page, unstyled, no test | 53 s | 0.10M |
| Hello-world | Plain Codex, one-paragraph brief (today) | Test written first and seen failing, page, 5 real-browser screenshots, guide. My independent rerun of its test passed | 190 s | 0.25M |
| Hello-world | Seldon new core, best build | Same deliverables | about 330 s, 8 LLM calls | 0.39M |
| Foundation, 3 buttons | Seldon, one worker | Reached scripted C, 2 of 2 | 9 to 10 min | 0.78M |
| Foundation, 3 buttons | Seldon, parallel units | Reached C 0 of 10 | 21 min in the furthest run | 1.6M |

The one-paragraph brief used what Seldon's runs taught us: where the browser tooling is, and the craft guidance. So the last two days produced real knowledge. It lives in about ten lines of prompt, not in the scheduler.

The page from that single call is at least as well designed as any page Seldon produced (`C:/seldon/tests/study/ev-b/play-desktop-revealed.png`). It is one run, so treat it as a strong signal, not proof.

### What I like

- **Code owns structure, the LLM owns meaning.** Correct, and the charter states it well (I1, I10).
- **Vision Lock and the A, B, C gates.** A real product idea for non-technical users.
- **Independent proof on the real path** (C15, C26): Seldon reruns the checks itself, in a real browser, on the exact delivered files, and a judge looks at real screenshots. This is the part a coding agent cannot be trusted to do for itself, and it is where Seldon can beat plain Codex: the 4 failed checks out of 40 on ShelfLife are Seldon's market.

### What I do not like

- **Seldon as micro-scheduler** (C12, C13, C17 as built). Every real failure since run 13 came from machinery between Seldon and the worker: the tests-first phase, unit files, dependencies, evidence reuse, question size. None came from a model being unable to build the thing.
- **The reference loop does not transfer fully.** The GenAI project's `run_turn` makes one enum decision per call. That fits routing and judging. Building software is not a chain of enum decisions; the heavy work is one long agent session. Forcing the plan into typed graph edits (`new:1` handles, unit positions) is where most retries come from.
- **Twenty-six required pieces.** A charter where everything is required and nothing may be dropped means every reset keeps the full scope. The old core did not die because it predated v1.2. It died of scope. The new core inherits the same scope.
- **Tests-first RED as a hard gate on new products** (C14). On a product that does not exist, a failing test proves only that a file is missing. This single gate caused failures in rounds 31 to 33 and runs 9, 13 to 15, 22, 24, 34 and 35. What C14 really wants is meaningful tests. A judge reading the test against the requirement gives that. Observed RED earns its place on existing code, where it shows a bug reproduces.

## 2. What is wrong with the current design

From reading the code at `e4024b6`:

1. **Phases are global.** All units write tests, then one RED judgment, then all units build, then one GREEN judgment. One doubtful verdict stops everything. The single wave is hard-coded. The audit said this on 11-09 and it is still true (`execution.py`, `verification.py`).
2. **The state machine lives in a dictionary.** The cursor carries about 30 loose keys (`repairCause`, `repairOrigin`, `repairPaths`, `resumeRepair`, `pendingRepair`, `authorizedRevision`, `demoCandidate`, and more). Which combinations are legal is nowhere stated. This is the "implicit state machine" problem found in the old core on 11-07, rebuilt.
3. **The split of `loop.py` is cosmetic.** `Loop` inherits four mixins that all share `self` and the cursor. It is one 900-line class in five files. Lines of 150 to 200 characters keep the count low. Line targets are being gamed by density, so the count no longer measures simplicity.
4. **Questions are dumps of internal records.** A judge gets JSON keyed by `r17`, with digests, attempt IDs and process receipts: 28 KB to judge a hello page. That is why judges answered "provide the remaining r17 content". A question should read like a short brief: the requirement, the test source, the output, the screenshot.
5. **Evidence reuse is a five-hash identity scheme** (test, inputs, obligations, scopes, check generation) built to avoid rerunning a two-second test. Rerunning every check on the final commit at each gate needs none of it and removes a class of failures (run 12, f11, f12).
6. **Each unit costs two fresh worker sessions.** Workers are 80% of tokens. Splitting three buttons into four units doubled the cost and time and never reached C.
7. **`processes.py` is 529 lines, 23% of the core,** for Windows process containment. Defensible, but it is plumbing, not the idea.
8. **Prompt text is already patch history.** "Commands are argv, never shell strings", "1-based positions", "automated checks never wait on manual review", "exit codes are execution facts": each sentence maps to one failed run.
9. **Citations are required and never used.** They are validated by schema, cause retries, and nothing reads them.
10. **There is no front door.** `pip install` still installs the old 32k-line core; the `seldon` command runs it. The new package is not in the wheel. The only way to run the new core is a dev script with a scripted "yes".

## 3. The mistakes we keep making

1. **We never compare against the plain agent.** The charter names the ShelfLife fight as the proof. It was run on 11-01, Seldon lost, and it was not run again. We measured Seldon against Seldon for nine days.
2. **We trust tests where we wrote both sides.** Scripted journeys passed 46 of 46 while real runs went 0 of 5. Named on 11-01 (fault twins), on 11-09 by Oren, and again at the core10 revert. It is still the gate that decides what goes to main.
3. **We read noise as signal.** "6 for 6" was followed by "1 of 3" on the next commit. At a true 80% success rate, three clean runs in a row happen half the time. Per build we ran 2 to 6 runs and credited or blamed the last change. Overall the ledger is 25 clean of 48.
4. **We ship faster than we can verify.** Twenty-one commits to main in about 30 hours, each written by one agent from a brief and applied by another that mostly read the report. Patches were landed over a REJECT, re-applied by hand, and twice silently removed earlier fixes. The core grew from 749 to 2,420 lines in a day.
5. **Nobody owns the whole design.** The chain is Oren, then the lead, then Sol writes, Sol reviews, Astra audits, the lead applies. The rule "CC manages, Codex does" saves usage and costs coherence. For a core this small, one author should write and read every line.
6. **Process stands in for product.** Charter clauses on every report, triage lines, a deviation register, 65 memory rules, a convergence percentage that the lead scores himself. The percentage went 59 to 67 on days when nothing shipped. It should be dropped; the only scores that count are oracle checks passed and clean runs out of N.
7. **Every reset keeps the scope.** North Star v1 to v4, charter 1.0 to 1.3, old core, thin path, clean core. The implementation restarts and the 26 requirements stay.
8. **The rig is treated as incidental.** Sleep and hibernate killed runs at least five times. Add the logged-out Claude CLI, the console encoding crash and PowerShell quoting. One laptop on battery is the whole test farm.
9. **No human has used it.** Every A, B and C in 48 runs was a scripted yes. The cofounder experience, which is the product, has had zero real exposure. All reviews were same-model, so C11 was never exercised either.

## 4. Other things I checked

- **Uncommitted work.** The Seldon repo has the `core10b` patch applied and staged: 15 files, about 1,470 added lines, including five recordings of real runs. It is not committed, not pushed, and its journeys were not run. I left it untouched.
- **Old core.** Its 31,685 lines and its tests are still in the repo, and its golden test has been failing since 11-09.
- **Cost.** A hello-world run costs about 0.4M input tokens, Foundation with units 1.6M. The 48 real runs plus lanes are a large share of the Codex budget for a button.
- **What works and should be kept.** `store.py`, the schema validator, `providers.py` (fresh calls, retries, recorded calls), running ordinary commands and capturing screenshots, the dev runner and the run report. Recording every real question and answer was the best decision of the rebuild.

## 5. Direction

### The reframe

Seldon is the **acceptance loop around a native agent build**, not a scheduler of small workers.

```
ALIGN  -> A      one call: improved vision, quality bar, visual direction
CONTRACT -> B    one call: requirements and the checks that prove each (plain list)
BUILD            one agent session: writes tests and product, runs them, looks at its own screenshots
VERIFY           code only: rerun every check on the delivered commit, capture screenshots
JUDGE            one call, another provider when available: contract vs evidence, screenshots, stubs
  gap -> resume the same build session with the judge's gaps (at most 3)
DEMO -> C        real user
```

Five or six LLM calls. The trace is requirement, check, evidence, verdict. Decomposition into waves comes back when a measured dream is too large for one session, and then as coarse feature-sized waves, each a full agent session.

My estimate is about 1,000 to 1,200 lines, reusing the kept modules. That is an estimate.

### Decisions for Oren

1. **Adopt the reframe?** It changes how C12, C13, C14 and C17 are met for small and medium dreams, so it needs a charter edit or a deviation. Only you can do that.
2. **Benchmark rule.** Every rung runs plain Codex first, same model, scored by a black-box oracle. Seldon counts only when it scores higher. Ten runs per build before any reliability claim.
3. **Shrink the required set for v1.** Proposed must-haves: C1 to C4, C6, C8, C15, C20, C26, and a reduced C9 (requirement, check, evidence). Everything else is parked by name, not required.
4. **One owner for the core.** I write and read every line; Codex reviews. No push to main without real runs.
5. **A front door this week,** so the first human run is yours.
6. **Drop the convergence percentage and the report boilerplate.** Keep `RUNS.md`.

### First step if you agree: two days, decided by numbers

- Build the loop above on a branch.
- Run hello-world 10 times, Foundation 10 times, ShelfLife 5 times, each against plain Codex on the same dreams.
- Seldon passes if it beats plain Codex on oracle score on ShelfLife and stays within about twice its time. If it does not, we learn that cheaply and decide again with facts.

### Where I may be wrong

- One baseline run per variant today. The benchmark exists to check exactly this.
- A single agent session will fail at some size. I expect that size to be well beyond ShelfLife, but we have no measurement.
- The charter's concurrency goals may matter more to you than this evidence suggests. That is your call.
