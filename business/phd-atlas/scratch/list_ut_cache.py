import json, pathlib

cache = pathlib.Path(".cache/pages")
urls = []
for f in sorted(cache.glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if "u-tokyo.ac.jp" in u:
        urls.append((u, d.get("status"), len(d.get("text", "")), d.get("method")))
        if "ci/admission_e.shtml" in u:
            print("=== ci/admission_e.shtml BODY ===")
            print(d["text"][3500:])
        if "2027_ag_d_e.pdf" in u:
            t = d["text"]
            for k in ["GRE", "IELTS", "supervisor", "advis", "waiv", "exempt"]:
                if k.lower() in t.lower():
                    i = t.lower().find(k.lower())
                    print(f"[2027_ag_d_e {k}]:", repr(t[max(0,i-40):i+120]))
        if "II%E3%80%90" in u:
            t = d["text"]
            for k in ["GRE", "TOEFL", "IELTS", "supervisor", "advis", "waiv", "exempt"]:
                if k.lower() in t.lower():
                    i = t.lower().find(k.lower())
                    print(f"[EngGen {k}]:", repr(t[max(0,i-40):i+120]))

print("\n=== CACHED UTOKYO URLS ===")
for u, s, l, m in sorted(urls):
    print(f"  {s} {m:8s} len={l:6d} {u}")
