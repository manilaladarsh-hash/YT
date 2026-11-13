import json, pathlib

p = pathlib.Path('data/programs/udel--datasci.json')
d = json.loads(p.read_text(encoding='utf-8'))

d['fields']['supervisor'] = {
    'code': 'Not required',
    'value': 'Applicants are instructed not to reach out to faculty independently; the admissions committee matches qualified applicants with faculty mentors.',
    'quote': 'Members of the committee will work with qualified applicants to identify a suitable faculty mentor to provide funding; applicants should not reach out to faculty independently.',
    'url': 'https://bioinformatics.udel.edu/education/prospective-students/admissions-frequently-asked-questions/'
}
d['fields']['funding'] = {
    'code': 'Guaranteed',
    'value': 'Admission to the full-time PhD is contingent upon securing an RA, which provides full tuition and a stipend.',
    'quote': 'Admission to the full-time PhD is contingent upon securing a Research Assistantship (RA), which would include a stipend and full tuition coverage.',
    'url': 'https://bioinformatics.udel.edu/education/prospective-students/admissions-frequently-asked-questions/'
}
d['checked'] = '2026-10-29'
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('udel--datasci updated.')
