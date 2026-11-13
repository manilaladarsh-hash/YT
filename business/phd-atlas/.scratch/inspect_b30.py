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
    ("fsu--math.json", "supervisor"),
    ("georgiatech--chemistry.json", "entry_route"),
    ("georgiatech--ece.json", "funding"),
    ("georgiatech--physics.json", "entry_route"),
    ("gmu--chemistry.json", "supervisor"),
    ("gmu--physics.json", "funding"),
    ("goettingen--biology.json", "supervisor"),
    ("goettingen--chemistry.json", "supervisor"),
    ("goettingen--chemistry.json", "english_waiver"),
    ("hamburg--biomed.json", "deadline"),
]

for fn, field in ROWS:
    j = json.loads((ROOT / "data" / "programs" / fn).read_text(encoding="utf-8"))
    f = j["fields"][field]
    u = f["url"]
    print(f"=== {fn} [{field}] ===")
    print("program_page:", j.get("program_page"))
    print("field:", json.dumps(f, indent=2, ensure_ascii=False))
    entries = url_map.get(u, [])
    print(f"cache entries ({len(entries)}):")
    for cname, cd in entries:
        t = cd.get("text", "")
        q = f.get("quote", "")
        print(f"  {cname}: status={cd.get('status')} method={cd.get('method')} via={cd.get('via')} fetched={cd.get('fetched')} len={len(t)}")
        norm_t = " ".join(t.split())
        norm_q = " ".join(q.split())
        # find first 35 chars of first quote part
        part = norm_q.split(" | ")[0][:35]
        idx = norm_t.lower().find(part.lower()) if part else -1
        if idx != -1:
            print("  CONTEXT:", repr(norm_t[max(0, idx-350):idx+500]))
        else:
            print("  FIRST PART NOT FOUND DIRECTLY; SAMPLE:", repr(norm_t[:500]))
    print()
