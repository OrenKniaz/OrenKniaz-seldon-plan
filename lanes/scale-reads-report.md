Base 6e704a25; src/seldon/{store,gitwork,proof,wave_verify}.py: +63/-66, net -3; tests unchanged (14 collected).
Deleted old-UnitRow compatibility default, unused blobs(named), redundant empty-entry guard, observer reuse/dirty bookkeeping and repeated RED decodes.
Cached immutable plans; Store.observation_index(commit, tuple(refs)) returns (checkRefs, unitTrees), primed by WAVE-VERIFY; batch E still owns replacing consumer scans.
Kept stale-consumer invalidation: records_and_skeleton_journey writes a canonical contract correction after DONE, reopens/reviews/B, and renews only consumer judges; dead claim not confirmed.
Kept integrated(..., scratch, ...): unused but its units.py caller is outside this lane; grep confirmed blobs named/empty-entry deletions have no reachable use.
Completed worker/observer worktrees are removed; uncertain cleanup remains retained. srd-3 exposed concurrent add/remove commondir race; only Git worktree-management commands now serialize.
srd-2: 13P/1F, 374.06s suite/375.53s wall, scale102.12s>90; unchanged srd-3: 13P/1F,177.79/179.07s, metadata race (corrected locally).
srd-4: 13P/1F,351.29s suite/352.58s wall,scale116.61s; final-byte srd-5: 13P/1F,360.91/362.29s,scale100.86s; both post-fix failures timing-only (>90s).
NOT GREEN: host-load attribution unknown; aggregate golden timing assertion not reached. Post-fix journeys/replays reach scripted B/C; final scale51 DONE has zero retained roots/linked registrations.
No commits, dependencies, real providers, test/constant/assertion or CHARTER/BLUEPRINT edits. Diff/reverse-apply checks pass; tracking T-125 and lane status updated; lead timing qualification remains.
