import json, glob
from bs4 import BeautifulSoup

for p in glob.glob('.cache/pages/*.json'):
    try:
        data = json.load(open(p, 'r', encoding='utf-8'))
    except Exception:
        continue
    url = data.get('url', '')
    if 'graduate-admission-deadlines-and-requirements' in url:
        print("Found:", p, "method:", data.get('method'), "len html:", len(data.get('html', '')))
        soup = BeautifulSoup(data.get('html', ''), 'lxml')
        # Check tables or rows
        tables = soup.find_all('table')
        print("Found tables:", len(tables))
        for table in tables:
            rows = table.find_all('tr')
            print(f"Table with {len(rows)} rows:")
            for r in rows[:15]:
                cells = [c.get_text(strip=True) for c in r.find_all(['th', 'td'])]
                print("  ", cells)
        # If no tables, check accordion or divs
        if not tables:
            for item in soup.find_all(['div', 'article', 'section']):
                t = item.get_text(" ", strip=True)
                if 'Ph.D.' in t or 'Doctorate' in t or 'Doctor of Philosophy' in t:
                    pass
