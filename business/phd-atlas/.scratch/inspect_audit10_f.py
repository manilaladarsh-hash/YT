import hashlib, json, pathlib, re

def get(u):
    p = pathlib.Path(f".cache/pages/{hashlib.sha1(u.encode()).hexdigest()[:16]}.json")
    return json.loads(p.read_text(encoding="utf-8")).get("text", "") if p.exists() else None

for fn in ["ku.json", "leiden.json", "lmu.json", "louisville.json"]:
    d = json.loads(pathlib.Path(f"data/universities/{fn}").read_text(encoding="utf-8"))
    print("========================================")
    print(fn, "notes:", d.get("notes", ""))
    for k, v in d["fields"].items():
        if (fn, k) in [
            ("ku.json", "toefl_min"),
            ("leiden.json", "app_fee"), ("leiden.json", "fee_waiver"), ("leiden.json", "gre_general"),
            ("lmu.json", "gre_general"),
            ("louisville.json", "toefl_min"),
        ]:
            print(f"  [{k}] code={v['code']!r} quote={v['quote']!r}")
            t = get(v["url"])
            if t:
                q0 = v["quote"].split("|")[0].strip()[:30]
                idx = t.lower().find(q0.lower())
                if idx != -1:
                    print("    ctx:", repr(t[max(0, idx-250):idx+450]))
                print("    GRE matches:", re.findall(r".{0,30}\bgre\b.{0,30}", t, re.I))
                print("    fee matches:", re.findall(r".{0,30}\bfee\b.{0,30}", t, re.I)[:5])
