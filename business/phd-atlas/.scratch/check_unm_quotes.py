import json
from pathlib import Path

urls = {}
for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'unm.edu' in u:
        urls[u] = rec.get('text', '')

def search_text(url, keywords):
    text = urls.get(url, '')
    print(f"=== {url} ===")
    for line in text.split('\n'):
        if any(k.lower() in line.lower() for k in keywords):
            print("  ", line.strip())

search_text("https://grad.unm.edu/prospective-students/apply-now.html", ["fee", "waiver", "gre"])
search_text("https://international.unm.edu/english-proficiency.html", ["79", "6.5", "waive", "exemption", "bachelor"])
search_text("https://geo.unm.edu/admission/graduate/requirements/academic.html", ["bachelor", "degree", "equivalent"])
