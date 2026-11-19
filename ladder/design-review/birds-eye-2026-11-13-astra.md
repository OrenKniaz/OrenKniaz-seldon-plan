**Verdict: two boundary rules explain most of this family, but two premises in the evidence note are wrong.** At `050f3e8`, x07 is evidence pollution, not demonstrated oversized work; T-119 directly consumed recoveries in x01. Read-only review used retained records/products and exercised current assignment functions on actual stored plans; no runs or files changed.

- **z04/z05 — ownership failure confirmed.** Workers identified defects outside their scopes. Their reported targets included `runtime.cjs:130-132` and `index.html:8-10`; T-118’s strict path parser would reject those original forms too.
- **z06 — shared-contract failure confirmed.** Independent accessible-name assumptions broke composition. A shared value needs one agreement; this supports a narrower T-119.
- **x01 — repair fan-out, compounded by T-119.** n010 was correctly wave-only, but `traced_units()` assigned repair to **both u001 and u002**, not just u001. u001 immediately exhausted because literal objections had already spent both recoveries. The greeting owner subsequently corrected its check.
- **x03/x06 — shared-checkout interference strongly supported.** Both fixture writers have `finally` cleanup; no fixture directories remain. Concurrent WAVE-VERIFY checks inspect the same checkout while peers temporarily write there. “Leftover directory” is unproven; a transient-directory race fits the source and retained results.
- **x04 — execution placement failure confirmed.** n011 says “wave-level” in prose but structurally names only n009; current `assigned()` therefore runs it in u002’s isolated checkout without the HTML producer.
- **x07 — reject the oversized-unit diagnosis.** The product script is 273 bytes. Its patch includes 13 PNGs; the retained check-source projection becomes **371,634 bytes**, versus **17,335 without PNGs**, because `judge_brief()` decodes binary check files as text. DETAIL size discipline remains worthwhile, but this run does not prove it missing.
- **x09 — ownership failure followed by malformed-target refusal.** n015/n020 reopened all four product units. u002 correctly reported an out-of-scope correction; T-118 then interpreted `Correction assignment: n015 and n020` as a filesystem path and exhausted it.

**Rule 1:** Before execution, each check has a canonical author, execution stage, prerequisites and proof mode; failures route to the diagnosed defect’s owner, never automatically to everyone covered by the check.

**Rule 2:** Every check observes an exact source revision in an isolated execution workspace, with runtime scratch and evidence outside the source tree and excluded from source judgment.

These address concrete gaps in [assignment and tracing](C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/src/seldon/plan.py:57), [shared-checkout verification](C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/src/seldon/wave_verify.py:8), and [judge-source construction](C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/src/seldon/questions.py:318).

**CODE owns** canonical handles, unambiguous reference normalization, ownership lookup, stage/dependency enforcement, isolated execution and commit-bound observations. **LLM owns** check meaning, missing semantic prerequisites, defect diagnosis, shared agreements and sensible unit splitting at DETAIL. Ambiguous prose requires a bounded semantic correction; neither guessing a path nor charging a worker recovery is normalization.

**T-118: simplify, retain its intent.** Keep owner-directed repair and waiting. Replace free-text-as-path routing and its separate one-handoff allowance with the canonical correction route and existing bounded recovery/steering policy.

**T-119: narrow its blanket prohibition; do not revert the shared-agreement fix.** Shared assertions must respect agreed contracts, but local implementation literals need not all be architecturally ratified. Recorded objections to RGB values, `lang="en"` and `outlineStyle="solid"` show the current rule exceeding its purpose.

**Delete** coverage-to-repair fan-out, runtime-stage inference from requirement subsets, arbitrary discovery text passed directly to `safe_path()`, binary-to-text evidence projection, and concurrent checks against the published checkout. Preserve scope enforcement and candidate-integrity checks.

**Disjoint implementation lanes:**

1. `schema.py`, `plan.py`, `architecture.py`, `detail.py`, `plan_review.py`: canonical check author/stage/prerequisites; DETAIL establishes bounded responsibilities and validates executable dependencies.
2. `questions.py`, `inference.py`: structured correction subjects, exact normalization before semantic clarification, narrowed literal guidance, source/evidence separation.
3. `fixups.py`, `units.py`, `scheduler.py`, `flow_review.py`: consume canonical diagnoses; repair only implicated owners and preserve unrelated progress.
4. `proof.py`, `gitwork.py`, `wave_verify.py`: isolated revision-based check workspaces and external scratch/evidence.
5. `tests/seldon/test_journey.py`: one integration owner extends the golden journey in the landing patch—canonical planning through execution, concurrent scratch, external-owner repair and binary evidence; existing happy-path fixtures missed these boundaries.

**Most likely remaining break:** repair proof semantics. In x09, u001 strengthened a local check, then had to pass it as `preserves` on the known-broken base. Correct routing and isolation alone will not make that repair provable.