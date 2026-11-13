import glob, json

for p in glob.glob('.cache/pages/*.json'):
    try:
        d = json.load(open(p, 'r', encoding='utf-8'))
        u = d.get('url', '')
        if 'gradschool.wayne.edu/admissions' in u:
            print("="*60)
            print("File:", p, "URL:", u)
            for item in d.get('links', []):
                if isinstance(item, list) and len(item) == 2:
                    t, h = item
                else:
                    t, h = "", str(item)
                if any(w in h.lower() or w in t.lower() for w in ['program', 'degree', 'deadline', 'phd', 'doctor', 'catalog', 'bulletin']):
                    print("  ", t, "->", h)
    except: pass
