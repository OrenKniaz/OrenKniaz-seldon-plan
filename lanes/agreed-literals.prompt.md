LANE agreed-literals (tickets T-119, absorbs T-63 and T-98). Worktree C:/Users/oren/codex-harness/work/lanes/agreed-literals-20261113 (Seldon main 9eddbb9). Temp only under C:/seldon/tests/alit-<n>. Gate ONLY with: bash scripts/gate.sh alit-<n> (C:/Users/oren/codex-harness/.venv/Scripts first on PATH). Do not commit. No new dependencies. Do not edit CHARTER.md or BLUEPRINT.md. Behaviour-only journeys, no unit tests. No real provider calls. Do not touch src/seldon/units.py or fixups.py (another lane owns them). Tickets per work/ladder/TRACKING.md.

Read CHARTER.md v1.7, BLUEPRINT.md v1.5 (R2, R4 contracts, R7, R12; "source judged once at unit"), then src/seldon/questions.py (ARCHITECT, DETAIL, REVIEW, unit judge prompts; DETAIL facts ~L215-256), architecture.py (contracts, assigned()), detail.py (contract_gap -> ARCHITECT), plan_review.py, and tests/seldon.

TRIAGE: DESIGN (lead + Fable consult). Evidence: M2 exit cohort #3 run z06 (C:/seldon/tests/m1/foundation-9eddbb9-z06/product): four areas asserted four different accessible names for the same Hello play button ("Play Hello", "Play: Hello greeting", "Play: reveal Hello greeting", "Play to reveal Hello greeting"); no contract carried it; u001's own check timed out and exhausted. Same family: T-98 (checks assert an engine error string nobody agreed), T-63 (an agreed literal the area could not see).

THE RULE: a check may assert an exact literal only if that literal is in agreed text visible to the area (accepted vision commitment, contract text, or its own requirement text); anything else is asserted by role, structure or behaviour; if two areas need the same unagreed literal, that is a contract_gap, never an invention. Corollary: an area never rebuilds another area's surface in its own fixture; cross-area checks run on the integrated product at wave level.

LLM decides semantics (which literals are shared and their text; whether an assertion is literal or role/behaviour). Code owns structure (delivers each agreed literal to every area that needs it; routes contract_gap to ARCHITECT, which exists). Do NOT add a check-source linter, literal registry, or new node kind; contract text is the shared-literal store.

CHANGES:
1. ARCHITECT prompt: contract text states every exact user-visible or machine-visible value two areas must share (labels, names, messages, ids, routes) and nothing more.
2. DETAIL prompt: the rule sentence; extend "do not invent an agreement" with "an exact value asserted by a check is an agreement".
3. Area REVIEW prompt: name any check that depends on an exact value absent from the vision, contracts or requirements as a concrete gap.
4. Unit source-judgment question: the same sentence (worker-written checks judged once at unit).
5. T-63: each area's DETAIL facts include the accepted commitments and the exact contract text it consumes or provides.
6. Delete any per-case guidance that lists specific strings or engines (e.g. error-string handling for T-98) if present.
Keep prompt additions to one sentence each; owner constants elsewhere stay word for word.

LEAD DECISIONS THAT MUST SURVIVE: everything on main (T-116 architecture review and labelled uncertainty, P10 rules, T-111 owned scope, T-113 own consumes, FLOW, fixups, judge-minimal, behaviour-only final judges, timing asserts, recorded real-question journeys and recorded replays reaching B or C). If a recorded replay's prompt hash or bytes change, re-record only by the existing mechanism and say so.
JOURNEYS (outcome only): a fault twin where stub DETAIL answers from two areas assert an unagreed shared literal -> contract_gap -> one ARCHITECT revision puts the literal in contract text -> run reaches B (or C); an area's DETAIL question carries the contract text it consumes; REVIEW bytes still flat 1 vs 50 units.
DELIVER in C:/Users/oren/codex-harness/work/lanes: agreed-literals.patch (git diff --binary, include new files), agreed-literals-report.md at most 10 lines: files and lines (net), journeys and gate seconds, prompt sentences added, anything wrong.
