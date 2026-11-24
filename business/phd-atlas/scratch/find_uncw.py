import sys, requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

for u in [
    "https://www.uncw.edu/admissions/graduate/index.html",
    "https://www.uncw.edu/admissions/graduate/dates.html",
    "https://catalogue.uncw.edu/index.php?catoid=82",
]:
    r = requests.get(u, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    print("===", u, r.status_code)
    soup = BeautifulSoup(r.text, "lxml")
    for a in soup.find_all("a", href=True):
        t = " ".join(a.get_text().split())
        h = urljoin(r.url, a["href"])
        low = (t + " " + h).lower()
        if any(k in low for k in ["ph.d", "phd", "admissions/graduate", "catoid=82", "coastal", "marine-bio", "pharma", "psych", "fee", "waiver", "english", "toefl", "ielts", "intl", "international"]):
            if not any(b in low for b in ["certificate", "add-on", "licensure", "m.s.", "m.a.", "m.ed.", "m.b.a.", "m.p.a.", "m.s.w.", "m.a.t.", "m.f.a."]):
                print(f"  [{t[:65]}] -> {h}")
