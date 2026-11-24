import json, pathlib

cache = pathlib.Path(".cache/pages")
out = []
keys = [
    "2027admin-guide-en.pdf",
    "civil.t.u-tokyo.ac.jp",
    "t.u-tokyo.ac.jp/en/study-at-utokyo/soe/",
    "t.u-tokyo.ac.jp/en/soe/admission/special",
    "scholarships.html",
    "s.u-tokyo.ac.jp/en/admission/doctor/index.html",
    "bs.s.u-tokyo.ac.jp/admission/",
    "m.u-tokyo.ac.jp/daigakuin/apply/appguidemain.html",
    "Guidelines-for-toefl-scores_2027_e.pdf",
    "2027_ag_d_e.pdf",
]
for f in sorted(cache.glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if "u-tokyo.ac.jp" not in u.lower():
        continue
    if any(k.lower() in u.lower() for k in keys):
        t = d.get("text", "")
        if "2027admin-guide-en.pdf" in u:
            out.append(f"=== {u} (tail 31000:) ===\n" + t[31000:])
        elif "2027_ag_d_e.pdf" in u:
            out.append(f"=== {u} (tail 21000:) ===\n" + t[21000:])
        else:
            st = d.get("status")
            out.append(f"=== {u} status={st} len={len(t)} ===\n" + t[:6000])
pathlib.Path("scratch/ut_ci_civil.txt").write_text("\n\n".join(out), encoding="utf-8")
print("Wrote", len(out))
