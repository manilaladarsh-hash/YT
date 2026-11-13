import hashlib, json, pathlib, re

def get(u):
    p = pathlib.Path(f".cache/pages/{hashlib.sha1(u.encode()).hexdigest()[:16]}.json")
    return json.loads(p.read_text(encoding="utf-8")).get("text", "") if p.exists() else None

for fn in ["heidelberg.json", "imperial.json", "ipparis.json"]:
    d = json.loads(pathlib.Path(f"data/universities/{fn}").read_text(encoding="utf-8"))
    print("========================================")
    print(fn, "notes:", d.get("notes", ""))
    for k, v in d["fields"].items():
        print(f"  [{k}] code={v['code']!r} quote={v['quote']!r} url={v['url']!r}")
    for k in set(v["url"] for v in d["fields"].values()):
        t = get(k)
        if t:
            print(f"  -- check {k} (len={len(t)}) --")
            print("     GRE matches:", re.findall(r".{0,40}\bgre\b.{0,40}", t, re.I))
            print("     fee matches:", re.findall(r".{0,40}\bfee\b.{0,60}", t, re.I)[:5])
