import json, pathlib

cache = pathlib.Path(".cache/pages")
for f in sorted(cache.glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if "u-tokyo.ac.jp" not in u:
        continue
    if any(x in u for x in ["ci/admission_e.shtml", "soe/international-programs", "s.u-tokyo.ac.jp/en/admission/graduate.html", "2027admin-guide-en.pdf"]):
        print("===", u, "len=", len(d.get("text","")), "links=", len(d.get("links",[])))
        if "2027admin-guide-en.pdf" in u:
            t = d["text"]
            for m in ["supervisor", "Supervisor", "advis", "Advis", "contact", "Contact", "prior", "Prior", "letter", "Doctor"]:
                idx = t.find(m, 15000)
                if idx != -1:
                    print(f"  [CI match {m}]:", repr(t[max(0,idx-80):idx+180]))
        elif "soe/international-programs" in u:
            for l in d.get("links", []):
                if ".pdf" in str(l).lower() or "civil" in str(l).lower() or "special" in str(l).lower():
                    print("  LINK:", l)
        else:
            print(d.get("text", "")[500:3500])
