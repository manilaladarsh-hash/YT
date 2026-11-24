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

targets = [
    ("qmul--cs.json", "entry_route", ["normally have an MSc", "degree", "master", "bachelor"]),
    ("queens--chemeng.json", "toefl_min", ["Overall minimum score", "TOEFL", "English"]),
    ("queens--chemeng.json", "entry_route", ["Students in the MSc program", "BSc", "MSc", "master", "bachelor", "degree", "direct"]),
    ("queens--chemistry.json", "entry_route", ["direct-entry PhD", "master", "bachelor", "degree", "MSc", "BSc"]),
]

out = []
for fname, field, kws in targets:
    d = json.loads((ROOT / "data" / "programs" / fname).read_text(encoding="utf-8"))
    fobj = d["fields"][field]
    url = fobj.get("url", "")
    out.append(f"=== {fname} | {field} ===")
    out.append(f"program_page: {d.get('program_page')}")
    out.append(f"field: {json.dumps(fobj, ensure_ascii=False)}")
    for label, u in [("field_url", url), ("prog_page", d.get("program_page", ""))]:
        if label == "prog_page" and u == url:
            continue
        if u in by_url:
            cname, text = by_url[u]
            out.append(f"{label} cache ({cname}, len={len(text)}):")
            for kw in kws:
                pos = 0
                hits = 0
                while hits < 3:
                    idx = text.lower().find(kw.lower(), pos)
                    if idx == -1:
                        break
                    start = max(0, idx - 250)
                    end = min(len(text), idx + 500)
                    out.append(f"  [kw={kw} @ {idx}] ...{text[start:end]}...")
                    pos = idx + len(kw)
                    hits += 1
        else:
            out.append(f"{label} cache: MISSING for {u}")
    out.append("")

(ROOT / ".scratch" / "b48_out.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote .scratch/b48_out.txt")
