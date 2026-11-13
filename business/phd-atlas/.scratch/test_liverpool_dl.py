import json, hashlib, re

u = "https://www.liverpool.ac.uk/courses/computer-science-phd"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d["text"]

print("CS text len:", len(t))

kw = r"deadline|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|\d{1,2}/\d|rolling|any time|year-round|throughout|open|round|apply by|position|vacanc|call"

for line in t.splitlines():
    if re.search(kw, line, re.I):
        if any(w in line.lower() for w in ["apply", "application", "deadline", "date", "start", "intake"]):
            print("MATCH:", line)
