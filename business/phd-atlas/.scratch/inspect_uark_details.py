import json
import glob
import re
import os

fields_map = {
    "physics": "https://catalog.uark.edu/graduatecatalog/programsofstudy/physicsphys/",
    "chemistry": "https://catalog.uark.edu/graduatecatalog/programsofstudy/chemistryandbiochemistrychbcdepartmentof/",
    "math": "https://catalog.uark.edu/graduatecatalog/programsofstudy/mathematicalsciencesdepartmentofmasc/",
    "cs": "https://catalog.uark.edu/graduatecatalog/programsofstudy/computerscienceandcomputerengineeringcsce/",
    "biology": "https://catalog.uark.edu/graduatecatalog/programsofstudy/biologicalsciencesbisc/",
    "biomed": "https://catalog.uark.edu/graduatecatalog/programsofstudy/cellandmolecularbiologycemb/",
    "materials": "https://catalog.uark.edu/graduatecatalog/programsofstudy/materialsengineeringmate/",
    "earth": "https://catalog.uark.edu/graduatecatalog/programsofstudy/geosciencesdepartmentofgeos/",
    "environment": "https://catalog.uark.edu/graduatecatalog/programsofstudy/environmentaldynamicsendy/",
    "ece": "https://catalog.uark.edu/graduatecatalog/programsofstudy/electricalengineeringeleg/",
    "mech": "https://catalog.uark.edu/graduatecatalog/programsofstudy/mechanicalengineeringmeeg/",
    "chemeng": "https://catalog.uark.edu/graduatecatalog/programsofstudy/chemicalengineeringralphemartindepartmentofcheg/",
    "civil": "https://catalog.uark.edu/graduatecatalog/programsofstudy/civilengineeringcveg/",
    "bme": "https://catalog.uark.edu/graduatecatalog/programsofstudy/biomedicalengineeringbmen/",
    "astronomy": "https://catalog.uark.edu/graduatecatalog/programsofstudy/spaceandplanetarysciencesspac/",
}

import hashlib
for field, url in fields_map.items():
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    cpath = f".cache/pages/{key}.json"
    if not os.path.exists(cpath):
        print(f"Missing cache for {field}")
        continue
    with open(cpath, encoding="utf-8") as f:
        text = json.load(f)["text"]
    
    print(f"\n=================== {field.upper()} ===================")
    # Search for PhD admission, requirements, deadline, funding, assistantship
    for line in text.split("\n"):
        line_l = line.lower()
        if any(k in line_l for k in ["deadline", "assistantship", "stipend", "admission to the ph.d.", "requirements for admission to the ph.d.", "gre", "supervisor", "advisor"]):
            if len(line.strip()) > 20:
                print("  •", line.strip()[:140])
