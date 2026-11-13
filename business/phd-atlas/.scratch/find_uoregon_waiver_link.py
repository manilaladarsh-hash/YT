import json
from pathlib import Path
from bs4 import BeautifulSoup

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'international-applicants' in u:
        html = rec.get('html', '')
        soup = BeautifulSoup(html, 'lxml')
        for a in soup.find_all('a'):
            if 'fee waiver' in a.get_text().lower() or 'discounts' in a.get_text().lower():
                print(a.get_text().strip(), "-->", a.get('href'))
            if 'admission requirements' in a.get_text().lower() or 'general requirements' in a.get_text().lower():
                print(a.get_text().strip(), "-->", a.get('href'))
            if 'programs' in a.get_text().lower():
                print(a.get_text().strip(), "-->", a.get('href'))
