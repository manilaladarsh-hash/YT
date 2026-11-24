import json
from pathlib import Path

CACHE = Path("C:/Users/manil/YT/business/phd-atlas/.cache/pages")
OUT = Path("C:/Users/manil/YT/business/phd-atlas/scratch/hku_extra_check.txt")

want = [
    "ece.hku.hk/study/scholarships/",
    "www.cds.hku.hk/prospective-students/scholarships/",
    "www.scifac.hku.hk/rpg/programme-info/phd",
    "gradsch.hku.hk/prospective_students/programmes",
    "gradsch.hku.hk/prospective_students/application/how_to_apply",
    "www.physics.hku.hk/prospective-students/rpg-admission",
    "www.earthsciences.hku.hk/prospective-students/postgraduate-students/research-postgraduates/general-information",
]

lines = []
for p in sorted(CACHE.glob("*.json")):
    r = json.loads(p.read_text(encoding="utf-8"))
    u = r.get("url", "")
    if any(u.endswith(w) for w in want):
        txt = r.get("text", "")
        lines.append(f"\n{'='*80}\nURL: {u}\nFINAL: {r.get('final_url')}\nLEN: {len(txt)}\nTEXT:\n{txt[-7000:]}\n")

OUT.write_text("\n".join(lines), encoding="utf-8")
print("Wrote", len(lines), "pages")
