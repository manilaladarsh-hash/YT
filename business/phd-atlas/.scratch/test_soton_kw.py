import json, re

KW = {
    "funding": r"fund|stipend|scholar|studentship|support|salar|employ|assistantship|fellowship|paid|tuition|contract|position|financ|award|bursar",
    "deadline": r"deadline|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|\d{1,2}/\d|rolling|any time|year-round|throughout|open|round|apply by|position|vacanc|call",
    "supervisor": r"supervis|advis|faculty|professor|rotation|committee|contact|mentor|lab|research group|principal investigator",
    "entry_route": r"degree|bachelor|master|honours|baccalaur|undergraduate|b\.s|m\.s|diploma",
}

p = json.load(open("data/programs/southampton--cs.json", encoding="utf-8"))
for fld, kw_pat in KW.items():
    q = p["fields"][fld]["quote"]
    u = p["fields"][fld]["url"]
    match = bool(re.search(kw_pat, q, re.I))
    print(f"{fld}: match={match}")
    print(f"  quote: {repr(q)}")
    print(f"  url: {u}")
