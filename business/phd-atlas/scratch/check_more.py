import json, os, re

cache_dir = ".cache/pages"
by_url = {}
for fn in os.listdir(cache_dir):
    if fn.endswith(".json"):
        with open(os.path.join(cache_dir, fn), encoding="utf-8") as f:
            d = json.load(f)
        by_url[d["url"]] = d.get("text", "")

out = []
for u, t in sorted(by_url.items()):
    if any(k in u for k in ["ime.t.u-tokyo.ac.jp/Prospectus-2027", "k.u-tokyo.ac.jp/en/exam/info", "koukikoku2027E.pdf", "doctor2027E.pdf", "i.u-tokyo.ac.jp/edu/course/cs/cs_admission_guide2027_en.pdf", "i.u-tokyo.ac.jp/edu/course/mi/upload/mi-2027-e.pdf", "i.u-tokyo.ac.jp/edu/course/ci/2026/2027admin-guide-en.pdf", "i.u-tokyo.ac.jp/edu/financial-support/index_e.shtml", "eps.s.u-tokyo.ac.jp", "bs.s.u-tokyo.ac.jp"]):
        if "Prospectus-2027" in u:
            out.append(f"\n=== {u} (English/TOEFL/IELTS/Form 3) ===")
            idx = t.find("Form 3")
            if idx != -1:
                out.append(t[max(0,idx-1200):idx+1800])
            idx2 = t.find("English")
            if idx2 != -1:
                out.append(t[max(0,idx2-200):idx2+1200])
        elif "koukikoku2027E.pdf" in u:
            out.append(f"\n=== {u} (period/fee) ===")
            for pat in [r"between\s+Fr", r"submission period", r"10,000|30,000|MEXT|Monbukagakusho"]:
                for m in re.finditer(pat, t, re.I):
                    out.append("  " + repr(t[max(0,m.start()-60):m.end()+260]))
        elif "doctor2027E.pdf" in u:
            out.append(f"\n=== {u} (fee/MEXT) ===")
            for pat in [r"Monbukagakusho|MEXT|exempt", r"Exam fee"]:
                for m in re.finditer(pat, t, re.I):
                    out.append("  " + repr(t[max(0,m.start()-60):m.end()+260]))
        elif "i.u-tokyo.ac.jp/edu/financial-support" in u:
            out.append(f"\n=== {u} ===")
            out.append(t)
        elif "eps.s.u-tokyo.ac.jp/index.php?page_id=16483" in u:
            out.append(f"\n=== {u} ===")
            out.append(t)
        elif "bs.s.u-tokyo.ac.jp/admission/" in u:
            out.append(f"\n=== {u} ===")
            out.append(t[:4000])
        elif "2027admin-guide-en.pdf" in u:
            out.append(f"\n=== {u} (Section 3.3) ===")
            idx = t.find("3.3")
            if idx != -1:
                out.append(t[idx:idx+3000])

# Also check any other cached u-tokyo funding/scholarship pages
for u, t in sorted(by_url.items()):
    if "u-tokyo.ac.jp" in u and any(w in u for w in ["scholarship", "financial", "fellowship", "support"]):
        out.append(f"\n=== FUNDING PAGE: {u} (len={len(t)}) ===")
        out.append(t[:2000])

with open("scratch/exact_more.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Wrote scratch/exact_more.txt, len:", sum(len(x) for x in out))
