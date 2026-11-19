# HANDOVER (lead, 2026-11-17, PC power-off parked)

## State
- Main (origin, branch cc/expansion-teach pushed HEAD:main) = **8fd8743**: M3 waves + R17 landed (src ~4,548 py lines, 64 journeys, cold imports pass; gate test-only fix not re-gated).
- BLUEPRINT v1.12 + held-out M3 exit (ff7ea98). Designs: work/ladder/design-review/{m3-readiness,m3-lanes,wave2,effic-*}-fable-2026-11-16.md.
- No lanes running. No Seldon runs running.

## Parked (resume on power-up)
- Run m3a n01 (Terra ShelfLife, 1-run regression check on 8fd8743) was killed mid-run: C:/seldon/tests/m1/shelflife-main-8fd8743-n01. Simplest: start a fresh 1-run cohort (cohort2.sh m3b n 1 1 1, Terra) rather than reopen.
- Keep-awake stopped; restart .claude/scripts/keep-awake.ps1 before runs.

## Next
0. FIRST: overnight run m3a n01 (8fd8743) looped 6,688 calls 00:22-06:54: ARCHITECT step failed repeatedly, sim user answered "Try again" ~2,200x (log C:/seldon/tests/m3a/n01.log). Triage the ARCHITECT failure (M3 regression) and the endless retry (repeated failure must go planner-first, sim user must not loop). Also add a stall watchdog to cohort2.sh. Every run launch pairs with a 10-min CronCreate check (HARD rule).
1. 1 Terra ShelfLife run on 8fd8743 (regression). Score: product-copy + oracle + usage.py + judged.py.
2. ShelfLife dictated in two waves, 1 run.
3. Quiet Bench (rig lane: work/ladder/briefs/L3/4-quietbench.json, quietbench_oracle.py): 1 run, then 5. Plain-Terra baseline command in work/lanes/rig-report.md.
4. M3 exit: held-out sealed second dream (separate reviewer writes brief+oracle).
5. Look for cuts in the +349 M3 lines once runs prove it.
Testing ladder: 1 run, then 5; 20 only at milestones. Terra for tests.

## Loop log 2026-11-19
- 00:xx microLean landed 6beb500 (gate 104/104, no env). Astra 6.2 prompt review done (design-review/astra62-prompts-2026-11-19.md). prompts2 lane 1 launched on Sol 6.2. Heartbeat cron every 30 min drives AGENDA.md.
- prompts2 landed 21b6381 (trial switch, off by default; cohort2 passes ON=). replayAB lane launched on Sol 6.2.
- loop: replayAB still running; judgeEval2 launched (real-defect judge cases + 2-arm judge prompt eval).
- loop: replayAB landed 49404d5; judgeEval2: judges 0/6 real defects on Terra both prompts; launched replay A/B generation (Terra, 5 WORK pairs) + judge eval on Sol 6.2 both arms.
- loop: replay tool got --full-access (Windows elevated sandbox can't deny :root; uncommitted in main tree until generation proves it); prompt A/B generation running (replayAB-21, 10 Terra builds); Sol 6.2 judge eval both arms running. 10-min check on both.
- loop: found Seldon used the 2nd Codex install (AppData npm, 0.164) -> updated it to 0.170; Sol judge eval (judgeEval2-15/16) and prompt A/B generation (replayAB-22) restarted and running.
- loop: judge 'recall 0/6' was a grading artefact (narrow keys + folded 'findings' shape unparsed); Terra AND Sol judges did flag the Stop/cancellation defect as must-fix. Replay tool double-write bug fixed; prompt A/B regenerating (replayAB-23). Next: blind semantic adjudication Terra vs Sol vs prompts2; trace why micro4c reached C despite judge Stop findings.
- loop: real micro4c Terra judge said satisfied on Stop; replays: Terra 2/6 catch, Sol 2/2 -> judge noise; added 'judge model in test runs' to For Oren.
- loop: replay tool fixes committed 04f8de0; prompt A/B generation running (replayAB-23); blind Sonnet grading of 42 judge findings vs keys (Terra/Sol x control/prompts2, sealed key) launched.
- loop: blind strict grading: judges catch ~1/14 real defects on any model/prompt; most answers satisfied; favicon/handles/code-quality never caught -> evidence lane queued before judge-model decision.
- loop: prompt A/B generation done (10/10, replayAB-23); packaged blind; two Sonnet reviewers voting on 5 WORK pairs (ballot-1/2.json); key sealed in private/.
- loop: prompt A/B unblinded: B (prompts2) wins code quality clearly 3/5 + both whole products, but lost fidelity once (renamed user's literal labels) and completeness once -> stays OFF by precommitted rule; prompts2b lane (verbatim user words + failure-path bar) launched, then re-run A/B.
- loop: evidence lane landed 3bf204d (gate 125/125 no env; judgeEvidence trial off by default). Started ShelfLife + Quiet Bench Terra runs with ON=judgeEvidence to measure whether judges now catch known defects; 10-min check on.
- loop: judgeEvidence runs: ShelfLife 37/40 (search/filter fails = oracle literal vs separate 'soon' panel), judge satisfied incl. code quality despite one-line app.js; Quiet Bench 8 pass/0 fail/6 unverified (was 8/2/4), 21 calls, 19 min, Stop now works, judge flagged golfed code only as nit. prompts2b landed 9375856; A/B round 2 generating (replayAB-24). Queued code-quality severity coaching.
- loop: replay re-pinned to 9375856 (round 2 generating, replayAB-25); codeSeverity lane launched (golfed code = must-fix in the judgeEvidence rubric).
- loop: codeSeverity green (waits for round-2 generation before landing); Astra 6.2 writing 3 SMALL-rung dreams + sealed oracles (work/ladder/briefs/S, C:/seldon/sealed/small).
- loop: codeSeverity landed 7be4158. Prompt A/B round 2: B wins code quality 4/5 (both reviewers), fidelity fixed, but 3 split single-reviewer losses on component pairs -> strict rule fail, stays OFF; decision added to For Oren.
- loop: launched ShelfLife + Quiet Bench with ON=judgeEvidence on 7be4158 (code-quality severity) to see if golfed code now gets a fix round.
- loop: code-quality severity works (ShelfLife app.js 27 lines/602-char max -> 146 lines/122 max) but stricter judge sent a small stale-notice UI issue to the user; Quiet Bench hit 'Every feature needs a requirement' step failure in DETAIL -> featureReq lane launched.
- loop: featureReq landed 114c4a8 (lane gate 129/129 no env on exact main base). Quiet Bench rerun with judgeEvidence started (frQB), 10-min check on.
- loop: 'Node 20' UNIT question = real dream-vs-machine mismatch (dream says Node 20, machine has v25.8.0); ideally the planner decides (use available, note it). Minor; noted for the planner-first coaching backlog.
- loop: launched ShelfLife + Quiet Bench with ON=prompts2,judgeEvidence (both trials) on 114c4a8 to give Oren real-run data for the two pending decisions.
- loop: escape-normalised ALIGN constraint match (both-trials Quiet Bench paused on JSON-escaped path) landed; Quiet Bench both-trials rerun (bothQB2).
- loop: both-trials runs failed on ALIGN/DETAIL bookkeeping refusals (prompts2 richer answers vs strict citation checks). alignNormalise lane launched. Recommendations for Oren recorded in AGENDA (prompts2 keep OFF for now; judges keep Terra).
- loop: alignNormalise landed 0f41344 (lane gate 134+1 test-only fix, exact base). Both-trials ShelfLife + Quiet Bench rerun (both3*), 10-min check.
- loop: both3QB looping on 2 more bookkeeping refusals (commitment handle in check; 'environment' as contract provider) -> refuseSweep lane: inventory every answer refusal, normalise all bookkeeping with one rule.
- loop: both3 runs: both stopped by the stall alarm on DETAIL bookkeeping refusals (refuseSweep lane addresses the class).
- loop: refuseSweep landed 8bf8550 (one rule: normalise derivable bookkeeping, re-ask only on meaning; ~30 refusal sites inventoried; +141 src). Both-trials reruns both4*, 10-min check.

## PARKED 2026-11-19 ~06:55 (Oren: unplugging for a couple of hours)
- main = 8bf8550 (pushed). Nothing uncommitted on main.
- In flight at unplug: both-trials runs (ON=prompts2,judgeEvidence) C:/seldon/tests/both4Shelf and both4QB (slots m1/shelflife-both4-8bf8550-b01, m1/qbu-both4-8bf8550-b01). If unfinished: do NOT reopen; just score whatever finished and re-launch fresh both-trials runs (cohort2.sh, ON=prompts2,judgeEvidence) with a 10-min CronCreate check.
- Crons are session-only and die with the session: on return, recreate the 30-min AUTONOMOUS LOOP cron and any run check.
- On return, FIRST confirm the PC actually went off (Get-CimInstance Win32_OperatingSystem | % LastBootUpTime) before claiming anything about the outage.
- Open decisions for Oren (AGENDA.md "For Oren"): prompts2 default (lead: keep off until both-trials real runs pass), judge model in tests (lead: keep Terra).
- Next agenda: both-trials result -> decide prompts2; then micro 5-run cohort; small rung dreams ready in briefs/S (sealed oracles C:/seldon/sealed/small).
- 06:55 both4Shelf (prompts2+judgeEvidence): SCRIPTED_C, oracle 39/40 (best ShelfLife), 0 part questions, 45 calls ~16 min 0.92M fresh; BUT web/app.js 16 lines max 1077 chars (golfed, code-quality judge let it pass). both4QB still running at unplug (44 calls).
- 07:03 both4QB: STALL at PRODUCT-JUDGE after 242 calls (planner-approach loop on the final quality judgment). Triage on return: why PRODUCT-JUDGE repeats and why the stall alarm needed 242 calls (identical-answer test too narrow; add a call-count/rate alarm).
- 09:20 resumed (PC did not reboot; boot 10-17). Added CALLS_ALARM (default 150) to cohort2.sh. productLoop lane launched (196 PRODUCT calls loop).
- loop: Oren chose dual mode (Lead + Orchestrator); Astra 6.2 drafting CHARTER-LEAD/BLUEPRINT-LEAD + design (UI/UX, coexistence, micro tests, lanes).
- loop: productLoop landed a4204ec (gate 143/143 no env). Zero-bug micro batch 1 started: hello x5 + Foundation x5 (trials off), 10-min check; batch 2 (ShelfLife x5 + Quiet Bench x5) after.
- loop: codeShape lane launched (measured code shape as a judge fact, judgeEvidence trial).
- loop 10:08: batch1 zero-bug census 10/10 C, 0 faults, 6 calls each; batch2 launched (zbShelf s, zbQB q).
- 10:12 batch1 census: functional 10/10 C, 0 fault records, 0 recoveries, 6 calls each (hello ~2 min, Foundation ~3 min). Hands-on review: hello output identical across 5. QUALITY DEFECT 5/5 Foundation: index.html inline CSS packed onto one line (304-1916 chars); code-quality judge passed it with trials off. Owner: codeShape lane (judgeEvidence trial). After landing, rerun Foundation x5 with SELDON_ON=judgeEvidence; if packing is gone, propose making codeShape default (outside the trial).
- 10:30 Oren: planner must write each bead's brief in words + schema attached. plannerBrief lane launched (trial switch, base a4204ec+codeShape). codeShape green, lands after batch 2.
- 10:35 Oren: CC at 38%, delegate more. Sol coordinator launched (coord.prompt.md): runs batch2 checks every 10 min, census, scoring, fault lanes, landings (no push), A/B. CC wakes hourly on COORD-STATUS.md only.
- 2026-11-19 10:25:50 +02:00 coordinator took over batch 2 at a4204ec, ShelfLife 4 terminal C receipts, Quiet Bench pending, codeShape queued and plannerBrief receipt pending.
- 10:50 Oren RATIFIED Lead charter v1.0 -> CHARTER-LEAD.md + BLUEPRINT-LEAD.md v0.1 in repo (pushed). Lead lane after the plannerBrief A/B; lab repo split proposed, unanswered.
