ASTRA BUILD-VS-BUY-1 — read-only. Read CHARTER.md first (C12 beads, C19 memory/mail/worktrees, C20 wrap providers/thin core/read-only cockpit, I9 thin and deleting).
Oren 11-04: Seldon's own logic should NOT be hard. Agent mail and beads should come from vendors (with small improvements); plan mode is ours; memory layer and the UI/UX frontend need checking too. Find out what we actually built ourselves.
For each area — (1) agent mail / inter-agent messaging, (2) beads / task-issue graph / claims, (3) memory layer (project memory, lessons, promotion, retrieval), (4) cockpit / UI / frontend (operator views, status API, web assets), (5) anything else that duplicates a vendor or provider capability (worktrees, scheduling, transport, approvals UI):
- files (src/codex_harness/** and any web/ui assets) + production LOC (count non-blank lines);
- what it does that Seldon truly needs (charter C#) vs what is reimplementation;
- vendor/provider option that fits (e.g. the Beads issue tracker, MCP Agent Mail, provider-native memory, provider app UI) — only ones you are confident exist; say "unsure" otherwise;
- recommendation: ADOPT vendor + thin adapter (est. LOC kept) / KEEP ours but shrink to X LOC / DELETE (not needed by charter);
- which reset stage absorbs it (astra-reset-1/2: 3c memory/mail, 3a dispatch, 4b providers, etc.) or NEW.
Also give: total core LOC now; a realistic target for "plan mode + loop + trace + judge + scheduling + integration/recovery + adapters" if everything else is vendor or deleted; and the 3 biggest simplification wins in order.
Final message only, <=70 lines; open with the CHARTER line; TRIAGE line for any design fault. No files changed.
