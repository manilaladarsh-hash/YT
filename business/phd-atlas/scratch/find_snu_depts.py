import bs4
import pathlib
import requests

CANDIDATES = [
    "https://www.math.snu.ac.kr",
    "https://stat.snu.ac.kr",
    "https://stat.snu.ac.kr/en",
    "https://physics.snu.ac.kr/en",
    "https://astron.snu.ac.kr/en/",
    "https://chem.snu.ac.kr/en",
    "https://biosci.snu.ac.kr/en",
    "https://sees.snu.ac.kr/en",
    "https://gses.snu.ac.kr/en/academics/doctoral-courses",
    "https://bcs.snu.ac.kr/",
    "https://science.snu.ac.kr/en",
    "https://eng.snu.ac.kr/en",
    "https://medicine.snu.ac.kr/en",
    "https://biomed.snu.ac.kr/",
    "https://bioeng.snu.ac.kr/en/",
    "https://mse.snu.ac.kr/",
    "https://me.snu.ac.kr/en/",
    "https://cuee.snu.ac.kr/en/",
    "https://cuee.snu.ac.kr/",
    "https://cbe.snu.ac.kr/",
    "https://ece.snu.ac.kr/en",
    "https://cse.snu.ac.kr/en",
    "https://gsds.snu.ac.kr/",
    "https://oga.snu.ac.kr/scholarship-finder",
]

out = []
for u in CANDIDATES:
    try:
        r = requests.get(u, timeout=10, allow_redirects=True)
        s = bs4.BeautifulSoup(r.text, "lxml")
        title = s.title.get_text(strip=True) if s.title else ""
        links = []
        for a in s.select("a"):
            href = (a.get("href") or "").strip()
            txt = " ".join(a.get_text().split())
            if any(k in (href + " " + txt).lower() for k in ["admiss", "grad", "phd", "doctor", "faq", "scholar", "fellow", "curriculum", "program", "english", "advisor", "edge"]):
                links.append(f"  {txt} -> {href}")
        out.append(f"[{r.status_code}] {u} -> {r.url} | {title}")
        for lk in dict.fromkeys(links):
            out.append(lk)
    except Exception as e:
        out.append(f"[ERR] {u} | {e}")

pathlib.Path("scratch/snu_depts_probe.txt").write_text("\n".join(out), encoding="utf-8")
print("Done:", len(out), "lines")
