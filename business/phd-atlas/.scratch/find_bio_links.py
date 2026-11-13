import urllib.request, re, ssl

ctx = ssl.create_default_context()
req = urllib.request.Request('https://cosam.auburn.edu/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')

for m in re.finditer(r'href=["\']([^"\']+)["\']', html):
    l = m.group(1)
    if 'bio' in l.lower() or 'dept' in l.lower() or 'department' in l.lower():
        print(l)
