import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
CACHE = ROOT / ".cache" / "pages"
by_url = {}
for p in CACHE.glob("*.json"):
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        by_url[d.get("url", "")] = (p.name, d.get("text", ""))
    except Exception:
        pass

out = []

# 1. NMSU cached pages
out.append("=== NMSU cached URLs ===")
for u, (fn, txt) in sorted(by_url.items()):
    if "nmsu.edu" in u:
        out.append(f"  {fn}: {u} (len={len(txt)})")
        if "ece.nmsu.edu" in u and "phd-requirements" in u:
            out.append(txt[:3000])

# 2. NYU Math cached pages
out.append("\n=== NYU Math admission-policies full ===")
for u, (fn, txt) in sorted(by_url.items()):
    if "math.nyu.edu" in u:
        out.append(f"  {fn}: {u} (len={len(txt)})")
nyu_math_url = "https://math.nyu.edu/dynamic/graduate/phd-mathematics/admission-policies/"
if nyu_math_url in by_url:
    out.append(by_url[nyu_math_url][1][2700:])

# 3. NYU Mech admission requirements
out.append("\n=== NYU Mech admission requirements ===")
nyu_mech_url = "https://engineering.nyu.edu/academics/programs/mechanical-engineering-phd"
if nyu_mech_url in by_url:
    txt = by_url[nyu_mech_url][1]
    idx = txt.find("Admission Requirements")
    out.append(txt[idx:idx+1500])

# 4. ODU Ecological Sciences in requirements + all odu*.json gre_general
out.append("\n=== ODU Ecological in requirements ===")
odu_req_url = "https://www.odu.edu/admission/graduate/requirements"
if odu_req_url in by_url:
    txt = by_url[odu_req_url][1]
    idx = txt.find("Ecological")
    out.append(txt[max(0, idx-200):idx+600])

out.append("\n=== ODU programs gre_general ===")
for p in sorted((ROOT / "data" / "programs").glob("odu--*.json")):
    d = json.loads(p.read_text(encoding="utf-8"))
    g = d["fields"].get("gre_general", {})
    out.append(f"  {p.name}: {g.get('code')} | {g.get('quote')} | {g.get('url')}")

(ROOT / ".scratch" / "b44_extra.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote .scratch/b44_extra.txt")
