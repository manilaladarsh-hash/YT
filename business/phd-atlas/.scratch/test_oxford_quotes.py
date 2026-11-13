import glob, json, re

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("£", "£")
    return re.sub(r"\s+", " ", s).strip().lower()

texts = {}
for p in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(p, encoding="utf-8"))
        t = norm(d.get("text", "").replace("\n", " "))
        for u in {d["url"], d.get("final_url", d["url"])}:
            texts[u] = texts[u] + " \x00 " + t if u in texts else t
    except:
        pass

quotes_to_check = [
    ("https://www.ox.ac.uk/admissions/graduate/application-guide/declaration-and-payment/application-fee",
     "The application fee for applications to research courses is...Research courses comprise Centres for Doctoral Training (CDT), DPhil"),
    ("https://www.ox.ac.uk/admissions/graduate/application-guide/declaration-and-payment/application-fee-waivers",
     "If you indicate on the application form that you are resident in one of the eligible countries in this section of the guidance, you will be asked additional questions relating to this waiver scheme."),
    ("https://www.ox.ac.uk/admissions/graduate/application-guide/supporting-documents/other-supporting-documents",
     "For a small number of courses, applicants are required or encouraged to submit GRE General Test scores. For other courses, they are not required."),
    ("https://www.ox.ac.uk/admissions/graduate/application-guide/qualifications-experience-languages-funding/english-language-proficiency",
     "To take up a place on one of our courses, you must be able to demonstrate English language proficiency at the University's standard or higher level. Each course page states the required level for that course."),
    ("https://www.ox.ac.uk/admissions/graduate/application-guide/qualifications-experience-languages-funding/english-language-test-waivers",
     "undertaken at a recognised institution where teaching and assessment throughout the course is undertaken entirely in English; and"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-computer-science",
     "12:00 midday UK time on Wednesday 2 December 2026"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-engineering-science",
     "12:00 midday UK time on Wednesday 2 December 2026"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-materials",
     "12:00 midday UK time on Friday 13 November 2026"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-mathematics",
     "12:00 midday UK time on Wednesday 6 January 2027"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-statistics",
     "12:00 midday UK time on Wednesday 6 January 2027"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-biology",
     "12:00 midday UK time on Wednesday 6 January 2027"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-earth-sciences",
     "12:00 midday UK time on Wednesday 27 January 2027"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-theoretical-physics",
     "12:00 midday UK time on Wednesday 6 January 2027"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-astrophysics",
     "12:00 midday UK time on Wednesday 6 January 2027"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-chemistry",
     "12:00 midday UK time on Friday 13 November 2026"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-neuroscience",
     "12:00 midday UK time on Tuesday 1 December 2026"),
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-medical-sciences",
     "12:00 midday UK time on Tuesday 1 December 2026"),
]

for url, q in quotes_to_check:
    found = norm(q) in texts.get(url, "")
    print(found, "-->", url.split("/")[-1])
