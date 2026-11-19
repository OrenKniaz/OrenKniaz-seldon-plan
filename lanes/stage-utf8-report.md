CHARTER: serves C1/C18/C23 — violates no I#.

CODE: machine JSON uses explicit UTF-8 at process boundaries, without encoding guesses. Scope is transport; no planning, consent, provider policy or acceptance changes.

- Producers fixed: `record_io.write_stdout_json` writes and flushes UTF-8 bytes; `plan_cli`, mail success/error JSON, spine impact JSON, and semantic worker/result/timeout JSON use it.
- Consumers fixed: audited-process stdout/stderr decoding on Windows and POSIX; shared dispatch Git text reader (including dispatch_attempts); acceptance revision and adapter provenance subprocess readers.
- Audited unchanged: `seldon_cli` emits human init/version/diagnostic prose, not machine JSON. MCP stdio, project-init handshake, provider readers, worker/judge record files and review diagnostics already specify UTF-8.

Existing planning-surface golden extended: user text `1–80 “quoted” café 日本` enters real chat, reaches A, then the real status CLI returns that exact text and the same request ID through the audited-process reader. This catches locale corruption/crashes missed by the existing MCP-only Unicode path. No unit tests or new test definitions. Observed RED: cp1252 UnicodeEncodeError at plan_cli. GREEN: 5.75s with parent and child PYTHONUTF8=0 and cp1252 stdio. Separately confirmed this host defaults to cp1252 with PYTHONIOENCODING unset. Evidence: `C:/seldon/tests/utf8/red.log` and `legacy-green.log`.

Delta against supplied f965c26-based golden-only snapshot: 10 files, +44/-29; production line delta 0; test-count delta 0. Final source total 32165, unchanged ceiling 32165. Patch reverse-apply check and diff whitespace check passed. No commit/push; no lane-local revision identifiers in deliverables.

Gate invoked ONCE: `bash ~/codex-harness/work/lanes/golden-gate.sh ~/codex-harness/work/lanes/stage-utf8 utf8`.

Gate: FAIL (exit 1) — 9 passed, 2 failed in 550.84s; browser phase 1 skipped in 21.67s. Log: `~/codex-harness/work/lanes/golden-utf8.log`.

TRIAGE: BUG — CLI golden cannot archive missing historical object c7219cb; sibling historical-fixture journeys also require retained history. Next action: validate the patch in the owning full-history checkout.

TRIAGE: BUG — initial candidate exceeded source ceiling by seven lines. Corrected after the gate by compacting the new writer and removing redundant subprocess text flags; transport behavior unchanged. Final count verified directly; gate was not rerun, so its original failure remains reported.

TRIAGE: BUG — browser launch closed before readiness; diagnostics include GPU exits and access-denied cleanup. Browser evidence remains UNVERIFIED; no privilege changes or denied-action retry attempted. Next action: owner resolves browser runtime before browser acceptance.

Last proven outcome: Unicode status readback at A under legacy Windows encoding. Live-provider continuation beyond A and full product acceptance remain unproven; this patch supplies fake-provider journey evidence only.

Patch SHA-256: `72cbc35cb2968b97ffc6d48f930d71d5276980777a87b3baf85b5b7d66df517d`.

## Round 2

CHARTER: serves C1/C18/C23 — violates no I#.

P2 corrected: audited third-party/product stdout and stderr are evidence text, decoded as UTF-8 with replacement on both Windows and POSIX. The changed Git text readers and process-list reader use replacement too; no Git encoding configuration is assumed or changed. This supersedes Round 1's strict decoding of arbitrary evidence. Seldon's machine JSON producers remain explicit UTF-8; status readback and the semantic-worker JSON consumer capture bytes and decode strictly before parsing.

The existing planning-surface journey now also audits a real command emitting valid UTF-8 and raw cp1252 `0x96` on stdout/stderr. It requires successful completion, intact UTF-8 text, and readable replacement evidence on both streams. Earlier Unicode-only coverage could not catch the invalid-byte crash. Observed RED: UnicodeDecodeError at audit_process.py decoding `0x96`. GREEN: 9.27s under PYTHONUTF8=0 and cp1252 stdio, including strict Unicode status readback. Evidence: `C:/seldon/tests/utf8b/red.log` and `green.log`.

Current aggregate delta: 10 files, +58/-32; production line delta 0; test-count delta 0. Source total 32165 at the unchanged ceiling. AST parsing, whitespace check, patch checksum and reverse-apply check passed. Historical object c7219cb now resolves; its retired-permission journey passed during this gate.

Round 2 patch SHA-256: `a45a283d895293c023c7df067412deaa8bc803ca62f2a31724508c04dd6b248a`.

Round 2 gate invoked ONCE: `bash ~/codex-harness/work/lanes/golden-gate.sh ~/codex-harness/work/lanes/stage-utf8 utf8b`. Result: exit 0; 11 passed in 849.30s (14:09), then 1 browser skip in 6.22s. Both prior test failures are resolved, including the complete CLI journey and source-size guard. Log: `~/codex-harness/work/lanes/golden-utf8b.log`. No source edits after starting this gate; no gate retry.

TRIAGE: BUG — the gate exceeds the ten-minute ceiling despite passing assertions; sibling execution/recovery journeys are long-running (main path 623.48s). Timing causality versus the baseline was not measured. Owner: existing golden/runtime owner; exit test: preserve semantic coverage while completing the gate within 600 seconds on the intended test host. Runtime optimization is outside this decoding repair.

TRIAGE: BUG — browser readiness remains UNVERIFIED: browserContext.newPage reports the target/page/context closed. Owner: browser runtime; exit test: readiness and the browser journey complete on the intended Windows host. No security/privilege changes or manual denied-action retries were attempted.

Last proven outcome: audited legacy-byte evidence completes without a decoding crash, strict Unicode machine-JSON readback succeeds, and the non-browser fake-provider gate passes. Browser and live-provider product acceptance remain unproven. No commit/push.
