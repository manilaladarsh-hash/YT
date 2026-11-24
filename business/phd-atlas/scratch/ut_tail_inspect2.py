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
    ("Science graduate.html bottom", "s.u-tokyo.ac.jp/en/admission/graduate.html", 12000, 30000),
    ("GSGC FAQ", "s.u-tokyo.ac.jp/GSGC/faq", 0, 15000),
    ("GSGC overview", "s.u-tokyo.ac.jp/GSGC/overview", 0, 15000),
    ("GSFS CBMS schedule", "cbms.k.u-tokyo.ac.jp/en/admission/schedule", 0, 15000),
    ("GSFS CBMS app", "cbms.k.u-tokyo.ac.jp/en/admission/application", 0, 15000),
    ("GSFS CBMS faq", "cbms.k.u-tokyo.ac.jp/en/admission/faq", 0, 15000),
    ("Med englishnotes DR", "englishnotes2027DR", 0, 15000),
    ("Med englishnotes IH", "englishnotes_2027koukikokuho", 0, 15000),
    ("Med sih", "sih.m.u-tokyo.ac.jp", 0, 10000),
    ("Med springgx", "springgx.html", 0, 10000),
    ("Agri D pg1-10", "3-2_Admission_Guidelines_D_e_2027.pdf", 0, 15000),
    ("Agri D pg11-end", "3-2_Admission_Guidelines_D_e_2027.pdf", 15000, 40000),
    ("IST 2027_ag_d_e tail2", "2027_ag_d_e.pdf", 18000, 40000),
    ("IST cs admission_e", "edu/course/cs/admission_e", 0, 12000),
    ("IST ipc admissions_e", "edu/course/ipc/admissions_e", 0, 12000),
    ("IST mi admission_e", "edu/course/mi/admission_e", 0, 12000),
    ("IST ci admission_e", "edu/course/ci/admission_e", 0, 12000),
    ("IME Prospectus bottom", "ime.t.u-tokyo.ac.jp/Prospectus-2027.html", 15000, 35000),
    ("Math Special", "ms.u-tokyo.ac.jp/kyoumu_e/liaison/guide_e.html", 0, 15000),
    ("UTokyo exemptions", "u-tokyo.ac.jp/en/prospective-students/exemptions.html", 0, 20000),
    ("GSFS Scholarship", "k.u-tokyo.ac.jp/en/gsfs/financial_support", 0, 12000),
    ("IST Financial support", "i.u-tokyo.ac.jp/edu/financial-support/index_e.shtml", 0, 12000),
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

Path("scratch/ut_tails2.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote scratch/ut_tails2.txt lines:", len("\n".join(out).splitlines()))
