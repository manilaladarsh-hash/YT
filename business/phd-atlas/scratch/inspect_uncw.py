import json, glob

urls = [
    "https://www.uncw.edu/academics/graduate-school/prospective-students/financial/index.html",
    "https://www.uncw.edu/myUNCW/academics/graduate-school/students/index.html",
    "https://gradapply.uncw.edu/portal/apply?cmd=prog_details&program=SE_PHD_DCOS_IDS",
    "https://gradapply.uncw.edu/portal/apply?cmd=prog_details&program=SE_PHD_DIMB_BIO",
    "https://gradapply.uncw.edu/portal/apply?cmd=prog_details&program=SE_PHD_DPCH_CHEM",
    "https://www.uncw.edu/academics/colleges/cse/departments/biology/graduate.html",
    "https://www.uncw.edu/academics/colleges/cse/departments/chemistry/graduate-programs.html",
]

with open('scratch/uncw_inspect.txt', 'w', encoding='utf-8') as out:
    for p in glob.glob('.cache/pages/*.json'):
        d = json.load(open(p, encoding='utf-8'))
        if d.get('url') in urls:
            out.write(f"=== URL: {d.get('url')} FINAL: {d.get('final_url')}\n")
            out.write(d.get('text', '') + "\n")
            out.write("--- LINKS ---\n")
            for l in d.get('links', []):
                s = ' '.join(l) if isinstance(l, list) else str(l)
                if any(k in s.lower() for k in ['finan', 'assist', 'tuition', 'fund', 'scholar', 'student-resources', 'money', 'cost', 'gra', 'gta', 'remission']):
                    out.write(f"   {l}\n")
            out.write("\n")
