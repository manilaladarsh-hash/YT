import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
CACHE = ROOT / ".cache" / "pages"
by_url = {}
for p in CACHE.glob("*.json"):
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        by_url[d.get("url", "")] = (p.name, d)
    except Exception:
        pass

urls = [
    ("cs", "https://www.ncl.ac.uk/postgraduate/degrees/8050f-23/"),
    ("earth", "https://www.ncl.ac.uk/postgraduate/degrees/8314f/"),
    ("ece", "https://www.ncl.ac.uk/postgraduate/degrees/8060f-24/"),
    ("environment", "https://www.ncl.ac.uk/postgraduate/degrees/8020f-2/"),
    ("materials", "https://www.ncl.ac.uk/postgraduate/degrees/8030f-11/"),
    ("math", "https://www.ncl.ac.uk/postgraduate/degrees/8080f-30/"),
    ("mech", "https://www.ncl.ac.uk/postgraduate/degrees/8090f-32/"),
    ("neuro", "https://www.ncl.ac.uk/postgraduate/degrees/8300f-75/"),
    ("physics", "https://www.ncl.ac.uk/postgraduate/degrees/8821f/"),
    ("statistics", "https://www.ncl.ac.uk/postgraduate/degrees/8080f-29/"),
]

out = []
for field, url in urls:
    if url not in by_url:
        out.append(f"=== {field} | {url} | MISSING ===")
        continue
    fname, data = by_url[url]
    text = data.get("text", "")
    out.append(f"=== {field} | {url} | {fname} ===")
    for marker in ["Typical entry requirements", "Academic entry requirements", "Closing Dates"]:
        idx = text.find(marker)
        if idx != -1:
            out.append(f"[{marker}] -> {text[idx:idx+700]}")
        else:
            out.append(f"[{marker}] -> NOT FOUND")
    out.append("")

(ROOT / ".scratch" / "b43_ncl.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote .scratch/b43_ncl.txt")
