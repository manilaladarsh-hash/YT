import json, pathlib

u_path = pathlib.Path('data/universities/uvm.json')
u_data = json.loads(u_path.read_text(encoding='utf-8'))

u_data['fields']['toefl_min'] = {
    'code': '90',
    'value': 'Minimum for admission to the Graduate College at UVM is TOEFL iBT 90 (or 4.5 on the new scale).',
    'quote': 'TOEFL: Minimum for admission to the Graduate College at UVM | 90 or 4.5*',
    'url': 'https://www.uvm.edu/graduate/international-student-admissions'
}
u_data['checked'] = '2026-10-29'
u_path.write_text(json.dumps(u_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

uni_keys = {'app_fee', 'fee_waiver', 'gre_general', 'toefl_min', 'ielts_min', 'english_waiver'}
for prog_file in pathlib.Path('data/programs').glob('uvm--*.json'):
    data = json.loads(prog_file.read_text(encoding='utf-8'))
    changed = False
    for k in list(data['fields'].keys()):
        if k in uni_keys and data['fields'][k].get('code') == 'Not stated':
            del data['fields'][k]
            changed = True
    if changed:
        data['checked'] = '2026-10-29'
        prog_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('uvm updated successfully.')
