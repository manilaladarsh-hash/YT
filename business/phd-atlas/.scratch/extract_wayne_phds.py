import glob, json

for p in glob.glob('.cache/pages/*.json'):
    try:
        d = json.load(open(p, 'r', encoding='utf-8'))
        if d.get('url') == 'https://bulletins.wayne.edu/programs/':
            links = d.get('links', [])
            print(f"Total links: {len(links)}")
            for t, h in links:
                if '(Ph.D.)' in t or 'Ph.D.' in t or 'Doctor' in t:
                    print(f"  {t} -> {h}")
    except: pass
