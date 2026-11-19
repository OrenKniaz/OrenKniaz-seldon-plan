TRIAGE: DESIGN — additive baseline copying violated exact bundle identity (P1); missing-build merge remedy corrected (P2 BUG) — siblings: fixture removals/replacements; none for P2.
CHARTER: serves C9/C14/C18 — uses DV2; violates no other I#.
Base: b6985fbaebaed7a16275962c454679545f778757 (lane scaffold of main 6114561); supersedes the review2-rejected candidate; its bypass-free admission constraints are retained.
Materialization: restore only declared testRoots from the committed integration candidate with literal paths/no-overlay (including deletions); verify the full bundle hash equals GREEN before observing fresh RED. Reuse uses that same identity.
Admission: contracts-only plans receive "add one build bead that depends on the contracts bead"; multiple builds keep the DV2 merge remedy. Existing 1j prepare/submit/read and retry ownership retained; bounded terminal traceback retained.
PROD: +88/-88 (net 0) · TEST: +132/-21 (net +111); cases: 19 versus base 19; fast marker retained; source ceiling unchanged versus base.
Verification: final full gate GREEN after the last candidate edit: 19 passed, 0 skips, wall 525.58s ≤600s (18 passed/291.78s + browser 1 passed/231.40s); targeted CLI GREEN/243.89s.
Golden: worker deletes a tracked fixture; helper enumerates fixtures before assertion RED→GREEN→C, with identical RED/GREEN bundle hashes and deleted fixture absent. Contracts-only refusal→public add-build replan→C; helper-change invalidation, persistence and cleanup retained.
Scope/risk: multi-build execution/final-HEAD support remains Stage 3a/DV2. Independent re-review and real-provider/ladder acceptance of this exact patch remain unverified; this lane uses scripted providers only.
Patch: ../stage-exec1.patch (exact diff versus base above; reverse-apply and whitespace checks passed); no commits or pushes.
SHA256: af8853ffe0f7f9fdb6c7a1650bffac3d2dafa70e310bbe64c269b5fcfa6366a3
Hash file: ../stage-exec1.patch.sha256; final log: ../golden-stage-exec1.log; scratch: C:/seldon/tests/stage-exec1/review2-cli-1.log. Only authorized golden commands ran.
