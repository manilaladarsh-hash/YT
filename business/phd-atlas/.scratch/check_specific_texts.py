import json
from pathlib import Path

CACHE = Path('.cache/pages')

files = [
    ('columbia--physics', '73d141088d65a5c6.json'),
    ('claremontgrad--math', 'f1a497382945f5c9.json'),
    ('binghamton--physics', '7491b05ca48ba8ec.json'),
    ('bgsu--math', '0c6781a86fad1426.json'),
    ('bc--math', '1d0d95b4fbc38bb3.json'),
    ('buffalo--math', '28c48df61a49baa8.json'),
    ('baylor--math', '3974098d1278f0aa.json'),
    ('baylor--physics', '44ef4ace6886b315.json'),
]

for name, fname in files:
    p = CACHE / fname
    if not p.exists():
        continue
    data = json.loads(p.read_text(encoding='utf-8'))
    print(f"\n=================== {name} ({fname}) ===================")
    print(f"URL: {data.get('url')}")
    text = data.get('text', '')
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    for i, line in enumerate(lines):
        if any(w in line.lower() for w in ['funding', 'stipend', 'assistantship', 'advisor', 'supervisor', 'fellowship', 'tuition', 'support', 'guarantee', 'admit', 'admission', 'gre']):
            print(f"  [{i}]: {line[:130]}")
