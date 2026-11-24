import json
from pathlib import Path

cache = Path(".cache/pages")
by_url = {}
for p in cache.glob("*.json"):
    rec = json.loads(p.read_text(encoding="utf-8"))
    u = rec.get("url", "")
    if "u-tokyo" in u:
        by_url[u] = rec

print(f"Total tokyo cached: {len(by_url)}")

targets = [
    ("IST 2027_ag_d_e.pdf tail", "i.u-tokyo.ac.jp/edu/entra/2027_ag_d_e.pdf", 8500, 35000),
    ("Eng II General Guidelines tail", "General%20Application%20Guidelines%202027_Doctoral", 8500, 35000),
    ("Eng Regular Guidelines tail", "Guidelines_gse_en_d_2027.pdf", 8500, 35000),
    ("IME Prospectus 2027", "ime.t.u-tokyo.ac.jp/Prospectus-2027.html", 0, 28000),
    ("ME guide", "me_guide", 0, 10000),
    ("EE guide", "ee_guide", 0, 10000),
    ("ChemSys guide", "cs_guide", 0, 10000),
    ("Eng Intl Eligibility", "requirements_for_eligibility_doctor", 0, 10000),
    ("Math Regular PDF", "59127a7335c3da45ab618a1da5ae3af387a2609065bc68980102cda1", 0, 20000),
    ("Math Special Selection", "ms.u-tokyo.ac.jp/kyoumu_e/liaison/guide_e.html", 0, 15000),
    ("GSFS exam info", "k.u-tokyo.ac.jp/en/exam/info", 0, 16000),
    ("GSFS FAQ", "k.u-tokyo.ac.jp/en/exam/faq", 0, 16000),
    ("GSFS Scholarship", "Scholarship_GSFS", 0, 16000),
    ("GSFS guidelines dc", "2027guidelines_for_applicants_to_dc", 0, 16000),
    ("GSFS AMS", "01AMS_BD_e.pdf", 0, 15000),
    ("GSFS CSE", "03CSE_BD_e.pdf", 0, 15000),
    ("GSFS IB", "04IB_BD_e.pdf", 0, 15000),
    ("GSFS CBMS", "05CBMS_BD_e.pdf", 0, 15000),
    ("GSFS NENV", "06NENV_BD_e.pdf", 0, 15000),
    ("GSFS GPSS", "12GPSS_BD_e.pdf", 0, 15000),
    ("Med koukikoku2027E", "koukikoku2027E.pdf", 0, 20000),
    ("Med doctor2027E", "doctor2027E.pdf", 0, 20000),
    ("Med sih", "sih.m.u-tokyo.ac.jp", 0, 10000),
    ("Agri D tail", "3-2_Admission_Guidelines_D_e_2027.pdf", 8500, 25000),
    ("DSS IST", "dss.i.u-tokyo.ac.jp", 0, 12000),
    ("IST CI admin guide", "2027admin-guide-en.pdf", 0, 20000),
    ("Eng soe/admission/special", "t.u-tokyo.ac.jp/en/soe/admission/special", 0, 8000),
    ("Eng depts", "t.u-tokyo.ac.jp/en/about/academics/soe/department", 0, 8000),
    ("UTokyo exemptions", "u-tokyo.ac.jp/en/prospective-students/exemptions.html", 0, 12000),
    ("UTokyo tuition_fees", "u-tokyo.ac.jp/en/prospective-students/tuition_fees.html", 0, 12000),
    ("UTokyo scholarships", "u-tokyo.ac.jp/en/prospective-students/scholarships", 0, 12000),
    ("GSGC Guidelines", "GSGC/pdf/Guidelines.pdf", 0, 20000),
    ("GSGC FAQ", "GSGC/faq", 0, 12000),
    ("EPS Grad Adm", "eps.s.u-tokyo.ac.jp", 0, 12000),
    ("Pharmacy exam", "f.u-tokyo.ac.jp/en/exam", 0, 10000),
    ("Pharmacy israr", "israr.f.u-tokyo.ac.jp", 0, 10000),
]

out = ["ALL CACHED TOKYO URLs:"]
for u in sorted(by_url):
    rec = by_url[u]
    out.append(f"  {rec.get('status')} len={len(rec.get('text',''))}: {u}")
out.append("")

for label, sub, s, e in targets:
    matches = [u for u in sorted(by_url) if sub in u]
    out.append("=" * 72)
    out.append(f"[{label}] matches={matches}")
    for u in matches:
        rec = by_url[u]
        txt = rec.get("text", "")
        out.append(f"--- {u} (status={rec.get('status')}, final={rec.get('final_url')}, len={len(txt)}) ---")
        out.append(txt[s:e])
        if s == 0 and rec.get("links"):
            # print only unique non-nav-spam links with useful keywords
            seen = set()
            useful = []
            for ltext, lurl in rec["links"]:
                if lurl in seen:
                    continue
                seen.add(lurl)
                if any(k in (ltext + " " + lurl).lower() for k in ["pdf", "guide", "admiss", "exam", "ime", "iap", "fee", "tuition", "toefl", "english", "gre", "scholar", "waiver", "exempt", "doc", "special", "gsgc", "info", "faq"]):
                    useful.append((ltext[:60], lurl))
            if useful:
                out.append("  USEFUL LINKS:")
                for lt, lu in useful[:40]:
                    out.append(f"    {lt!r} -> {lu}")

Path("scratch/ut_deep.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote scratch/ut_deep.txt lines:", len("\n".join(out).splitlines()))
