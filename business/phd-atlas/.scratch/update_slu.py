import json, pathlib

u_path = pathlib.Path('data/universities/slu.json')
u_data = json.loads(u_path.read_text(encoding='utf-8'))

q_fee = "SLU's application portal does not require an application fee."
q_gre = "Each department has different requirement standards for graduate admission tests such as the GRE. Contact the individual program or department for specific information regarding test scores and other admission requirements."

u_data['fields']['app_fee'] = {
    'code': '0 USD',
    'value': 'Saint Louis University application portal does not require an application fee for graduate admission.',
    'quote': q_fee,
    'url': 'https://www.slu.edu/admission/graduate/faq.php'
}
u_data['fields']['fee_waiver'] = {
    'code': 'No fee',
    'value': 'No application fee is charged by the SLU portal, so no waiver is needed.',
    'quote': q_fee,
    'url': 'https://www.slu.edu/admission/graduate/faq.php'
}
u_data['fields']['gre_general'] = {
    'code': 'Not required',
    'value': 'GRE General is not required at the university level; individual departments set their own testing requirements.',
    'quote': q_gre,
    'url': 'https://www.slu.edu/admission/graduate/faq.php'
}
u_data['checked'] = '2026-10-29'
u_path.write_text(json.dumps(u_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

uni_keys = {'app_fee', 'fee_waiver', 'gre_general', 'toefl_min', 'ielts_min', 'english_waiver'}
for prog_file in pathlib.Path('data/programs').glob('slu--*.json'):
    data = json.loads(prog_file.read_text(encoding='utf-8'))
    changed = False
    for k in list(data['fields'].keys()):
        if k in uni_keys and data['fields'][k].get('code') == 'Not stated':
            del data['fields'][k]
            changed = True
    if changed:
        data['checked'] = '2026-10-29'
        prog_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('slu updated successfully.')
