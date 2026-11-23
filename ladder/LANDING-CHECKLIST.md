# Landing checklist (lead, from real incidents)

Read the diff, apply only the items whose trigger matches (usually 2-5). Each item: trigger → check → the incident behind it.
Idea from the Claude Code team's reliability checklist (verification post, 2026-11-16). Prune items that never fire.

| # | Trigger (read from the diff) | Check before landing | Incident |
|---|---|---|---|
| 1 | Any change to `schema.py`, an answer shape, or a prompt's example | Journeys pass with the strict stub (every property required, additionalProperties false); no field made optional | 11-17: STEER left `areas` optional → Codex 400 on every call, 6,688-call loop |
| 2 | Any new or moved `import` in `src/seldon` | Cold-import every module alone (`python -B -c "import seldon.<m>"`, src on PYTHONPATH) | 11-06 `seldon init` broke; 11-16 providers↔questions cycle |
| 3 | Two or more lanes land together | One gate on the merged tree, never only the lanes' own gates; read each report's "blocked/unproven" lines | 11-16 guide crash (guideParallel + seeProof); seePeers + judgeOnce test; M3 wiring |
| 4 | Change to the guide unit, walkthrough or `plan.GUIDE_*` | A journey where the guide is DONE and its walkthrough runs on the integrated product; PRODUCT reads it | 11-16 g03 KeyError 'answer' on guide judgment |
| 5 | Change to recovery, decisions, scheduler or step questions | A fault twin where the same failure repeats: it reaches the planner, then the user, and never loops on "Try again" | 11-17 overnight loop |
| 6 | Change to a fact a test reads by name (renamed/removed fact) | Grep tests for the old name; update the journey, don't delete the outcome assertion | 11-16 "Proof execution" removed → prompt-order test failed |
| 7 | Change to scope, snapshots or out-of-scope messages | A Terra 1-run check: byproducts (`__pycache__`) never count as writes; workers don't leave stray files | 11-16 7/13 runs WAITING on pycache |
| 8 | New coaching sentence in any prompt | 5 Terra runs before any 20-run cohort; the sentence names no oracle check | 11-16 DEFECT_HANDOFF wording regression; held-out rule |
| 9 | Change to judge wording or gap routing | Replay the judge eval tune set (work/ladder/judge-eval) before runs; holdout only at milestones | s04 missed filter; z11 over-demand |
| 10 | Any real run launched | Unique slot name; a 10-minute CronCreate check in the same step; the cohort stall alarm on | 11-16/17 slot collision; unwatched loop |
| 11 | BLUEPRINT/CHARTER edit | Re-read the file after writing; `grep` the new wording | 11-16 v1.11 edit not saved (script never wrote) |
| 12 | Any new failure path, refusal or error a model or user can see | A golden-path test breaks it on purpose (RED) and asserts the message is helpful: what failed, what was expected vs got, what to do next, in the answer's or user's words (no bare Python errors) | 11-17 "list index out of range" gave the planner nothing to reason with (Oren: "failures like regular SW for humans, should be informative and helpful") |
| 13 | Any lane report or gate run that sets an environment variable (e.g. SELDON_OFF=...) | Re-run the gate on the landed tree with NO env vars before calling it green; journeys select their own feature arm in the test | 11-18 T-225: growLoop gated with SELDON_OFF=growAlign set; main's plain gate failed ~78 journeys after landing |
| 14 | Rebasing a lane diff onto a newer main | In a `git worktree add work/lanes/<L>-wt` of semantic-cc (never switch branches in the shared checkout: the coordinator lands from it), commit the diff on its real base, `git rebase origin/main`; check the exit code unpiped and that a file the diff adds exists before asking for a gate | 11-22 `git apply --3way` in a lane repo (no base blobs) failed atomically behind a pipe; the leadImportsR gate and smoke tested plain main |
| 15 | Launching a long run (cohort, plain arm, lane) from a Claude session | Detach it from the session (PowerShell Start-Process, or setsid/nohup) so it survives the session ending; record the PID | 11-22 plain Sol arms died mid-turn with no error when the launching session went away |
