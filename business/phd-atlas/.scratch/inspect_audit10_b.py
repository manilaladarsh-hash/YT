import json, hashlib, pathlib

targets = [
    ("byu.json", "toefl_min"),
    ("byu.json", "english_waiver"),
    ("canterbury-nz.json", "toefl_min"),
    ("clemson.json", "english_waiver"),
    ("clevelandstate.json", "gre_general"),
    ("cmu.json", "fee_waiver"),
    ("cmu.json", "gre_general"),
    ("colostate.json", "toefl_min"),
]

seen = {}
for fn, field in targets:
    if fn not in seen:
        seen[fn] = json.loads((pathlib.Path("data/universities") / fn).read_text(encoding="utf-8"))
    v = seen[fn]["fields"][field]
    print("========================================")
    print(f"{fn} | {field} | code={v['code']!r}")
    print(f"  value={v['value']!r}")
    print(f"  quote={v['quote']!r}")
    print(f"  url={v['url']!r}")
    if "also" in v:
        print(f"  also={v['also']!r}")
    h = hashlib.sha1(v["url"].encode()).hexdigest()[:16]
    cp = pathlib.Path(f".cache/pages/{h}.json")
    if cp.exists():
        txt = json.loads(cp.read_text(encoding="utf-8")).get("text", "")
        print(f"  [cache len={len(txt)}]")
        q0 = v["quote"].split("|")[0].strip()[:35]
        idx = txt.lower().find(q0.lower()) if q0 else -1
        if idx != -1:
            print("  [context]:", repr(txt[max(0, idx-350):idx+550]))
        else:
            print("  [snippet]:", repr(txt[:700]))
    else:
        print("  [cache missing by sha1]")
