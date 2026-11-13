import hashlib, json, pathlib, re

def get(u):
    p = pathlib.Path(f".cache/pages/{hashlib.sha1(u.encode()).hexdigest()[:16]}.json")
    return json.loads(p.read_text(encoding="utf-8")).get("text", "") if p.exists() else None

targets = [
    ("portlandstate.json", "toefl_min"),
    ("princeton.json", "gre_general"),
    ("rockefeller.json", "ielts_min"),
    ("sissa.json", "toefl_min"),
    ("sissa.json", "ielts_min"),
    ("siucarbondale.json", "gre_general"),
    ("sorbonne.json", "app_fee"),
    ("sorbonne.json", "fee_waiver"),
]

seen = set()
for fn, k in targets:
    d = json.loads(pathlib.Path(f"data/universities/{fn}").read_text(encoding="utf-8"))
    v = d["fields"][k]
    print("========================================")
    print(f"{fn} [{k}] code={v['code']!r} url={v['url']}")
    print(f"  value: {v['value']!r}")
    print(f"  quote: {v['quote']!r}")
    print(f"  also:  {v.get('also')}")
    t = get(v["url"])
    if t:
        q0 = v["quote"].split("|")[0].strip()[:30]
        idx = t.lower().find(q0.lower())
        if idx != -1:
            print("  ctx:", repr(t[max(0, idx-350):idx+450]))
        else:
            print("  QUOTE NOT FOUND; len=", len(t))
        if (fn, v["url"]) not in seen:
            seen.add((fn, v["url"]))
            for kw_name, pat in [("GRE", r".{0,40}\bgre\b.{0,40}"), ("IELTS/TOEFL/ENG", r".{0,35}\b(?:ielts|toefl|english)\b.{0,35}"), ("FEE", r".{0,35}\bfee\b.{0,35}")]:
                m = re.findall(pat, t, re.I)
                if m:
                    print(f"  {kw_name} matches ({len(m)}):", m[:8])
    else:
        print("  NO CACHE")
