import sys, json, glob, re

sys.stdout.reconfigure(encoding='utf-8')
for f in glob.glob('.cache/pages/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    if d.get('url') == 'https://careers.univie.ac.at/en/praedoc/stem-call':
        html = d.get('html', '')
        for m in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL):
            t = re.sub(r'<[^>]+>', '', m.group(2)).strip()
            u = m.group(1)
            if 'open positions' in t.lower() or any(k in u.lower() for k in ['chemistry', 'physics', 'computer', 'ecology', 'microbiology']):
                print(f"{t} -> {u}")
        break
