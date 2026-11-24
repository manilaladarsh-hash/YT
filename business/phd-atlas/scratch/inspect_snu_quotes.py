import hashlib, json
from pathlib import Path

CACHE = Path(".cache/pages")

def get_text(url):
    p = CACHE / f"{hashlib.sha1(url.encode()).hexdigest()[:16]}.json"
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8")).get("text", "")

urls = [
    "https://stat.snu.ac.kr/en/admission/graduate/",
    "https://stat.snu.ac.kr/en/courses/graduate/",
    "https://cuee.snu.ac.kr/EN/index.php",
    "https://health.snu.ac.kr/en/",
    "https://cals.snu.ac.kr/en",
    "https://chem.snu.ac.kr/en/admission/faq",
    "https://ece.snu.ac.kr/en/academics/graduate/curriculum",
    "https://ece.snu.ac.kr/en/academics/resources/scholarship",
    "https://ece.snu.ac.kr/en/community/notice?md=v&bbsidx=58088",
    "https://gses.snu.ac.kr/en/information/scholarship",
    "https://gses.snu.ac.kr/en/academics/doctoral-courses",
    "https://physics.snu.ac.kr/en/academics/graduate/curriculum",
    "https://sees.snu.ac.kr/en/academics/graduate/courses",
    "https://gsds.snu.ac.kr/",
    "https://gsds.snu.ac.kr/academics/acadmic-admission/",
    "https://gsds.snu.ac.kr/integrated/admission/",
    "https://astron.snu.ac.kr/en",
    "https://www.math.snu.ac.kr/eng",
    "https://eng.snu.ac.kr/en/academics/graduate-programs/interdisciplinary-program-in-bioengineering",
    "https://eng.snu.ac.kr/en/academics/graduate-programs/materials-science-and-engineering",
    "https://eng.snu.ac.kr/en/academics/graduate-programs/mechanical-engineering",
    "https://eng.snu.ac.kr/en/academics/graduate-programs/civil-urban-and-environmental-engineering",
    "https://eng.snu.ac.kr/en/academics/graduate-programs/chemical-and-biological-engineering",
    "https://eng.snu.ac.kr/en/academics/graduate-programs/computer-science-and-engineering",
    "https://eng.snu.ac.kr/en/admissions/scholarship/scholarships",
    "https://en.snu.ac.kr/admission/graduate/application",
    "https://en.snu.ac.kr/admission/graduate/before_application",
]

with open("scratch/snu_verify.txt", "w", encoding="utf-8") as f:
    for u in urls:
        t = get_text(u)
        f.write(f"=== {u} (len={len(t) if t else 'MISSING'}) ===\n")
        if t:
            f.write(t[:3500] + "\n\n")
print("Wrote scratch/snu_verify.txt")
