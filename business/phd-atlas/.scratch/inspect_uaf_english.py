import sys, json
sys.path.insert(0, '.')
from scripts.research import cache_paths

d = json.load(open(cache_paths('https://catalog.uaf.edu/getting-started/admission/'), 'r', encoding='utf-8'))
text = d['text']
idx = text.find('English Proficiency Requirements')
if idx == -1:
    idx = text.find('English proficiency')
print(text[idx:idx+2500])
