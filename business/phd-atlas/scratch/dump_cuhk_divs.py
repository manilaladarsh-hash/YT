import hashlib, json
from pathlib import Path

urls = [
    "https://www.bme.cuhk.edu.hk",
    "https://www.cse.cuhk.edu.hk",
    "https://www.cse.cuhk.edu.hk/academics/rpg/admission/",
    "https://www.cse.cuhk.edu.hk/academics/rpg/",
    "http://www.ee.cuhk.edu.hk/en-gb/curriculum/mphil-phd-programme",
    "http://www.ee.cuhk.edu.hk/en-gb/curriculum/mphil-phd-programme/admission",
    "https://www.ie.cuhk.edu.hk/programmes/mphil-phd-in-information-engineering/admission-to-mphil-phd/",
    "https://www.ie.cuhk.edu.hk/programmes/phd.shtml",
    "https://www4.mae.cuhk.edu.hk/research-postgraduate-programme/",
    "http://www.se.cuhk.edu.hk/programmes/mphil-phd.html",
    "http://www.iseis.cuhk.edu.hk/en/phd.html",
    "https://www3.sbs.cuhk.edu.hk/en/graduate-education/",
    "https://sphpc.cuhk.edu.hk/rpg-programme",
    "http://www.mect.cuhk.edu.hk/research/phd.html",
    "https://www.pae.cuhk.edu.hk/rpgs",
    "https://mic.cuhk.edu.hk/information-for-postgraduate-study-in-department-of-microbiology/",
    "https://www.pharmacy.cuhk.edu.hk/1/education/rpg/",
    "https://www.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-physics",
    "https://www.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-materials-science-engineering",
    "https://www.sls.cuhk.edu.hk/education/postgraduate/programmes-and-admissions/",
    "https://www.sta.cuhk.edu.hk/rpSTA",
    "http://www.math.cuhk.edu.hk/postgraduates/research-programmes",
    "https://www.ees.cuhk.edu.hk/programme/postgraduate-programme/",
    "http://www.cuhk.edu.hk/chem/en/prog/mph.html",
    "https://www.grm.cuhk.edu.hk/en/pg/research-postgraduate/admission-rpg/",
    "https://www.gs.cuhk.edu.hk/programmes/social-science/mphil-phd-psychology",
    "https://www.psy.cuhk.edu.hk/academics/research-postgraduate-programmes/",
]

out = []
for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    p = Path(".cache/pages") / f"{h}.json"
    if not p.exists():
        out.append("=" * 80)
        out.append(f"MISSING: {u}")
        continue
    d = json.load(open(p, encoding="utf-8"))
    out.append("=" * 80)
    out.append(f"URL: {u}  (STATUS: {d.get('status')}, FINAL: {d.get('final_url', u)})")
    out.append(d.get("text", ""))
    links = []
    for l in d.get("links", []):
        t = l[0] if isinstance(l, (list, tuple)) else l.get("text", "")
        hr = l[1] if isinstance(l, (list, tuple)) else l.get("href", "")
        if any(k in hr.lower() or k in t.lower() for k in ["admi", "phd", "mphil", "rpg", "postgrad", "astro", "faq", "fund", "scholar", "supervis", "gre"]):
            links.append((t, hr))
    if links:
        out.append("RELEVANT LINKS:")
        seen = set()
        for t, hr in links:
            if hr not in seen:
                seen.add(hr)
                out.append(f"  {t} -> {hr}")

txt = "\n".join(out)
Path("scratch/cuhk_divs.txt").write_text(txt, encoding="utf-8")
print("Wrote lines:", len(txt.splitlines()))
