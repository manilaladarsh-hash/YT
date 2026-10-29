import json

for fname in ['0bcf2ceb97b7d267.json', '4d5c833f7b384bb6.json']:
    d = json.load(open(f".cache/pages/{fname}", encoding="utf-8"))
    print(f"=== {fname}: {d.get('url')} ===")
    for line in d["text"].split("\n"):
        if any(w in line.lower() for w in ["fee", "gre", "toefl", "ielts", "cost", "charge"]):
            print("  ", line[:100])
