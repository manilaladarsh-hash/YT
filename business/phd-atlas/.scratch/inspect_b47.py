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
    ("pitt--bme.json", "entry_route", ["minimum QPA", "bachelor", "master", "degree", "BS", "MS", "PhD"]),
    ("portlandstate--chemistry.json", "entry_route", ["apply directly to the Ph.D.", "bachelor", "master", "degree", "BS", "MS"]),
    ("princeton--biology.json", "supervisor", ["proceed directly to Graduate Admission", "advisor", "supervisor", "rotation", "faculty", "committee", "lab"]),
    ("princeton--materials.json", "gre_general", ["General Test", "GRE", "Subject"]),
    ("princeton--math.json", "gre_general", ["General Test", "GRE", "Subject"]),
    ("princeton--mech.json", "gre_general", ["General Test", "GRE", "Subject"]),
    ("qmul--biomed.json", "deadline", ["Medicine and Dentistry studentships", "deadline", "closing", "apply", "date", "PhD"]),
    ("qmul--bme.json", "deadline", ["Other Science and Engineering Studentships", "deadline", "closing", "apply", "date", "PhD"]),
    ("qmul--bme.json", "funding", ["apply early in order", "funding", "studentship", "scholarship", "competitive", "stipend"]),
    ("qmul--chemeng.json", "deadline", ["Other Science and Engineering Studentships", "deadline", "closing", "apply", "date", "PhD"]),
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

(ROOT / ".scratch" / "b47_out.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote .scratch/b47_out.txt")
