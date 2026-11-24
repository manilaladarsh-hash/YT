import json, os, re

cache_dir = ".cache/pages"
by_url = {}
for fn in os.listdir(cache_dir):
    if fn.endswith(".json"):
        with open(os.path.join(cache_dir, fn), encoding="utf-8") as f:
            d = json.load(f)
        by_url[d["url"]] = d.get("text", "")

out = []
def show(u_substr, patterns):
    for u, t in by_url.items():
        if u_substr in u:
            out.append(f"\n=== {u} ===")
            for pat in patterns:
                for m in re.finditer(pat, t, re.I):
                    s = max(0, m.start() - 60)
                    e = min(len(t), m.end() + 260)
                    out.append(f"  [{pat}] -> {repr(t[s:e])}")
                    break

show("Prospectus-2027.html", [r"Only those who receive", r"DO NO NEED", r"GRE is required", r"IELTS score", r"medium of instruction|English was the primary|certificate of English|exemption|exempt", r"MEXT", r"Master's degree", r"Doctor"])
show("civil.t.u-tokyo.ac.jp/en/admission/", [r"19 March 2027", r"ADB-Japan", r"IELTS|TOEFL", r"GRE", r"supervisor", r"Master"])
show("cs_admission_guide2027_en.pdf", [r"Before sending an Application Form", r"Master", r"examination fee|10,000|30,000", r"Winter Entrance"])
show("mi-2027-e.pdf", [r"Applicants are required to meet", r"Master", r"examination fee|10,000|30,000"])
show("2027admin-guide-en.pdf", [r"3\. Doctoral", r"Doctoral program", r"Winter entrance examination", r"Research Plan"])
show("2027_ag_d_e.pdf", [r"10,000|30,000|Examination Fee", r"MEXT|exempt|waiv", r"14:00 on Tuesday, November 17"])
show("i.u-tokyo.ac.jp/edu/financial-support/index_e.shtml", [r"WINGS", r"IST-RA", r"SPRING GX"])
show("k.u-tokyo.ac.jp/en/exam/faq/", [r"contact professors", r"prior to application", r"10,000|30,000|Examination fee"])
show("koukikoku2027E.pdf", [r"Application period", r"must contact faculty", r"10,000|30,000|Exam fee", r"MEXT|exempt", r"Tuition|scholarship|fellowship"])
show("doctor2027E.pdf", [r"From Friday, July 3", r"must contact|prospective supervisor|advance approval", r"30,000", r"Master"])

with open("scratch/exact_utf8.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Wrote scratch/exact_utf8.txt, lines:", len(out))
