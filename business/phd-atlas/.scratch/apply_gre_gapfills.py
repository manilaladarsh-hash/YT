import json
from pathlib import Path

ROOT = Path('.')
CACHE = ROOT / '.cache' / 'pages'

def find_exact_quote(url, text_fragment):
    for cp in CACHE.glob('*.json'):
        try:
            data = json.loads(cp.read_text(encoding='utf-8'))
            if data.get('url') == url or data.get('final_url') == url:
                lines = [l.strip() for l in data.get('text', '').splitlines() if l.strip()]
                for l in lines:
                    if text_fragment.lower() in l.lower():
                        return l, data.get('url')
        except Exception:
            pass
    return None, None

updates = [
    # Math
    ('denver--math', 'gre_subject', 'Optional', 'GRE scores are optional for admission to this program'),
    ('illinoistech--math', 'gre_subject', 'Optional', 'GRE Scores - Optional'),
    ('marquette--math', 'gre_subject', 'Optional', 'GRE scores (optional)'),
    ('miami--math', 'gre_subject', 'Optional', 'Note that the GRE test is accepted but not required'),
    ('ohiou--math', 'gre_subject', 'Optional', 'The Graduate Record Examination (GRE) is optional, but applicants are encouraged to submit their GRE scores if available'),
    ('oregonstate--math', 'gre_subject', 'Optional', 'GRE scores (optional)'),
    ('ou--math', 'gre_subject', 'Not required', 'GRE scores are not required this year'),
    ('utoledo--math', 'gre_subject', 'Optional', 'The GRE is not required but students may have it submitted to the University by ETS'),
    ('epfl--math', 'gre_subject', 'Recommended', 'Highly recommended: TOEFL and GRE'),
    
    # Physics
    ('dayton--physics', 'gre_subject', 'Not required', 'Results from the GRE are not required'),
    ('denver--physics', 'gre_subject', 'Optional', 'GRE scores are optional for admission to this program'),
    ('louisville--physics', 'gre_subject', 'Not required', 'GRE requirement is not needed for admission to the PhD program'),
]

for pid, field, code, fragment in updates:
    path = ROOT / 'data' / 'programs' / f'{pid}.json'
    d = json.loads(path.read_text(encoding='utf-8'))
    page_url = d['program_page']
    quote, found_url = find_exact_quote(page_url, fragment)
    if not quote:
        print(f"FAILED to find quote for {pid}: {fragment}")
        continue
    d['fields'][field] = {
        'code': code,
        'value': f"GRE requirement stated on program page.",
        'quote': quote,
        'url': found_url
    }
    path.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    print(f"Applied {pid}.{field} = {code} -> {quote[:70]}")
