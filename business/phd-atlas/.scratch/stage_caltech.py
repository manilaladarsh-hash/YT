import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CALTECH_PROGS = {
    "cs": {
        "url": "https://www.cms.caltech.edu/academics/grad-cs",
        "dept": "Computer Science (CS)",
        "gre_row": "Computer Science PhD R",
        "note": "Computing and Mathematical Sciences (CMS) is a separate option with a December 15 deadline."
    },
    "astronomy": {
        "url": "https://www.astro.caltech.edu/",
        "dept": "Astrophysics (AY)",
        "gre_row": "Astrophysics PhD R / (Physics subject test required)",
        "note": "Astrophysics graduate option administered within PMA at Caltech."
    },
    "biology": {
        "url": "https://www.bbe.caltech.edu/academics/biology",
        "dept": "Biology (BI)",
        "gre_row": "Biology PhD R",
        "note": "Biology graduate option in the Division of Biology and Biological Engineering (BBE) at Caltech."
    },
    "bme": {
        "url": "https://www.bbe.caltech.edu/academics/bioengineering",
        "dept": "Bioengineering (BE)",
        "gre_row": "Bioengineering PhD R",
        "note": "Bioengineering graduate option in the Division of Biology and Biological Engineering (BBE) at Caltech."
    },
    "chemeng": {
        "url": "https://cce.caltech.edu/academics/graduate-studies/chemical-engineering",
        "dept": "Chemical Engineering (ChE)",
        "gre_row": "Chemical Engineering PhD R",
        "note": "Chemical Engineering graduate option in the Division of Chemistry and Chemical Engineering (CCE) at Caltech."
    },
    "chemistry": {
        "url": "https://cce.caltech.edu/academics/graduate-studies/chemistry",
        "dept": "Chemistry (CH)",
        "gre_row": "Chemistry PhD M",
        "note": "Chemistry graduate option in the Division of Chemistry and Chemical Engineering (CCE) at Caltech."
    },
    "civil": {
        "url": "https://mce.caltech.edu/academics/graduate/civil-engineering",
        "dept": "Civil Engineering (CE)",
        "gre_row": "Civil Engineering PhD R",
        "note": "Civil Engineering graduate option in the Department of Mechanical and Civil Engineering (MCE) at Caltech."
    },
    "ece": {
        "url": "https://www.ee.caltech.edu/academics/grad",
        "dept": "Electrical Engineering (EE)",
        "gre_row": "Electrical Engineering MS - PhD R",
        "note": "Electrical Engineering graduate option in the Department of Electrical Engineering at Caltech."
    },
    "environment": {
        "url": "https://ese.caltech.edu/academics/grad",
        "dept": "Environmental Science and Engineering (ESE)",
        "gre_row": "Environmental Science and Engineering PhD R",
        "note": "Environmental Science and Engineering graduate option at Caltech."
    },
    "materials": {
        "url": "https://www.aphms.caltech.edu/academics/grad",
        "dept": "Materials Science (MS)",
        "gre_row": "Materials Science PhD R",
        "note": "Materials Science graduate option in Applied Physics and Materials Science (APHMS) at Caltech."
    },
    "math": {
        "url": "https://www.pma.caltech.edu/academics/mathematics-graduate-studies",
        "dept": "Mathematics (MA)",
        "gre_row": "Mathematics PhD N",
        "note": "Mathematics graduate option in the Division of Physics, Mathematics and Astronomy (PMA) at Caltech."
    },
    "mech": {
        "url": "https://mce.caltech.edu/academics/graduate/mechanical-engineering",
        "dept": "Mechanical Engineering (ME)",
        "gre_row": "Mechanical Engineering PhD R",
        "note": "Mechanical Engineering graduate option in the Department of Mechanical and Civil Engineering (MCE) at Caltech."
    },
    "neuro": {
        "url": "https://www.bbe.caltech.edu/academics/neurobiology",
        "dept": "Neurobiology (NB); Computation and Neural Systems (CNS)",
        "gre_row": "Neurobiology PhD R",
        "note": "Neurobiology graduate option in the Division of Biology and Biological Engineering (BBE) at Caltech."
    },
    "earth": {
        "url": "https://www.gps.caltech.edu/academics/graduate-studies",
        "dept": "Geology (GE) and related geoscience options",
        "gre_row": "Geology PhD M",
        "note": "Geology and related geoscience graduate options in the Division of Geological and Planetary Sciences (GPS) at Caltech."
    }
}

staging_progs = ROOT / "data" / "staging" / "programs"
staging_unis = ROOT / "data" / "staging" / "universities"
staging_progs.mkdir(parents=True, exist_ok=True)
staging_unis.mkdir(parents=True, exist_ok=True)

# Copy university record to staging
shutil.copy(ROOT / "data" / "universities" / "caltech.json", staging_unis / "caltech.json")

# Stage 14 programs
header = "GRADUATE RECORD EXAM (GRE)"

for fld, info in CALTECH_PROGS.items():
    orig_path = ROOT / "data" / "programs" / f"caltech--{fld}.json"
    data = json.loads(orig_path.read_text(encoding="utf-8"))
    
    data["program_page"] = info["url"]
    data["department"] = info["dept"]
    data["notes"] = info["note"]
    
    # Fix gre_general quote to include header
    data["fields"]["gre_general"]["quote"] = f"{header}... {info['gre_row']}"
    
    out_file = staging_progs / f"caltech--{fld}.json"
    out_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {out_file.name}")
