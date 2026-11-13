import urllib.request, re, ssl

ctx = ssl.create_default_context()
req = urllib.request.Request('https://set.kuleuven.be/phd/regulations.htm', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')

for m in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL):
    text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
    href = m.group(1)
    if any(k in text.lower() for k in ['regulation', 'consult', 'degree', 'interdisciplinary', 'particulars']):
        print(f'{text} -> {href}')
