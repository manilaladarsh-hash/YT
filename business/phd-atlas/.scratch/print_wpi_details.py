import json

data = json.load(open('.cache/pages/307454e2314cb615.json', 'r', encoding='utf-8'))
lines = data.get('text', '').splitlines()

targets = [
    "Physics PhD",
    "Mathematical Sciences PhD",
    "Statistics PhD",
    "Computer Science PhD",
    "Data Science PhD",
    "Electrical & Computer Engineering PhD",
    "Mechanical Engineering PhD",
    "Chemical Engineering PhD",
    "Civil Engineering PhD",
    "Biomedical Engineering PhD",
    "Materials Science & Engineering PhD",
    "Molecular and Cellular Biology PhD"
]

for t in targets:
    for i, line in enumerate(lines):
        if line.strip() == t or line.strip() == f"PhD in {t.replace(' PhD', '')}":
            print("="*50)
            print("TARGET:", t, "at line", i)
            for k in range(max(0, i - 2), min(len(lines), i + 20)):
                clean = lines[k].encode('ascii', errors='replace').decode('ascii')
                print(f"  [{k}] {clean}")
            break
