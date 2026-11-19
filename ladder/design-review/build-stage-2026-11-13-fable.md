# Build-stage failures f01/f02 (ShelfLife, main ad3a8a6) — Fable triage, 2026-11-13

Evidence: `C:/seldon/tests/m1/shelflife-ad3a8a6-f0{1,2}` (`calls/`, `product/.seldon/state.sqlite3`), `src/seldon/{units,questions,inference,providers}.py`.

## 1. f01 u002 "Provider timed out" — TRIAGE: BUG (classification), in `providers.py`
**Rule:** a deadline Seldon itself enforced (`result.timedOut`) is a code fact and always transient; "denied" is read only from the provider's own terminal error event, never from log noise.
- Timeout value: WORK runs as role `build` = **900 s** (`providers.ROLES`; `worker: 600` is dead, `role_for` never returns it). Call `call-2d632da3` ran 900.05 s, `timedOut`, `cleanupVerified`.
- Why it was terminal: `Codex.invoke` keyword-scans **stderr** for denial words. Codex printed its own start-up warning `codex_skills_extension ... failed to install system skills ... Access is denied. (os error 5)` (three fresh workers started in the same second; 2 of 7 WORK calls carry it). So `denied=True` -> `transient=False` -> `recover(retryable=False)` -> `exhausted` at recovery 1 with `recoveries=0` -> FAILED -> guide BLOCKED.
- Proof it is only the classification: u001 hit the same 900 s wall (`call-12144622`, resume call, empty stderr) -> `transient=True` -> REWORK -> resumed session -> DONE. f02 u002 likewise recovered.
- Progress: yes. u002's stream has 14 file_changes and 24 commands; last message "The local check now passes ... I'll finish the check documentation". It was minutes from done. The existing REWORK path (same worktree, `thread_from_recording`, resume session, R8) is already the "fresh life of the same unit"; it just was not taken.
- Tuning note (not design): 3 of 10 WORK calls across both runs hit 900 s while visibly progressing. Every hit spends a C18 recovery. Raise `build` to 1800 s, or the wall keeps eating the recovery budget on UI units.

## 2. f02 u002 "JUDGE brief is 84772 bytes (limit 65536)" — TRIAGE: DESIGN, in `questions.py` / `units.py`
**Rule:** a unit JUDGE is sized by the unit's own patch, each fact once; a patch too big for one question is split by code into more JUDGE questions on the same commit (R3). The product never shrinks to fit a brief. BLUEPRINT §5 already lists "the 64 KB error as a limit" under Drop.
- What the cap does today (worse than the failure itself): `UnitTooLarge` -> `recover` -> REWORK with `Exact failure: ... reduce the scoped text`. The **worker deletes tests and product to fit Seldon's byte count**, and it costs a C18 recovery. f02 u002: 121237 -> 84772 bytes by cutting checks 48.5 -> 25.6 KB (`establishment.cjs` deleted, wave check 17.8 -> 9.9 KB) and product 23.5 -> 18.0 KB. f01 u001 72458 -> 62651 and u004 75434 -> 61076 "passed" the same way. That is an unapproved narrowing (C21) and anti-C6, inside a quality fight. Hit in 3 of 5 product-unit first judgments.
- What grows the brief (f01 recorded questions; f02 from git trees at T/P):
  - `Check sources` 18-31 KB (f02: 48.5 KB) — largest fact.
  - `Product files at P` 2-10 KB (f02: 23.5 KB) **plus** `Product changes` (T..P diff) 2.5-11 KB (f02: 24.3 KB) — the same text twice on greenfield.
  - `Observations` 2-16 KB (4 KB tail x stdout/stderr x T and P per check); requirements + checks + contracts 6-11 KB; prompt/schema/example ~5 KB fixed.
- Scaling: not with unit count (each judge sees one unit), so R2's 1-vs-50 check passes. But `Product files at P` is the **whole scope tree at P** (`gitwork.blobs(scope + checkPaths)`), not the patch. A later-wave or brownfield unit scoped `static/**` carries every existing file there. So it does grow with the product; that breaks R2 on huge apps. Judge latency is not the limit: 61-63 KB judges answered in 26-31 s of a 180 s budget.

## Siblings
- `questions.bounded_unit` ARCHITECT/DETAIL 65536 cap: f02's largest DETAIL was 60551 bytes — next wall. Same rule: code subdivides the area (the prompt already offers `subdivide`), never a terminal error.
- `judgment.refresh_units` builds `judge_brief` at the final commit; `UnitTooLarge` there is not caught by the unit loop.
- `units.run_unit`: JUDGE `ProviderFailure` -> `retryable=False` -> FAILED + dependants BLOCKED after 3 transport tries. Never-block-delivery says: verdict "not judged" (DV6, labelled), unit integrates.
- Same stderr scan decides `ResumeUnavailable` vs denied; any stderr warning containing "login", "forbidden", "access denied" turns any failure non-transient.
- Exhaustion ends in "start a fresh run"; BLUEPRINT §3.2 says unit steering. One failed unit of N still ends the dream (f02: 3 units blocked behind one).

## Minimal change set
**Fix A (bug, <=20 lines, lead can land alone)** — `providers.py::Codex.invoke`: `denied` only when `not result["timedOut"]`, and only from `turn.failed`/`error` events in stdout (drop `stderr` from `native_errors`). Delete `"worker": ("medium", 600)` from `ROLES`; set `build` 1800.
- Journey twin: WORK stub times out once with a progress stream, then completes on resume -> unit DONE, `recoveries == 1`, run reaches C.
- Fault twin: same timeout, stub stderr carries the exact `Access is denied. (os error 5)` skills line -> same outcome (DONE). Replace the `native-denied` assertion: denial must arrive as a `turn.failed` event to stop after one call.

**Fix B (design lane)** — `questions.py` + `units.py`:
1. `judge_brief`: each file once and patch-bound. Files added base..P -> full text at P; files modified -> diff only; untouched scope files -> name and size. Delete the `Product changes` fact for added files. Open point for the lane: T-86 (a fixup life on a rebased base has an empty diff) is why the whole scope is sent today; the patch must be measured against the unit's first base, not the current one — confirm that id is still recorded before deleting the workaround.
2. New `questions.judge_briefs(store, ref)` returns 1..n questions. Over budget -> split on the seam the schema already has: (a) requirements + "Meaningful tests" with check sources and observations; (b) the other three `SOURCE_TARGETS` with the product patch. Still over -> pack files by bytes, each part naming the requirements whose check `command` names a file in it; un-named helper files ride with every part. A single file over budget goes alone, never refused.
3. `units.run_unit` JUDGING: ask each part, combine with the existing `judgment.combined` (code AND), record one `unit_verdict` listing its part sources.
4. Delete: the WORK/JUDGE branch of `bounded_unit`, `except questions.UnitTooLarge` in `run_unit`, the `UnitTooLarge` arm in `inference.call`, and the `big-source` / `big-product` assertions that require the worker to shrink (they assert the defect).
- Journey twin: a unit whose patch is ~150 KB -> n>1 JUDGE calls, every target assessed exactly once, unit DONE, `recoveries == 0`, exactly one WORK launch, file bytes at P unchanged from the worker's return.
- Fault twin: one part answers `gap` -> a single REWORK whose `Exact failure` is the judge's correction (no byte count anywhere); a second twin with a 300 KB untouched file in scope -> largest JUDGE question equals the no-extra-file run (R2 on real scope).

Order: A now (unblocks the fight), B as one lane. Not verified by running anything; all numbers are read from the two slots.
