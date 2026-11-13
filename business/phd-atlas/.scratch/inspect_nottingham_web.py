import urllib.request, re

import string

for ch in string.ascii_lowercase:
    url = f"https://www.nottingham.ac.uk/pgstudy/courses/courses.aspx?level=research&letter={ch}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            links = re.findall(r'href="(/pgstudy/course/research/[^"]+)"', html)
            for l in sorted(set(links)):
                if any(k in l for k in ["med", "bio", "neuro", "pharma"]):
                    print(ch, l)
    except Exception as e:
        print(ch, "Error:", e)

