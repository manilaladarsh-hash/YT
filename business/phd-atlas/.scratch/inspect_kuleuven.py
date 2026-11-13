import json, glob

for f in sorted(glob.glob('data/programs/kuleuven--*.json')):
    d = json.load(open(f, encoding='utf-8'))
    print(f"{d['id']}: dept='{d['department']}' page='{d['program_page']}'")
