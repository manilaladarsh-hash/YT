import json, os

cache_dir = ".cache/pages"
by_url = {}
for fn in os.listdir(cache_dir):
    if fn.endswith(".json"):
        with open(os.path.join(cache_dir, fn), encoding="utf-8") as f:
            d = json.load(f)
        by_url[d["url"]] = d.get("text", "")

out = []
targets = [
    "https://www.ime.t.u-tokyo.ac.jp/Prospectus-2027.html",
    "https://www.k.u-tokyo.ac.jp/en/gsfs/financial_support/",
    "https://www.u-tokyo.ac.jp/en/prospective-students/scholarships.html",
    "https://www.s.u-tokyo.ac.jp/en/admission/scholarship.html",
    "https://www.civil.t.u-tokyo.ac.jp/en/admission/",
    "https://www.t.u-tokyo.ac.jp/en/study-at-utokyo/soe/admission/financial-aid",
]
for u in targets:
    t = by_url.get(u, "")
    out.append(f"\n=== {u} (len={len(t)}) ===")
    if "Prospectus" in u:
        idx = t.find("Full Academic Transcript")
        out.append(t[idx:] if idx != -1 else t)
    elif "scholarship.html" in u and "s.u-tokyo" in u:
        idx = t.find("Scholarships\n")
        out.append(t[idx:idx+6000] if idx != -1 else t[-6000:])
    else:
        out.append(t[-4000:])

with open("scratch/tails_bodies.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Wrote scratch/tails_bodies.txt")
