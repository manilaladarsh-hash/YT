import json, os, hashlib

cache_dir = ".cache/pages"
urls = [
    "https://www.ets.org/gre/test-takers/subject-tests/scores.html",
    "https://www.ets.org/gre/score-users/about/subject-tests.html",
    "https://www.ms.u-tokyo.ac.jp/kyoumu_e/liaison/guide_e.html",
    "https://www.ms.u-tokyo.ac.jp/kyoumu/liaison/ab618a1da5ae3af387a2609065bc68980102cda1.pdf",
]

for u in urls:
    h = hashlib.sha256(u.encode()).hexdigest()[:24]
    # let's check index or scan cache
print("Checking cache files...")
matches = {}
for fn in os.listdir(cache_dir):
    if fn.endswith(".json"):
        with open(os.path.join(cache_dir, fn), encoding="utf-8") as f:
            d = json.load(f)
        if d.get("url") in urls or "ms.u-tokyo.ac.jp" in d.get("url", "") or "ets.org/gre" in d.get("url", ""):
            matches[d["url"]] = (fn, d.get("status"), len(d.get("text", "")), d.get("text", ""))

for u, (fn, st, ln, txt) in sorted(matches.items()):
    print(f"=== {u} [{fn}, status={st}, len={ln}] ===")
    if "ab618" in u:
        print(txt[:3000])
    elif "guide_e" in u:
        print(txt[:2500])
    else:
        for kw in ["discontinued", "Mathematics, Physics and Psychology", "Chemistry Test"]:
            idx = txt.lower().find(kw.lower())
            if idx != -1:
                print(f"  [{kw}]: {txt[max(0,idx-60):idx+220]!r}")
