import json, pathlib

u_path = pathlib.Path('data/universities/rochester.json')
u_data = json.loads(u_path.read_text(encoding='utf-8'))

u_data['fields']['fee_waiver'] = {
    'code': 'Limited',
    'value': 'Requests for application fee waivers are considered on a case-by-case basis by departments.',
    'quote': 'Requests for application fee waivers are considered on a case-by-case basis. Only applicants who have completed their application with all the required materials submitted will be considered for a waiver.',
    'url': 'https://www.rochester.edu/college/gradstudies/admissions/faq.html'
}
u_data['fields']['gre_general'] = {
    'code': 'Not required',
    'value': 'GRE requirements vary by program and are not required centrally.',
    'quote': 'GRE requirements vary by program.',
    'url': 'https://www.rochester.edu/college/gradstudies/admissions/test-requirements.html'
}
u_data['checked'] = '2026-10-29'
u_path.write_text(json.dumps(u_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

uni_keys = {'app_fee', 'fee_waiver', 'gre_general', 'toefl_min', 'ielts_min', 'english_waiver'}
for prog_file in pathlib.Path('data/programs').glob('rochester--*.json'):
    data = json.loads(prog_file.read_text(encoding='utf-8'))
    changed = False
    for k in list(data['fields'].keys()):
        if k in uni_keys and data['fields'][k].get('code') == 'Not stated':
            del data['fields'][k]
            changed = True
    if changed:
        data['checked'] = '2026-10-29'
        prog_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('rochester updated successfully.')
