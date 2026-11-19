TRIAGE: DESIGN — absent/stale semantic verdicts lacked a shared durable owner — sibling cases: expansion/consent (1b), missing-qualitative-judgment (1c).
CHARTER: serves C2/C3/C4 — violates no I1–I9.
Changed: one typed Judgment in existing PlanStore events; canonical subject/evidence revisions, source snapshots, optional candidate, explicit verdict/rationale/meaning/gaps; no new store/engine.
Pending persists across reload; unsupported/inconclusive stay pending; initial malformed output gets exactly two exact fixes, then durable steer; every submission releases ownership and grants no human consent.
FINAL FULL GATE GREEN: 18 batch checks / 136.55s + web 1 / 277.50s; combined test elapsed 414.05s (<600s); suite 19 vs base 19; no skips; one authorized golden-gate.sh run, no other test commands.
Golden proves public submission→store→reload→consumer; current positive/negative decisions, subject/evidence/candidate invalidation, unrelated-branch preservation, correction success and exact retry exhaustion.
1b/1c contract: prepare_judgment → submit_judgment(raw response, source) → judgment(id, candidate=current identity); public harness_prepare_judgment / harness_submit_judgment / harness_judgment; harness_schema exposes shape/recovery.
Consumers use positiveCredit/concreteGap; both false while pending/stale. Meaning is open-domain; consumer owners enforce their semantic field shapes. Existing consent/execution/review migrations remain their assigned lanes.
Existing input validator/read-only node inspection moved to planner_schema; frozen owner ceilings preserved; discovery JUDGMENT-1 recorded in docs/legacy-capability-audit.md.
Base afacbd7f086c699492ce56300485d09f2f9b1c96; exact diff 5 files +483/-140; [stage-1j.patch](stage-1j.patch); SHA256 a8d2e4c1d461142f0202aad7d7c3fe8a7a3ba9f6c99f048667f86086970d3b8e ([checksum](stage-1j.patch.sha256)).
Next: integrate this prerequisite into 1b/1c, then establish L0; ladder_promoted=false; actual_provider_acceptance=false; no commits or pushes. Gate log: golden-stage-1j.log.
