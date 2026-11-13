import glob
import json

urls_to_check = {
    "env": "https://environment.leeds.ac.uk/see-research-degrees/doc/entry-requirements",
    "apply": "https://www.leeds.ac.uk/research-applying/doc/applying-research-degrees",
    "ets": "https://www.ets.org/gre/score-users/about/subject-tests.html"
}

cached = {}
for p in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(p, encoding="utf-8"))
        u = d.get("url", "")
        for k, target in urls_to_check.items():
            if target == u:
                cached[k] = d.get("text", "")
    except Exception:
        pass

print("Found targets:", list(cached.keys()))

if "env" in cached:
    t = cached["env"]
    idx_entry = t.find("A degree equivalent to a UK first class or upper second class")
    if idx_entry != -1:
        print("Entry quote exact:", repr(t[idx_entry:idx_entry+200]))
    else:
        # Search for first class
        idx_fc = t.find("first class honours degree")
        print("Near first class:", repr(t[idx_fc-50:idx_fc+150]))

    q_ielts = "IELTS: 6.0 overall with at least 5.5 in all components."
    print("IELTS quote in text:", q_ielts in t)

    q_waiver = "a postgraduate degree from a majority English speaking country. The duration of the degree must be at least 12 months and awarded less than 2 years and 4 months from the proposed start date of the PhD"
    print("Waiver quote in text:", q_waiver in t)

if "apply" in cached:
    t = cached["apply"]
    q_dl = "We advise you to apply at least four months before your proposed start date. This is to allow sufficient time to review your application and undertake any additional checks."
    print("DL quote in text:", q_dl in t)
    q_sup = "You need to identify the supervisors available to work with you. They must be experts in the topic you are interested in to ensure that your research is accurate and adding to current knowledge."
    print("Sup quote in text:", q_sup in t)
    q_fund = "UK research councils: competition for these scholarships is high but the majority of your fees will be funded so it is well worth applying."
    print("Fund quote in text:", q_fund in t)
