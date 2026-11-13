import glob
import json
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

cache = {}
for f in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(f, encoding="utf-8"))
        cache[d.get("url")] = d.get("text", "")
    except Exception:
        pass

def normalize(text):
    return re.sub(r"\s+", " ", text).strip().lower()

normalized_cache = {url: normalize(text) for url, text in cache.items()}

def verify_quote(url, quote, name=""):
    norm_quote = normalize(quote)
    if url in normalized_cache:
        if norm_quote in normalized_cache[url]:
            print(f"[OK] {name}: found in {url}")
            return True
        else:
            print(f"[FAIL] {name}: quote NOT found in {url}")
            print(f"       Quote: {quote[:80]}...")
            return False
    else:
        print(f"[FAIL] {name}: URL not in cache: {url}")
        return False

tests = [
    # CS
    ("https://catalog.utdallas.edu/2026/graduate/programs/ecs/computer-science", "Fall Deadline - December 15", "cs deadline"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/ecs/computer-science", "While not required, applicants are encouraged to submit any of the following supplemental items to be considered: GRE Scores.", "cs gre_general"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/ecs/computer-science", "For priority consideration for funding, completed application files should be received by the deadlines posted below.", "cs funding"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/ecs/computer-science", "Admission Option Two A BS in related area that includes two semesters of calculus and linear algebra with A GPA of at least 3.5 in the last 60 semester credit hours", "cs entry_route"),

    # BME
    ("https://catalog.utdallas.edu/current/graduate/programs/ecs/biomedical-engineering", "Fall Deadline - December 15", "bme deadline"),
    ("https://catalog.utdallas.edu/current/graduate/programs/ecs/biomedical-engineering", "Students are encouraged to directly contact faculty about research opportunities and their willingness to serve as their supervising professor.", "bme supervisor"),
    ("https://catalog.utdallas.edu/current/graduate/programs/ecs/biomedical-engineering", "75 semester credit hours minimum beyond the baccalaureate degree", "bme entry_route"),

    # ECE
    ("https://catalog.utdallas.edu/current/graduate/programs/ecs/electrical-engineering", "Fall Deadline - December 15", "ece deadline"),
    ("https://catalog.utdallas.edu/current/graduate/programs/ecs/electrical-engineering", "GRE scores are temporarily being waived", "ece gre_general"),
    ("https://catalog.utdallas.edu/current/graduate/programs/ecs/electrical-engineering", "75 semester credit hours minimum beyond the baccalaureate degree", "ece entry_route"),

    # MATERIALS
    ("https://catalog.utdallas.edu/2026/graduate/programs/ecs/materials-science", "Fall Deadline - December 15", "materials deadline"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/ecs/materials-science", "GRE revised scores which are recommended as 154 or above, 154 or above, and 4 for the verbal, quantitative, and analytical writing components, respectively, are advisable based on our experience with student success in the program.", "materials gre_general"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/ecs/materials-science", "75 semester credit hours minimum beyond the baccalaureate degree", "materials entry_route"),

    # MECH
    ("https://catalog.utdallas.edu/current/graduate/programs/ecs/mechanical-engineering", "Fall Deadline - December 15", "mech deadline"),
    ("https://catalog.utdallas.edu/current/graduate/programs/ecs/mechanical-engineering", "78 semester credit hours minimum beyond the baccalaureate degree", "mech entry_route"),

    # PHYSICS
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/physics", "Fall Deadline - May 1", "physics deadline"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/physics", "GRE scores are temporarily being waived.", "physics gre_general"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/physics", "75 semester credit hours minimum beyond the baccalaureate degree", "physics entry_route"),

    # CHEMISTRY
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/chemistry-and-biochemistry", "Fall Deadline - December 15", "chemistry deadline"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/chemistry-and-biochemistry", "Foreign students with TOEFL scores less than 600 (paper test), 250 (computer test), or 100 (internet test) are admitted only in special circumstances.", "chemistry toefl_min"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/chemistry-and-biochemistry", "75 semester credit hours minimum beyond the baccalaureate degree", "chemistry entry_route"),

    # MATH
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/mathematics", "Fall Deadline - December 15", "math deadline"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/mathematics", "First-round Scholarship Deadline: For first-round consideration for assistantships and scholarships, complete application files must be received by the following deadlines: Fall Deadline - December 15", "math funding"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/mathematics", "75 semester credit hours minimum beyond the baccalaureate degree", "math entry_route"),

    # STATISTICS
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/mathematics", "All complete application files received by the December 15 deadline will be reviewed for first-round scholarships and assistantships consideration.", "statistics funding"),

    # EARTH
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/sustainable-earth-systems-sciences", "Fall Deadline - December 15", "earth deadline"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/sustainable-earth-systems-sciences", "GRE scores are temporarily being waived.", "earth gre_general"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/sustainable-earth-systems-sciences", "First-round Scholarship Deadline: For first-round consideration for assistantships and scholarships, complete application files must be received by the following deadlines: Fall Deadline - December 15", "earth funding"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/sustainable-earth-systems-sciences", "75 semester credit hours minimum beyond the baccalaureate degree", "earth entry_route"),

    # BIOLOGY
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/biological-sciences", "Fall Deadline - December 15", "biology deadline"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/nsm/biological-sciences", "75 semester credit hours minimum beyond the baccalaureate degree", "biology entry_route"),

    # NEURO
    ("https://catalog.utdallas.edu/2026/graduate/programs/bbs/doctoral-programs", "Fall Deadline - December 1", "neuro deadline"),
    ("https://catalog.utdallas.edu/2026/graduate/programs/bbs/doctoral-programs", "75 semester credit hours minimum beyond the baccalaureate degree", "neuro entry_route"),
]

for url, quote, name in tests:
    verify_quote(url, quote, name)
