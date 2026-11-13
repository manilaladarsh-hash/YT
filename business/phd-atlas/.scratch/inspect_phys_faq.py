import json

rec = json.loads(open(".cache/pages/61d39d8d8a5e9bd0.json", encoding="utf-8").read())
print("URL:", rec.get("url"))
for line in rec.get("text", "").splitlines():
    if line.strip():
        print(line.strip().encode("ascii", errors="replace").decode("ascii"))
