Round 2. Independent review findings are in ~/codex-harness/work/lanes/stage-core6-rv.md. Fix all four at their owners, by rule rather than case:
1. Tests-phase repair must invalidate the repaired checks and account for retained evidence, so RED can be re-established for what changed.
2. A provider reply persisted before the report was saved is recoverable: reconcile the recorded terminal reply on reopen.
3. Git ignore rules must not make the published manifest differ from HEAD: require commit and manifest equality, and refuse clearly if they differ.
4. REPAIR must be able to amend unit ownership and requirement membership through the existing work contract, including adding a requirement, its test, and an authorized writer for a new file.

Prove each by outcome in the existing journey style. Also bring this tree up to main before regenerating the patch: apply these two commits' changes from ~/codex-harness/work/sprint-20261027/semantic-cc (git show eb79da3 and git show 70ef851), keeping them intact in their new module locations. Regenerate stage-core6.patch (cumulative against this lane's base) and stage-core6.patch.sha256, and rewrite stage-core6-report.md (at most 12 lines, with module sizes and journey result). Do not commit. No real provider calls. You cannot delete folders; use new names.
