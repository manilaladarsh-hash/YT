import json

rec = json.loads(open(".cache/pages/701d7928a2bed60f.json", encoding="utf-8").read())
print(rec.get("text", "")[:2000].encode("ascii", errors="replace").decode("ascii"))
print("Links:", len(rec.get("links", [])))
for l in rec.get("links", [])[:30]:
    print(" ", l)
