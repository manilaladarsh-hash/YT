import json, sys, hashlib, re
from pathlib import Path
url = sys.argv[1]
pat = sys.argv[2] if len(sys.argv) > 2 else None
key = hashlib.sha1(url.encode()).hexdigest()[:16]
rec = json.loads(Path(f"/home/user/YT/business/phd-atlas/.cache/pages/{key}.json").read_text())
text = rec["text"]
print("status", rec["status"], "method", rec["method"], "chars", len(text))
if pat is None:
    print(text[:6000])
else:
    for m in re.finditer(pat, text, re.I):
        s = max(0, m.start()-300); e = min(len(text), m.end()+400)
        print("...", text[s:e].replace("\n", " | "), "...\n")
