import json
import pathlib

targets = {
    "https://www.ms.u-tokyo.ac.jp/kyoumu_e/liaison/guide_e.html",
    "https://www.ms.u-tokyo.ac.jp/kyoumu/ab618a1da5ae3af387a2609065bc68980102cda1.pdf",
    "https://www.k.u-tokyo.ac.jp/en/gsfs/financial_support/",
    "https://www.cbms.k.u-tokyo.ac.jp/en/admission/application/",
    "https://www.s.u-tokyo.ac.jp/en/offices/ilo/scholarship.html",
    "https://www.m.u-tokyo.ac.jp/english/daigakuin/apply/appguidemain.html",
    "https://www.t.u-tokyo.ac.jp/hubfs/admission/2026/0403/Guidelines_gse_en_d_2027.pdf",
    "https://www.i.u-tokyo.ac.jp/edu/entra/2027_ag_d_e.pdf",
    "https://www.s.u-tokyo.ac.jp/en/admission/graduate.html",
    "https://www.s.u-tokyo.ac.jp/en/admission/doctor/index.html",
    "https://www.k.u-tokyo.ac.jp/en/exam/info/",
}
out = []
for p in sorted(pathlib.Path(".cache/pages").glob("*.json")):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    fu = d.get("final_url", "")
    if u in targets or fu in targets:
        out.append(f"=== {u} (final={fu}, file={p.name}) ===")
        if u != "https://www.m.u-tokyo.ac.jp/english/daigakuin/apply/appguidemain.html":
            out.append(d.get("text", ""))
        if "ms.u-tokyo" in u or "m.u-tokyo" in u or "cbms.k.u-tokyo" in u:
            for lnk in d.get("links", []):
                out.append(f"LINK: {lnk}")
pathlib.Path("scratch/utokyo_task4581.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote", len(out), "lines")
