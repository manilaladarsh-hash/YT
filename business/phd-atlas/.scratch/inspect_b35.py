import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
CACHE = ROOT / ".cache" / "pages"

url_map = {}
for cp in CACHE.glob("*.json"):
    d = json.loads(cp.read_text(encoding="utf-8"))
    for u in {d.get("url", ""), d.get("final_url", "")}:
        if u:
            url_map.setdefault(u, []).append((cp.name, d))

ROWS = [
    ("leeds--physics.json", "deadline"),
    ("leeds--statistics.json", "deadline"),
    ("lehigh--biology.json", "gre_general"),
    ("lmu--biomed.json", "supervisor"),
    ("lmu--earth.json", "supervisor"),
    ("lmu--math.json", "supervisor"),
    ("lmu--math.json", "entry_route"),
    ("lmu--physics.json", "supervisor"),
    ("louisville--math.json", "gre_subject"),
]

out = []
for fn, field in ROWS:
    j = json.loads((ROOT / "data" / "programs" / fn).read_text(encoding="utf-8"))
    f = j["fields"][field]
    u = f["url"]
    out.append(f"=== {fn} [{field}] ===")
    out.append(f"program_page: {j.get('program_page')}")
    out.append("field: " + json.dumps(f, indent=2, ensure_ascii=False))
    entries = url_map.get(u, [])
    out.append(f"cache entries ({len(entries)}):")
    for cname, cd in entries:
        t = cd.get("text", "")
        q = f.get("quote", "")
        out.append(f"  {cname}: status={cd.get('status')} method={cd.get('method')} via={cd.get('via')} fetched={cd.get('fetched')} len={len(t)}")
        norm_t = " ".join(t.split())
        norm_q = " ".join(q.split())
        part = norm_q.split(" | ")[0][:35]
        idx = norm_t.lower().find(part.lower()) if part else -1
        if idx != -1:
            out.append("  CONTEXT: " + repr(norm_t[max(0, idx-350):idx+550]))
        else:
            out.append("  FIRST PART NOT FOUND DIRECTLY; SAMPLE: " + repr(norm_t[:500]))
        links = [l for l in cd.get("links", []) if "en" in str(l).lower() or "promot" in str(l).lower()]
        if links:
            out.append("  LINKS SAMPLE: " + repr(links[:12]))
    out.append("")

(ROOT / ".scratch" / "b35_out.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote .scratch/b35_out.txt", len(out))
