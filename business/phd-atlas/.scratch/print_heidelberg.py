import json

for fname in ['14e48d84865f3733.json', 'b1c1ab773bd53322.json', '6167545f9f60cbe7.json', '21396b73aa0be878.json']:
    d = json.load(open(f".cache/pages/{fname}", encoding="utf-8"))
    print(f"=== {fname}: {d.get('url')} ===")
    for line in d["text"].split("\n"):
        if any(w in line.lower() for w in ["doctoral", "doctorate", "phd", "fee", "tuition", "language", "gre", "toefl", "ielts"]):
            print("  ", line[:100])
