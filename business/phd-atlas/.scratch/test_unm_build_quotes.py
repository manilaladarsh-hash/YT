import json
from pathlib import Path

urls = {}
for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'unm.edu' in u:
        urls[u] = rec.get('text', '')

def verify(url, quote):
    t = urls.get(url, '')
    if quote not in t:
        raise ValueError(f"Quote not found in {url}:\n{quote}")
    return True

# ETS quote
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

# URLs
apply_url = "https://grad.unm.edu/prospective-students/apply-now.html"
eng_url = "https://international.unm.edu/english-proficiency.html"
geo_acad_url = "https://geo.unm.edu/admission/graduate/requirements/academic.html"

# Verify university level quotes
verify(apply_url, "When you have completed your application and are ready to submit it, you will be required to pay an application fee via credit card online ($60 for domestic applications, $70 for international applications).")
verify(apply_url, "Application fee waivers are not available to international applicants.")
verify(apply_url, "Each graduate and professional program has specific requirements for admissions, as well as its own deadlines. Before applying, be sure to review the application requirements and instructions for your program of interest, as well as the information below.")
verify(eng_url, "79 (4.5)")
verify(eng_url, "6.5")
verify(eng_url, "Bachelor's degree from a regionally-accredited US college or university or a recognized institution in English-Speaking Canada, the United Kingdom, South Africa, Australia, or New Zealand.")

print("All university level quotes verified successfully!")
