import json

rec = json.loads(open(".cache/pages/027e3a77d0bee2c7.json", encoding="utf-8").read())
print("URL:", rec["url"])
for line in rec.get("text", "").splitlines():
    print(" ", line.encode("ascii", errors="replace").decode("ascii"))
for l in rec.get("links", []):
    if any(k in str(l).lower() for k in ["deadline", "program"]):
        print("LINK:", l)
