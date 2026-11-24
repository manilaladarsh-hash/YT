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
    ("nmsu--ece.json", "entry_route", ["BSEE", "MSEE", "Ph.D.", "degree", "admission", "prerequisite", "Bachelor", "Master"]),
    ("northwestern--biomed.json", "gre_general", ["GRE", "optional", "Subject", "scores", "test"]),
    ("northwestern--biomed.json", "gre_subject", ["GRE", "optional", "Subject", "scores", "test"]),
    ("northwestern--civil.json", "ielts_min", ["IELTS", "TOEFL", "English", "7 or higher"]),
    ("northwestern--materials.json", "english_waiver", ["TOEFL", "IELTS", "English", "waiver", "exempt", "India", "language"]),
    ("nyu--math.json", "supervisor", ["supervisor", "advisor", "adviser", "faculty", "committee", "Admission decisions"]),
    ("nyu--mech.json", "entry_route", ["Admission to this program", "BS", "B.S.", "bachelor", "MS", "M.S.", "master"]),
    ("odu--biology.json", "gre_general", ["GRE", "Biology", "Graduate", "Transcripts", "Test", "Entrance", "exam"]),
    ("odu--environment.json", "gre_general", ["GRE", "Ocean", "Earth", "Transcripts", "Test", "Entrance", "exam"]),
]

out = []
seen_pages = set()
for fname, field, kws in targets:
    p = ROOT / "data" / "programs" / fname
    d = json.loads(p.read_text(encoding="utf-8"))
    fobj = d["fields"][field]
    url = fobj.get("url", "")
    out.append(f"=== {fname} | {field} ===")
    out.append(f"program_page: {d.get('program_page')}")
    out.append(f"field: {json.dumps(fobj, ensure_ascii=False)}")
    if url in by_url:
        cname, text = by_url[url]
        out.append(f"cache ({cname}, len={len(text)}):")
        for kw in kws:
            pos = 0
            hits = 0
            while hits < 3:
                idx = text.lower().find(kw.lower(), pos)
                if idx == -1:
                    break
                start = max(0, idx - 250)
                end = min(len(text), idx + 450)
                out.append(f"  [kw={kw} @ {idx}] ...{text[start:end]}...")
                pos = idx + len(kw)
                hits += 1
    else:
        out.append(f"cache: MISSING for {url}")
    pp = d.get("program_page", "")
    if pp and pp != url and pp in by_url and pp not in seen_pages:
        seen_pages.add(pp)
        cname, text = by_url[pp]
        out.append(f"program_page cache ({cname}, len={len(text)}):")
        for kw in kws:
            idx = text.lower().find(kw.lower())
            if idx != -1:
                start = max(0, idx - 200)
                end = min(len(text), idx + 400)
                out.append(f"  [pp kw={kw} @ {idx}] ...{text[start:end]}...")
    out.append("")

(ROOT / ".scratch" / "b44_out.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote .scratch/b44_out.txt")
