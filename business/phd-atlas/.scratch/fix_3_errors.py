import json

def fix_bgsu():
    p = 'data/programs/bgsu--math.json'
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    d['fields']['entry_route']['code'] = "Master's usually required"
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print("Fixed bgsu--math.json")

def fix_binghamton():
    p = 'data/programs/binghamton--physics.json'
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    d['fields']['funding']['code'] = "Typical"
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print("Fixed binghamton--physics.json")

def fix_kit():
    p = 'data/programs/kit--physics.json'
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    d['fields']['deadline']['quote'] = "There is no centrally organized application portal for doctoral researchers at the department. Applications should be addressed to potential supervisors."
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print("Fixed kit--physics.json")

fix_bgsu()
fix_binghamton()
fix_kit()
