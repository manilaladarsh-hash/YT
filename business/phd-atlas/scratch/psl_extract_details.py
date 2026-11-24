import glob, json

urls_wanted = [
    "https://psl.eu/en/education/international-students",
    "https://psl.eu/en/education/admissions/graduate-admissions",
    "https://psl.eu/en/lifepsl/campus-life-paris/financial-aids",
    "https://psl.eu/en/graduate-programs/astrophysics",
    "https://psl.eu/en/graduate-programs/chemistry",
    "https://psl.eu/en/graduate-programs/computer-science",
    "https://psl.eu/en/graduate-programs/engineering-isai",
    "https://psl.eu/en/graduate-programs/mathematics-and-applications",
    "https://psl.eu/en/graduate-programs/physics",
    "https://psl.eu/en/graduate-programs/earth-science-and-biodiversity",
    "https://psl.eu/en/graduate-programs/life-sciences",
    "https://psl.eu/en/graduate-programs/cognitive-sciences",
    "https://psl.eu/en/programmes-gradues/programme-data",
    "https://ecole-doctorale.obspm.fr",
    "https://www.minesparis.psl.eu/ismme/",
    "https://www.chimieparistech.psl.eu/en/admissions/phd-admissions/",
    "https://www.ephe.fr/formations/doctorat",
    "https://ecole-doctorale.dauphine.psl.eu/programmes-doctoraux/informatique",
    "https://ecole-doctorale.dauphine.psl.eu/programmes-doctoraux/mathematique",
    "https://ecole-doctorale.dauphine.psl.eu/candidature/1ere-annee-de-these",
    "https://www.espci.psl.eu/en/education/phd-studies/",
    "https://ed388.sorbonne-universite.fr/en",
    "https://ed391.sorbonne-universite.fr/",
    "https://ed406.sorbonne-universite.fr/",
    "https://ed129.sorbonne-universite.fr/fr/index.html",
    "https://ed515.sorbonne-universite.fr/en/ed-515",
    "https://ed3c.sorbonne-universite.fr/",
]

by_url = {}
for f in sorted(glob.glob(".cache/pages/*.json")):
    d = json.load(open(f, encoding="utf-8"))
    by_url[d.get("url", "")] = d

with open("scratch/psl_digest.txt", "w", encoding="utf-8") as out:
    for u in urls_wanted:
        d = by_url.get(u)
        if not d:
            out.write(f"MISSING: {u}\n")
            continue
        out.write(f"================ {u} (final={d.get('final_url')}) ================\n")
        txt = d.get("text", "")
        # strip common PSL nav header if present
        if "psl.eu/" in u and "Print\n" in txt:
            idx = txt.find("Print\n")
            txt = txt[idx+6:]
        if "psl.eu/" in u and "\nMain navigation\n" in txt:
            txt = txt[:txt.find("\nMain navigation\n")]
        out.write(txt.strip() + "\n\n")
print("wrote scratch/psl_digest.txt")
