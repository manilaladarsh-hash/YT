import json, os

cache_dir = ".cache/pages"
by_url = {}
for fn in os.listdir(cache_dir):
    if fn.endswith(".json"):
        with open(os.path.join(cache_dir, fn), encoding="utf-8") as f:
            d = json.load(f)
        by_url[d["url"]] = d.get("text", "")

out = []
for u in [
    "https://www.civil.t.u-tokyo.ac.jp/en/admission/",
    "https://www.s.u-tokyo.ac.jp/en/admission/scholarship.html",
    "https://www.u-tokyo.ac.jp/en/prospective-students/graduate_course_list.html",
    "https://www.k.u-tokyo.ac.jp/en/exam/info/",
]:
    t = by_url.get(u, "")
    out.append(f"\n=== {u} (len={len(t)}) ===")
    if "s.u-tokyo" in u:
        idx = t.find("Various Scholarships")
        if idx == -1: idx = t.find("GSGC")
        out.append(t[max(0, idx-200):idx+5000])
    else:
        out.append(t[:7000])

with open("scratch/civil_sci_bodies.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Wrote scratch/civil_sci_bodies.txt")
