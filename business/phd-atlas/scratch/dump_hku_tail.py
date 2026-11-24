import json
from pathlib import Path

CACHE = Path("C:/Users/manil/YT/business/phd-atlas/.cache/pages")
OUT = Path("C:/Users/manil/YT/business/phd-atlas/scratch/hku_cached_tail.txt")

want = [
    "admission_requirement",
    "application_period",
    "stipend-support",
    "Fields-of-Study",
    "ece.hku.hk/study/scholarships",
    "scifac.hku.hk/rpg/apply",
    "sbms.hku.hk/study",
    "psychology.hku.hk/cognitive",
    "psychology.hku.hk/human-neuroscience",
]

lines = []
all_hku = []
for p in sorted(CACHE.glob("*.json")):
    r = json.loads(p.read_text(encoding="utf-8"))
    u = r.get("url", "")
    if "hku.hk" in u:
        all_hku.append((u, r.get("status"), len(r.get("text", ""))))
    if any(w in u for w in want):
        txt = r.get("text", "")
        # strip repetitive menu lines if long, just keep unique/last portion or full if <15000
        lines.append(f"\n{'='*80}\nURL: {u}\nSTATUS: {r.get('status')}\nLEN: {len(txt)}\nTAIL TEXT:\n{txt[-6000:]}\n")

lines.insert(0, "ALL HKU CACHED URLS:\n" + "\n".join(f"  [{st}] ({ln} ch) {u}" for u, st, ln in all_hku))
OUT.write_text("\n".join(lines), encoding="utf-8")
print("Done:", len(all_hku), "HKU URLs")
