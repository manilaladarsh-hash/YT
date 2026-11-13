import json

for fname in ["3bc3b70c1002099f.json", "6d430b325eb30c63.json", "e3b6e5cc34c9ca31.json"]:
    try:
        rec = json.loads(open(f".cache/pages/{fname}", encoding="utf-8").read())
        if "uic.edu" in rec.get("url", ""):
            print("FOUND:", fname, rec["url"])
            lines = rec.get("text", "").splitlines()
            for i, line in enumerate(lines):
                if any(w in line for w in ["English Proficiency Test Score Minimums", "TOEFL iBT", "IELTS Academic", "REQUIREMENT EXEMPTIONS"]):
                    for j in range(max(0, i-1), min(len(lines), i+15)):
                        print("  ", lines[j].encode("ascii", errors="replace").decode("ascii"))
                    print("---")
    except Exception as e:
        pass
