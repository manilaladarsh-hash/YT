import json, pathlib

cache_dir = pathlib.Path(".cache/pages")
targets = {
    "https://bulletin.uakron.edu/graduate/colleges-programs/engineering/polymer-science-engineering/polymer-science-phd/",
    "https://www.uah.edu/admissions/graduate/apply-for-admission/test-score-requirements",
}
for p in cache_dir.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if u in targets:
        print(f"=== {u} ===")
        print(d.get("text", ""))
        print()
