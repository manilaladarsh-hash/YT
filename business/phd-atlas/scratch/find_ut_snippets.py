import json, os, re

cache_dir = ".cache/pages"
by_url = {}
for fn in os.listdir(cache_dir):
    if fn.endswith(".json"):
        with open(os.path.join(cache_dir, fn), encoding="utf-8") as f:
            d = json.load(f)
        by_url[d["url"]] = d.get("text", "")

queries = [
    ("u-tokyo.ac.jp/en/prospective-students/tuition_fees.html", ["Examination fee", "30,000", "Japanese government", "exemptions.html"]),
    ("s.u-tokyo.ac.jp/en/admission/graduate.html", ["December", "10,000", "TOEFL", "GRE", "supervisor", "stipend", "Doctoral"]),
    ("s.u-tokyo.ac.jp/GSGC/overview/index.html", ["10,000", "180,000", "December", "Physics", "Astronomy", "Chemistry", "Biological", "Earth"]),
    ("bs.s.u-tokyo.ac.jp/admission/", ["TOEFL", "GRE", "supervisor", "contact", "December", "October", "Master"]),
    ("eps.s.u-tokyo.ac.jp/index.php?page_id=16483", ["GSGC", "GRE", "TOEFL", "supervisor", "admission", "Doctor"]),
    ("i.u-tokyo.ac.jp/edu/entra/Guidelines-for-toefl-scores_2027_e.pdf", ["native English", "TOEFL"]),
    ("cs_admission_guide", ["supervisor", "contact", "research proposal", "GRE", "TOEFL"]),
    ("mi-2027-e.pdf", ["advisor", "supervisor", "contact", "meet", "GRE", "TOEFL"]),
    ("2027admin-guide-en.pdf", ["Doctoral", "Research Plan", "Winter", "advisor", "supervisor", "TOEFL"]),
    ("i.u-tokyo.ac.jp/edu/financial-support/index_e.shtml", ["WINGS", "RA", "SPRING", "fellowship", "stipend", "yen"]),
    ("Prospectus-2027", ["10,000", "Round III", "2/17", "supervisor", "acceptance letter", "GRE", "TOEFL", "Mechanical", "Electrical", "Materials", "Chemical System", "Bioengineering"]),
    ("civil.t.u-tokyo.ac.jp/en/admission/", ["March", "2027", "MEXT", "ADB", "TOEFL", "GRE", "supervisor"]),
    ("k.u-tokyo.ac.jp/en/exam/faq/", ["contact", "professor", "supervisor", "fee"]),
    ("k.u-tokyo.ac.jp/en/exam/info/", ["10,000", "30,000", "November", "Sustainability"]),
    ("sih.m.u-tokyo.ac.jp/", ["Biomedical", "Genetics", "International Health", "doctor", "admission"]),
    ("koukikoku2027E.pdf", ["January", "2027", "contact", "faculty", "30,000", "10,000", "Master", "TOEFL"]),
    ("doctor2027E.pdf", ["contact", "professor", "faculty", "supervisor", "30,000", "Master", "Neuroscience", "July"]),
    ("ece", ["acceptance letter", "supervisor", "GRE", "TOEFL", "IME"]),
    ("material.t.u-tokyo.ac.jp", ["acceptance letter", "supervisor", "GRE", "TOEFL", "IME", "Doctoral"]),
    ("chemsys.t.u-tokyo.ac.jp", ["acceptance letter", "supervisor", "GRE", "TOEFL", "IME", "Doctoral"]),
    ("bioeng.t.u-tokyo.ac.jp", ["acceptance letter", "supervisor", "GRE", "TOEFL", "IME", "Doctoral"]),
    ("mech.t.u-tokyo.ac.jp", ["acceptance letter", "supervisor", "GRE", "TOEFL", "IME", "Doctoral"]),
]

out = []
for ufrag, kws in queries:
    matched = [u for u in by_url if ufrag in u]
    out.append(f"\n### QUERY: {ufrag} (matches={len(matched)}) ###")
    for u in matched[:5]:
        t = by_url[u]
        out.append(f"  URL: {u} (len={len(t)})")
        for kw in kws:
            for m in re.finditer(re.escape(kw), t, re.I):
                s = max(0, m.start() - 80)
                e = min(len(t), m.end() + 180)
                snippet = " ".join(t[s:e].split())
                out.append(f"    [{kw}]: {snippet}")
                break

with open("scratch/ut_snippets.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Wrote scratch/ut_snippets.txt, lines:", len(out))
