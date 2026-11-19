CHARTER: serves C13/C14/C18/C26 — violates no I#. Read-only; no files changed, tests run, or providers launched.

1. **Yes, the worker ran:** run `bb5614d9e7b8`, B1, Codex `gpt-6.1-sol`/medium; `didExecuteRealProvider=true`, exit 0. It wrote `server.py`, `pantry.py`, `import_items.py`, `static/{index.html,styles.css,app.js}`, `README.md`, and `tests/test_integration.py`. **It never created `tests/test_browser.py`.**
   T1 declared `argv=["python","tests/test_integration.py"]`, `testRoots=["tests/test_integration.py"]`; T2 declared the corresponding browser-file argv/root.
   Controller validation failed **while preparing fallback RED**, before semantic tests ran: [planner_candidate.py:123](/C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_candidate.py:123), introduced by exec1 `6aff167`.
   Exact operation: `git --literal-pathspecs restore --source a8f9b1c46c189bdec12fca9db20b82259b641053 --worktree --no-overlay -- tests/test_browser.py tests/test_integration.py`; exit 1: **`error: pathspec 'tests/test_browser.py' did not match any file(s) known to git`**.
   Crucial correction: `a8f9b1c` is the **candidate**, not the baseline; baseline is `84030c2f`. Separately, the worker’s integration suite reported four tests, three cleanup errors (`PermissionError: [WinError 32] … pantry.db`); subsequent connection/interpreter fixes were unverified.

2. **TRIAGE: BUG — unfinished worker output plus poor missing-bundle diagnostics.** The declared browser file is missing from the candidate itself; this does **not** establish that restoring newly created tests onto an older baseline is broken.
   `testRoots` filenames are valid: [planner_schema.py:403](/C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_schema.py:403) teaches exactly that shape. The declaration describes intended output; the worker stopped before fulfilling it. Siblings: omitted test modules/helpers and partially completed bundles. Seldon’s `execution_sources` retains missing files as null hashes, then exposes a Git exception.

3. **Tests-first proposal:** add contracts bead B0 owning both test files; make B1 depend on B0 and own only product/docs. B would change from one exact worker assignment to two sequential assignments; models/reviewers, `maxParallel=1`, timeout 1800 and product scope stayed unchanged.
   **Scope+limits consent could cover this only if it explicitly authorized same-scope bead repartitioning within the approved provider/model envelope.** Merely removing `planRevision` would not suffice: [approvals.py:167](/C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/approvals.py:167) also fingerprints exact worker/bead assignments. Current consent therefore required another card. The earlier turn-4 refusal was revision-only; its card diff confirms that.

4. **`spine-parent-kind-not-allowed`:** DISC2 included bead B1 as a discovery parent; `spine.py:32` excludes beads. The planner corrected parents to R2/T1/T2 successfully.
   **Generic tool errors:** event #76 requested `harness_schema(tool="semanticScenarios")`, mistaking a response section for a tool; #212 was `harness_worker_status` reporting the already-described Git failure—no additional crash.

5. **Concrete fixes by owner:**
   - **Missing bundle — worker B1; `runners.py`/`planner_candidate.py`:** finish the browser test, and report missing declared candidate inputs before attempting baseline materialization; retain failed/unproven status.
   - **Consent churn — `approvals.py`:** bind B to approved scope, provider/model permissions and limits, explicitly permitting internal repartitioning; keep revision binding for review/evidence.
   - **Ancestry/schema calls — planner caller:** use allowed discovery parents and request an actual tool’s schema; both already have supported corrections.
   - **Cleanup — ShelfLife `pantry.py` and `tests/test_integration.py`:** close SQLite connections and wait for owned server termination before deleting temporary databases; verify the retained repair.
   - **Preview mismatch — `dispatch.py` worker guidance / preview adapter:** provide a served preview for this HTTP app; `--preview .` sought nonexistent root `index.html` and returned `ERR_FILE_NOT_FOUND`. Process inspection also returned `Access denied`; preserve that stop and use supported owned-process cleanup.

Last proven transition: worker output retained as candidate `a8f9b1c`; integrated validation and working ShelfLife remain unproved.