import glob
import json

urls_to_check = {
    "bmh": "https://www.bmh.manchester.ac.uk/study/research/getting-started/eligibility-and-entry-requirements/",
    "se": "https://www.se.manchester.ac.uk/study/postgraduate-research/getting-started/applying/",
    "lang": "https://www.manchester.ac.uk/study/international/admissions/language-requirements/",
    "ets": "https://www.ets.org/gre/score-users/about/subject-tests.html"
}

cached_texts = {}
for p in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(p, encoding="utf-8"))
        u = d.get("url", "")
        for k, target in urls_to_check.items():
            if target == u:
                cached_texts[k] = d.get("text", "")
    except Exception:
        pass

print("Found targets:", list(cached_texts.keys()))

if "bmh" in cached_texts:
    t = cached_texts["bmh"]
    idx = t.find("To be considered for entry")
    if idx != -1:
        entry_quote = t[idx:t.find("International applicants must", idx)].strip()
        print("BMH entry quote exact:\n", repr(entry_quote))

    idx_eng = t.find("a minimum IELTS score of 6.5")
    if idx_eng != -1:
        print("BMH english quote exact:\n", repr(t[idx_eng:idx_eng+150]))

if "se" in cached_texts:
    t = cached_texts["se"]
    q_sup = "Contacted the project supervisor and spoken to them about your suitability for the project."
    print("SE sup quote in text:", q_sup in t)
    q_fund = "If you are nominated for funding by your supervisor, you may be invited to further interviews to determine your suitability for funding."
    print("SE fund quote in text:", q_fund in t)
    q_roll = "We will try and notify you within 4-6 weeks of your application. However, due to various funding applications and deadlines, you may not receive an answer during this timeframe."
    print("SE roll quote in text:", q_roll in t)

if "lang" in cached_texts:
    t = cached_texts["lang"]
    q_lang = "For Student Route visa purposes, the UKVI has a prescribed list of Majority English-speaking countries (this list is not defined by The University of Manchester)."
    print("Lang quote in text:", q_lang in t)
