import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
CACHE = ROOT / ".cache" / "pages"
by_url = {}
for p in CACHE.glob("*.json"):
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        by_url[d.get("url", "")] = d
    except Exception:
        pass

out = []
u1 = "https://ece.nmsu.edu/grad-study/phd-requirements.html"
if u1 in by_url:
    out.append("=== NMSU ECE phd-requirements.html ===")
    out.append(by_url[u1]["text"][1500:])

u2 = "https://catalog.odu.edu/graduate/sciences/"
if u2 in by_url:
    out.append("\n=== ODU catalog/graduate/sciences links & Ecological/Oceanography ===")
    d = by_url[u2]
    txt = d["text"]
    for kw in ["Ecological", "Oceanography", "GRE", "310"]:
        idx = txt.find(kw)
        if idx != -1:
            out.append(f"[{kw} @ {idx}]: {txt[max(0,idx-300):idx+700]}")
    for label, href in d.get("links", []):
        if any(k in href.lower() for k in ["ecolog", "ocean", "biolog", "science"]):
            out.append(f"LINK: {label} -> {href}")

(ROOT / ".scratch" / "b44_2pages.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote .scratch/b44_2pages.txt")
