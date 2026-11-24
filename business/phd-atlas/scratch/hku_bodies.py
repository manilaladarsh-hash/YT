import pathlib, json, hashlib

urls = [
  'https://gradsch.hku.hk/prospective_students/research_areas',
  'https://gradsch.hku.hk/prospective_students/application/admission_requirement',
  'https://gradsch.hku.hk/prospective_students/application/application_period',
  'https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/fees',
  'https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/postgraduate_scholarships',
  'https://engg.hku.hk/About-Us/Departments',
  'https://www.physics.hku.hk/graduate_studies/for_prospective_students/research_postgraduate_program/',
  'https://www.scifac.hku.hk/rpg-programme/',
  'https://www.geog.hku.hk/mphil-phd',
]
out = []
for u in urls:
  h = hashlib.sha1(u.encode()).hexdigest()[:16]
  p = pathlib.Path('.cache/pages') / f'{h}.json'
  if not p.exists():
    out.append(f'=== MISSING {u} ===')
    continue
  d = json.loads(p.read_text(encoding='utf-8'))
  lines = d.get('text','').splitlines()
  fu = d.get('final_url')
  out.append(f'=== {u} (final={fu}, lines={len(lines)}) ===')
  if len(lines) > 220:
    out.append('\n'.join(lines[160:]))
  else:
    out.append('\n'.join(lines))
  links = [f'{l[0]} -> {l[1]}' for l in d.get('links',[]) if any(k in (l[0]+l[1]).lower() for k in ['phd','mphil','rpg','material','energy','astro','planet','env','bio','chem','mech','civil','ece','eee','dase','stat','cds','neuro','psych'])]
  if links:
    out.append('LINKS:\n  ' + '\n  '.join(list(dict.fromkeys(links))[:40]))
pathlib.Path('scratch/hku_bodies.txt').write_text('\n'.join(out), encoding='utf-8')
print('Wrote scratch/hku_bodies.txt')
