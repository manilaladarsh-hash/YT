import json, pathlib

cache = pathlib.Path(".cache/pages")
targets = [
    "GSGC/pdf/Guidelines.pdf",
    "chem_graduate/apply_en.html",
    "dss.i.u-tokyo.ac.jp",
    "englishnotes2027DR_0507en.pdf",
    "englishnotes_2027koukikokuho_en.pdf",
    "TOEFL_2027(E)_2.pdf",
    "Schdedule_B_2.pdf",
    "2027guidelines_for_applicants_to_dc.pdf",
    "s.u-tokyo.ac.jp/en/admission/graduate.html",
    "u-tokyo.ac.jp/en/prospective-students/exemptions.html",
    "u-tokyo.ac.jp/en/prospective-students/tuition_fees.html",
]
out = []
for f in sorted(cache.glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if any(t.lower() in u.lower() for t in targets):
        txt = d.get("text", "")
        if "2027guidelines_for_applicants_to_dc" in u or "graduate.html" in u:
            out.append(f"=== {u} (len={len(txt)}) ===\n{txt[:6000]}\n---TAIL---\n{txt[-4000:]}")
        else:
            out.append(f"=== {u} (len={len(txt)}) ===\n{txt}")
pathlib.Path("scratch/ut_verify_quotes.txt").write_text("\n\n".join(out), encoding="utf-8")
print("Wrote", len(out))
