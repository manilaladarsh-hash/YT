import urllib.request, re, ssl

ctx = ssl.create_default_context()
req = urllib.request.Request('https://set.kuleuven.be/phd', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')

links = sorted(set(re.findall(r'href=["\']([^"\']+)["\']', html)))
for l in links:
    if 'set.kuleuven.be' in l or l.startswith('/'):
        print(l)
