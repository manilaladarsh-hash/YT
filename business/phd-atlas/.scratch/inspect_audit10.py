import json, hashlib, pathlib

targets = [
    ("adelaide.json", "english_waiver"),
    ("albany.json", "fee_waiver"),
    ("albany.json", "english_waiver"),
    ("anu.json", "app_fee"),
    ("anu.json", "fee_waiver"),
    ("arizona.json", "ielts_min"),
    ("auckland.json", "app_fee"),
    ("baylor.json", "toefl_min"),
    ("bristol.json", "fee_waiver"),
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
    h = hashlib.sha1(v["url"].encode()).hexdigest()[:16]
    cp = pathlib.Path(f".cache/pages/{h}.json")
    if cp.exists():
        txt = json.loads(cp.read_text(encoding="utf-8")).get("text", "")
        print(f"  [cache len={len(txt)}]")
        # find snippet around first 30 chars of quote
        q0 = v["quote"].split("|")[0].strip()[:35]
        idx = txt.lower().find(q0.lower()) if q0 else -1
        if idx != -1:
            print("  [context]:", repr(txt[max(0, idx-300):idx+500]))
        else:
            print("  [first 35 chars not exact-matched; snippet]:", repr(txt[:600]))
    else:
        print("  [cache missing by sha1(url)]")
