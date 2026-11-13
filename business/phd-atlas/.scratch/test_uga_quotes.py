import json, hashlib
from pathlib import Path

ROOT = Path(".")
CACHE = ROOT / ".cache" / "pages"

def cache_file(url):
    k = hashlib.sha1(url.encode()).hexdigest()[:16]
    return CACHE / f"{k}.json"

def test_q(url, quote):
    if not quote:
        return True, ""
    f = cache_file(url)
    if not f.exists():
        return False, f"Missing cache: {url}"
    t = " ".join(json.load(open(f, encoding="utf-8"))["text"].split())
    for p in quote.split(" | "):
        p_norm = " ".join(p.split())
        if p_norm not in t:
            return False, f"Not in {url}:\n  LOOKING FOR: {p_norm}\n"
    return True, ""

with open(".scratch/build_uga.py", encoding="utf-8") as f:
    lines = f.readlines()

prog_lines = lines[:708]
exec_ns = {"__file__": str((ROOT / ".scratch" / "build_uga.py").resolve())}
exec("".join(prog_lines), exec_ns)
programs = exec_ns["programs"]

mismatches = []
for p in programs:
    for fld in ["deadline", "gre", "subj", "supervisor", "funding", "entry"]:
        url = p[fld + "_url"]
        q = p[fld + "_q"]
        ok, msg = test_q(url, q)
        if not ok:
            mismatches.append((p["id"], fld, msg))
    for ef_k, ef in p.get("extra_fields", {}).items():
        ok, msg = test_q(ef["url"], ef["quote"])
        if not ok:
            mismatches.append((p["id"], f"extra_{ef_k}", msg))

print(f"Total mismatches: {len(mismatches)}")
for pid, fld, msg in mismatches:
    print(f"[{pid}] {fld} -> {msg}")
