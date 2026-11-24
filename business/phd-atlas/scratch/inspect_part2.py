import json
from pathlib import Path

cache = Path('.cache/pages')
by_url = {}
for p in cache.glob('*.json'):
    try:
        r = json.loads(p.read_text(encoding='utf-8'))
        by_url[r.get('url', '')] = r
        if r.get('final_url'):
            by_url[r['final_url']] = r
    except Exception:
        pass

def dump(u, start=0, length=12000, show_links=False):
    r = by_url.get(u)
    lines = [f'=== {u} (found={bool(r)}, total_chars={len(r.get("text","")) if r else 0}) ===']
    if r:
        lines.append(r.get('text', '')[start:start+length])
        if show_links and r.get('links'):
            lines.append('--- LINKS ---')
            for lnk in r['links']:
                lines.append(f'  LINK: {lnk}')
    return '\n'.join(lines)

parts = [
    dump('https://www.s.u-tokyo.ac.jp/en/admission/graduate.html', 6000, 22000, True),
    dump('https://www.s.u-tokyo.ac.jp/en/admission/doctor/index.html', 6000, 10000, True),
    dump('https://www.s.u-tokyo.ac.jp/en/overview/graduate02.html', 6000, 22000, True),
    dump('https://www.civil.t.u-tokyo.ac.jp/en/admission/', 4000, 8000, True),
    dump('https://www.i.u-tokyo.ac.jp/edu/entra/2027_ag_d_e.pdf', 5500, 20000, False),
    dump('https://www.i.u-tokyo.ac.jp/edu/entra/entra_e.shtml', 0, 28000, True),
    dump('https://www.m.u-tokyo.ac.jp/english/daigakuin/apply/appguidemain.html', 5500, 6000, True),
    dump('https://www.k.u-tokyo.ac.jp/complex/html/examinee/examinee_e.html', 0, 14000, False),
    dump('https://www.k.u-tokyo.ac.jp/en/assets/files/04IB_BD_e.pdf', 0, 6000, False),
    dump('https://www.k.u-tokyo.ac.jp/en/assets/files/05CBMS_BD_e.pdf', 0, 6000, False),
    dump('https://www.k.u-tokyo.ac.jp/en/assets/files/06NENV_BD_e.pdf', 0, 6000, False),
]

Path('scratch/utokyo_check_part2.txt').write_text('\n'.join(parts), encoding='utf-8')
print('Wrote scratch/utokyo_check_part2.txt')
