"""Compare Not stated rates, live vs staged, for the universities that have staged records.

Usage: python3 handoff/measure.py [UID ...]   (default: every staged university)
A staged program replaces the live one with the same id; live programs with no staged copy are kept.
"""

import json
import sys
from pathlib import Path

R = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R / "scripts"))
from coverage import effective  # noqa: E402


def load(d, pattern):
    return {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (R / d).glob(pattern)}


def rate(uid, staged):
    unis = load("data/universities", f"{uid}.json")
    progs = load("data/programs", f"{uid}--*.json")
    if staged:
        unis.update(load("data/staging/universities", f"{uid}.json"))
        progs.update(load("data/staging/programs", f"{uid}--*.json"))
    ns = vals = 0
    for p in progs.values():
        e = effective(p, unis.get(uid))
        ns += sum(v["code"] == "Not stated" for v in e.values())
        vals += len(e)
    return ns, vals


uids = sys.argv[1:] or sorted(p.stem for p in (R / "data/staging/universities").glob("*.json"))
tot = [0, 0, 0, 0]
for uid in uids:
    a, b = rate(uid, False), rate(uid, True)
    tot = [tot[0] + a[0], tot[1] + a[1], tot[2] + b[0], tot[3] + b[1]]
    print(f"{uid:<18}{(format(a[0] / a[1], '.0%') if a[1] else 'new'):>6} -> {b[0] / max(b[1], 1):>4.0%}   ({b[1] // 11} programs)")
print(f"{'TOTAL':<18}{tot[0] / max(tot[1], 1):>6.0%} -> {tot[2] / max(tot[3], 1):>4.0%}")
