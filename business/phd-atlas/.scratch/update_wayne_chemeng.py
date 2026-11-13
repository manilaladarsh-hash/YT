import json

path = 'data/staging/programs/wayne--chemeng.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

data['fields']['entry_route'] = {
    "code": "Either",
    "value": "Regular admission requires a 3.5 grade point average in a Master of Science program, or a Bachelor of Science program from an accredited U.S. institution.",
    "quote": "Regular admission requires a 3.5 grade point average in a Master of Science program, or a Bachelor of Science program from an accredited U.S. institution.",
    "url": data['program_page']
}

data['fields']['supervisor'] = {
    "code": "Not stated",
    "value": "Pre-application supervisor requirement is not stated.",
    "quote": "",
    "url": data['program_page']
}

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Updated wayne--chemeng.json")
