import json, hashlib, re

h = hashlib.sha1('https://www.southampton.ac.uk/study/postgraduate-research'.encode()).hexdigest()[:16]
d = json.load(open(f'.cache/pages/{h}.json', encoding='utf-8'))
links = set(re.findall(r'href="([^"]+)"', d.get('html', '')))
print('Total links in study/postgraduate-research:', len(links))
for l in sorted(links):
    if any(k in l for k in ['course', 'subject', 'phd', 'apply', 'research', 'programme']):
        print(' ', l)
