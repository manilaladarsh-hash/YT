import glob
import json

urls_to_check = {
    "propose": "https://www.birmingham.ac.uk/study/postgraduate/research/how-to-apply/propose-research",
    "ad": "https://www.birmingham.ac.uk/study/postgraduate/research/how-to-apply/advertised-phd",
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

if "propose" in cached:
    t = cached["propose"]
    q_entry = "Once you have found your subject area you will need to check the entry requirements to see if you are eligible to undertake research with us. Typically you will need to have a good Honours degree and usually a Masters degree."
    print("Entry quote in text:", q_entry in t)
    
    q_sup = "Once you've identified a subject area, you will need to find a supervisor for your project. All Doctoral Researchers are provided with a lead supervisor, who will act as the main source of academic supervisory support and research mentoring during your time as a Doctoral Researcher at the University."
    print("Sup quote in text:", q_sup in t)
    
    q_fund = "To pay for your research, there’s a range of funding available from scholarships, charities, loans and self-finance."
    if q_fund not in t:
        # Check unicode apostrophe
        q_fund_alt = "To pay for your research, there's a range of funding available from scholarships, charities, loans and self-finance."
        print("Fund quote in text (straight):", q_fund_alt in t)
        idx = t.find("To pay for your research")
        if idx != -1:
            print("Exact fund quote:", repr(t[idx:idx+120]))
    else:
        print("Fund quote in text:", True)

    idx_waiver = t.find("For those who have recently graduated")
    if idx_waiver != -1:
        print("Exact waiver quote:", repr(t[idx_waiver:idx_waiver+400]))

if "ad" in cached:
    t = cached["ad"]
    q_dl = "Make sure you read all the detailed information about the research project including duration, funding level/type, entry requirements and application deadlines."
    print("DL quote in text:", q_dl in t)
