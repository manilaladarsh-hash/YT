import urllib.request, re

url = "https://www.southampton.ac.uk/study/postgraduate-research"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode("utf-8", errors="ignore")

links = set(re.findall(r'href="([^"]+)"', html))
print(f"Total hrefs: {len(links)}")
for l in sorted(links):
    print(" ", l)

