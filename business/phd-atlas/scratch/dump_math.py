import json, os

cache_dir = ".cache/pages"
out = []
for fn in os.listdir(cache_dir):
    if not fn.endswith(".json"): continue
    with open(os.path.join(cache_dir, fn), encoding="utf-8") as f:
        d = json.load(f)
    u = d.get("url", "")
    if "ab618" in u or "guide_e.html" in u or "foreign_students_overseas" in u or "content_10.html" in u:
        out.append(f"=== {u} ===")
        out.append(d.get("text", ""))
with open("scratch/math_dump.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Wrote scratch/math_dump.txt")
