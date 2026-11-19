Build ShelfLife, a small local pantry tracker for one household. Python 3.12 standard library only (sqlite3, http.server, csv, json); no third-party packages, no network access at runtime, no build step.

Backend: `python server.py --port PORT --db PATH` serves a JSON API and the web UI on 127.0.0.1.
- Items have: id, name (1-80 chars), quantity (integer >= 0), unit (text, optional), expires (YYYY-MM-DD or null), created_at.
- GET /api/items (optional ?expiring_within=DAYS, ?q=TEXT name search) returns items sorted by expiry (nulls last).
- POST /api/items creates; PATCH /api/items/{id} updates quantity/name/unit/expires; POST /api/items/{id}/consume {"amount": n} reduces quantity (never below 0; 409 if amount exceeds quantity); DELETE /api/items/{id}.
- Invalid input returns 400 with {"error": "..."}; unknown id 404. Data persists in the SQLite file across restarts. Concurrent requests must not corrupt data or lose updates (two simultaneous consumes of the last unit: exactly one succeeds).

UI (served at /): one responsive page that works at phone and desktop sizes.
- "Expiring soon" section (next 7 days, expired items clearly marked), full list with search and an expiry filter, add-item form with inline validation messages, consume and delete actions, empty state and a visible error state when the API fails.
- Keyboard accessible with visible focus; readable contrast; no horizontal scrolling at 375px. Clean, calm visual design.

Import: `python import_items.py FILE.csv --db PATH` loads rows (name,quantity,unit,expires) into the same database, skipping invalid rows and printing one summary line "imported N, skipped M" (exit 0), or exit 2 with an error on an unreadable file.

Done means: the server, UI and importer work together from a fresh folder; a short README explains how to run them.
