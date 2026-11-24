import pathlib
import bs4
import requests

for url, name in [
    ("https://en.snu.ac.kr/academics/programs/graduate", "snu_prog_links.txt"),
    ("https://en.snu.ac.kr/admission/graduate/application", "snu_app_links.txt"),
    ("https://admission.snu.ac.kr/international/graduate/spring/guide", "snu_guide_links.txt"),
]:
    r = requests.get(url, timeout=30)
    s = bs4.BeautifulSoup(r.text, "lxml")
    lines = []
    for a in s.select("a"):
        href = a.get("href", "").strip()
        txt = " ".join(a.get_text().split())
        if href and not href.startswith("#"):
            lines.append(f"{txt} | {href}")
    pathlib.Path("scratch", name).write_text("\n".join(lines), encoding="utf-8")
    print(f"{name}: {len(lines)} links")
