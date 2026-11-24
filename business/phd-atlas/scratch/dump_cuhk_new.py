import hashlib
import json
import pathlib

urls = [
    "https://www.bme.cuhk.edu.hk/new/mphil-phd.php",
    "https://www.cse.cuhk.edu.hk/admission/mphil-phd/",
    "https://www.cse.cuhk.edu.hk/academics/mphil-phd/",
    "https://www.cse.cuhk.edu.hk/academics/scholarships/",
    "https://www.sls.cuhk.edu.hk/education/postgraduate/",
    "https://www.gs.cuhk.edu.hk/programmes/medicine/phd-imaging-and-interventional-radiology",
    "https://www.gs.cuhk.edu.hk/programmes/medicine/phd-chemical-pathology",
    "https://www.ets.org/gre/score-users/about/subject-tests.html",
    "http://www.ee.cuhk.edu.hk/en-gb/curriculum/mphil-phd-programme/faq",
    "https://www.se.cuhk.edu.hk/programmes/postgraduate-programmes/research-postgraduate-programmes/qualifications-for-admission/",
    "https://www.se.cuhk.edu.hk/programmes/postgraduate-programmes/research-postgraduate-programmes/m-phil-ph-d-programme-finanical-aid/",
    "https://www3.sbs.cuhk.edu.hk/en/admission/",
    "https://www.sta.cuhk.edu.hk/programmes/3",
    "https://www.math.cuhk.edu.hk/postgraduates/admission",
    "https://www.math.cuhk.edu.hk/postgraduates/research-programmes/phd-mathematics",
    "https://app.phy.cuhk.edu.hk/research-areas/astrophysics-fundamental-physics/",
    "https://www.erg.cuhk.edu.hk/erg/Departments",
    "https://www.psy.cuhk.edu.hk/en/graduate/m-phil-ph-d-in-psychology.html",
]

out = []
for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    p = pathlib.Path(".cache/pages") / f"{h}.json"
    if not p.exists():
        out.append(f"MISSING: {u}")
        continue
    d = json.loads(p.read_text(encoding="utf-8"))
    out.append("=" * 80)
    out.append(f"URL: {u} (final={d.get('final_url')})")
    out.append(d.get("text", ""))

pathlib.Path("scratch/cuhk_new_pages.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote lines:", sum(x.count("\n") + 1 for x in out))
