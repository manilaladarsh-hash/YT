import json
from pathlib import Path

cache = Path(r"C:\Users\manil\YT\business\phd-atlas\.cache\pages")
by_url = {}
for p in cache.glob("*.json"):
    rec = json.loads(p.read_text(encoding="utf-8"))
    by_url[rec["url"]] = rec

targets = [
    "https://www.i.u-tokyo.ac.jp/edu/entra/2027_ag_d_e.pdf",
    "https://www.i.u-tokyo.ac.jp/edu/course/cs/cs_admission_guide2027_en.pdf",
    "https://www.i.u-tokyo.ac.jp/edu/course/ci/admission_e.shtml",
    "https://www.i.u-tokyo.ac.jp/edu/course/mi/upload/mi-2027-e.pdf",
    "https://www.i.u-tokyo.ac.jp/edu/entra/entra_e.shtml",
    "https://www.t.u-tokyo.ac.jp/en/study-at-utokyo/soe/international-programs",
    "https://www.t.u-tokyo.ac.jp/hubfs/admission/2026/international-admission/II%E3%80%90%E5%85%B1%E9%80%9A%E3%80%91General%20Application%20Guidelines%202027_Doctoral%20Degree.pdf",
    "https://www.t.u-tokyo.ac.jp/hubfs/admission/2026/0403/Guidelines_gse_en_d_2027.pdf",
    "https://www.civil.t.u-tokyo.ac.jp/en/admission/",
    "https://www.chembio.t.u-tokyo.ac.jp/e/admission/exam_special.html",
    "https://www.k.u-tokyo.ac.jp/en/assets/files/01AMS_BD_e.pdf",
    "https://www.a.u-tokyo.ac.jp/english/pstudents_e/3-2_Admission_Guidelines_D_e_2027.pdf",
    "https://www.s.u-tokyo.ac.jp/en/admission/graduate.html",
    "https://www.s.u-tokyo.ac.jp/en/admission/doctor/index.html",
    "https://www.s.u-tokyo.ac.jp/en/admission/scholarship.html",
    "https://www.eps.s.u-tokyo.ac.jp/index.php?page_id=16483",
    "https://www.chem.s.u-tokyo.ac.jp/chem_graduate/apply_en.html",
    "https://www.bs.s.u-tokyo.ac.jp/english/",
    "https://www.f.u-tokyo.ac.jp/en/",
    "https://www.t.u-tokyo.ac.jp/en/campus-life/community/scholarships",
    "https://www.t.u-tokyo.ac.jp/en/soe/admission/scholarship",
]

out = []
for u in targets:
    rec = by_url.get(u)
    if not rec:
        out.append(f"=== MISSING {u} ===")
        continue
    out.append(f"=== {u} (status={rec.get('status')}, final={rec.get('final_url')}, len={len(rec.get('text',''))}) ===")
    out.append(rec.get("text", "")[:15000])
    links = rec.get("links", [])
    if links:
        out.append("--- LINKS (filtered) ---")
        for l in links:
            out.append(f"  {l}")
    out.append("")

Path(r"C:\Users\manil\YT\business\phd-atlas\scratch\ut_dump_a.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote scratch/ut_dump_a.txt lines:", len("\n".join(out).splitlines()))
