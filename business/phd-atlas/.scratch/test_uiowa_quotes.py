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
    ("https://grad.admissions.uiowa.edu/instructions/graduate-college",
     "Submit the online application to the Graduate College and pay the $60 application fee by credit card ($100 for international applicants)."),
    ("https://grad.admissions.uiowa.edu/cost-and-funding",
     "Applicants for whom payment of the application fee presents a significant financial hardship may request an application fee waiver."),
    ("https://grad.admissions.uiowa.edu/instructions/graduate-college",
     "Application deadlines and required supplemental materials vary by academic program so it’s important that you review the program-specific instructions including supplemental materials required by your academic program."),
    ("https://grad.admissions.uiowa.edu/english-proficiency-requirements",
     "Total score 81"),
    ("https://grad.admissions.uiowa.edu/english-proficiency-requirements",
     "Overall score of 7 with no subscore less than 6"),
    ("https://grad.admissions.uiowa.edu/english-proficiency-requirements",
     "Applicants will be given a waiver if they are a citizen, or have earned the equivalent of a bachelor’s degree, master's degree, or Ph.D. in the United States, or any of the following countries:"),

    # Programs
    # Physics
    ("https://grad.admissions.uiowa.edu/academics/physics-ms-or-phd",
     "Jan. 15"),
    ("https://grad.admissions.uiowa.edu/academics/physics-ms-or-phd",
     "Attention Fall 2026 Applicants: We anticipate admissions this year to be extremely competitive and will likely have fewer than five support packages available."),

    # CS
    ("https://grad.admissions.uiowa.edu/academics/computer-science-phd",
     "Jan. 1"),

    # Chemistry
    ("https://grad.admissions.uiowa.edu/academics/chemistry-ms-or-phd",
     "January 1"),

    # Math
    ("https://grad.admissions.uiowa.edu/academics/mathematics-ms-or-phd",
     "Jan. 15"),
    ("https://grad.admissions.uiowa.edu/academics/mathematics-ms-or-phd",
     "*Offers of admission and teaching assistantships are usually sent out February through May."),

    # Statistics
    ("https://grad.admissions.uiowa.edu/academics/statistics-ms-or-phd",
     "Decisions for graduate financial support are typically made by April 15 for the upcoming academic year, so applications from students requesting financial support should reach us by Jan. 15."),
    ("https://grad.admissions.uiowa.edu/academics/statistics-ms-or-phd",
     "All applicants are considered for financial support, for graduate assistantships, such as research assistants, teaching assistants and graders. However, it is important to note, that the applications must be fully complete by the deadline dates to be considered for this financial support."),

    # Biology
    ("https://grad.admissions.uiowa.edu/academics/integrated-biology-phd",
     "PhD Deadline: January 1"),

    # Biomed
    ("https://grad.admissions.uiowa.edu/academics/biomedical-science-phd",
     "Dec. 1"),
    ("https://grad.admissions.uiowa.edu/academics/biomedical-science-phd",
     "Students admitted to the PhD program receive a nationally competitive stipend and a health insurance allowance in addition to full payment of their tuition and mandatory fees."),
    ("https://grad.admissions.uiowa.edu/academics/biomedical-science-phd",
     "GRE scores are not required for this program."),

    # BME
    ("https://grad.admissions.uiowa.edu/academics/biomedical-engineering-ms-or-phd",
     "Jan. 1"),
    ("https://grad.admissions.uiowa.edu/academics/biomedical-engineering-ms-or-phd",
     "The department strongly encourages prospective students to identify and contact a research advisor prior to applying."),

    # ChemEng
    ("https://grad.admissions.uiowa.edu/academics/chemical-and-biochemical-engineering-ms-or-phd",
     "Jan. 15"),

    # Civil
    ("https://grad.admissions.uiowa.edu/academics/civil-environmental-engineering-ms-or-phd",
     "Fall semester?Jan. 15 is the priority date to be considered for financial aid. After this date, applications will be considered until July 15 for U.S. students and April 15 for international students."),

    # ECE
    ("https://grad.admissions.uiowa.edu/academics/electrical-computer-engineering-ms-or-phd",
     "Fall: Priority consideration will be given to all complete applications received by Dec. 15th. We will accept applications on a rolling basis from U.S. citizens until July 15."),

    # Mech
    ("https://grad.admissions.uiowa.edu/academics/mechanical-engineering-ms-or-phd",
     "Jan. 15 (Admission Decision: March 1)")
]

all_ok = True
for u, q in quotes:
    clean_q = norm(q)
    page_t = texts.get(u, "")
    ok = clean_q in page_t
    if not ok:
        all_ok = False
        print(f"FAILED: [{q[:40]}...] in {u}")
    else:
        print(f"OK: [{q[:35]}...]")

print("ALL UIOWA QUOTES MATCH:", all_ok)
