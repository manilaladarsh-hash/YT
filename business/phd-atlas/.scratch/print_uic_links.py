import json

for fname in ["11adea942239f975.json", "0f3b6a3247d5d16e.json"]:
    rec = json.loads(open(f".cache/pages/{fname}", encoding="utf-8").read())
    print(f"=== {rec['url']} ===")
    for label, link in rec.get("links", []):
        if any(w in (label + " " + link).lower() for w in ["waiver", "international", "requirement", "english", "deadline", "test", "fee"]):
            print(f"  [{label}] -> {link}")
