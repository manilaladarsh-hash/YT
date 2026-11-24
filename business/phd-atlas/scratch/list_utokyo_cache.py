import json
from pathlib import Path

cache = Path('.cache/pages')
rows = []
for p in cache.glob('*.json'):
    try:
        r = json.loads(p.read_text(encoding='utf-8'))
    except Exception:
        continue
    u = r.get('url', '')
    fu = r.get('final_url', '')
    if 'u-tokyo' in u or 'u-tokyo' in fu or 'utokyo' in u.lower():
        rows.append((p.name, r.get('status'), r.get('method'), 'via' in r, len(r.get('text', '')), u, fu))

rows.sort(key=lambda x: x[5])
for name, st, m, has_via, ch, u, fu in rows:
    extra = f' -> {fu}' if fu and fu != u else ''
    print(f'{name} | st={st} | m={m} | via={has_via} | ch={ch:6d} | {u}{extra}')
print(f'Total: {len(rows)}')
