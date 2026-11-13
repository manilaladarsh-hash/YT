import urllib.request, re

urls_to_try = [
    "https://www.southampton.ac.uk/courses?level=postgraduate-research",
    "https://www.southampton.ac.uk/study/postgraduate-research/courses",
    "https://www.southampton.ac.uk/study/postgraduate-research",
    "https://www.southampton.ac.uk/courses/research",
]

for u in urls_to_try:
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            print(f"{u}: status=200, len={len(html)}")
            links = re.findall(r'href="(/courses/[^"]+)"', html)
            print(f"  found {len(set(links))} course links:")
            for l in sorted(set(links))[:15]:
                print("   ", l)
    except Exception as e:
        print(f"{u}: {e}")
