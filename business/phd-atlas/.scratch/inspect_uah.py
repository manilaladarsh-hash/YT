import glob, json

for p in glob.glob('.cache/pages/*.json'):
    try:
        d = json.load(open(p, 'r', encoding='utf-8'))
        u = d.get('url', '')
        if 'uah.edu/admissions/graduate' in u and d.get('status') == 200:
            print("File:", p, "URL:", u)
            for l in d.get('text', '').splitlines()[:25]:
                print("  ", l[:100])
            print("Links:")
            for t, h in d.get('links', []):
                print(f"  {t} -> {h}")
    except: pass
