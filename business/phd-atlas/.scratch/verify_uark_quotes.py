import json
import re

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("\u00a0", " ")
    return re.sub(r"\s+", " ", s).strip().lower()

with open('.cache/pages/d73cb49ac4de1f4b.json', encoding='utf-8') as f:
    uark_adm = norm(json.load(f)['text'].replace('\n', ' '))
with open('.cache/pages/3143dafdfa1c89da.json', encoding='utf-8') as f:
    uark_cat = norm(json.load(f)['text'].replace('\n', ' '))

quotes = [
    (uark_adm, 'The application fee is $75 for all new international graduate applicants.'),
    (uark_adm, 'An application fee waiver will be granted to individuals that qualify under these | circumstances: | Full-time employees at the U of A main campus | U of A summer REU program participants'),
    (uark_adm, 'The University of Arkansas Graduate School does not require a standardized test score | (GRE, GMAT or other graduate-level standardized test) for official admission to the | university. However, individual programs may require a standardized test score.'),
    (uark_cat, '4.0 on the Internet-based Test of English as a Foreign Language (TOEFL)'),
    (uark_cat, '6.5 on the International English Language Testing System Academic (IELTS)'),
    (uark_cat, "unless they have received a bachelor's or graduate degree from an accredited U.S. college or university or receive a waiver of the English Language proficiency requirement by the Graduate Council Academic Appeals Committee by demonstrating an acceptable level of language proficiency as defined in the Graduate School Handbook located on the Graduate School website.")
]

for text, q in quotes:
    parts = [norm(p.strip()) for p in q.split(' | ')]
    ok = all(p in text for p in parts)
    print(ok, ':', q[:60])
