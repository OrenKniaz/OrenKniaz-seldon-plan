# Blocker-clearance ladder

From PowerShell:

```powershell
& '~/codex-harness/.venv/Scripts/python.exe' '~/codex-harness/work/ladder/ladder.py' status
& '~/codex-harness/.venv/Scripts/python.exe' '~/codex-harness/work/ladder/ladder.py' run --dry-run
& '~/codex-harness/.venv/Scripts/python.exe' '~/codex-harness/work/ladder/ladder.py' run --parallel 4
```

The real command runs continuously using farm's existing runtime/source and install_build.
It does not start the farm CLI loop. Do not run another installer against that runtime concurrently.
Create `STOP` in this directory to stop dispatching. Already started jobs drain to their normal
deadline; removing STOP allows the next invocation to resume. `.ladder.lock` prevents concurrent
ladder invocations. Inspect the recorded PID before manually removing a stale lock.

`STATE.json` records the current level, consecutive clean window, installed SHA, remaining
briefs and interrupted-sweep status. L0 counts full five-brief sweeps; L1/L2 count individual
verified results; L3 requires all three. A blocker resets the window and stops new dispatches;
the next cohort retries only failed/unstarted briefs before starting another full sweep.
Quota errors remain pending without clearing the clean window or becoming blockers.
A new installed SHA clears the window and unfinished sweep; above L0 it must pass a spot
run from the preceding level before resuming. Per-run budgets are 6/12/20/40 minutes.

`BLOCKERS.md` retains the first blocker per failed cohort with raw receipt location.
Classify it `TRIAGE: BUG|DESIGN — why — sibling cases` before assigning a fix lane.
`PROMOTIONS.md` records each cleared level. Tool verdicts and simulated approvals are not
authenticated human acceptance. This runner never creates fix lanes or publishes changes.

Run receipts live below `C:/seldon/runs/ladder/<level>`; slots and verification evidence below
`C:/seldon/tests/ladder-1`. Dry runs use their own `dry-runs/dry-...` state/log directory and
tagged run/slot roots. They never install Seldon, invoke real Codex, or advance real STATE.json.

L1 and the six existing L2 web briefs are byte-for-byte farm copies. External oracle checks
name a Python script plus argv placeholders `{product}`, `{evidence}`, `{brief}`. The script
prints JSON `totals` with integer `pass`, `fail`, `unverified` counts; verifier retains its
stdout/stderr and full result. All checks must pass by default. ShelfLife explicitly requires
36 of exactly 40; its original subjective-design unverified result is retained, not relabeled.
The ShelfLife adapter imports fight-1/oracle.py unchanged, including oracle_ui, and redirects
its output/isolated-copy roots into ladder evidence. New HTTP oracles start a fresh server on
a free loopback port, inspect API readbacks, and terminate it. Kanban/booking additionally check
their importer through SQLite into the API, and browser actions through that same API.
