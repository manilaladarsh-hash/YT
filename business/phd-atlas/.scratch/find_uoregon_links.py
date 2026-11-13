import json
from pathlib import Path
from bs4 import BeautifulSoup

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'how-to-apply' in u:
        html = rec.get('html', '')
        soup = BeautifulSoup(html, 'lxml')
        for a in soup.find_all('a', href=True):
            href = a['href']
            text = a.get_text().strip()
            if any(k in href.lower() or k in text.lower() for k in ['fee', 'waiver', 'english', 'international', 'requirement', 'program', 'admission']):
                print(f"{text} -> {href}")
