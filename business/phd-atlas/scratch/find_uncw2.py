import sys, requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

js = requests.get("https://www.uncw.edu/_global/js/programs/slate-embeds.js", timeout=20).text
print("=== slate-embeds.js ===")
print(js)

for u in [
    "https://www.uncw.edu/academics/majors-programs/cms/applied-coastal-ocean-sciences-phd/details/index.html",
    "https://www.uncw.edu/academics/colleges/cse/departments/biology/index.html",
    "https://www.uncw.edu/seahawk-life/support-success/international/students-scholars/stem-designated-programs.html",
]:
    r = requests.get(u, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    print("===", u, r.status_code)
    soup = BeautifulSoup(r.text, "lxml")
    for a in soup.find_all("a", href=True):
        t = " ".join(a.get_text().split())
        h = urljoin(r.url, a["href"])
        if "/departments/biology/" in h or "/applied-coastal-" in h or "assist" in (t+h).lower() or "phd" in (t+h).lower() or "stem" in (t+h).lower():
            print(f"  [{t[:60]}] -> {h}")
