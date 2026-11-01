"""Print the ONE next job to do, and which task card in handoff/GEMINI_TASKS.md to follow.

Usage: python3 handoff/next.py
Order: repair generic pages -> review audit rows -> add US universities -> screen US universities -> gap-fill.
"""

import csv
import json
import subprocess
import sys
import tempfile
from pathlib import Path

R = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R / "scripts"))
from coverage import effective  # noqa: E402

REVIEWED = R / "handoff" / "audit_reviewed.csv"  # rows you checked and found fine: check,file,field


def audit_rows():
    out = Path(tempfile.gettempdir()) / "atlas_audit.csv"
    subprocess.run([sys.executable, str(R / "scripts" / "audit_quality.py"), "--csv", str(out)], check=True, capture_output=True)
    ok = set()
    if REVIEWED.exists():
        ok = {(r["check"], r["file"], r["field"]) for r in csv.DictReader(REVIEWED.open(encoding="utf-8"))}
    return [r for r in csv.DictReader(out.open(encoding="utf-8")) if (r["check"], r["file"], r["field"]) not in ok]


def main():
    rows = audit_rows()
    generic = [r for r in rows if r["check"] == "generic_page"]
    if generic:
        counts = {}
        for r in generic:
            counts[r["file"].split("--")[0]] = counts.get(r["file"].split("--")[0], 0) + 1
        uid, n = max(sorted(counts.items()), key=lambda x: x[1])
        print(f"CARD 2 (repair generic pages)\nuniversity: {uid}\nprograms to repair: {n}")
        for r in generic:
            if r["file"].startswith(uid + "--"):
                print(f"  {r['file']}  department now: {r['detail']}")
        return
    other = [r for r in rows if r["check"] in ("off_topic", "absence", "odd_cache")]
    if other:
        print(f"CARD 3 (review audit rows) - do these {min(10, len(other))} rows, {len(other)} left in total")
        for r in other[:10]:
            print(f"  {r['check']} | {r['file']} | {r['field']} = {r['code']} | {r['url']}\n     quote: {r['detail']}")
        return
    us = list(csv.DictReader((R / "handoff" / "us_r1r2.csv").open(encoding="utf-8")))
    order = [("R1", "add"), ("R1", "screen-health-sciences"), ("R1", "screen-check-stem-phd"),
             ("R2", "add"), ("R2", "screen-check-stem-phd"), ("R2", "screen-health-sciences")]
    for tier, st in order:
        for u in us:
            if u["tier"] == tier and u["status"] == st:
                card = "CARD 4 (add a US university)" if st == "add" else "CARD 5 (screen a US university)"
                extra = "  Health-science school: research only biomed, neuro, bme (and biology if it has a PhD)." if "health" in st else ""
                print(f"{card}\nname: {u['carnegie_name']}\nstate: {u['state']}\ntier: {tier}\n{extra}")
                return
    unis = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (R / "data/universities").glob("*.json")}
    count = {}
    for p in (R / "data/programs").glob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        e = effective(d, unis.get(d["university"]))
        count[d["university"]] = count.get(d["university"], 0) + sum(v["code"] == "Not stated" for v in e.values())
    uid, n = max(count.items(), key=lambda x: x[1])
    print(f"CARD 6 (gap-fill)\nuniversity: {uid}\nNot stated values: {n}\nRun: python3 handoff/research_prompt.py {uid}")


if __name__ == "__main__":
    main()
