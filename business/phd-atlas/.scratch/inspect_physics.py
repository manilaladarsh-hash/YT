import json

rec = json.loads(open(".cache/pages/c8808f0ccbd5418e.json", encoding="utf-8").read())
text = rec.get("text", "")
for line in text.splitlines():
    if line.strip():
        print(line.strip().encode("ascii", errors="replace").decode("ascii"))
