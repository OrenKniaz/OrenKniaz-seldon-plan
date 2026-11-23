# Lane smallDreams (Sol 6.2 medium): write the next, bigger dreams for Seldon's ladder. No code.
Context: Seldon turns a person's dream into a working product. The micro rung (ShelfLife-size apps, about 4 min of plain Codex) is getting boring. Oren 11-22: "if things get boring, increase dream sizes... single larger and larger dream during discovery."
Size scale: micro is minutes of agent work; small is days of single-agent work across several sessions, several milestones, real persistence and UI, roughly 3-8k lines; medium is weeks, 10k+ lines, auth, SQL, front end, background jobs.
Style reference: ~/codex-harness/work/fight-1/shelflife-brief.md. Briefs are in a real person's voice: who they are, their situation, what hurts, what they want to do, a few hard constraints. No API spec dump; Seldon's planner grows the spec with them.
Write these into ~/codex-harness/work/ladder/briefs/S/ (create the dir if needed), one markdown file each:
1. S1-doorcount.md (small): a small venue's door/attendance counter with live capacity, several door staff on phones on the local network, history and reports.
2. S2-rehearsalkeys.md (small): a community theatre's rehearsal scheduler: cast availability, conflicts, scene/role calls, printable call sheets, changes over weeks.
3. S3-loadin.md (small): a touring band's load-in planner: venues, gear lists, truck pack order, timings, checklists used on show day by several crew.
4. M1-repairnet.md (medium): a neighbourhood repair-cafe network: volunteers with skills, item intake with photos, queue per event, repair outcomes, parts, accounts with roles, email-less local notifications, monthly stats, a background job for reminders/reports.
For each brief:
- 250-450 words in owner voice.
- 5-8 hard constraints at the end. Local-only and runnable on Windows; Python and/or Node are allowed; no paid services; no network assets at runtime.
- Make it naturally milestone-shaped: an obvious first usable slice, then growth.
- Make it testable by a person walking it: concrete names, numbers and edge cases a real user would hit (concurrent edits, restart, wrong input, an empty state).
Also write C:/seldon/tests/smallDreams-0/REPORT.md (max 10 lines): file list, and for each brief an estimate of milestones and lines, and why it is the size it claims.
Do NOT write oracles or acceptance tests (those are sealed and written separately). Never read C:/seldon/sealed/. Never open desktop windows.
