import requests, re

sitemaps = [
    "https://nusgs.nus.edu.sg/page-sitemap.xml",
    "https://www.science.nus.edu.sg/page-sitemap.xml",
    "https://cde.nus.edu.sg/page-sitemap.xml",
    "https://cde.nus.edu.sg/page-sitemap2.xml",
    "https://www.comp.nus.edu.sg/page-sitemap.xml",
    "https://medicine.nus.edu.sg/page-sitemap.xml",
    "https://fass.nus.edu.sg/geog/page-sitemap.xml",
    "https://sph.nus.edu.sg/page-sitemap.xml",
    "https://sph.nus.edu.sg/education-page-sitemap.xml",
    "https://www.dbs.nus.edu.sg/page-sitemap.xml",
    "https://chemistry.nus.edu.sg/page-sitemap.xml",
    "https://www.math.nus.edu.sg/page-sitemap.xml",
    "https://www.physics.nus.edu.sg/wp-sitemap-posts-page-1.xml",
    "https://www.stat.nus.edu.sg/page-sitemap.xml",
]
kw = ["phd", "doctor", "grad", "admis", "requir", "faq", "deadlin", "toefl", "ielts", "gre", "fee", "bme", "chbe", "cee", "ece", "mse", "me/", "isep", "data", "scholar"]
for sm in sitemaps:
    try:
        r = requests.get(sm, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        locs = re.findall(r"<loc>(.*?)</loc>", r.text)
        print(f"=== {sm} ({len(locs)}) ===")
        for u in sorted(set(locs)):
            ul = u.lower()
            if "undergrad" in ul:
                continue
            if any(k in ul for k in kw):
                print(" ", u.replace("http://", "https://"))
    except Exception as e:
        print("ERR", sm, e)
