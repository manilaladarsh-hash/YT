import urllib.request, re

req = urllib.request.Request('https://www.southampton.ac.uk/study/postgraduate-research', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

with open('.scratch/pgr.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Saved pgr.html, length:', len(html))
hrefs = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
print('Total hrefs:', len(hrefs))
for h in sorted(set(hrefs))[:30]:
    print(' ', h)
