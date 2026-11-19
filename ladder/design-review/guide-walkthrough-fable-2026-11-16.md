# Try-it guide walkthrough: make it an ordinary unit (Fable, 2026-11-16) — T-185, T-183

Read-only. Basis: thin tree `work/lanes/thinJudgePlain/src/seldon` (4,237 lines; line numbers are that tree), stores
`C:/seldon/tests/m1/shelflife-thinab-e78f656-r01..r05` (mode=ro), `m2terra1/r05.log`. No tests or providers run. Line counts are estimates.

## Cause (TRIAGE: FAULT SELDON, DESIGN)
1. **Code reads a document written for a person and runs it.** `guide.py:15,23` takes every json/argv fence as a command;
   `proof.py:36,56` runs each to exit. r05's guide fenced `python server.py --port 8765 --db walkthrough.sqlite` (what a reader
   types). It never exits: timedOut, check gap, guide ASKED. `plan.py:11` ("one JSON argv fence") is what asked for this.
2. **The guide is written blind.** `plan.py:305` gives the guide unit `dependencies: []`, so it starts at minute 0 in an empty
   worktree (start offset 0.0 in all five runs). The author cannot try anything. Result: **5 of 5 runs failed the first
   walkthrough** and paid a guide fixup plus a second full WAVE-VERIFY (guide WORK calls: 2, 3, 2, 2, 4).
3. **The guide has no room for a real check.** Scope is the one .md file (`plan.py:304`) and its declared checks are thrown
   away (`plan.py:61-63`). So the four "passing" guides carry a one-line `node -e`/`python -c` that extracts and evals a second
   fence of the guide itself: a human document bent into a machine script. r05's own checks grep the prose for landmarks.
4. Everyone but the code was right in r05: the worker wrote "do not wait for the server to exit", COACH said "the guide scope
   cannot repair a verifier that invokes the command", the sim user said "have someone follow it from a fresh folder with the
   server in the background". Four identical corrections went back anyway (`proof.py:95-97` dumps the timeout record).

## The one rule
**The guide is for the reader; code never reads it. The guide unit is an ordinary unit: written after the product exists,
walked by its author, proven by an ordinary declared check that code runs on the delivered commit.**

## Design
- **Order:** `add_guide` sets `dependencies` to every other unit. The guide worker starts in a worktree that holds the whole
  integrated product, with full access, and tries what it writes (the "person in a fresh checkout" is the author, for free).
- **Room:** guide scope becomes `docs/try-it.md` + `docs/try-it/**`. Its WORK answer declares checks like every unit; they become
  check nodes owned by `guide`, run by unchanged WAVE-VERIFY. Background servers are already solved by `checks/kit/serve.cjs`.
- **Words (`plan.GUIDE_WORK`):** "Write docs/try-it.md for the reader: the shortest path from a fresh copy to using the
  product, with the exact commands and what they will see. The product is in your worktree: follow your own guide as that
  reader would (start what it starts, use the page and the API, stop it) and fix what trips you. Then leave one check under
  docs/try-it/ that repeats that walk on its own from temporary data, saves a screenshot of what the reader sees to
  SELDON_EVIDENCE_DIR, and stops what it started; declare it. Nothing in the guide is for a machine."
- **Judge:** PRODUCT subject `tryItGuide` stays the one judge. Its trace is the guide unit's checks; facts add "Walkthrough check
  sources" (blobs of the guide's checkPaths at the final commit) beside "Guide file". It decides by meaning: does the check do
  what the guide tells the reader, and does the evidence show it worked. That keeps T-83 closed without code parsing prose.
- **No charter or blueprint change.** This brings the walkthrough under the existing Check row (one owner, file in its scope,
  ordinary command) and R9. C9 holds: planner words, worker executes, judge decides.

Rejected: (a) a separate model "reader session" at WAVE-VERIFY: new call kind, +40 lines, one more model call on every
re-verify, flaky evidence, and R9/R12 would need rewording. (b) fences that declare background processes: more format for the
referee to police. (c) no walkthrough, judge reads prose only: reopens T-83.

## Removed / added (src)
| File | Change | Lines |
|---|---|---|
| `guide.py` | deleted (fence and link regexes, path probe, 2 refusals: "must link paths", "argv must contain nonempty strings") | -34 |
| `proof.py` | 22-23, 34-43 (`walkthrough`, `guide.checks`, `guide:format` refusal), 72-74 (walkthrough clean/dirty), 110 owner special case, import | -15 |
| `judgment.py` | 19-20 trace special case becomes `plan.assigned(document)["guide"]` (drop `store` arg at 3 call sites), 25-26 owners special case, import; +2 check-sources fact | -4 |
| `run.py` | 38 `guide.checks(...)`, import | -2 |
| `plan.py` | 61, 63 guide exceptions; 263 compares to the guide scope; 304-305 scope + dependencies; `GUIDE_WORK` reworded | -1 |
| `fixups.py` | 24 comment (guide gaps now route by check owner like any other) | -1 |
Net about **-55** (4,237 to ~4,180). Kept: `units.py:140-143` (guide file must exist; no unit JUDGE for a unit with no requirement).

## Lane brief: thinGuideUnit (one lane; files above are shared with nothing else in flight)
Base: `work/lanes/thinJudgePlain`. Files: `src/seldon/{guide,proof,judgment,run,plan,fixups}.py`, `tests/seldon/test_journey.py`,
`tests/seldon/kit_journey.py`. Change: exactly the table. Do not add a call kind, a schema field, a validator or a refusal.
Scripted worker (`test_journey.py:63-65`): the `docs` branch writes plain prose and declares one check instead of a fence.
Proof, golden/journey only:
1. Replace `test_guide_walkthrough_journey` with: guide prose contains a fenced `python server.py` line (never exits) and the
   declared check uses the kit server; run reaches SCRIPTED_C; no guide fixup; PRODUCT `tryItGuide` brief carries the check's
   final observation, its source and the guide text. RED on base (base times out on the fence).
2. Journey asserts the guide WORK question is asked only after every other unit is DONE and its worktree holds their files.
3. Keep the `broken-guide` kit twin: failing declared check returns one gap to `guide` with the real output.
4. Fast golden once. Report src lines before/after.
Then (lead): Terra cohort of 5 on the lane; T-185 closes at 5/5 with zero guide fixups from walkthrough timeouts; port to main for T-183.

Note, not in lane: r05 stderr shows `POST /mcp 404` hitting the guide's fixed port 8765 during the check, so something else on the
host probes that port. Kit `{port}` avoids it in checks; worth one look when a real run binds a fixed port.
