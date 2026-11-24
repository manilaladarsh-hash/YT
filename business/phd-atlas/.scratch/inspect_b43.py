import hashlib
import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
CACHE = ROOT / ".cache" / "pages"
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
    h = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
    p = CACHE / f"{h}.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    text = data.get("text", "")
    out.append(f"=== {field} | {url} | {h}.json ===")
    for marker in ["Typical entry requirements", "Academic entry requirements", "Closing Dates"]:
        idx = text.find(marker)
        if idx != -1:
            out.append(f"[{marker}] -> {text[idx:idx+700]}")
        else:
            out.append(f"[{marker}] -> NOT FOUND")
    out.append("")

(ROOT / ".scratch" / "b43_ncl.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote .scratch/b43_ncl.txt")
