import json
import hashlib
import re

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("\u00a0", " ")
    return re.sub(r"\s+", " ", s).strip().lower()

def get_text(url):
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    with open(f'.cache/pages/{key}.json', encoding='utf-8') as f:
        return norm(json.load(f)['text'].replace('\n', ' '))

entity = get_text('https://uwyo.catalog.acalog.com/preview_entity.php?catoid=19&ent_oid=3180')
policies = get_text('https://uwyo.catalog.acalog.com/content.php?catoid=19&navoid=2054')
adm = get_text('https://uwyo.catalog.acalog.com/content.php?catoid=19&navoid=2018')
bms = get_text('https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20502')
neuro = get_text('https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20505')
pie2 = get_text('https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20503')
che = get_text('https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20437')

quotes = [
    (entity, 'The priority deadline for students entering in the fall is March 1.'),
    (policies, 'It is the responsibility of the graduate student, in consultation with their major advisor (usually the Committee Chair) to form a viable committee within the first two semesters of their graduate program.'),
    (policies, 'Students wishing to pursue direct entry into a doctoral program following their bachelor’s degree must meet the following criteria:'),
    (adm, 'Graduate Assistantships: Many graduate programs offer assistantships, which provide tuition benefits and stipends to eligible students.'),
    (bms, 'To ensure full application review for fall semester admission, applications should be received by February 15.'),
    (neuro, 'GRE: Accepted but not required;'),
    (pie2, 'Agreement by a member of the PiE2 faculty to sponsor the student, or to co-sponsor the student together with a PiE2 affiliate'),
    (che, 'A master’s degree is not required to enter a Ph.D. program.')
]

for text, q in quotes:
    ok = norm(q) in text
    print(ok, ':', q[:60])
