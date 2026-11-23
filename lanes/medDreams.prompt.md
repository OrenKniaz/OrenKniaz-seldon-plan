# Lane medDreams (Sol 6.2 medium): write medium dreams that genuinely take a plain agent 45-60+ minutes. No code.
Calibration: plain Codex (Terra 6.1 medium, one turn) built ~/codex-harness/work/ladder/briefs/S/M1-repairnet.md (6 milestones, auth, SQL, background jobs) in 5 minutes and 305 lines. It compressed or skipped depth. Small briefs took 4-5 minutes. The owner (Oren) wants medium dreams with at minimum a front end, back end, auth system and database. The goal is dreams where a single plain session must work 45-60+ minutes, compact its context several times, and still struggle to keep everything consistent. That is where a planner with memory and proof should show its value.
What makes a dream big without being artificial: real breadth a real owner needs, where every part is load-bearing.
- many distinct roles, screens and workflows, with an explicit permission matrix
- real data rules: money with exact rounding, inventory or stock, dates/time zones/recurrence
- a documented import/export format with a sample file and error rows
- audit trail and undo
- reports with several views and filters
- notifications and background jobs with catch-up
- accessibility and keyboard use
- the owner explicitly expects production quality: readable code, migrations, an automated test per workflow, seed data for a demo, and a setup guide a non-developer can follow
Lean into the owner's world. Concrete names, numbers and real edge cases.
Write two briefs in owner voice into ~/codex-harness/work/ladder/briefs/M/ (create the dir):
1. M2-<name>.md: a small-business full-stack product, e.g. a bike-repair shop with work orders, parts inventory, customer portal, invoices and payments recorded (not processed), technician scheduling and staff accounts. Your choice of domain, but keep it plausible.
2. M3-<name>.md: noticeably bigger, a multi-tenant product, e.g. several clinics or schools sharing one system with tenant isolation, roles, scheduling with recurrence, billing records, an import from a legacy CSV, and a reporting suite.
Each brief should be 600-1000 words plus 10-15 hard constraints: Windows host; Python and/or Node; local only; no paid services or network-hosted assets; a SQL database; real login with hashed passwords and sessions; role-based authorization. Make it naturally milestone-shaped, and include at least one mid-project-style change the owner already anticipates ("next season we'll also need...").
Also write C:/seldon/tests/medDreams-0/REPORT.md (max 10 lines): an estimate for each of screens, workflows, lines and plain minutes, and why it can't be golfed into 300 lines. Do NOT write oracles. Never read C:/seldon/sealed/. Never open desktop windows.
