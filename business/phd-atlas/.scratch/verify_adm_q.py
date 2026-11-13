import json, hashlib

u = "https://www.cardiff.ac.uk/study/postgraduate/applying/admissions-criteria"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
t = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))["text"]

q = "Our online course finder and postgraduate prospectus will give you a broad overview of the entry requirements for particular degree programmes. However, we welcome applications from those offering alternative qualifications. We will also consider applications from those with combinations of qualifications and those with other relevant life/work experience."
print("q in t:", q in t)
