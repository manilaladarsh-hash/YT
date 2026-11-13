import json, shutil

shutil.copy('data/programs/buffalo--cs.json', 'data/staging/programs/buffalo--cs.json')
with open('data/staging/programs/buffalo--cs.json', encoding='utf-8') as f:
    d1 = json.load(f)
d1['fields']['entry_route']['quote'] = (
    "First-year students may be admitted into either the MS or the PhD program. "
    "Normally, students with a master's degree in computer science and engineering "
    "(and some other students upon the recommendation of the Graduate Admissions Committee) "
    "are admitted directly into the PhD program."
)
with open('data/staging/programs/buffalo--cs.json', 'w', encoding='utf-8') as f:
    json.dump(d1, f, indent=2, ensure_ascii=False)
    f.write('\n')

shutil.copy('data/programs/byu--chemistry.json', 'data/staging/programs/byu--chemistry.json')
with open('data/staging/programs/byu--chemistry.json', encoding='utf-8') as f:
    d2 = json.load(f)
d2['fields']['fee_waiver']['quote'] = (
    'contact Alena Allred to request a fee waiver. The request must be received on or before December 20'
)
d2['fields']['english_waiver']['quote'] = (
    'Generally, all applicants are required to demonstrate an acceptable level of English language proficiency '
    'in order to satisfy the university requirements for graduate admission. '
    'Only applicants who are citizens of the United States, Canada, the U.K., '
    'the Republic of Ireland, New Zealand, or Australia'
)
with open('data/staging/programs/byu--chemistry.json', 'w', encoding='utf-8') as f:
    json.dump(d2, f, indent=2, ensure_ascii=False)
    f.write('\n')
print("Staged buffalo--cs and byu--chemistry cleanly.")
