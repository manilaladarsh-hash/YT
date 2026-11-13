import glob
import json

urls_to_check = {
    "apply": "https://www.sheffield.ac.uk/postgraduate/phd/apply",
    "eng": "https://www.sheffield.ac.uk/postgraduate/english-language",
    "ets": "https://www.ets.org/gre/score-users/about/subject-tests.html"
}

cached = {}
for p in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(p, encoding="utf-8"))
        u = d.get("url", "")
        for k, target in urls_to_check.items():
            if target in u or u in target:
                cached[k] = d.get("text", "")
    except Exception:
        pass

print("Found targets:", list(cached.keys()))

if "apply" in cached:
    t = cached["apply"]
    q_entry = "Information about academic entry requirements is available from the school in which your research is based. Entry requirements vary depending on what you study – some subjects require a masters degree, others ask for a good undergraduate degree (a 2:1 or a First)."
    print("Entry in text:", q_entry in t)
    if q_entry not in t:
        idx = t.find("Information about academic entry requirements")
        print("Near entry:", repr(t[idx:idx+250]))

    q_sup = "If you want to research your own idea, you should contact the relevant academic school before you submit a formal application, to check that they have an appropriately-qualified supervisor in the area you'd like to study."
    print("Sup in text:", q_sup in t)

    q_dl = "Although we advise students to start in September/October, it's often possible to start postgraduate research at any point in the year. You can state your preferred start date in your application, although this will need to be confirmed by the academic school."
    print("DL in text:", q_dl in t)

    q_fund = "You can search for supervisors, projects and Centres for Doctoral Training on our Find A PhD page."
    print("Fund in text:", q_fund in t)

if "eng" in cached:
    t = cached["eng"]
    q_waiver = "If you have recently been awarded a first degree or postgraduate diploma taught in English in person in a majority native English speaking country, you will not normally need to provide other evidence of English language ability."
    print("Waiver in text:", q_waiver in t)
