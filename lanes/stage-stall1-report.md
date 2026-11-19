TRIAGE: BUG — portable fallback omitted the established launch/cleanup contract — sibling cases: none (one shared boundary consumed by dispatch/acceptance).
CHARTER: serves C18/C14/C20/C25 — violates no I# identified; native portable execution and product acceptance remain unclaimed.
NOT READY: exact-candidate full suite GREEN (19/19, exit 0) after last edit, but fast gate MISSED: 743.83s > 600s; next: CC timing disposition. No retry in this round.
Changed: portable owner launches a private POSIX session/group, calls on_launch with the real PID, observes native CPU/output activity under a fixed deadline, kills only its group and verifies group absence before returning audit_control.
Windows Job class and full execution/cleanup branch are unchanged from reviewed round 2 (static reconstruction verified); consumers have no platform branch. No taskkill, denied retry, elevation or window control.
Regression/gap: successful portable providers previously lost provenance and consumers raised AttributeError; existing canonical golden now requires the owner payload PID to match persisted provenance and verifies zero-member cleanup.
PROD: +270/-310 (net -40) · TEST: +157/-70 (net +87); cases versus base: 19→19; no new cases/files; total production ceiling 34844→34804.
ONE full gate: 18 passed/531.40s + web 1 passed/209.91s; wall 743.83s, log ../golden-stage-stall1.log. No individual test failed; no other pytest command ran this round.
Portable evidence: syntax and independent impact checked only; this Windows host lacks os.killpg, so native Linux/macOS group behavior was not executed. No OS changes or new packages.
Independent Sol exact-patch impact review: APPROVE; Windows deadline/cancellation zero receipts observed again; git diff --check passed. No real-provider, ladder or full-vision acceptance.
Patch: ../stage-stall1.patch versus lane base 5b0ae422c6336202177913ed03b41abff173ee8d (main 43782a9 snapshot); no commit/push; discoveries in docs/legacy-capability-audit.md.
SHA256: 7349462b277c14ed881aa67945d15eae13d5b6bc51dfc5054aa165332f3e7eb7
