import glob, json, re
for p in glob.glob(".cache/pages/*.json"):
    d = json.load(open(p, encoding="utf-8", errors="ignore"))
    if d.get("url") == "https://www.sheffield.ac.uk/postgraduate/phd":
        html = d.get("html", "")
        links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
        for l in sorted(set(links)):
            if "postgraduate" in l:
                print(l)
