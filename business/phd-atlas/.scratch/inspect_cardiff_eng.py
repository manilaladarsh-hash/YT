import json, hashlib

def p(u):
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    t = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))["text"]
    print(f"=== {u} ===")
    print(t[:2000])

p("https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/engineering")
