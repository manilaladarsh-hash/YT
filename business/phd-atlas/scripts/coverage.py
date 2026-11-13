"""Coverage report: which universities and fields are researched, and how many
effective values are still 'Not stated' (department value, else university value).

Usage: python3 scripts/coverage.py [--dir data] [--gate] [--detail]
--gate exits non-zero unless the release gate in BUSINESS_PLAN_README.md is met.
"""

import argparse
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SCHEMA = json.loads((DATA / "schema.json").read_text(encoding="utf-8"))
FIELDS = json.loads((DATA / "fields.json").read_text(encoding="utf-8"))["fields"]
UNIS = json.loads((DATA / "universities.json").read_text(encoding="utf-8"))["universities"]
UF, PF = list(SCHEMA["university_fields"]), list(SCHEMA["program_fields"])
GATE = {"universities": 180, "fields": 12, "not_stated_overall": 0.15, "not_stated_per_field": 0.25}


def effective(prog, uni):
    out = {}
    for k in PF:
        out[k] = prog["fields"][k]
    for k in UF:
        own = prog["fields"].get(k)
        out[k] = own if own and own["code"] != "Not stated" else (uni["fields"][k] if uni else {"code": "Not stated"})
    return out


def report(base):
    unis = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (base / "universities").glob("*.json")}
    progs = [json.loads(p.read_text(encoding="utf-8")) for p in (base / "programs").glob("*.json")]
    per_field = collections.defaultdict(lambda: [0, 0, 0])  # programs, not stated, values
    per_uni = collections.Counter()
    ns_total = vals_total = 0
    for p in progs:
        eff = effective(p, unis.get(p["university"]))
        ns = sum(1 for v in eff.values() if v["code"] == "Not stated")
        for fid in [p["field"]] + p.get("also_fields", []):
            pf = per_field[fid]
            pf[0] += 1; pf[1] += ns; pf[2] += len(eff)
        ns_total += ns; vals_total += len(eff)
        per_uni[p["university"]] += 1
    return unis, progs, per_field, per_uni, ns_total, vals_total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="data")
    ap.add_argument("--gate", action="store_true")
    ap.add_argument("--detail", action="store_true")
    a = ap.parse_args()
    base = ROOT / a.dir
    unis, progs, per_field, per_uni, ns, vals = report(base)
    listed = [u["id"] for u in UNIS]
    print(f"{len(unis)} of {len(listed)} listed universities have a record; {len(per_uni)} have programs; {len(progs)} programs")
    print(f"Not stated overall: {ns}/{vals} = {ns / max(vals, 1):.0%}")
    print(f"{'field':<14}{'programs':>9}{'not stated':>12}")
    for f in FIELDS:
        n, fns, fv = per_field.get(f["id"], [0, 0, 0])
        print(f"{f['id']:<14}{n:>9}{(fns / fv if fv else 0):>11.0%}")
    if a.detail:
        missing = [u for u in listed if u not in per_uni]
        print("no programs yet:", " ".join(missing))
    if a.gate:
        covered_fields = [f for f, (n, fns, fv) in per_field.items() if n >= 30]
        ok = (len(per_uni) >= GATE["universities"] and len(covered_fields) >= GATE["fields"]
              and ns / max(vals, 1) < GATE["not_stated_overall"]
              and all(fns / fv < GATE["not_stated_per_field"] for f, (n, fns, fv) in per_field.items() if n >= 30))
        print("GATE", "PASS" if ok else "NOT MET")
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
