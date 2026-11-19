"""Check and summarise the lead's tracking files. Run after every edit: python work/ladder/tracking.py

TICKETS.json, RECOMMENDATIONS.json and STATUS.json are the source of truth for the dashboard. Rules: TRACKING.md.
It also refreshes STATUS.json "recentRuns" from RUNS.md, so the scoreboard is never typed by hand.
Exit code 1 means a file is invalid; the message names the row and field.
"""

import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
TICKET = {"severity": {"critical", "high", "medium", "low"}, "type": {"design", "code", "idea"},
          "status": {"open", "in_progress", "fixed", "done", "dropped"}}
TICKET_TEXT = ("id", "title", "milestone", "area", "direction", "evidence")
REC = {"priority": {"now", "before M2", "later"}, "decision": {"proposed", "ratified", "rejected", "deferred"},
       "implementation": {"not started", "in progress", "incorporated", "dropped"}}
REC_TEXT = ("id", "target", "source", "change", "why")
ACTION = {"status": {"next", "open", "in progress", "later", "done", "dropped"}}


def rows(path, key, enums, text):
    data = json.loads((HERE / path).read_text(encoding="utf-8"))
    errors, seen = [], set()
    for row in data[key]:
        rid = row.get("id", "?")
        if rid in seen:
            errors.append(f"{path} {rid}: duplicate id")
        seen.add(rid)
        errors += [f"{path} {rid}: missing {f}" for f in text if not str(row.get(f, "")).strip()]
        errors += [f"{path} {rid}: {f}={row.get(f)!r} not in {sorted(v)}" for f, v in enums.items()
                   if row.get(f) not in v]
    return data, errors


def sync_runs(count=15):
    lines = [l for l in (HERE / "RUNS.md").read_text(encoding="utf-8").splitlines() if l.startswith("| 20")]
    runs = []
    for line in lines[-count:][::-1]:
        c = [x.strip() for x in line.strip("|").split("|")]
        runs.append({"date": c[0], "run": c[1].replace("\\", "/").rsplit("/", 1)[-1], "commit": c[2][:7],
                     "outcome": c[3], "furthest": c[4], "repairs": c[5], "gaps": c[7], "uncertain": c[8],
                     "wall": c[9].rstrip("s*"), "flags": c[13]})
    path = HERE / "STATUS.json"
    status = json.loads(path.read_text(encoding="utf-8"))
    status["recentRuns"] = runs
    path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return status


def main():
    status = sync_runs()
    errors = [f"STATUS.json: missing {f}" for f in ("updated", "lead", "main", "milestone", "now", "next")
              if not status.get(f)]
    errors += [f"STATUS.json lanes[{i}]: missing {f}" for i, lane in enumerate(status.get("lanes", []))
               for f in ("name", "what", "state") if not lane.get(f)]
    tickets, more = rows("TICKETS.json", "tickets", TICKET, TICKET_TEXT)
    errors += more
    recs, more = rows("RECOMMENDATIONS.json", "recommendations", REC, REC_TEXT)
    errors += more
    errors += rows("RECOMMENDATIONS.json", "leadActions", ACTION, ("id", "change"))[1]
    for t in tickets["tickets"]:
        if t.get("status") == "done" and "VALIDATED" not in t.get("evidence", ""):
            errors.append(f"TICKETS.json {t['id']}: done needs 'VALIDATED' evidence naming commit and run")
    names = [f.get("name") for f in tickets.get("families", [])]
    errors += [f"TICKETS.json families: {f.get('name', '?')} missing {k}" for f in tickets.get("families", [])
               for k in ("name", "idea", "remedy", "rule") if not str(f.get(k, "")).strip()]
    errors += [f"TICKETS.json {t['id']}: family={t.get('family')!r} not in families[].name"
               for t in tickets["tickets"] if t.get("family") not in names]
    for line in errors:
        print("ERROR", line)
    live = ("open", "in_progress")
    print("tickets", dict(Counter(t["status"] for t in tickets["tickets"])))
    print("open by severity", dict(Counter(t["severity"] for t in tickets["tickets"] if t["status"] in live)))
    fam = {n: (sum(t["family"] == n and t["status"] in live for t in tickets["tickets"]),
               sum(t["family"] == n and t["status"] in live and t["severity"] == "critical"
                   for t in tickets["tickets"]),
               sum(t["family"] == n for t in tickets["tickets"])) for n in names}
    print("families", dict(sorted(fam.items(), key=lambda kv: -kv[1][0])))
    print("recommendations", dict(Counter((r["decision"], r["implementation"]) for r in recs["recommendations"])))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
