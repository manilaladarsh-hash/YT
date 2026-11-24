import json, glob

urls = [
    "https://www.uncw.edu/myUNCW/academics/graduate-school/students/assistantships.html",
    "https://www.uncw.edu/academics/graduate-school/prospective-students/financial/scholarships-fellowships.html",
    "https://www.uncw.edu/seahawk-life/money-matters/student-accounts-cashiers-office/tuition-fees/graduate-tuition/index.html",
    "https://www.uncw.edu/myUNCW/academics/colleges/cse/departments/chemistry/student-resources/index.html",
    "https://www.uncw.edu/myUNCW/academics/colleges/cse/departments/biology/student-resources/index.html",
]

with open('scratch/uncw_inspect2.txt', 'w', encoding='utf-8') as out:
    for p in glob.glob('.cache/pages/*.json'):
        d = json.load(open(p, encoding='utf-8'))
        if d.get('url') in urls:
            out.write(f"=== URL: {d.get('url')} FINAL: {d.get('final_url')}\n")
            out.write(d.get('text', '') + "\n")
            out.write("--- LINKS ---\n")
            for l in d.get('links', []):
                out.write(f"   {l}\n")
            out.write("\n")
