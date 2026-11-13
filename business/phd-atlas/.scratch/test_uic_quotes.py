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
    ("https://grad.uic.edu/admissions/domestic-admission/",
     "A non-refundable application fee of $80 (U.S. currency) is required to have your application reviewed."),
    ("https://admissions.uic.edu/graduate-professional/application-process/application-fee-waivers",
     "Unfortunately, financial hardship waivers for graduate and professional applications are not granted."),
    ("https://admissions.uic.edu/graduate-professional/requirements-deadlines/international-requirements",
     "These are determined by program. See the program's website for complete details. Program requirements may include (but are not limited to) items such as: GRE scores - use our Institutional Code 1851 to report your results"),
    ("https://admissions.uic.edu/graduate-professional/requirements-deadlines/international-requirements",
     "80"),
    ("https://admissions.uic.edu/graduate-professional/requirements-deadlines/international-requirements",
     "Enrollment at an accredited U.S. institution for at least two years of full-time, academic study."),

    # Physics
    ("https://phys.uic.edu/academics/graduate-studies/graduate/",
     "February 15th for International Applicants seeking a Teaching/Research Assistantship."),
    ("https://phys.uic.edu/academics/graduate-studies/graduate/",
     "December 1st to be considered for an application fee waiver. Applicants requesting application fee waivers must complete their applications by December 1st."),

    # CS
    ("https://cs.uic.edu/graduate/admissions/",
     "February 15: all PhD and MS applicants"),
    ("https://cs.uic.edu/graduate/admissions/",
     "PhD students in their first five years of enrollment are guaranteed a funded appointment for fall and spring that includes a full tuition waiver, a partial fee waiver, and a stipend."),
    ("https://cs.uic.edu/graduate/admissions/",
     "New! Doctoral applicants applying to the computer science PhD graduate program are not required to submit GRE scores. GRE scores will be considered, if provided, but are not required. This GRE score waiver only applies to doctoral applicants, and not to masters program applicants."),

    # MSCS (Math & Stats)
    ("https://mscs.uic.edu/graduate/admissions/",
     "PhD students are admitted as a cohort each Fall semester, and the annual application deadline for both domestic and international students is December 15."),

    # Chemistry
    ("https://chem.uic.edu/graduate-studies/",
     "For Fall 2026 admission to the Chemistry PhD program, applications are reviewed as soon as they are complete. For fullest consideration, including University Fellowship awards, all materials should be submitted by January 1, 2026."),

    # Biological Sciences
    ("https://bios.uic.edu/academics/graduate-studies/graduate-application/",
     "To receive full consideration, applications must be received by December 1st."),

    # BME
    ("https://bme.uic.edu/graduate/admissions/",
     "The application fee for the Biomedical Engineering (BME) or Bioinformatics (BIOI) Doctoral/PhD programs will be waived for all applicants if the application is submitted by December 15, 2026."),
    ("https://bme.uic.edu/graduate/admissions/",
     "The GRE requirement is waived for applicants seeking admission to the BME graduate programs at UIC."),
    ("https://bme.uic.edu/graduate/admissions/",
     "PhD students in BME will be funded with stipend, full tuition waiver, and partial fee waiver year around for the duration of their studies as long as they are making satisfactory progress towards the didactic and research requirements set forth by BME/UIC."),

    # ECE
    ("https://ece.uic.edu/admissions/",
     "PhD applications must be submitted by Dec. 15, 2026"),
    ("https://ece.uic.edu/admissions/",
     "GRE general test scores. Students do not need to submit scores but are encouraged to do so if they feel their test performance would enhance their prospects for admission or financial aid."),

    # MIE (Mech)
    ("https://mie.uic.edu/graduate/admissions/",
     "The PhD application fee will be waived for applicants who submit their applications by December 15, 2026."),
    ("https://mie.uic.edu/graduate/admissions/",
     "Four-Year PhD Funding Guarantee: PhD students who are admitted into the MIE program with financial support in the form of a teaching or research assistantship will receive a funded appointment that includes a waiver of tuition and certain fees in the fall and spring semesters of their first four years."),

    # CHE (ChemEng)
    ("https://che.uic.edu/graduate-programs/admissions/",
     "February 15, 2027: International PhD applicants seeking to begin in August 2027"),
    ("https://che.uic.edu/graduate-programs/admissions/",
     "Please note that GRE general test scores are not required."),

    # CME (Civil & Materials)
    ("https://cme.uic.edu/graduate/admissions/",
     "GRE general test scores (PhD applicants only). GRE general test scores are required only for applicants to our PhD programs. Requirements are a minimum combined verbal and quantitative score of 305.")
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

print("ALL UIC QUOTES MATCH:", all_ok)
