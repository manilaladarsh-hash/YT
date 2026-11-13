import json, pathlib

u_path = pathlib.Path('data/universities/tulane.json')
u_data = json.loads(u_path.read_text(encoding='utf-8'))

u_data['fields']['app_fee'] = {
    'code': '0 (no fee)',
    'value': 'Tulane does not charge application fees for School of Science & Engineering or Biomedical graduate PhD programs.',
    'quote': 'there are no application fees for our PhD, MS, or Graduate Certificate programs',
    'url': 'https://sse.tulane.edu/graduate/admissions'
}
u_data['fields']['fee_waiver'] = {
    'code': 'No fee',
    'value': 'No application fee is charged, so no waiver is required.',
    'quote': 'there are no application fees for our PhD, MS, or Graduate Certificate programs',
    'url': 'https://sse.tulane.edu/graduate/admissions'
}
u_data['fields']['gre_general'] = {
    'code': 'Not required',
    'value': 'The School of Science and Engineering does not require GRE scores for review; requirements vary by department.',
    'quote': 'The School of Science and Engineering does not require GRE scores for review by the department. Applicants who have taken the GRE may include their scores on the application.',
    'url': 'https://sse.tulane.edu/graduate/admissions'
}
u_data['fields']['toefl_min'] = {
    'code': '87',
    'value': 'Minimum overall score on TOEFL iBT is 87 for Science & Engineering graduate programs.',
    'quote': 'Minimum overall score on TOEFL iBT: 87.',
    'url': 'https://sse.tulane.edu/graduate/admissions',
    'conflict': True
}
u_data['fields']['ielts_min'] = {
    'code': '7',
    'value': 'Minimum overall band score on IELTS Academic is 7.0 for Science & Engineering graduate programs.',
    'quote': 'Minimum overall band score on IELTS Academic: 7.0.',
    'url': 'https://sse.tulane.edu/graduate/admissions'
}
u_data['fields']['english_waiver'] = {
    'code': 'No',
    'value': 'English test is waived only for degrees from the US or countries where English is the primary spoken language of daily life; India is not exempt.',
    'quote': 'A bachelor’s degree or higher from an accredited university located in the U.S or another country in which English is both the primary spoken language of daily life and the language of instruction',
    'url': 'https://sse.tulane.edu/graduate/admissions'
}
u_data['checked'] = '2026-10-29'
u_path.write_text(json.dumps(u_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

# Update tulane--biomed.json
bm_path = pathlib.Path('data/programs/tulane--biomed.json')
bm_data = json.loads(bm_path.read_text(encoding='utf-8'))
bm_data['fields']['funding'] = {
    'code': 'Guaranteed',
    'value': 'All PhD students receive a full tuition waiver, paid health insurance and a stipend of approximately $35,000 per year.',
    'quote': 'All PhD students receive a full tuition waiver, paid health insurance and a stipend of approximately $35,000 per year for the entire duration of the program, usually between four and seven years.',
    'url': 'https://medicine.tulane.edu/biomedical-sciences-graduate-program/interdisciplinary-phd-program'
}
bm_data['fields']['supervisor'] = {
    'code': 'Recommended',
    'value': 'Applicants are asked to name faculty members whose research is of interest in their personal statement.',
    'quote': 'You will also be asked to include the names of any Tulane School of Medicine faculty members whose research is of interest.',
    'url': 'https://medicine.tulane.edu/biomedical-sciences-graduate-program/interdisciplinary-phd/admission-requirements'
}
bm_data['checked'] = '2026-10-29'
bm_path.write_text(json.dumps(bm_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

# Clean redundant Not stated from tulane programs
uni_keys = {'app_fee', 'fee_waiver', 'gre_general', 'toefl_min', 'ielts_min', 'english_waiver'}
for prog_file in pathlib.Path('data/programs').glob('tulane--*.json'):
    data = json.loads(prog_file.read_text(encoding='utf-8'))
    changed = False
    for k in list(data['fields'].keys()):
        if k in uni_keys and data['fields'][k].get('code') == 'Not stated':
            del data['fields'][k]
            changed = True
    if changed:
        data['checked'] = '2026-10-29'
        prog_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('tulane updated successfully.')
