import hashlib, json, pathlib

def get(u):
    p = pathlib.Path(f".cache/pages/{hashlib.sha1(u.encode()).hexdigest()[:16]}.json")
    return json.loads(p.read_text(encoding="utf-8")).get("text", "") if p.exists() else None

targets = [
    ("floridatech.json", "toefl_min"),
    ("floridatech.json", "english_waiver"),
    ("freiburg.json", "gre_general"),
    ("fuberlin.json", "gre_general"),
    ("georgetown.json", "fee_waiver"),
    ("glasgow.json", "app_fee"),
    ("glasgow.json", "fee_waiver"),
]

seen = {}
for fn, k in targets:
    if fn not in seen:
        seen[fn] = json.loads((pathlib.Path("data/universities") / fn).read_text(encoding="utf-8"))
    v = seen[fn]["fields"][k]
    print("========================================")
    print(f"{fn} | {k} | code={v['code']!r}")
    print(f"  notes={seen[fn].get('notes','')!r}")
    print(f"  value={v['value']!r}")
    print(f"  quote={v['quote']!r}")
    print(f"  url={v['url']!r}")
    t = get(v["url"])
    if t:
        q0 = v["quote"].split("|")[0].strip()[:30]
        idx = t.lower().find(q0.lower()) if q0 else -1
        if idx != -1:
            print("  ctx:", repr(t[max(0, idx-300):idx+600]))
