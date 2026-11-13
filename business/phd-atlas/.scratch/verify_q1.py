import json, hashlib

u_apply = "https://www.cardiff.ac.uk/study/postgraduate/applying/how-to-apply"
h = hashlib.sha1(u_apply.encode()).hexdigest()[:16]
t_apply = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))["text"]

prefix = "Follow the steps below to find out exactly how to apply for our postgraduate degree programmes and what to expect after you have applied."
suffix = "Check the entry requirements - if you have not yet met the entry requirements, you can usually still apply for a course. You may receive an offer of a place on the condition that you meet the requirements before you start the course."

idx1 = t_apply.find(prefix)
idx2 = t_apply.find(suffix)
print("idx1:", idx1, "idx2:", idx2)
if idx1 != -1 and idx2 != -1:
    print(repr(t_apply[idx1:idx2 + len(suffix)]))
