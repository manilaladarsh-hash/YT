import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
STAGING_PROGS = ROOT / "data" / "staging" / "programs"
STAGING_PROGS.mkdir(parents=True, exist_ok=True)

def load_prog(name):
    return json.loads((ROOT / "data" / "programs" / name).read_text(encoding="utf-8"))

def save_prog(name, data):
    (STAGING_PROGS / name).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

# 1 & 2. minnesota--biomed.json (gre_general and gre_subject)
d = load_prog("minnesota--biomed.json")
mn_gre_q = (
    "Do you require the Graduate Record Examination (GRE)? | "
    "No. The GRE general and subject scores are NOT required to apply to the program. "
    "Note that the University's Graduate School application system still includes a spot "
    "for GRE scores; however, you are not required to enter them. Please be aware that "
    "our application review committee will NOT view these scores, even if you do submit them."
)
d["fields"]["gre_general"]["quote"] = mn_gre_q
d["fields"]["gre_subject"]["quote"] = mn_gre_q
save_prog("minnesota--biomed.json", d)

# 3. mit--environment.json (gre_general)
d = load_prog("mit--environment.json")
d["fields"]["gre_general"]["quote"] = (
    "Graduate Record Examination (GRE) – optional | General test is optional"
)
save_prog("mit--environment.json", d)

# 4. mit--neuro.json (gre_subject)
d = load_prog("mit--neuro.json")
d["fields"]["gre_subject"]["quote"] = (
    "BCS does not accept GRE scores and will not consider GRE scores in the evaluation "
    "of your application. Scores sent to MIT will not be reviewed during application review."
)
save_prog("mit--neuro.json", d)

# 5. mit--physics.json (gre_general)
d = load_prog("mit--physics.json")
d["fields"]["gre_general"]["quote"] = (
    "Graduate Record Examination (GRE) | General test and subject test are recommended "
    "but not required"
)
save_prog("mit--physics.json", d)

# 6. mizzou--biology.json (ielts_min)
d = load_prog("mizzou--biology.json")
d["fields"]["ielts_min"]["quote"] = (
    "Some academic programs require test scores that are higher than the minimum "
    "university requirements | IELTS Academic | Biological Sciences 7"
)
save_prog("mizzou--biology.json", d)

# 7. mizzou--biomed.json (ielts_min)
d = load_prog("mizzou--biomed.json")
d["fields"]["ielts_min"]["quote"] = (
    "Some academic programs require test scores that are higher than the minimum "
    "university requirements | IELTS Academic | Biomedical Sciences 7"
)
save_prog("mizzou--biomed.json", d)

# 8. montana--chemistry.json (funding)
d = load_prog("montana--chemistry.json")
d["fields"]["funding"]["quote"] = (
    "Students will typically serve as a Graduate Teaching Assistant (GTA) for 2-3 "
    "sections of a large, undergraduate chemistry or biochemistry class. | "
    "Any student who falls below the minimum 3.00 GPA may not receive financial "
    "support (i.e an appointment as a GTA) or a tuition waiver."
)
d["fields"]["funding"]["also"] = [
    {
        "quote": (
            "If accepted into the PhD program, support in the first year will be in "
            "the form of a Graduate Teaching Assistantship (GTA). The GTA position "
            "offers a biweekly stipend and a tuition waiver for the academic year."
        ),
        "url": "https://chemistry.montana.edu/graduate/Applying.html",
    }
]
save_prog("montana--chemistry.json", d)

# 9. montana--math.json (supervisor -> Not stated, inferred from silence)
d = load_prog("montana--math.json")
d["fields"]["supervisor"]["code"] = "Not stated"
d["fields"]["supervisor"]["value"] = "Not stated on the page checked"
d["fields"]["supervisor"]["quote"] = ""
save_prog("montana--math.json", d)

# 10. montana--physics.json (entry_route)
d = load_prog("montana--physics.json")
d["fields"]["entry_route"]["value"] = (
    "Admitted applicants must show proof of a bachelor's degree (and any "
    "post-bachelor's transcripts if applicable)."
)
d["fields"]["entry_route"]["quote"] = (
    "If you are admitted to the program and accept the offer, you must submit "
    "official transcripts showing proof of a bachelors degree, all post-bachelors "
    "transcripts, and any transcripts including 60 or more credits taken prior to "
    "the completion of a bachelors degree."
)
save_prog("montana--physics.json", d)

print("Staged 9 files for Batch 39")
