import json, hashlib

u_apply = "https://www.cardiff.ac.uk/study/postgraduate/applying/how-to-apply"
h = hashlib.sha1(u_apply.encode()).hexdigest()[:16]
t_apply = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))["text"]

print(repr(t_apply[1375:1800]))
