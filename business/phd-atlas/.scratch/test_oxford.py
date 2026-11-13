import urllib.request
import re

url = "https://www.ox.ac.uk/admissions/graduate/applying-to-oxford/application-guide"
req = urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
)
try:
    with urllib.request.urlopen(req) as resp:
        print("Status:", resp.status)
        html = resp.read().decode("utf-8", errors="ignore")
        print("Length:", len(html))
        links = re.findall(r'href="([^"]*fee[^"]*)"', html, re.I)
        print("Fee links:", set(links))
        lang_links = re.findall(r'href="([^"]*language[^"]*)"', html, re.I)
        print("Language links:", set(lang_links))
except Exception as e:
    print("Error:", e)
