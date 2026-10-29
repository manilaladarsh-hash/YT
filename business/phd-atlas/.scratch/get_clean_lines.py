import json, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
CACHE = Path('.cache/pages')

def inspect_lines(fname, lines_idx):
    p = CACHE / fname
    data = json.loads(p.read_text(encoding='utf-8'))
    lines = [l.strip() for l in data.get('text', '').splitlines() if l.strip()]
    print(f"=== {fname} ({data.get('url')}) ===")
    for idx in lines_idx:
        if 0 <= idx < len(lines):
            print(f"L{idx}: {repr(lines[idx])}")

inspect_lines('73d141088d65a5c6.json', range(25, 30))
inspect_lines('f1a497382945f5c9.json', [412, 453])
inspect_lines('7491b05ca48ba8ec.json', [23, 27])
inspect_lines('0c6781a86fad1426.json', [161, 209])
inspect_lines('1d0d95b4fbc38bb3.json', range(114, 120))
inspect_lines('28c48df61a49baa8.json', range(65, 80))
inspect_lines('3974098d1278f0aa.json', range(65, 80))
inspect_lines('44ef4ace6886b315.json', range(30, 45))
