import json

d = json.load(open(".cache/pages/1a0de6245ba748f8.json", encoding="utf-8"))
lines = d["text"].split("\n")
for i, l in enumerate(lines):
    if "Financing Your Doctorate" in l:
        for j in range(i, min(len(lines), i+30)):
            print(f"{j}: {lines[j].encode('ascii', 'replace').decode('ascii')}")
        break
