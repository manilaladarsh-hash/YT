import json

rec = json.loads(open(".cache/pages/ae5c09fd1988b39e.json", encoding="utf-8").read())
print("URL:", rec["url"])
for line in rec.get("text", "").splitlines():
    print(" ", line.encode("ascii", errors="replace").decode("ascii"))
