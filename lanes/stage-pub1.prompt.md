Seldon lane stage-pub1 (Sol high). Tree: ~/codex-harness/work/lanes/stage-pub1 (base = Seldon GitHub main f965c26, golden-only copy). Read CHARTER.md (binding), AGENTS.md, then ~/codex-harness/work/ladder/design-review/partial-publication-audit.md (your spec), recov1-host4-diag.md, web-phase-race.md, and work/ladder/SWEEP-BACKLOG.md (PUB1, TD#6, CONTROLLER-LOSS-PRE-ENTRY, WEB-PHASE-RACE).

CHARTER: C2/C14/C18/C23/C26; I1/I6/I9.
TRIAGE: DESIGN — one logical fact is published by 2+ writes and readers (loop, status, cockpit, MCP, acceptance, recovery, test observers) can observe the gap; 6 host reds in 2 days.
SIMPLEST (one rule): "An owner publishes one identity-bound terminal outcome LAST, after its required artifacts exist. Every consumer — including tests — reads that outcome; earlier records mean pending." CODE owns publication/consumption structure; LLM supplies semantic verdicts only. No new framework, store, lock or counter.

Apply in the audit's order, stop when the budget is spent (do 1-3 fully; 4 only if net-negative and cheap):
1. Admission + recovery: complete admission binding before a segment is selectable; publish outcome+cleanup through the segment owner; consumers (job status, evidence admission, recovery context) read the segment outcome, not the root mirror; delete root-mirror precedence/fallback branches. Remove absence-based certainty before the outcome.
2. Interrupted revalidation: _consume_completed_effect lacks a judgment-continuation branch — consume the retained terminal result after interruption, then settle the cursor.
3. Validation/delivery: delivery completion is published once (one terminal fact); VALIDATED alone never implies delivery; delete premature completion inference.
4. Materialization/advisory readers follow the owner's completed selection.
Target: net-NEGATIVE src (audit estimate −40..−100). Report the delta per item.

Tests: golden/journey only (NO unit tests, no tautological tests), outcome assertions; add fault twins where a gap was product-visible (e.g. kill between the two writes → reader sees pending, never a wrong claim; interrupted revalidation → consumed once). Existing observer fixes from 2e/noP stay.
Rules: temp/basetemp only under C:/seldon/tests/pub1; NO LANE-LOCAL SHAS; no commit/push; no screen control; no shared-env installs. Gate: `bash ~/codex-harness/work/lanes/golden-gate.sh <tree> pub1` at most twice (web may skip in your sandbox — say so). Cold-start import check with PYTHONPATH=src.
Deliver: lanes/stage-pub1.patch (+ .sha256) and lanes/stage-pub1-report.md (CHARTER/TRIAGE/SIMPLEST lines, per-item what changed + deleted, src/test delta, gate). Final message: SHA, delta, gate line.
