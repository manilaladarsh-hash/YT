import urllib.request, re, ssl

ctx = ssl.create_default_context()
req = urllib.request.Request('https://careers.univie.ac.at/en/praedoc/stem-call', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')

for m in re.finditer(r'href=["\']([^"\']+)["\']', html):
    l = m.group(1)
    if 'stem-call' in l or 'praedoc' in l or 'vds' in l:
        print(l)
