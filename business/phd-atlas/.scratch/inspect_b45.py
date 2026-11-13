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
    ("odu--math.json", "gre_general", ["Computational", "Applied Mathematics", "GRE", "Transcripts"]),
    ("ohiostate--chemistry.json", "english_waiver", ["Only applicants", "TOEFL", "IELTS", "English", "exempt", "waiver"]),
    ("ohiostate--ece.json", "entry_route", ["direct BS to PhD", "master", "bachelor", "MS", "BS"]),
    ("ohiostate--environment.json", "entry_route", ["Regular-admit", "Direct-admit", "bachelor", "master"]),
    ("ohiostate--math.json", "funding", ["Graduate Teaching Associateships", "stipend", "funding", "support", "tuition"]),
    ("ohsu--datasci.json", "entry_route", ["Minimum GPA", "bachelor", "master", "degree", "PhD", "admission"]),
    ("ohsu--neuro.json", "entry_route", ["NGP does not have", "bachelor", "master", "degree", "prerequisite", "admission"]),
    ("okstate--chemistry.json", "gre_subject", ["Graduate Record", "GRE", "subject", "chemistry", "admission"]),
    ("olemiss--physics.json", "gre_subject", ["It is not required", "GRE", "subject", "physics"]),
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
                while hits < 2:
                    idx = text.lower().find(kw.lower(), pos)
                    if idx == -1:
                        break
                    start = max(0, idx - 250)
                    end = min(len(text), idx + 450)
                    out.append(f"  [kw={kw} @ {idx}] ...{text[start:end]}...")
                    pos = idx + len(kw)
                    hits += 1
        else:
            out.append(f"{label} cache: MISSING for {u}")
    out.append("")

(ROOT / ".scratch" / "b45_out.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote .scratch/b45_out.txt")
