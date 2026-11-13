import json
from pathlib import Path

urls = {}
for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    for u in {rec['url'], rec.get('final_url', rec['url'])}:
        urls[u] = rec.get('text', '')

def check(u, q):
    t = urls.get(u, '')
    if q not in t:
        print(f"FAILED: {q!r} NOT in {u}")
        return False
    else:
        print(f"OK: {q[:35]}... in {u.split('/')[-1]}")
        return True

# University level
how_to_apply = "https://graduatestudies.uoregon.edu/apply/how-to-apply"
waivers_url = "https://graduatestudies.uoregon.edu/apply/application-fee-waivers-discounts"
intl_url = "https://graduatestudies.uoregon.edu/apply/international-applicants"

check(how_to_apply, "Domestic applicants: $70")
check(how_to_apply, "International applicants: $90")
check(how_to_apply, "Submit GMAT or GRE scores (if required by your program)")
check(waivers_url, "We offer a limited number of full fee waivers for international applicants with significant financial need. Applicants must be nominated by their prospective program.")
check(intl_url, "88 or 4.5")
check(intl_url, "7.0 Overall Band Score")
check(intl_url, "The University of Oregon does not accept English-medium-of-instruction certificates in place of approved English proficiency documentation.")

# Programs
bio_url = "https://naturalsciences.uoregon.edu/biology/apply/graduate-admissions"
bio_prog_url = "https://naturalsciences.uoregon.edu/biology/graduate-programs"
check(bio_url, "The deadline to apply is December 2, 2026.")
check(bio_url, "IMPORTANT: GRE scores are no longer considered in our application review process. You will not see a place for them on the application and you do not need to send in a score report.")
check(bio_url, "internet-based test =105, or 5.0 under the new 1–6 scale")
check(bio_url, "IELTS: 7.5")
check(bio_prog_url, "Funding is provided for doctoral students through a combination of Department of Biology and associated research institute resources.")

chem_url = "https://naturalsciences.uoregon.edu/chemistry-biochemistry/apply/graduate-admissions"
chem_apply_url = "https://naturalsciences.uoregon.edu/chemistry-biochemistry/apply"
check(chem_url, "The priority deadline for applications is December 2, 2026.")
check(chem_url, "The GRE general test (verbal, quantitative, analytical/writing) is optional for all applicants.")
check(chem_url, "The GRE subject test is not required.")
check(chem_url, "Minimum Score: 90 or 4.5 (scores after January 21, 2026) with a speaking score of 26.")
check(chem_apply_url, "Students accepted into the doctoral program receive financial support in the form of teaching and research assistantships unless other arrangements are made.")

cs_url = "https://scds.uoregon.edu/graduate-programs/admissions"
check(cs_url, "December 15, 2026")
check(cs_url, "Only required for the Computer Science PhD program.")
check(cs_url, "iBt (internet based TOEFL) = 100 (or 5.0 with the new scoring system)")
check(cs_url, "IELTS (International English Language Testing System) = 7")

earth_url = "https://naturalsciences.uoregon.edu/earth-sciences/apply/graduate-admissions"
check(earth_url, "The online application will close at the end of the day on December 22.")
check(earth_url, "No. We are no longer considering the GRE in our applications.")
check(earth_url, "Our students typically receive graduate employee positions that provide tuition waivers, health insurance, and a stipend.")
check(earth_url, "Prospective students are encouraged to browse the webpages of individual faculty members and inquire about research opportunities by contacting faculty via email.")

math_url = "https://naturalsciences.uoregon.edu/mathematics/apply/graduate-admissions"
check(math_url, "all of your materials must be received by the application deadline of January 15, 2027.")
check(math_url, "Math subject GRE scores are recommended but not required—the University of Oregon’s Institution Code is 4846.")
check(math_url, "all of whom are supported by Graduate Employee positions that carry a stipend, full tuition waiver, and health insurance.")
check(math_url, "TOEFL internet-based test: score of 100 or better (on the 0-120 scale) or 5 or better (on the new 1-6 scale), with at least 26 (on the 0-30 scale) or 5 (on the new 1-6 scale) on the speaking section.")
check(math_url, "IELTS exam: overall band score of 7.0 or better, with at least 7.0 on the speaking band.")
check(math_url, "To be considered for admission, you must have a bachelor’s degree or expect to attain one by the end of summer 2027.")

phys_url = "https://naturalsciences.uoregon.edu/physics/apply/graduate-admissions"
check(phys_url, "We are currently accepting applications for Fall 2027 PhD admission with an application deadline of January 12, 2027.")
check(phys_url, "GRE Scores (Optional)")
check(phys_url, "Ideally, applicants should take the GRE test(s) in time for the official results to arrive before the January 15 deadline.")
check(phys_url, "Students who apply to our PhD program by the deadline are automatically considered for a number of fellowships and/or awards that support graduate student success.")
check(phys_url, "List any research areas of interest to you as well as faculty members you would be interested in working with. This section is not required for MS applicants.")
