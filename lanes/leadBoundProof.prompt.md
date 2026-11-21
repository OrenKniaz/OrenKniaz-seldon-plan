# Lane leadBoundProof (Sol 6.2 medium). Codex quota ~5%: be economical; if Codex reports a usage limit, stop and write the report with what is left.

Repo: this lane dir = Seldon main 64f465f. Binding: CHARTER.md, CHARTER-LEAD.md v1.1, BLUEPRINT-LEAD.md v0.3 — read section 2a "Bound proof" first; it is ratified and is the spec for this lane.

## Why (~/codex-harness/work/ladder/census-lead-1.md, T-270, T-271)
- T-270: of 33 Lead ShelfLife lead_failure rows, 32 came after the builder's checks exited 0. The judge asked for a new witness each round (one more negative case, then the neutral style, then an explanatory error). Outcome: 1/5 C, 37 WORK, 34 JUDGE. Two LLMs are negotiating the proof standard with no shared text.
- T-271: ls05's judge prompt was 11.4 MB, mostly Playwright node_modules committed under docs/try-it/work/fresh. The judge source projection must exclude generated dependencies and scratch, and the walkthrough's scratch must live outside the product tree.

## Build (as the default; keep SELDON_OFF=leadBoundProof for the old path)
1. B: each promise's schema gets `notMetIf` (one or two plain-words wrong behaviours). It is planner semantics; the planner writes no checks. Normalise if it is missing (ask the planner to amend it, never refuse).
2. The builder brief quotes action, result and notMetIf per promise. Checks are written against exactly that text.
3. Judge: a must-fix must quote the B line (result or notMetIf) the product or check violates, plus the evidence. Anything else is a note, visible, and never sends work back. Missing or ambiguous B means a planner amendment, not a judge standard. Reuse an earlier verdict when the code and evidence are unchanged.
4. Repair resumes the same builder session where the provider supports it (codex exec resume <id>), carrying the quoted line and the observation. Fall back to a cold session otherwise.
5. T-271: the judge source excludes node_modules, venvs, build outputs and walkthrough scratch; the walkthrough scratch goes outside the product.
Net src lines in lead.py + judgment.py must be ≤ 0 (delete the old strength-negotiation coaching that this replaces). Report the reachable-lines change.

## Prove
- Golden/journey tests only (no unit tests, no timing asserts). Extend the golden path so a judge must-fix without a quoted B line becomes a note.
- Cold-import every changed module. Gate: PATH=~/codex-harness/.venv/Scripts:$PATH bash scripts/gate.sh leadBoundProof (no SELDON_* env).
- Real exit: Lead ShelfLife x1 on Terra medium from this lane's src (cohort2.sh, as the coordinator ran leadShelf7; read cohort2.sh). Report WORK, JUDGE, lead_failure, recoveries, wall min, C. Target: ≤2 WORK, C verified. If quota allows, run Foundation x1 too.
## Report: C:/seldon/tests/leadBoundProof-0/REPORT.md, ≤25 lines. Leave a git diff; do not push. Temp only under C:/seldon/tests/leadBoundProof-0. Never open desktop windows.
