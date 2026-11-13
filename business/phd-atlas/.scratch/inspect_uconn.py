import hashlib, json, pathlib, re

def load(u):
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    return json.loads(pathlib.Path(f'.cache/pages/{h}.json').read_text(encoding='utf-8'))

eng = load('https://engineering.uconn.edu/')
print('=== KEYS:', list(eng.keys()))
# Wait: does cache store html or just text/links? Let's check!
print('=== engineering.uconn.edu links field:', eng.get('links'))
raw = eng.get('html', '') or eng.get('text', '')
for l in sorted(set(re.findall(r'https://[a-z0-9\-\.]*uconn\.edu[^\s"\'<>]*', raw))):
    print(' ', l)

for u in [
    'https://chemical-biomolecular.engineering.uconn.edu/graduate/how-to-apply/',
    'https://chemical-biomolecular.engineering.uconn.edu/graduate/program-details/',
    'https://electrical-computer.engineering.uconn.edu/graduate/graduate-degree-programs/',
]:
    d = load(u)
    txt = d.get('text', '')
    idx = txt.find('Skip to content')
    if idx == -1:
        idx = txt.find('Be Aware:')
    print('====================================')
    print('URL:', u, 'len:', len(txt))
    print(txt[max(idx, 0):max(idx, 0) + 6000])
