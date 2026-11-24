import json
from pathlib import Path

urls = {
    "https://www.ms.u-tokyo.ac.jp/kyoumu/content_10.html",
    "https://www.ms.u-tokyo.ac.jp/kyoumu_e/liaison/index_e.html",
    "https://www.ms.u-tokyo.ac.jp/kyoumu/",
    "https://www.s.u-tokyo.ac.jp/GSGC/pdf/Guidelines.pdf",
    "https://www.s.u-tokyo.ac.jp/GSGC/overview/index.html",
    "https://www.eps.s.u-tokyo.ac.jp/index.php?page_id=16483",
    "https://www.ime.t.u-tokyo.ac.jp/content/files/requirements/requirements_for_eligibility_doctor_2027.pdf",
    "https://www.cbms.k.u-tokyo.ac.jp/en/admission/schedule/",
    "https://nenv.k.u-tokyo.ac.jp/en/admission/admission-information",
    "https://www.k.u-tokyo.ac.jp/en/assets/files/12GPSS_BD_e.pdf",
    "https://www.k.u-tokyo.ac.jp/en/assets/files/Scholarship_GSFS_Entrance_Examination_2026Bver0914.pdf",
    "https://www.m.u-tokyo.ac.jp/daigakuin/apply/file/englishnotes_2027koukikokuho_en.pdf",
    "https://www.sih.m.u-tokyo.ac.jp/",
}

out = []
for p in sorted(Path(".cache/pages").glob("*.json")):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if u in urls or d.get("final_url", "") in urls:
        out.append(f"=== {u} (final={d.get('final_url')}, file={p.name}) ===")
        out.append(d.get("text", ""))
        if d.get("links"):
            out.append("--- LINKS ---")
            for l in d["links"][:80]:
                out.append(str(l))
        out.append("")

Path("scratch/utokyo_new.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote", len(out), "lines", Path("scratch/utokyo_new.txt").stat().st_size, "bytes")
