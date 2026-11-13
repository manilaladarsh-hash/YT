import json
import re
from pathlib import Path

def norm(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def check():
    texts = {}
    cache = Path(".cache/pages")
    for p in cache.glob("*.json"):
        rec = json.loads(p.read_text(encoding="utf-8"))
        t = norm(rec.get("text", "").replace("\n", " "))
        for u in {rec["url"], rec.get("final_url", rec["url"])}:
            texts[u] = texts[u] + " \x00 " + t if u in texts else t

    help_url = "https://graduateadmissions.ucsc.edu/help-for-applicants/"
    test_url = "https://graduateadmissions.ucsc.edu/test-score-requirements/"
    deadlines_url = "https://graduateadmissions.ucsc.edu/application-deadlines/"
    fin_url = "https://graduateadmissions.ucsc.edu/financial-support/"

    quotes = [
        (help_url, "The application fee is $135.00 for domestic applicants and $155.00 for international applicants. Electronic payment options are available through our application system; a small fee (approximately $4) will also be charged for credit card processing."),
        (help_url, "If you are a US Citizen, AB 540, or Permanent Resident of the United States, you may request an application fee waiver if you believe you are eligible. Please be aware that fee waivers are extremely limited."),
        (help_url, "GRE requirements vary by program; applicants whose native language is not English may be required to take the TOEFL iBT (including the Home Edition) or IELTS Academic exam."),
        (test_url, "83 for all other programs."),
        (test_url, "For those choosing to take the IELTS Academic (in-person and online versions), a minimum overall score of 7 from the IELTS test is required for admission."),
        (help_url, "TOEFL/IELTS waivers for admission purposes may be requested by applicants who do not have English as their first language and who have completed a four-year bachelor’s degree at an English-speaking institution."),
        (help_url, "Awarding of a bachelor’s degree or its equivalent from an accredited university prior to the quarter for which admission is sought"),
        (fin_url, "Read about the 5/2 Year Graduate Student Funding Packages – offered to MFA and PhD admits.")
    ]

    for u, q in quotes:
        nq = norm(q)
        page_t = texts.get(u, "")
        ok = nq in page_t
        print(f"[{ok}] quote: {q[:50]}... in {u}")

if __name__ == "__main__":
    check()
