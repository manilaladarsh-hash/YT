import json, sys, hashlib, re
from pathlib import Path
url = sys.argv[1]; pat = sys.argv[2]; before=int(sys.argv[3]) if len(sys.argv)>3 else 200; after=int(sys.argv[4]) if len(sys.argv)>4 else 500
key = hashlib.sha1(url.encode()).hexdigest()[:16]
t = json.loads(Path(f"/home/user/YT/business/phd-atlas/.cache/pages/{key}.json").read_text())["text"]
last=-10**9
for m in re.finditer(pat, t, re.I):
    if m.start() - last < after: continue
    last=m.start()
    print("▸", t[max(0,m.start()-before):m.end()+after].replace("\n"," ¶ "), "\n")
