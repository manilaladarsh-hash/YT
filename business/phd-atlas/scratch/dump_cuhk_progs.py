import hashlib
import json
import pathlib

urls = [
    "https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-biomedical-engineering",
    "https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-computer-science-and-engineering",
    "https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-electronic-engineering",
    "https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-information-engineering",
    "https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-mechanical-and-automation-engineering",
    "https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-systems-engineering-and-engineering-management",
    "https://www.gs.cuhk.edu.hk/programmes/inter-faculty/mphil-phd-earth-system-and-geoinformation-science",
    "https://www.gs.cuhk.edu.hk/programmes/medicine/mphil-phd-biomedical-sciences",
    "https://www.gs.cuhk.edu.hk/programmes/medicine/mphil-phd-translational-genomics",
    "https://www.gs.cuhk.edu.hk/programmes/medicine/mphil-phd-public-health",
    "https://www.gs.cuhk.edu.hk/programmes/medicine/phd-medical-sciences",
    "https://www.gs.cuhk.edu.hk/programmes/medicine/phd-microbiology",
    "https://www.gs.cuhk.edu.hk/programmes/medicine/phd-pharmacy",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-physics",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-biochemistry",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-biology",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-cell-and-molecular-biology",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-environmental-science",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-food-and-nutritional-sciences",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-molecular-biotechnology",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-statistics",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-mathematics",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-materials-science-and-engineering",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-earth-and-environmental-sciences",
    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-chemistry",
    "https://www.gs.cuhk.edu.hk/programmes/social-science/mphil-phd-geography-and-resource-management",
]

out = []
for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    p = pathlib.Path(".cache/pages") / f"{h}.json"
    if not p.exists():
        out.append(f"MISSING: {u}")
        continue
    d = json.loads(p.read_text(encoding="utf-8"))
    txt = d.get("text", "")
    # strip repeated header nav up to last Breadcrumb
    idx = txt.rfind("Breadcrumb")
    if idx != -1:
        txt = txt[idx:]
    end = txt.find("This website uses Cookies")
    if end != -1:
        txt = txt[:end]
    out.append("=" * 80)
    out.append(f"URL: {u}")
    out.append(txt.strip())
    links = [f"  {a} -> {b}" for a, b in d.get("links", []) if "gs.cuhk.edu.hk" not in b and "facebook" not in b and "instagram" not in b and "linkedin" not in b and "cuhk.edu.hk/" in b]
    if links:
        out.append("DIV LINKS:")
        out.extend(links)

pathlib.Path("scratch/cuhk_progs.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote", len(out), "lines to scratch/cuhk_progs.txt")
