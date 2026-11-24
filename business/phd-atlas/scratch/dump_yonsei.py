import json, os

cache_dir = ".cache/pages"
targets = [
    "s_f_guide_2027-1_e.pdf",
    "s_f_guide_2026-2_e.pdf",
    "forein_fall_schedule.do",
    "forein_schedule.do",
    "departlist.do",
    "scholarship.do",
    "scholarship02.do",
    "scholarship03.do",
    "language.do",
    "foreigner.do",
    "bk21_program01.do",
]

out = []
for fn in sorted(os.listdir(cache_dir)):
    if not fn.endswith(".json"):
        continue
    p = os.path.join(cache_dir, fn)
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    u = d.get("url", "")
    if any(t in u for t in targets):
        out.append(f"=== {u} (len={len(d.get('text',''))}) ===")
        out.append(d.get("text", ""))

with open("scratch/yonsei_dump.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Wrote scratch/yonsei_dump.txt, total chars:", sum(len(x) for x in out))
