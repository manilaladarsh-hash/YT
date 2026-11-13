import json, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path('.')
CACHE = ROOT / '.cache' / 'pages'

for field in ['math', 'physics']:
    print(f"\n====================== {field.upper()} ======================")
    progs = [json.loads(p.read_text(encoding='utf-8')) for p in Path('data/programs').glob(f'*--{field}.json')]
    for p in progs:
        if p['fields'].get('gre_subject', {}).get('code') != 'Not stated':
            continue
        url = p['program_page']
        # find in cache
        for cp in CACHE.glob('*.json'):
            try:
                cd = json.loads(cp.read_text(encoding='utf-8'))
                if cd.get('url') == url or cd.get('final_url') == url:
                    text = cd.get('text', '')
                    m = re.findall(r'([^.\n]*\bGRE\b[^.\n]*)', text, re.IGNORECASE)
                    if m:
                        clean_m = [s.strip() for s in m if len(s.strip()) > 10 and len(s.strip()) < 150]
                        if clean_m:
                            print(f"{p['id']}: {clean_m[0]}")
                            print(f"   URL: {url}")
                    break
            except Exception:
                pass
