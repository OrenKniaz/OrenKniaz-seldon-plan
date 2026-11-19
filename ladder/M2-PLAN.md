# M2 plan (lead, 2026-11-12)

Source: Astra read-only review of the frozen drafts `m2-flow-20261111` (abfd4a5) and `m2-area-20261111` (6733da7) against blueprint v1.4. Full text: `work/lanes/astra-m2-review.md`.

Order: L1 records+skeleton -> (L2 wave proof+flow review || L3 local fixups, disjoint files; freeze the failure interface first) -> L4 ARCHITECT+DETAIL -> L5 area REVIEW. The lead wires run.py, states.py, store.py, questions.py and the journey per landing. M2 starts after T-85/T-86/T-87 land and a canonical Foundation run reaches C without new failures.

Do not land either draft wholesale. I compared their changes from M2 base `2fc6bac`, read the new modules, and checked against the supplied checkout at `e63839c`; its local `main` ref is older.

The flow draft (`abfd4a5`) builds ARCHITECT, parallel area DETAIL, recursive subdivision, contract dependencies, area REVIEW and later-wave continuation. Its area boundaries, single contract provider and merged approval fit M2. It builds planning before the required verification foundation, lacks the new flow-review replacement, and retains reviewer-selected walkthroughs, file inspections, final source reads and a whole-product quality question. Skeleton-first is largely prompt guidance, without durable placeholder obligations.

The area draft (`6733da7`) extends that draft with contract-crossing facts, WAVE-FLOW, scoped decisions, file prerequisites, failed-check repair and placeholder tracking. Those additions address real M2 needs. However, WAVE-FLOW still calls the source-reading feature judge, PRODUCT judgment remains, and flow gaps end the run instead of creating local fixups. Both drafts also include later-wave machinery belonging to M3.

Reuse selectively; paths below are under `src/seldon/` in the named draft:
- From area `architecture.py`: `contracts_for`, `endpoint`, `area_decisions`, `crossed_contracts`, and the ownership/link checks in `local_plan`, `merge` and `subdivision`; adapt them to current main.
- From area `fixups.py`: adapt `assign` and `checks_for`; from `obligations.py`: adapt `for_area` and `remaining` to canonical obligations and flow verdicts.
- From either `plan_review.py`: retain area grouping, bounded calls and code combining verdicts. Drop `choose_walkthrough`, inspection selection and inherited walkthrough state.
- Drop both drafts’ `questions.feature_brief`, `product_brief`, inspection helpers and `gitwork.inspection_catalog`. Defer `area_product.py` source paging and later-wave continuation.
- I found no homemade evidence-reuse hash scheme in these modules: `Store.artifact` hashes stored bytes, not verdict validity. Preserve main’s Git scope-tree checks.

Proposed lanes, with new filenames where needed:
1. Records and skeleton: `schema.py`, `plan.py`, `obligations.py`. Exit: one canonical Area/Contract/Decision model, one provider per contract, runnable skeleton, and open placeholders blocking C.
2. Wave proof and flow review: new `wave_verify.py`, `flow_review.py`, plus `proof.py`. Exit: all accumulated checks on one commit; one behaviour-only question per flow; code combines results; old DEMO/PRODUCT judgments removed.
3. Local fixups: `fixups.py`, `units.py`. Exit: failed checks and flow gaps reach the owning scope, repair survives reopen, and unrelated units and verdicts remain valid.
4. ARCHITECT and DETAIL: `architecture.py`, new `detail.py`. Exit: architecture writes no units; area questions run concurrently; code merges links and scopes; uncovered agreements return to ARCHITECT.
5. Area REVIEW: `plan_review.py`. Exit: bounded reviews cover every area and feed one B approval, without choosing walkthroughs or inspections.
Order: 1 → 2 and 3 concurrently on disjoint files → 4 → 5. Freeze the failure interface before 2/3 start.
The lead alone wires `run.py`, `states.py`, `store.py`, `questions.py` and each landing’s `tests/seldon/test_journey.py` extension.

Brief risks: preserve main’s newer judgment and disposable guide checks; preserve staged edits; explicitly define flow coverage, contract-change invalidation, placeholder closure and fixup ownership, including older scopes.
Measure question sizes at 1 and 50 units, including real recordings, plus total judgment calls/bytes. Array limits alone do not bound incoming facts.
Keep M3 continuation out. M2 acceptance remains Foundation 8/10 and ShelfLife C in 3/5, at least matching the plain-agent oracle, on one candidate.
This was source review only: no tests, providers, edits or tracking writes. The lead should record these findings.

## M2 exit cohort (lead, 2026-11-13)
- Foundation: 10 canonical runs on one named commit (`C:/seldon/tests/m1/val-e5a4ead/foundation-canon.txt`); exit 8 of 10 reach C without new failure classes.
- ShelfLife fight (P5): dream `work/fight-1/shelflife-brief.md`; oracle `python work/fight-1/oracle.py <product_dir> <label>` (40 black-box checks; Playwright Chromium; hardcoded C:/seldon/tests/fight-1). Seldon side: `tests/seldon/real_hello.py <slot> --dream-file work/fight-1/shelflife-brief.md`, then copy the delivered product (server.py, import_items.py, README.md) to a clean dir and run the oracle. Plain side: rerun `python work/fight-1/fight.py native` the same day (gpt-6.1-sol medium) for a same-model baseline; previous baseline 36/40 (oracle-native-r2.json; 3 of 4 misses from one CSP bug). M2 exit: ShelfLife C in 3 of 5, oracle score at least the plain agent's.
