import json
import re
from pathlib import Path

def norm(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()

cache = Path(".cache/pages")
texts = {}
for p in cache.glob("*.json"):
    rec = json.loads(p.read_text(encoding="utf-8"))
    t = norm(rec.get("text", "").replace("\n", " "))
    for u in {rec["url"], rec.get("final_url", rec["url"])}:
        texts[u] = texts[u] + " \x00 " + t if u in texts else t

quotes = [
    # University fields
    ("https://www.uh.edu/graduate-school/admissions/how-to-apply/",
     "Application fees are $50 for domestic applicants, $80 for international applicants and $25 for non-degree (Certificate based programs). Limited application fee waivers are available. Please check with program regarding eligibility for application fee waivers."),
    ("https://www.uh.edu/graduate-school/admissions/how-to-apply/",
     "Limited application fee waivers are available. Please check with program regarding eligibility for application fee waivers."),
    ("https://www.uh.edu/graduate-school/admissions/how-to-apply/",
     "Test Scores (GRE, GMAT, etc.) should be sent by the testing agency. Refer to the program's website for test score requirements. Use school code 6870 when reporting test scores to University of Houston."),
    ("https://www.uh.edu/nsm/computer-science/graduate/admissions/",
     "Minimum score required by UH for internet-based = 79 (120 scale) overall or 4 (6-point scale) overall internet-based test"),
    ("https://www.uh.edu/nsm/computer-science/graduate/admissions/",
     "Minimum score required by UH = 6.5 overall"),
    ("https://www.uh.edu/nsm/computer-science/graduate/admissions/",
     "Baccalaureate degree (or higher) earned from a regionally accredited U.S. institution or at an institution at which English is the medium of instruction in the countries listed here."),

    # General entry_route
    ("https://www.uh.edu/graduate-school/admissions/how-to-apply/",
     "Please follow these instructions to properly scan and upload your transcript. If admitted, however, you will not be able to enroll without the official transcript(s) showing undergraduate degree conferral on file."),

    # Physics
    ("https://www.uh.edu/nsm/physics/graduate/faq/",
     "In order to guarantee consideration please apply by January 15. However late applications"),
    ("https://www.uh.edu/nsm/physics/graduate/faq/",
     "We typically accept 20-25 new graduate students and grant 15-20 teaching assistantships"),
    ("https://www.uh.edu/nsm/physics/graduate/faq/",
     "Students are required to identify their research advisors by the middle of the spring"),

    # CS
    ("https://www.uh.edu/nsm/computer-science/graduate/admissions/",
     "January 15 (PhD and MS program) International applicants"),
    ("https://www.uh.edu/nsm/computer-science/graduate/admissions/",
     "It is helpful, but not required to contact faculty of interest before or at the time of application."),
    ("https://www.uh.edu/nsm/computer-science/graduate/admissions/",
     "BS degree in Computer Science or related field (e.g. Engineering, Mathematics, Statistics)"),

    # Math & Stats
    ("https://www.uh.edu/nsm/math/graduate/admissions/",
     "materials be submitted before January 15. The regular deadline is April 1, but by"),
    ("https://www.uh.edu/nsm/math/graduate/admissions/",
     "The Graduate Record Examination (GRE) is waived for all graduate applications within the Department of Mathematics."),
    ("https://www.uh.edu/nsm/math/graduate/admissions/",
     "To be admitted to any of the graduate programs in mathematics, a student must have an undergraduate degree and demonstrate competence in mathematics."),

    # Chemistry
    ("https://www.uh.edu/nsm/chemistry/graduate/",
     "The application deadline for International (all visa types) is January 31."),
    ("https://www.uh.edu/nsm/chemistry/graduate/faq/",
     "All Ph.D. students admitted into the Graduate Program in the Department of Chemistry \u00b6 are automatically given a Teaching Assistantship for the first year. The monthly stipend \u00b6 for this assistantship is approximately $2,325. After the first year, students who"),
    ("https://www.uh.edu/nsm/chemistry/graduate/faq/",
     "If you are admitted, you have until the beginning of your second semester (end of \u00b6 January) to choose a research advisor."),
    ("https://www.uh.edu/nsm/chemistry/graduate/admissions/",
     "Request Educational Testing Service (ETS) to send GRE Chemistry or Physics Test scores to the University of Houston Main Campus (ETS code 6870). These tests are \u00b6 optional but encouraged for consideration of fellowship awards."),

    # Biology & Biomed
    ("https://www.uh.edu/nsm/biology-biochemistry/graduate/prospective-students/phd-programs/",
     "Deadline: December 1"),
    ("https://www.uh.edu/nsm/biology-biochemistry/graduate/prospective-students/phd-programs/",
     "You will receive a monthly stipend of $2,386/month (U. S. $28,632 per year) through \u00b6 either a Teaching Assistantship (TA) or Research Assistantship (RA). \u00b6 In addition, tuition and mandatory fees will be covered by the Graduate Tuition Fellowship \u00b6 (GTF)."),
    ("https://www.uh.edu/nsm/biology-biochemistry/graduate/prospective-students/phd-programs/",
     "The Graduate Record Examination (GRE) is waived for all graduate applications within the Department of Biology & Biochemistry."),

    # BME
    ("https://www.bme.uh.edu/graduate/admissions",
     "Feb 15(*priority)"),
    ("https://www.bme.uh.edu/graduate/admissions",
     "(MS) 3.00/4.00 on last 60 hours (Ph.D.) 3.30/4.00 on last 60 hours or Graduate hours if hold MS degree"),

    # ChemEng
    ("https://www.chee.uh.edu/graduate/admissions",
     "The deadline to submit your Online Application is February 15 of each year for the upcoming Fall Term. Be advised that all required documents must be uploaded by this date."),
    ("https://www.chee.uh.edu/graduate/admissions",
     "At this time, the current stipend is $34,200 per year. All qualified candidates accepted into our PhD program receive full financial assistance. No separate application is necessary.")
]

all_ok = True
for u, q in quotes:
    clean_q = norm(q.replace("\u00b6", " "))
    page_t = texts.get(u, "")
    ok = clean_q in page_t
    if not ok:
        all_ok = False
        print(f"FAILED: [{q[:40]}...] in {u}")
    else:
        print(f"OK: [{q[:35]}...]")

print("ALL QUOTES MATCH:", all_ok)
