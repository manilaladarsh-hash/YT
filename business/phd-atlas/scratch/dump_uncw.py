import hashlib, json, sys
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
CACHE = Path(".cache/pages")

urls = [
    "https://www.uncw.edu/admissions/graduate/index.html",
    "https://www.uncw.edu/admissions/graduate/apply/index.html",
    "https://www.uncw.edu/admissions/graduate/getting-started.html",
    "https://www.uncw.edu/admissions/graduate/dates.html",
    "https://www.uncw.edu/admissions/graduate/int-graduate.html",
    "https://catalogue.uncw.edu/content.php?catoid=82&navoid=12358",
    "https://catalogue.uncw.edu/content.php?catoid=82&navoid=12361",
    "https://www.uncw.edu/academics/majors-programs/cms/applied-coastal-ocean-sciences-phd/index.html",
    "https://www.uncw.edu/academics/majors-programs/cse/integrative-comparative-marine-biology-phd/index.html",
    "https://www.uncw.edu/academics/majors-programs/cse/pharmaceutical-chemistry-phd/index.html",
    "https://www.uncw.edu/academics/majors-programs/cse/psychology-phd/index.html",
]

out = []
for u in urls:
    p = CACHE / (hashlib.sha1(u.encode()).hexdigest()[:16] + ".json")
    if p.exists():
        d = json.loads(p.read_text(encoding="utf-8"))
        out.append(f"=== {u} (final={d.get('final_url')}, status={d.get('status')}) ===\n{d.get('text','')}\n")
Path("scratch/uncw_dump.txt").write_text("\n".join(out), encoding="utf-8")
print("wrote scratch/uncw_dump.txt")

# Also extract catalogue PhD links and check assistantship links from admissions/graduate
r = requests.get("https://catalogue.uncw.edu/content.php?catoid=82&navoid=12361", timeout=20, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(r.text, "lxml")
for a in soup.find_all("a", href=True):
    t = " ".join(a.get_text().split())
    h = urljoin(r.url, a["href"])
    if any(k in t.lower() for k in ["ph.d", "coastal", "marine biology", "pharmaceutical", "psychology"]):
        print(f"CAT: [{t}] -> {h}")

r2 = requests.get("https://www.uncw.edu/academics/graduate-school/index.html", timeout=20, headers={"User-Agent": "Mozilla/5.0"})
soup2 = BeautifulSoup(r2.text, "lxml")
for a in soup2.find_all("a", href=True):
    t = " ".join(a.get_text().split())
    h = urljoin(r2.url, a["href"])
    if any(k in (t+" "+h).lower() for k in ["fund", "assist", "fellow", "financ", "tuition", "stipend"]):
        print(f"GS: [{t}] -> {h}")
