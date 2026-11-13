import json, pathlib

cache_dir = pathlib.Path(".cache/pages")
targets = {
    "https://www.bristol.ac.uk/study/media/postgraduate/admissions-statements/2026/phd-civil-engineering.pdf",
    "https://www.bristol.ac.uk/study/media/postgraduate/admissions-statements/2026/phd-electrical-and-electronic-engineering.pdf",
    "https://www.bristol.ac.uk/study/media/postgraduate/admissions-statements/2026/phd-mechanical-engineering.pdf",
}
needle = "We will not be able to proceed with your application until we have received a completed copy of this document."
for p in cache_dir.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if u in targets:
        t = d.get("text", "")
        idx = t.find(needle)
        print(f"=== {u} ===")
        print(t[max(0, idx - 600): idx + 300])
        print()
