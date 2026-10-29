import json, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

CACHE = Path('.cache/pages')

def inspect_file(fname):
    p = CACHE / fname
    d = json.loads(p.read_text(encoding='utf-8'))
    print(f"URL: {d.get('url')}")
    print("--- TEXT SAMPLE ---")
    lines = [line.strip() for line in d.get('text', '').splitlines() if line.strip()]
    for i, line in enumerate(lines):
        if any(w in line.lower() for w in ['fee', 'gre', 'toefl', 'ielts', 'tuition', 'chf 100', 'exempt', 'test']):
            print(f"L{i}: {line}")

print("=== HEIDELBERG 0bcf2ceb97b7d267 ===")
inspect_file("0bcf2ceb97b7d267.json")

print("\n=== KIT 1a0de6245ba748f8 ===")
inspect_file("1a0de6245ba748f8.json")

print("\n=== FUBERLIN 201bd0297e2098ff ===")
inspect_file("201bd0297e2098ff.json")

print("\n=== STUTTGART fecf3401f1a38f4d ===")
inspect_file("fecf3401f1a38f4d.json")

print("\n=== STUTTGART 2d33ffcc354d67ff ===")
inspect_file("2d33ffcc354d67ff.json")

print("\n=== UNIBE 4a5dac5fee75274d ===")
inspect_file("4a5dac5fee75274d.json")
