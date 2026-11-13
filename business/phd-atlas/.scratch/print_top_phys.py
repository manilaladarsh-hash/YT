import json

rec = json.loads(open(".cache/pages/404bcc40fb08826e.json", encoding="utf-8").read())
lines = rec.get("text", "").splitlines()
for i in range(20, min(140, len(lines))):
    print(f"{i}: {lines[i].encode('ascii', errors='replace').decode('ascii')}")
