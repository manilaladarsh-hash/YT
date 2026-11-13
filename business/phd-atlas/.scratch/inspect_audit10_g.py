import hashlib, json, pathlib, re

def get(u):
    p = pathlib.Path(f".cache/pages/{hashlib.sha1(u.encode()).hexdigest()[:16]}.json")
    return json.loads(p.read_text(encoding="utf-8")).get("text", "") if p.exists() else None

targets = [
    ("loyolachicago.json", "ielts_min"),
    ("lsu.json", "gre_general"),
    ("marquette.json", "fee_waiver"),
    ("memphis.json", "toefl_min"),
    ("mines.json", "toefl_min"),
    ("minnesota.json", "fee_waiver"),
    ("mps-photonics.json", "gre_general"),
    ("ou.json", "toefl_min"),
    ("portlandstate.json", "fee_waiver"),
]

for fn, k in targets:
    d = json.loads(pathlib.Path(f"data/universities/{fn}").read_text(encoding="utf-8"))
    v = d["fields"][k]
    print("========================================")
    print(f"{fn} [{k}] code={v['code']!r} url={v['url']}")
    print(f"  quote: {v['quote']!r}")
    print(f"  also:  {v.get('also')}")
    t = get(v["url"])
    if t:
        q0 = v["quote"].split("|")[0].strip()[:35]
        idx = t.lower().find(q0.lower())
        if idx == -1:
            q0 = v["quote"].split("|")[0].strip()[:20]
            idx = t.lower().find(q0.lower())
        if idx != -1:
            print("  ctx:", repr(t[max(0, idx-350):idx+450]))
        else:
            print("  QUOTE HEAD NOT FOUND; head=", repr(t[:400]))
        if k == "gre_general":
            print("  GRE matches:", re.findall(r".{0,40}\bgre\b.{0,40}", t, re.I))
    else:
        print("  NO CACHE")
