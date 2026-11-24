import re, urllib.request, ssl
from urllib.parse import urljoin

ctx = ssl._create_unverified_context()

targets = [
    "https://www.u-tokyo.ac.jp/en/",
    "https://www.ms.u-tokyo.ac.jp/index.html",
    "https://www.f.u-tokyo.ac.jp/en/exam/",
    "https://www.a.u-tokyo.ac.jp/english/pstudents_e/g_rcourses.html",
    "https://www.t.u-tokyo.ac.jp/en/study-at-utokyo/soe/apply/guideline",
    "https://www.m.u-tokyo.ac.jp/english/daigakuin/apply/appguidemain.html",
    "https://www.s.u-tokyo.ac.jp/en/admission/",
    "https://www.s.u-tokyo.ac.jp/en/admission/graduate.html",
    "https://ipads.a.u-tokyo.ac.jp/admissions/how-to-apply-phd/",
]

kws = ["admis", "grad", "exam", "doct", "phd", "gsgc", "ipads", "guideline", "pdf", "fee", "exemp", "fellow", "scholar", "toefl", "english", "foreign", "biome", "neuro", "chem", "mech", "elec", "civil", "mat", "info", "cs", "math", "phys", "astro", "earth", "bio", "iap"]

for u in targets:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        html = urllib.request.urlopen(req, timeout=15, context=ctx).read().decode("utf-8", "replace")
        raw = re.findall(r'href=["\']([^"\'#]+)["\']', html)
        links = sorted({urljoin(u, x) for x in raw})
        print(f"\n=== {u} ({len(links)} total) ===")
        for l in links:
            low = l.lower()
            if any(k in low for k in kws) and not any(x in low for x in [".css", ".ico", ".png", ".jpg", ".svg"]):
                print(" ", l)
    except Exception as e:
        print(f"\nERR {u}: {e}")
