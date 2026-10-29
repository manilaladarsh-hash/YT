import json, re, sys
from pathlib import Path
from urllib.parse import urlparse

sys.stdout.reconfigure(encoding='utf-8')

CACHE = Path('.cache/pages')

TARGETS = ['heidelberg', 'kit', 'tuberlin', 'fuberlin', 'stuttgart', 'unibe', 'sorbonne', 'paris-saclay', 'ntnu']

domains = {
    'heidelberg': ['uni-heidelberg.de'],
    'kit': ['kit.edu'],
    'tuberlin': ['tu.berlin', 'tu-berlin.de'],
    'fuberlin': ['fu-berlin.de'],
    'stuttgart': ['uni-stuttgart.de'],
    'unibe': ['unibe.ch'],
    'sorbonne': ['sorbonne-universite.fr', 'sorbonne.fr'],
    'paris-saclay': ['universite-paris-saclay.fr'],
    'ntnu': ['ntnu.edu', 'ntnu.no'],
}

def search_text(text, patterns):
    matches = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        line_s = line.strip()
        for p in patterns:
            if re.search(p, line_s, re.IGNORECASE):
                start = max(0, i - 1)
                end = min(len(lines), i + 2)
                ctx = ' | '.join(lines[j].strip() for j in range(start, end) if lines[j].strip())
                matches.append((p, ctx))
                break
    return matches

out_lines = []

for uni in TARGETS:
    doms = domains[uni]
    out_lines.append(f'================ {uni.upper()} ================')
    uni_matches = []
    for p in CACHE.glob('*.json'):
        try:
            d = json.loads(p.read_text(encoding='utf-8'))
            url = d.get('url', '')
            host = urlparse(url).netloc.lower()
            if any(dom in host for dom in doms):
                text = d.get('text', '')
                m = search_text(text, [r'\bapplication fee\b', r'\btuition fee\b', r'\bno fee\b', r'\bfees?\b.*doctoral', r'\bgre\b', r'\btoefl\b', r'\bielts\b', r'english.*language'])
                if m:
                    for pat, ctx in m[:4]:
                        uni_matches.append((p.name, url, pat, ctx))
        except Exception:
            pass
    for fname, url, pat, ctx in uni_matches[:10]:
        out_lines.append(f'[{pat}] ({fname}) {ctx[:200]}')
        out_lines.append(f'   URL: {url}')

Path('.scratch/euro_search_results.txt').write_text('\n'.join(out_lines), encoding='utf-8')
print('Wrote .scratch/euro_search_results.txt')
