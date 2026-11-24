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

targets = [
    'https://www.u-tokyo.ac.jp/en/prospective-students/tuition_fees.html',
    'https://www.u-tokyo.ac.jp/en/prospective-students/exemptions.html',
    'https://www.u-tokyo.ac.jp/en/prospective-students/tuition_scholarships.html',
    'https://www.s.u-tokyo.ac.jp/en/overview/graduate02.html',
    'https://www.s.u-tokyo.ac.jp/en/admission/graduate.html',
    'https://www.civil.t.u-tokyo.ac.jp/en/admission/',
    'https://dss.i.u-tokyo.ac.jp/',
    'https://www.i.u-tokyo.ac.jp/edu/entra/2027_ag_d_e.pdf',
    'https://www.chem.s.u-tokyo.ac.jp/chem_graduate/apply_en.html',
    'https://www.bs.s.u-tokyo.ac.jp/english/',
    'https://www.m.u-tokyo.ac.jp/english/daigakuin/apply/appguidemain.html',
]

out = []
for u in targets:
    r = by_url.get(u)
    out.append(f'=== {u} (found={bool(r)}) ===')
    if r:
        out.append(r.get('text', '')[:6000])

Path('scratch/utokyo_check_part1.txt').write_text('\n'.join(out), encoding='utf-8')
print('Wrote scratch/utokyo_check_part1.txt', len(out))
