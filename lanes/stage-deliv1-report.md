TRIAGE: BUG — deleting delivery's guard admitted provider configuration — sibling cases: none.
CHARTER: serves C8/C14/C15/C18/C20/C23/C26 — violates no I#.
BASE: d01ad3a5fef149642636178c25d442f49175bb99 (main 499cd4d lane snapshot); complete round-3 diff; no push.
OWNER: completion excludes reserved roots from productHashes using host registry PATH/permissions paths plus Git/Seldon metadata; no second provider list.
BACKSTOP: delivery refuses any remaining reserved-root entry before product writes; ordinary product dot-files remain deliverable.
GOLDEN: template .codex/config.toml stays observed but is absent from productHashes/workspace; product .gitignore is delivered unchanged through revalidation/C.
PROD: +140/-140 (net 0) · TEST: +86/-7; cases 19 vs base 19; no new test files.
CHECKS: CLI golden passed/464.29s; ONE final full gate GREEN, exit 0: 18 passed + 1 browser-unavailable skip, 570.27s; diff --check clean; LOG_OK.
LIMITS: CC reports round-2 normal-Chromium 19/19 and P1/P2 confirmed; round-3 unsandboxed web and actual-provider ShelfLife revalidation/C remain unperformed here.
PATCH: ../stage-deliv1.patch; checksum ../stage-deliv1.patch.sha256; scratch C:/seldon/tests/stage-deliv1; no screen/window control.
SHA256: 9e359dd58e313726c95c1e4b3551b9b8f9b3b7d97e8005797ad27b28fd6457c7
NEXT: CC review/run unsandboxed web on this exact patch, then apply/revalidate the original ShelfLife job and complete C.
