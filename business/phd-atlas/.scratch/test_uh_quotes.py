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

    how_to_apply_url = "https://www.uh.edu/graduate-school/admissions/how-to-apply/"
    eng_url = "https://www.uh.edu/undergraduate-admissions/apply/international/english-language-requirements/"
    physics_faq_url = "https://www.uh.edu/nsm/physics/graduate/faq/"
    cs_adm_url = "https://www.uh.edu/nsm/computer-science/graduate/admissions/"
    math_adm_url = "https://www.uh.edu/nsm/math/graduate/admissions/"

    quotes = [
        (how_to_apply_url, "Application fees are $50 for domestic applicants, $80 for international applicants and $25 for non-degree (Certificate based programs). Limited application fee waivers are available. Please check with program regarding eligibility for application fee waivers."),
        (how_to_apply_url, "Limited application fee waivers are available. Please check with program regarding eligibility for application fee waivers."),
        (how_to_apply_url, "Test Scores (GRE, GMAT, etc.) should be sent by the testing agency. Refer to the program's website for test score requirements. Use school code 6870 when reporting test scores to University of Houston."),
        (how_to_apply_url, "Please follow these instructions to properly scan and upload your transcript. If admitted, however, you will not be able to enroll without the official transcript(s) showing undergraduate degree conferral on file."),
        (eng_url, "6.5"),
        (eng_url, "Earn a high school diploma, Associate of Arts, Associate of Science, bachelor's degree"),
        (physics_faq_url, "In order to guarantee consideration please apply by January 15. However late applications"),
        (physics_faq_url, "We typically accept 20-25 new graduate students and grant 15-20 teaching assistantships"),
        (physics_faq_url, "Students are required to identify their research advisors by the middle of the spring"),
        (cs_adm_url, "January 15 (PhD and MS program) International applicants"),
        (cs_adm_url, "PhD applicants - GRE is optional"),
        (math_adm_url, "materials be submitted before January 15. The regular deadline is April 1, but by"),
        (math_adm_url, "The Graduate Record Examination (GRE) is waived for all graduate applications within the Department of Mathematics.")
    ]

    for u, q in quotes:
        nq = norm(q)
        page_t = texts.get(u, "")
        ok = nq in page_t
        print(f"[{ok}] quote: {q[:50]}... in {u}")

if __name__ == "__main__":
    check()
