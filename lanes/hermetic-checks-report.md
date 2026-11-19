Base: supplied e29d71f (base 050f3e8 golden-only); source uncommitted; no new dependencies or real provider calls.
Files/net lines: gitwork.py +6; proof.py +26; wave_verify.py -3; test_journey.py +6; new test_proof.py +122; total +157 (+193/-36).
Each worker reuses a private exact-commit checkout, reset/cleaned after checks; per-check temp/evidence live under run scratch.
New golden fault journey: RED herm-2 -> scripted C herm-4; four concurrent transient fixtures, discarded tracked/untracked writes, unchanged candidate, zero recoveries, screenshots available to judges.
Gate ONLY bash scripts/gate.sh herm-4 with venv first on PATH: 14 passed in 298.00s (base 14 tests; one new golden journey); existing recorded replays reach B/C.
Windows wave-of-4: before 0.563s (herm-2), after 0.703s (herm-4), delta +0.140s.
Earlier failures: herm-1 inherited T-99 bootstrap/timeout mismatch; herm-2 intended RED; herm-3 scale50 100.58s >90s, resolved by worker checkout reuse. Timing assertions unchanged.
Publication guard, CREATE_NO_WINDOW, cleanupVerified semantics and owner constants retained; unverified cleanup retains checkout and forbids reuse. Clean disposable checkouts remain under scratch for reuse.
Pending: lead review/landing and real-provider qualification; worker-authored binary source filtering remains the check-owner lane's T-56 part. Patch includes new file and passes reverse-apply check.
