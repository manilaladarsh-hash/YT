import json
from pathlib import Path

cache = Path(".cache/pages")
by_url = {}
for p in cache.glob("*.json"):
    rec = json.loads(p.read_text(encoding="utf-8"))
    u = rec.get("url", "")
    if "u-tokyo" in u:
        by_url[u] = rec

targets = [
    ("Math Regular PDF", "ab618a1da5ae3af387a2609065bc68980102cda1", 0, 40000),
    ("IST CS guide", "cs_admission_guide2027_en.pdf", 0, 20000),
    ("IST MI guide", "mi-2027-e.pdf", 0, 20000),
    ("IST CI guide (all)", "2027admin-guide-en.pdf", 18000, 45000),
    ("IST TOEFL guide", "Guidelines-for-toefl-scores_2027_e.pdf", 0, 20000),
    ("ME guide tail", "me_guide", 9000, 30000),
    ("EE guide tail", "ee_guide", 9000, 30000),
    ("ChemSys guide tail", "cs_guide", 9000, 30000),
    ("Civil admission", "civil.t.u-tokyo.ac.jp", 0, 15000),
    ("Med doctor2027E tail", "doctor2027E.pdf", 18000, 45000),
    ("Med koukikoku2027E tail", "koukikoku2027E.pdf", 18000, 45000),
    ("Tuition scholarships", "tuition_scholarships.html", 0, 15000),
    ("Sci departments", "s.u-tokyo.ac.jp/en/departments/index.html", 0, 15000),
    ("Sci grad adm links", "s.u-tokyo.ac.jp/en/admission/graduate.html", 0, 20000),
    ("GSFS guidelines dc tail", "2027guidelines_for_applicants_to_dc", 16000, 45000),
    ("GSFS CSE web", "complex/html/examinee", 0, 15000),
    ("GSFS AMS full", "01AMS_BD_e.pdf", 0, 15000),
    ("GSFS NENV web", "nenv.k.u-tokyo.ac.jp", 0, 15000),
    ("Pharmacy", "f.u-tokyo.ac.jp", 0, 15000),
]

out = []
for label, sub, s, e in targets:
    matches = [u for u in sorted(by_url) if sub in u]
    out.append("=" * 72)
    out.append(f"[{label}] matches={matches}")
    for u in matches:
        rec = by_url[u]
        txt = rec.get("text", "")
        out.append(f"--- {u} (status={rec.get('status')}, final={rec.get('final_url')}, len={len(txt)}) ---")
        out.append(txt[s:e])
        if rec.get("links"):
            seen = set()
            useful = []
            for ltext, lurl in rec["links"]:
                if lurl in seen:
                    continue
                seen.add(lurl)
                if any(k in (ltext + " " + lurl).lower() for k in ["pdf", "guide", "admiss", "exam", "english", "toefl", "phys", "astron", "chem", "bio", "math", "special", "gsgc", "tuition", "exempt", "scholar"]):
                    useful.append((ltext[:60], lurl))
            if useful:
                out.append("  USEFUL LINKS:")
                for lt, lu in useful[:60]:
                    out.append(f"    {lt!r} -> {lu}")

Path("scratch/ut_tails.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote scratch/ut_tails.txt lines:", len("\n".join(out).splitlines()))
