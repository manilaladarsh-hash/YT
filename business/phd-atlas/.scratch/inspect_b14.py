import hashlib, json, pathlib

cache_dir = pathlib.Path(".cache/pages")

def show_url(url):
    h = hashlib.sha256(url.encode()).hexdigest()[:16]
    p = cache_dir / f"{h}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    print(f"=== {url} ({p.name}) ===")
    print(d.get("text", ""))
    print()

show_url("https://www.uts.edu.au/for-students/admissions-entry/how-to-apply/masters-by-research-phd")
show_url("https://www.uva.nl/en/research/phd/admission-to-a-doctoral-programme/admission-to-a-doctoral-programme.html")

print("=== ALL uva.nl caches ===")
for p in cache_dir.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if "uva.nl" in u:
        t = d.get("text", "")
        hits = [w for w in ("fee", "gre", "cost", "free", "charge", "euro", "tuition") if w in t.lower()]
        print(f"{p.name} | {u} | hits={hits}")
