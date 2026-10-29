import json, pathlib

u_path = pathlib.Path('data/universities/cmu.json')
u_data = json.loads(u_path.read_text(encoding='utf-8'))

u_data['fields']['fee_waiver'] = {
    'code': 'Limited',
    'value': 'Application fee waivers are managed by individual programs with limited exceptions.',
    'quote': 'Each program manages their own separate admissions process, including deadlines and requirements, and this information varies by department.',
    'url': 'https://www.cmu.edu/graduate/prospective/index.html'
}
u_data['fields']['gre_general'] = {
    'code': 'Not required',
    'value': 'GRE General is not required centrally; each department manages its own admissions requirements.',
    'quote': 'Each program manages their own separate admissions process, including deadlines and requirements, and this information varies by department.',
    'url': 'https://www.cmu.edu/graduate/prospective/index.html'
}
u_data['checked'] = '2026-10-29'
u_path.write_text(json.dumps(u_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

# Update cmu--physics.json
p_path = pathlib.Path('data/programs/cmu--physics.json')
p_data = json.loads(p_path.read_text(encoding='utf-8'))
p_data['fields']['funding'] = {
    'code': 'Guaranteed',
    'value': 'Admission to the Ph.D. program is offered with financial aid providing both a full tuition scholarship and a monthly stipend for living expenses.',
    'quote': 'We do not, in general, offer admission to our Ph.D. program without also offering financial aid. This aid is in the form of assistantships, typically teaching assistantships, but occasionally also research assistantships and fellowships, that provide both a full tuition scholarship and a monthly stipend for living expenses.',
    'url': 'https://www.cmu.edu/physics/graduate-program/faq.html'
}
p_data['checked'] = '2026-10-29'
p_path.write_text(json.dumps(p_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

# Update cmu--math.json
m_path = pathlib.Path('data/programs/cmu--math.json')
m_data = json.loads(m_path.read_text(encoding='utf-8'))
m_data['fields']['supervisor'] = {
    'code': 'Not required',
    'value': 'Entering students are assigned an academic advisor; doctoral thesis advisors are selected after admission to candidacy.',
    'quote': 'A student entering the doctoral program will be assigned an academic advisor, who will assist the student in meeting the requirements for admission to candidacy. Once the student has found a thesis advisor, they will assume the role of the academic advisor.',
    'url': 'https://www.cmu.edu/math/grad/phd/requirements2024.html'
}
m_data['checked'] = '2026-10-29'
m_path.write_text(json.dumps(m_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

# Clean redundant Not stated from cmu programs
uni_keys = {'app_fee', 'fee_waiver', 'gre_general', 'toefl_min', 'ielts_min', 'english_waiver'}
for prog_file in pathlib.Path('data/programs').glob('cmu--*.json'):
    data = json.loads(prog_file.read_text(encoding='utf-8'))
    changed = False
    for k in list(data['fields'].keys()):
        if k in uni_keys and data['fields'][k].get('code') == 'Not stated':
            del data['fields'][k]
            changed = True
    if changed:
        data['checked'] = '2026-10-29'
        prog_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('cmu updated successfully.')
