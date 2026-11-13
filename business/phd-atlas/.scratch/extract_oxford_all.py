import sys, os
sys.path.insert(0, os.getcwd())
from scripts.validate_data import cached_texts, norm
import re

texts = cached_texts()

targets = [
    ("materials", "https://www.ox.ac.uk/admissions/graduate/courses/dphil-materials"),
    ("math", "https://www.ox.ac.uk/admissions/graduate/courses/dphil-mathematics"),
    ("statistics", "https://www.ox.ac.uk/admissions/graduate/courses/dphil-statistics"),
    ("physics", "https://www.ox.ac.uk/admissions/graduate/courses/dphil-theoretical-physics"),
    ("astronomy", "https://www.ox.ac.uk/admissions/graduate/courses/dphil-astrophysics"),
    ("chemistry", "https://www.ox.ac.uk/admissions/graduate/courses/dphil-chemistry"),
    ("biology", "https://www.ox.ac.uk/admissions/graduate/courses/dphil-biology"),
    ("earth", "https://www.ox.ac.uk/admissions/graduate/courses/dphil-earth-sciences"),
    ("neuro", "https://www.ox.ac.uk/admissions/graduate/courses/dphil-neuroscience"),
    ("biomed", "https://www.ox.ac.uk/admissions/graduate/courses/dphil-medical-sciences"),
]

for fid, url in targets:
    page = texts[url]
    print(f"==================== {fid} ====================")
    
    # 1. Degree
    idx_deg = page.find("degree-level qualifications")
    if idx_deg != -1:
        snippet = page[idx_deg:idx_deg+500]
        # find sentence with first-class or honours or bachelor or master
        m = re.search(r"as a minimum.*?(\.|\n)", snippet)
        print("DEGREE:", repr(snippet[:300]))
    else:
        print("DEGREE: NOT FOUND")

    # 2. Supervisor
    idx_sup = page.find("do i need to contact anyone before i apply")
    if idx_sup != -1:
        print("SUP 1:", repr(page[idx_sup:idx_sup+250]))
    else:
        idx_sup2 = page.find("allocation of graduate supervision")
        if idx_sup2 != -1:
            print("SUP 2:", repr(page[idx_sup2:idx_sup2+250]))
        else:
            print("SUP: NOT FOUND")

    # 3. Funding
    idx_fund = page.find("oxford scholarships")
    if idx_fund != -1:
        print("FUNDING:", repr(page[idx_fund-60:idx_fund+100]))
    else:
        print("FUNDING: NOT FOUND")
