import re, urllib.request, ssl
from urllib.parse import urljoin

ctx = ssl._create_unverified_context()
targets = [
    "https://www.i.u-tokyo.ac.jp/edu/course/cs/admission_e.shtml",
    "https://www.i.u-tokyo.ac.jp/edu/course/mi/admission_e.shtml",
    "https://www.i.u-tokyo.ac.jp/edu/entra/entra_e.shtml",
    "https://www.t.u-tokyo.ac.jp/en/study-at-utokyo/soe/international-programs",
    "https://www.ms.u-tokyo.ac.jp/index.html",
    "https://www.ms.u-tokyo.ac.jp/visitor_e/graduate_e.html",
    "https://www.ms.u-tokyo.ac.jp/kyoumu/",
    "https://www.u-tokyo.ac.jp/en/prospective-students/graduate_course_list.html",
    "https://www.chem.s.u-tokyo.ac.jp/en/",
    "https://www.eps.s.u-tokyo.ac.jp/en/",
    "https://www.material.t.u-tokyo.ac.jp/e/prospective_students/",
    "https://bioeng.t.u-tokyo.ac.jp/prospective-students/",
]
for u in targets:
    try:
        html = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=15, context=ctx).read().decode("utf-8", "replace")
        links = sorted({urljoin(u, x) for x in re.findall(r'href=["\']([^"\'#]+)["\']', html)})
        print(f"=== {u} ===")
        for l in links:
            low = l.lower()
            if any(k in low for k in [".pdf", "guide", "admis", "exam", "iap", "2026", "2027", "doctoral", "mater", "mech", "chem", "eeis", "civil", "bio", "mi-", "cs-", "dss", "math", "english"]):
                if not any(x in low for x in [".css", ".png", ".jpg", ".svg", ".ico", ".js"]):
                    print(" ", l)
    except Exception as e:
        print("ERR", u, e)
