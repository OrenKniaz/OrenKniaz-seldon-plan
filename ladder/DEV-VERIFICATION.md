# How we verify Seldon's own development (from the Claude Code verification post, 2026-11-16)

Oren 11-17: "also for our dev process of seldon, take notes from the article." What we adopt, and where it lives.

1. **Verification means running the change.** A landing is verified by a real Terra run, not only the gate. Ladder: gate → 1 Terra run → 5 → 20 only at milestones. Our "verify skill" is `cohort2.sh` + `oracle.py` + `usage.py` + `judged.py`; keep it fast and rock solid (stall alarm, unique slots, 10-minute check).
2. **Cheap checks first.** Lanes run their journeys and cold imports before the gate; the lead runs the gate before any real run. Never spend a Terra run on code the gate has not seen.
3. **Three rounds, then a human.** A lane or a fix that still fails after three rounds stops and comes to the lead (and to Oren if it is a design question). No fourth patch on the same symptom (bird's-eye trigger).
4. **Owners write their checks; a failing check says why.** Each lane writes the journey that proves its behaviour; a report line names what is unproven.
5. **Diff-triggered checklist, not memory.** `LANDING-CHECKLIST.md`: read the diff, run only the matching items. Every incident adds a row.
6. **One reviewer, tuned, rounds build on each other.** One review lane per landing, given the previous findings and incidents; no stacked reviewers. Astra/Fable only for deep design questions.
7. **A change never edits the check that judges it.** Lanes don't weaken outcome assertions; oracles and the judge eval holdout are sealed from the builders (held-out dream rule). BLUEPRINT/CHARTER change only with Oren.
8. **Review the reviewers.** Judge wording is tuned on `work/ladder/judge-eval/tune.jsonl` and checked on the holdout only at milestones. Score recall on real misses and false alarms on clean controls separately.
9. **Severity on findings.** Must-fix / nit / pre-existing, in Seldon's judges and in our own reviews. Nits never start a fix round.
10. **Stamp each landing with how it was verified.** Commit message ends with `Verified: gate N/N | Terra 1-run <score> | none`.
11. **New gates start in observe mode.** A new rule first logs what it would have refused; it enforces only after the log shows no false positives (matches "measure, never refuse").
12. **Flaky checks are fixed or deleted with a reason**, never retried, slept or timing-asserted (no-test-tuning).
13. **Prune.** Checklist rows, coaching sentences and journeys that never fire get removed on a routine (with the 48h drift review).
14. **Every feature has an off switch where possible (Oren 11-17)** so a cohort can A/B its effect on score, time and tokens. See below.

## Feature switches (A/B)
- One place: `src/seldon/features.py` with `enabled(name)` reading `SELDON_OFF` (comma list of feature names); default all on. No other config.
- Each new lane names its feature and puts the switch at the one point where behaviour branches; the old path stays only while the switch exists. Report line: "switch: <name>".
- Cohorts A/B with `OFF=<name>` passed through `cohort2.sh`; compare autonomous C, oracle, wall, calls, fresh tokens, judged share.
- When a feature has proven itself (or failed) in an A/B, the lead deletes the switch and the losing path (thin: no permanent forks).
- Where an off switch would need a large old path back (already deleted code), say so instead of resurrecting it.
