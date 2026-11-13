import json
from pathlib import Path

urls = {}
for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'unm.edu' in u:
        urls[u] = rec.get('text', '')

def check_quote(u, q):
    t = urls.get(u, '')
    if q in t:
        print(f"OK: {q[:40]}... in {u}")
        return True
    else:
        print(f"FAILED: {q} NOT in {u}")
        return False

# University level
check_quote("https://grad.unm.edu/prospective-students/apply-now.html",
            "When you have completed your application and are ready to submit it, you will be required to pay an application fee via credit card online ($60 for domestic applications, $70 for international applications).")

check_quote("https://grad.unm.edu/prospective-students/apply-now.html",
            "Application fee waivers are not available to international applicants.")

check_quote("https://grad.unm.edu/prospective-students/apply-now.html",
            "Each graduate and professional program has specific requirements for admissions, as well as its own deadlines. Before applying, be sure to review the application requirements and instructions for your program of interest, as well as the information below.")

check_quote("https://international.unm.edu/english-proficiency.html", "79 (4.5)")
check_quote("https://international.unm.edu/english-proficiency.html", "6.5")
check_quote("https://international.unm.edu/english-proficiency.html",
            "Bachelor's degree from a regionally-accredited US college or university or a recognized institution in English-Speaking Canada, the United Kingdom, South Africa, Australia, or New Zealand.")
