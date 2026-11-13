import sys, json
sys.path.insert(0, '.')
from scripts.research import cache_paths

d = json.load(open(cache_paths('https://catalog.uaf.edu/academic-programs/'), 'r', encoding='utf-8'))
text = d['text']
for l in text.splitlines():
    if any(k in l for k in ['Ph.D.', 'Doctor of Philosophy']):
        print(l.strip())
