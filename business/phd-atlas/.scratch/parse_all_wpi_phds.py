import json

data = json.load(open('.cache/pages/307454e2314cb615.json', 'r', encoding='utf-8'))
lines = data.get('text', '').splitlines()

# Let's find every line that has " PhD"
results = []
for i, line in enumerate(lines):
    l = line.strip()
    if l.endswith(' PhD') or l.startswith('PhD in '):
        # Scan forward for department, deadline, GRE, qualifications
        info = {'name': l, 'line': i}
        for k in range(i, min(len(lines), i + 35)):
            txt = lines[k].strip()
            if txt == 'Department' and k + 1 < len(lines):
                info['dept'] = lines[k+1].strip()
            elif txt == 'Application Submission Deadline' and k + 1 < len(lines):
                info['deadline'] = lines[k+1].strip()
            elif txt == 'GRE' and k + 1 < len(lines):
                info['gre'] = lines[k+1].strip()
            elif 'Admissions Qualifications' in txt and k + 1 < len(lines):
                info['qual'] = lines[k+1].strip()
        results.append(info)

print(f"Total PhD programs found: {len(results)}")
for r in results:
    clean_name = r['name'].encode('ascii', errors='replace').decode('ascii')
    print(f"{clean_name} | Dept: {r.get('dept')} | DL: {r.get('deadline')} | GRE: {r.get('gre')}")
