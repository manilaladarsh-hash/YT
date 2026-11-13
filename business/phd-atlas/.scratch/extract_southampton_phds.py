import urllib.request, re

url = "https://www.southampton.ac.uk/courses?level=postgraduate-research"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode("utf-8", errors="ignore")

links = set(re.findall(r'href="(/courses/[^"]+)"', html))
suffixes = set(l.split("-")[-1] for l in links)
print("Suffixes:", sorted(suffixes))

all_links = set(re.findall(r'href="([^"]+)"', html))
pgr_links = [l for l in all_links if "research" in l or "phd" in l]
print(f"Total links with research/phd: {len(pgr_links)}")
for l in sorted(set(pgr_links))[:25]:
    print(" ", l)

