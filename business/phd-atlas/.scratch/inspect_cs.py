import json

rec = json.loads(open(".cache/pages/9cbd916133303f61.json", encoding="utf-8").read())
text = rec.get("text", "")
for line in text.splitlines():
    if line.strip():
        print(line.strip().encode("ascii", errors="replace").decode("ascii"))
