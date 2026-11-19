TRIAGE: BUG — P1 inferred bundle inputs from argv; P2 preview bypassed owned cleanup and used forbidden desktop control — sibling cases: none.
CHARTER: serves C14/C18/C20/C26 — final candidate violates no I#.
P1: completeness, hashes and baseline restoration use ONLY declared testRoots. Golden observes legitimate Contracts RED with a later Build's product file in argv, then Build GREEN with fallback RED still RED; missing-test recovery through C remains proven.
P2: preview is headless and completes automatically inside the existing bounded process owner. An uncontained golden caller verifies actual HeadlessChrome, owned Job membership/quiescence/zero processes, launcher-child server port closure and unchanged checkout; no outer teardown supplies success.
Boundary: removed the entire desktop-control handler and title fixture. The prior window-controlled 193.45s result is invalid and unused; the interrupted CLI has no credit. No user-browser attachment or visible preview.
PROD: +60/-62 (net -2) · TEST: +58/-21 (net +37); cases versus base: 19→19; size ratchet: 34846→34844, dispatch 2570→2554.
Final fast gate NOT GREEN under ≤600s: 19/19 passed (18/428.20s + web 1/186.72s); exact timing line: exit=0; wall_seconds=617.26. Budget missed by 17.26s; no timing retry.
Fresh focused checks: headless web GREEN/203.80s, CLI GREEN/346.54s. ONE full bash ../golden-gate.sh . stage-exec3 ran after the last candidate edit.
Base: cd52a3ada3e6d2c761e54dad25a9efa2a172b1f7 (golden-only snapshot of main b984d7f).
Patch: stage-exec3.patch · SHA256: 4234abd2796e84403b6712a24577c7143bd7b97bd0126a565c79339ae0c49cd6.
Evidence: golden-stage-exec3.log; C:/seldon/tests/stage-exec3/headless-full-gate-time.txt; discoveries and invalidated history: stage-exec3/docs/legacy-capability-audit.md (STAGE-EXEC3 rows).
Risk/next: fast budget remains unmet; shared-machine causality is unproven. CC re-review/serial integration is next. Scripted-provider evidence only; actual-provider ShelfLife/ladder acceptance unperformed. No pushes.
