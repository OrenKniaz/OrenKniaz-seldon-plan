# Semantic default deletion ledger

Candidate: cc/semantic-wiring, base 0a656d1. These are nonoverlapping production
ranges in this working tree, counted inclusively, excluding separating blank lines.
Nothing listed here is deleted by this opt-in slice. This is a conservative inventory,
not a claim that all related call sites/tests can be deleted without migration.

Charter: rules 3, 4 and 7; planner-owned data reaches controller-proven CLI behavior.
Owner/scope: canonical spine/store, existing worker packets and sequential dispatcher;
legacy stays default. No new tools, provider launches, publication or new scheduler.
Acceptance: new opt-in/data/RED/error/immutability/Validation tests plus owning regressions.
Budget: <=650 net production and <=350 test lines; tool-count delta zero.

Delete these old-path ranges only when semantic-v1 becomes default and their existing
CLI/MCP/status/review consumers have been migrated. Keep semantic scenario/contract
immutability, ordinary review/publication, process cleanup and candidate identities.
`show_node` retains its generic node-reading interface; only its protected-test
branch is counted. Claim helpers require migrating the
remaining legacy proof-accounting/acceptance consumers to semantic receipts first.
Do not delete shared requirement-file revision/path guards or `audit_process`:
semantic-v1 reuses them for frozen data and process containment.

| File | Old-path owner | Lines | Count |
| --- | --- | --- | ---: |
| `src/codex_harness/core/test_audit.py` | `_interface_assertion` | 57-114 | 58 |
| `src/codex_harness/core/test_audit.py` | `_expectations` | 194-340 | 147 |
| `src/codex_harness/core/test_audit.py` | `_cli_expectations` | 343-500 | 158 |
| `src/codex_harness/core/test_audit.py` | `_cli_launch_matches` | 503-541 | 39 |
| `src/codex_harness/core/test_audit.py` | `_bound_cli_launches` | 544-616 | 73 |
| `src/codex_harness/core/test_audit.py` | `_cli_stub_provenance` | 619-641 | 23 |
| `src/codex_harness/core/test_audit.py` | `_owned_cli_stub` | 644-754 | 111 |
| `src/codex_harness/core/test_audit.py` | `_failure_provenance` | 757-1009 | 253 |
| `src/codex_harness/core/test_audit.py` | `_ProspectiveWorkspace` | 1012-1043 | 32 |
| `src/codex_harness/core/test_audit.py` | `audit_prospective_tests` | 1046-1440 | 395 |
| `src/codex_harness/core/test_audit.py` | `_overlay_requirements` | 1443-1457 | 15 |
| `src/codex_harness/core/test_audit.py` | `_proof` | 1460-1468 | 9 |
| `src/codex_harness/core/test_audit.py` | `audit_revised_tests` | 1471-1616 | 146 |
| `src/codex_harness/core/plan_store.py` | `PlanStore.revise_test` | 422-520 | 99 |
| `src/codex_harness/core/plan_store.py` | `PlanStore.show_node protected-test branch` | 268-352 | 85 |
| `src/codex_harness/core/plan_store.py` | `PlanStore.record_audit` | 1585-1589 | 5 |
| `src/codex_harness/core/plan_store.py` | `PlanStore._insert_audit` | 1591-1607 | 17 |
| `src/codex_harness/core/plan_store.py` | `PlanStore.passing_audit` | 1779-1829 | 51 |
| `src/codex_harness/core/mcp_planner.py` | `_node_test_blocks` | 829-853 | 25 |
| `src/codex_harness/core/proof_imports.py` | `_protected_tests` | 95-131 | 37 |
| `src/codex_harness/core/proof_imports.py` | `protected_helpers` | 52-92 | 41 |
| `src/codex_harness/core/dispatch.py` | `_claim_inputs` | 417-460 | 44 |
| `src/codex_harness/core/dispatch.py` | `_claim` | 463-477 | 15 |
| `src/codex_harness/core/dispatch.py` | `_changed_claim_inputs` | 480-496 | 17 |
| `src/codex_harness/core/dispatch.py` | `_bead_prompt` | 574-596 | 23 |

**Total inventoried: 1918 production lines in 25 disjoint ranges.**

Additional retirement work, not counted above: remove legacy test-node/proofModule
branches in spine/graph, prospective publish/audit tool routes and schemas, protected
planner-test fixtures, and the legacy branch of worker_packet.build_packet. Keep
new worker unit tests and semantic source tests. Inventory these call sites when
migration is authorized; do not inflate this total with shared implementations.

## Observations and disposition

- Windows Git path length: a deeply nested worker-job test failed `git add` with an
  object-path error. Owner: existing dispatch/job workspace layout. DEFERRED inherited
  operator friction; this slice uses short disposable test roots and changes no global
  settings. Exit: the same ordinary job succeeds from a long workspace without OS or
  global Git changes.
- Actual provider execution and qualitative/user acceptance are UNPERFORMED by this
  code-only assignment. Owner: separately authorized qualification. Exit: an authorized
  real job yields linked Contracts RED and final Validation PASS, then the accepted
  Vision Lock quality/feeling is reviewed. Source/mock tests are not that evidence.

## Source validation and inherited failures

Final semantic regressions: 15 passed, including canonical planning/review/publication,
execution admission, real CLI RED/PASS, immutability, status, resume and no RED lesson credit.
Owning modules: 596 passed, 31 failed, 93 setup errors; dispatch: 119 passed, 33 failed.
All 157 failing/error case IDs and result types reproduced against untouched base 0a656d1.
No skips occurred. These are source/simulated-worker checks, not provider qualification.

| Existing test owner | Failed | Setup errors | Disposition / exit |
| --- | ---: | ---: | --- |
| `tests/python/core/test_dispatch_cancel.py` | 11 | 0 | DEFERRED inherited fixture/proof mismatch; repair owning fixtures against canonical contracts, then rerun affected cases. |
| `tests/python/core/test_dispatch_record_io.py` | 14 | 0 | DEFERRED inherited fixture/proof mismatch; repair owning fixtures against canonical contracts, then rerun affected cases. |
| `tests/python/core/test_dispatch_resume.py` | 1 | 0 | DEFERRED inherited fixture/proof mismatch; repair owning fixtures against canonical contracts, then rerun affected cases. |
| `tests/python/core/test_dispatch_timeout_resume.py` | 5 | 0 | DEFERRED inherited fixture/proof mismatch; repair owning fixtures against canonical contracts, then rerun affected cases. |
| `tests/python/core/test_dispatch_worker_transport.py` | 2 | 0 | DEFERRED inherited fixture/proof mismatch; repair owning fixtures against canonical contracts, then rerun affected cases. |
| `tests/python/core/test_plan_cli.py` | 1 | 0 | DEFERRED inherited fixture/proof mismatch; repair owning fixtures against canonical contracts, then rerun affected cases. |
| `tests/python/core/test_plan_quality.py` | 28 | 0 | DEFERRED inherited fixture/proof mismatch; repair owning fixtures against canonical contracts, then rerun affected cases. |
| `tests/python/core/test_readiness.py` | 1 | 0 | DEFERRED inherited fixture/proof mismatch; repair owning fixtures against canonical contracts, then rerun affected cases. |
| `tests/python/core/test_roundtable.py` | 1 | 91 | DEFERRED inherited fixture/proof mismatch; repair owning fixtures against canonical contracts, then rerun affected cases. |
| `tests/python/core/test_roundtable_overflow_protocol.py` | 0 | 2 | DEFERRED inherited fixture/proof mismatch; repair owning fixtures against canonical contracts, then rerun affected cases. |

Full named case list and command-output logs are retained outside the clone under
`~/AppData/Local/Temp/semantic-cc-pre-existing-failures.txt` and
`semantic-cc-{owners-final,dispatch-final,base-failures-2,base-dispatch}.txt`.

Corrected findings in this slice: nested status transactions from a mode read
(raw canonical snapshots now preserve legacy status); semantic publication freshness
no longer assumes oracle proof; Contracts RED cannot confirm lessons as validated.
The relevant canonical publication/dispatch regressions pass.
