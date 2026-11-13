import sys, json
sys.path.insert(0, '.')
from scripts.research import cache_paths

d = json.load(open(cache_paths('https://catalog.uaf.edu/academic-programs/'), 'r', encoding='utf-8'))
for t, h in d.get('links', []):
    if 'ph.d' in t.lower():
        print(f"{t} -> {h}")
