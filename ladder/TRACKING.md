# Tracking files: rules for whoever leads

Claude, Astra and Codex workers all maintain these. The JSON files are the source of truth; the dashboard is a view of them.

| File | What |
|---|---|
| `TICKETS.json` | Every failure (Blueprint P9). |
| `RECOMMENDATIONS.json` | Proposed and ratified changes to CHARTER.md / BLUEPRINT.md, plus lead actions. |
| `STATUS.json` | Now: main commit, docs, milestone, what is running (lanes), next steps, decisions for Oren. `recentRuns` is filled by `tracking.py` from `RUNS.md`; never edit it by hand. |
| `tracking.py` | Validator. Run `python work/ladder/tracking.py` after every edit; exit 1 names the bad row. |

## Tickets
- Fields: `id` (next free `T-NN`), `title`, `severity` (critical, high, medium, low), `type` (design, code, idea), `status`, `milestone`, `area`, `direction`, `evidence`; optional `note`, `resolution`.
- Status: `open` → `in_progress` (a lane is on it; name the lane in `direction`) → `fixed` (landed on main; name the commit) → `done` (validated; `evidence` contains `VALIDATED:` with commit and run or journey). `dropped` needs a reason.
- Open a ticket the same day a failure is found. Append to `evidence`; never delete history.
- Every ticket has a `family` (its root-cause idea, one of `families[].name`). A new family needs a one-line `idea` (the wrong assumption) and `remedy` (the rule that kills it); the lead reads the family counts printed by `tracking.py` in each efficiency debrief (BLUEPRINT P11).

## Recommendations
- `decision`: proposed, ratified, rejected, deferred. Only Oren ratifies or rejects; record his words and the date in `decidedBy`.
- `implementation`: not started, in progress (name the lane), incorporated (say where), dropped.
- New proposals go in with `decision: proposed`; they do not change CHARTER.md or BLUEPRINT.md until ratified.

## Status
- Update `STATUS.json` whenever main moves, a lane or real run starts or ends, or the next steps change. Keep `now` to two sentences.
- Run `python work/ladder/tracking.py`: it validates all three files and refreshes `recentRuns` from `RUNS.md`.

## Dashboard
https://claude.ai/artifact/7uzbq8wRGaAFmETpLCLYtH (private to Oren). Only Claude can upload to it: the Claude lead re-uploads all three JSON files at the end of each turn. When Astra leads, the JSON files stay current and the dashboard catches up when Claude is back; the files, not the page, are the truth.

## Pace rules (Oren 2026-11-13: "can we cut dev time in half?")
Measured 11-13: a loop took ~2.5 h; lanes took 10-13 min, triage and landing 30-40 min, the real cohort 1.5-2 h. The cohort is the long pole.
1. Cohorts run with `bash /c/seldon/tests/cohort.sh <dir> <prefix>`: 5 streams, fail-fast (stops starting runs once 3 have failed, so 8/10 is unreachable).
2. `first-fail.sh <dir>` wakes the lead on the first failure; triage and the next lane start while the rest of the cohort finishes.
3. Land each lane as soon as it is green; do not wait for sibling lanes (resolve journey-file conflicts at landing).
4. The lead makes fixes of 20 lines or fewer directly at review; lanes are for design changes.
5. Dashboard and ticket sync happen once per loop (after a cohort or a landing), not after every step.
6. Probe, then exit: while fixing, run a 5-run probe (`cohort.sh <dir> <prefix> 5 5 1`, one round of ~30 min, stops at 2 failures). Run the full 10-run exit cohort only after a clean probe. Only the 10-run cohort counts toward the 8/10 bar.
8. Gates run one at a time on the machine: never two lane gates, a landing gate or a probe at once (11-13: three overlapping gates all failed timing-only, 50-unit bound 99-116 s vs 90). Lanes may code in parallel; gating is serialized by the lead (lanes stop at a written patch when told "lead gates").
9. Nothing long runs unwatched (11-13: the fight script hung ~1 h in a tar copy and nobody noticed). Every background chain gets `C:/seldon/tests/stall-watch.sh <pid> <quiet_min> <max_min> <paths>` (STALL = no file change for quiet_min, default 35 for real runs / 25 for lanes; OVERTIME = max_min); it exits and wakes the lead with the live process list. Watch the chain's lowest pid (`ps -ef | grep "<script>.sh" | awk '{print $2}' | sort -n | head -1`): a subshell shares the script name and ends early (11-13). Every copy or wait step carries `timeout`; product copies use `product-copy.sh` (robocopy, junctions and state skipped), never tar on a slot.
10. No hard size budgets in runs (Oren 11-13): a question is never refused or sent back for being large; sizes are measured ("Largest questions") and reviewed for efficiency after runs finish.
7. Before a probe, replay a failed run's recorded answers against the fix when a replay exists (minutes, no provider calls).
11. Testing must not eat the sprint (Oren 11-13: "stop with nonsense testing"; six gates of 7-12 min failed or re-ran over timing and test wiring). Timing is printed, never asserted. One landing gate per loop, lanes batched. A lane that changes an outcome greps ALL of main's tests/ (not only its golden copy) and fixes old-outcome assertions before delivering. If a gate fails on a test-only cause (stale assertion, wiring, flake), the lead fixes it and lands without a second full gate when the fix touches only tests and compiles; a product-code fix still gates. Never tune tests to fit a limit.

12. M2 exit bar (Oren 2026-11-14): ShelfLife 5/5 C, then 20/20 C, each C at oracle >= native; only then M3. Usage/auth/power pauses are not misses; any Seldon-caused question the planner could answer is a miss.
