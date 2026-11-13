import subprocess
import sys

urls = [
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/physicsphys/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/chemistrychem/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/mathematicalsciencesmath/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/computerscienceandcomputercsce/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/biologicalsciencesbiol/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/cellandmolecularbiologycemb/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/materialsscienceandengineeringmsen/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/geosciencesgeos/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/environmentaldynamicsendy/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/electricalengineeringeleg/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/mechanicalengineeringmeeg/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/chemicalengineeringcheg/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/civilengineeringcveg/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/biomedicalengineeringbmeg/",
    "https://catalog.uark.edu/graduatecatalog/programsofstudy/spaceandplanetarysciencesspac/",
]

for url in urls:
    print(f"Fetching {url}...")
    res = subprocess.run(["python", "scripts/research.py", url], capture_output=True, text=True, encoding="utf-8")
    print(res.stdout[:200])

print("Done fetching.")
