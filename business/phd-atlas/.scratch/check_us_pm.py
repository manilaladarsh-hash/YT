import json
from pathlib import Path

ROOT = Path('.')
CACHE = ROOT / '.cache' / 'pages'

programs_to_check = [
    'brown--math',
    'buffalo--math',
    'columbia--physics',
    'bostonu--physics',
    'bostonu--math',
    'baylor--physics',
    'baylor--math',
    'binghamton--math',
    'binghamton--physics',
    'bgsu--math',
    'bc--math',
    'bc--physics',
    'claremontgrad--math',
    'berkeley--physics',
    'asu--physics',
    'arizona--physics',
    'arizona--math',
]

for pid in programs_to_check:
    path = ROOT / 'data' / 'programs' / f'{pid}.json'
    if not path.exists():
        continue
    data = json.loads(path.read_text(encoding='utf-8'))
    url = data['program_page']
    print(f"\n==================== {pid} ====================")
    print(f"URL: {url}")
    # find cached file
    cached_file = None
    for cp in CACHE.glob('*.json'):
        try:
            cd = json.loads(cp.read_text(encoding='utf-8'))
            if cd.get('url') == url or cd.get('final_url') == url:
                cached_file = cp
                break
        except Exception:
            pass
    if not cached_file:
        print("  NO CACHED FILE FOUND")
        continue
    print(f"  Cached file: {cached_file.name}")
    text = json.loads(cached_file.read_text(encoding='utf-8')).get('text', '')
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    for i, line in enumerate(lines):
        if any(w in line.lower() for w in ['advisor', 'supervisor', 'funding', 'assistantship', 'stipend', 'gre', 'direct', 'master']):
            if len(line) < 160:
                print(f"  L{i}: {line}")
