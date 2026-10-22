"""Build every customer-facing file from the verified program records.

Outputs (dist/):
  Physics-PhD-Atlas-2027/            the product folder that goes into the ZIP
    Atlas.html  Atlas.xlsx  Atlas.csv  Playbook.pdf  START-HERE.pdf  LICENSE.txt
  Physics-PhD-Atlas-2027-v<version>.zip
  Free-Sample-Physics-PhD-Atlas-2027.pdf

Usage: python3 product/build.py
Refuses to build if scripts/validate_data.py reports errors.
"""

import csv
import html
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
import zipfile
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from validate_data import validate  # noqa: E402

VERSION = "1.1"
PRODUCT = "Physics-PhD-Atlas-2027"
DIST = ROOT / "dist"
OUT = DIST / PRODUCT
CONTENT = ROOT / "product" / "content"
TEMPLATES = ROOT / "product" / "templates"
BUILD = ROOT / ".cache" / "build"
SAMPLE_IDS = ["rice", "pennstate", "stanford", "utaustin", "utoronto", "waterloo", "ualberta", "ubc", "cambridge", "epfl"]
NORTH_AMERICA = {"USA", "Canada"}
CURRENCIES = ["USD", "CAD", "GBP", "EUR", "CHF"]
PRICE_LINE = ("Priced for students: about ₹190 in India (Gumroad shows rupees and accepts UPI), $5 elsewhere. "
              "A batch licence covers up to 30 students for about ₹750. Can't afford it? Reply to your receipt for a free copy.")

FX = json.loads((ROOT / "data" / "fx.json").read_text())


def convert(amount, cur, to):
    rates = FX["cad_per_unit"]
    if amount is None or cur not in rates or to not in rates:
        return None
    return amount * rates[cur] / rates[to]


def fmt_inr(amount):
    """Rupees rounded to the nearest 100, with Indian digit grouping (₹1,23,400)."""
    n = int(round(amount, -2))
    head, tail = str(n)[:-3], str(n)[-3:]
    groups = []
    while len(head) > 2:
        groups.insert(0, head[-2:])
        head = head[:-2]
    if head:
        groups.insert(0, head)
    return "₹" + ",".join(groups + [tail]) if groups else "₹" + tail


FIELD_LABELS = {
    "deadline": "Deadline (2027 entry)",
    "app_fee": "Application fee",
    "fee_waiver": "Intl fee waiver",
    "gre_general": "GRE General",
    "gre_physics": "Physics GRE",
    "toefl_min": "TOEFL minimum",
    "english_waiver": "English-test waiver (English-medium degree)",
    "supervisor": "Supervisor before admission",
    "funding": "PhD funding",
    "entry_route": "Entry route",
}
SHORT = {
    "utoronto": "Toronto", "ubc": "UBC", "mcgill": "McGill", "mcmaster": "McMaster", "waterloo": "Waterloo",
    "ualberta": "Alberta", "calgary": "Calgary", "queens": "Queen's", "sfu": "SFU", "uottawa": "Ottawa",
    "uiuc": "UIUC", "wisconsin": "UW-Madison", "utaustin": "UT Austin", "purdue": "Purdue", "ohiostate": "Ohio State",
    "maryland": "Maryland", "stonybrook": "Stony Brook", "berkeley": "Berkeley", "uchicago": "UChicago",
    "rice": "Rice", "minnesota": "Minnesota", "stanford": "Stanford", "caltech": "Caltech", "columbia": "Columbia",
    "cornell": "Cornell", "pennstate": "Penn State", "rutgers": "Rutgers", "tamu": "Texas A&M", "ucsb": "UCSB",
    "georgiatech": "Georgia Tech", "bostonu": "Boston University",
    "cambridge": "Cambridge", "edinburgh": "Edinburgh", "epfl": "EPFL", "ethz": "ETH Zurich", "heidelberg": "Heidelberg (HGSFP)",
    "munich-mcqst": "Munich (MCQST)", "bonn-cologne": "Bonn-Cologne (BCGS)", "sissa-cm": "SISSA", "leiden": "Leiden",
    "bristol": "Bristol", "durham": "Durham", "imperial": "Imperial College London",
    "imprs-solar": "IMPRS Solar System (Göttingen)", "imprs-qd": "IMPRS Quantum Dynamics (Heidelberg)",
    "imprs-cpqm": "IMPRS Quantum Materials (Dresden)", "imprs-hd": "IMPRS Astronomy (Heidelberg)",
    "uzh": "Zurich (UZH)", "tum": "TU Munich", "tcd-physics": "Trinity College Dublin", "icfo-phd": "ICFO (Barcelona)",
    "paris-saclay-physics": "Paris-Saclay", "padova-physics": "Padova", "nbi-copenhagen": "Copenhagen (NBI)",
    "stockholm": "Stockholm", "kth": "KTH Stockholm", "chalmers": "Chalmers", "uppsala": "Uppsala",
    "uva": "Amsterdam (UvA)", "tudelft": "TU Delft", "aalto": "Aalto",
    "arizona": "Arizona", "brown": "Brown", "cuboulder": "CU Boulder", "duke": "Duke", "harvard": "Harvard",
    "iub": "Indiana (Bloomington)", "jhu": "Johns Hopkins", "mit": "MIT", "msu": "Michigan State", "ncsu": "NC State",
    "notredame": "Notre Dame", "pitt": "Pittsburgh", "rochester": "Rochester", "uci": "UC Irvine", "ucla": "UCLA",
    "upenn": "Penn (UPenn)", "utah": "Utah", "uwashington": "U Washington (Seattle)", "vanderbilt": "Vanderbilt",
    "virginia": "Virginia (UVA)", "yale": "Yale", "ucsd": "UC San Diego", "ucdavis": "UC Davis", "asu": "Arizona State",
    "princeton": "Princeton", "umass": "UMass Amherst", "northeastern": "Northeastern", "buffalo": "Buffalo",
    "carleton": "Carleton", "dalhousie": "Dalhousie", "guelph": "Guelph", "umanitoba": "Manitoba", "usask": "Saskatchewan",
    "western": "Western", "yorku": "York", "laval": "Laval", "umontreal": "Montréal", "concordia": "Concordia",
    "uvic": "Victoria", "mun": "Memorial (Newfoundland)",
}


def area(r):
    return "North America" if r["country"] in NORTH_AMERICA else "Europe"


# ---------------------------------------------------------------- data

def load():
    recs = [json.loads(p.read_text()) for p in sorted((ROOT / "data" / "programs").glob("*.json"))]
    return sorted(recs, key=lambda r: r["institution"])


def short(r):
    return SHORT.get(r["id"], r["institution"])


def names(recs, pred):
    chosen = [short(r) for r in recs if pred(r)]
    return ", ".join(chosen) if chosen else "none in this edition"


def fee_parts(code):
    m = re.match(r"^(\d+(?:\.\d+)?) (USD|CAD|GBP|EUR|CHF|SEK|DKK|NOK)$", code)
    if m:
        return float(m.group(1)), m.group(2)
    if code.startswith("0"):
        return 0.0, ""
    return None, ""


def deadline_cell(r):
    code = r["fields"]["deadline"]["code"]
    return date.fromisoformat(code) if re.match(r"^\d{4}-\d{2}-\d{2}$", code) else None


def flags_text(f):
    out = []
    if f.get("inferred"):
        out.append("year inferred")
    if f.get("rolling"):
        out.append("rolling")
    if f.get("conflict"):
        out.append("sources conflict")
    if f.get("time_sensitive"):
        out.append(f"act by {f['time_sensitive']}")
    if f.get("scope"):
        out.append(f["scope"])
    return "; ".join(out)


def deadline_text(r):
    code = r["fields"]["deadline"]["code"]
    d = deadline_cell(r)
    return d.strftime("%b %d, %Y") if d else code


def stats(recs):
    checked = max(r["checked"] for r in recs)
    fees = {c: [fee_parts(r["fields"]["app_fee"]["code"])[0] for r in recs if r["fields"]["app_fee"]["code"].endswith(" " + c)]
            for c in CURRENCIES}
    dated = sorted((r["fields"]["deadline"]["code"], short(r)) for r in recs if deadline_cell(r))
    first = dated[:4]
    fw = lambda code: (lambda r: r["fields"]["fee_waiver"]["code"] == code)
    eu = [r for r in recs if area(r) == "Europe"]
    code = lambda r, f: r["fields"][f]["code"]
    by_deadline = sorted(recs, key=lambda r: r["fields"]["deadline"]["code"] if deadline_cell(r) else "9" + r["fields"]["deadline"]["code"])
    return {
        "VERSION": VERSION,
        "CHECKED": date.fromisoformat(checked).strftime("%B %d, %Y").replace(" 0", " "),
        "N": str(len(recs)),
        "N_US": str(sum(r["country"] == "USA" for r in recs)),
        "N_CA": str(sum(r["country"] == "Canada" for r in recs)),
        "N_EU": str(len(eu)),
        "EU_COUNTRIES": ", ".join(sorted({r["country"] for r in eu})),
        "MEDIAN_USD": f"{statistics.median(fees['USD']):.0f}" if fees["USD"] else "n/a",
        "MEDIAN_CAD": f"{statistics.median(fees['CAD']):.0f}" if fees["CAD"] else "n/a",
        "MEDIAN_USD_INR": fmt_inr(convert(statistics.median(fees["USD"]), "USD", "INR")) if fees["USD"] else "n/a",
        "MEDIAN_CAD_INR": fmt_inr(convert(statistics.median(fees["CAD"]), "CAD", "INR")) if fees["CAD"] else "n/a",
        "TEN_US_INR": fmt_inr(10 * convert(statistics.median(fees["USD"]), "USD", "INR")) if fees["USD"] else "n/a",
        "FX_DATE": date.fromisoformat(FX["date"]).strftime("%B %d, %Y").replace(" 0", " "),
        "USD_INR": f"{FX['cad_per_unit']['USD'] / FX['cad_per_unit']['INR']:.1f}",
        "RICE_WAIVER_DATE": "Nov 1, 2026",
        "US_DEC15_COUNT": str(sum(r["country"] == "USA" and code(r, "deadline") == "2026-12-15" for r in recs)),
        "US_DATED_COUNT": str(sum(r["country"] == "USA" and deadline_cell(r) is not None for r in recs)),
        "US_DEC1_LIST": names(recs, lambda r: r["country"] == "USA" and code(r, "deadline") <= "2026-12-03" and deadline_cell(r) is not None),
        "CA_JAN_LIST": names(recs, lambda r: r["country"] == "Canada" and code(r, "deadline").startswith("2027-01")),
        "CA_LATE_LIST": names(recs, lambda r: r["country"] == "Canada" and (code(r, "deadline") >= "2027-02" or code(r, "deadline") == "Rolling")),
        "EARLIEST_DEADLINES": "; ".join(f"{date.fromisoformat(d).strftime('%b %d')}: {n}" for d, n in first),
        "PGRE_REQUIRED_LIST": "\n".join(
            f"- **{short(r)}**: {r['fields']['gre_physics']['value']}" for r in recs if code(r, "gre_physics") == "Required"
        ),
        "PGRE_REQUIRED_NAMES": ", ".join(
            short(r) + (f" ({r['fields']['gre_physics']['scope']})" if r["fields"]["gre_physics"].get("scope") else "")
            for r in recs if code(r, "gre_physics") == "Required"
        ),
        "GRE_NONE_LIST": names(recs, lambda r: code(r, "gre_physics") == "Not considered" and code(r, "gre_general") == "Not considered"),
        "GENERAL_IGNORED_LIST": names(recs, lambda r: code(r, "gre_general") == "Not considered" and code(r, "gre_physics") != "Not considered"),
        "ENGLISH_YES_LIST": names(recs, lambda r: code(r, "english_waiver") == "Yes"),
        "ENGLISH_CONDITIONAL_LIST": names(recs, lambda r: code(r, "english_waiver") == "Conditional"),
        "ENGLISH_NO_LIST": names(recs, lambda r: code(r, "english_waiver") == "No"),
        "FREE_LIST": names(recs, lambda r: code(r, "app_fee") == "0 (waived)"),
        "NO_FEE_LIST": names(recs, lambda r: code(r, "app_fee") == "0 (no fee)"),
        "INTL_WAIVER_LIST": names(recs, lambda r: fw("Available")(r) and not code(r, "app_fee").startswith("0")),
        "LIMITED_LIST": names(recs, fw("Limited")),
        "DOMESTIC_ONLY_LIST": names(recs, fw("Domestic only")),
        "NO_WAIVER_LIST": names(recs, fw("None")),
        "MASTERS_FIRST_LIST": names(recs, lambda r: r["country"] == "Canada" and code(r, "entry_route") == "Master's usually required"),
        "EITHER_LIST": names(recs, lambda r: r["country"] == "Canada" and code(r, "entry_route") in ("Either", "Direct from bachelor's")),
        "EU_POSITION_LIST": names(eu, lambda r: code(r, "deadline") in ("Per position", "Rolling") or code(r, "supervisor") == "Required"),
        "EU_SCHOOL_LIST": names(eu, lambda r: deadline_cell(r) is not None or code(r, "deadline") == "Not stated" and code(r, "supervisor") != "Required"),
        "EU_MASTERS_LIST": names(eu, lambda r: code(r, "entry_route") == "Master's usually required"),
        "EU_BACHELORS_LIST": names(eu, lambda r: code(r, "entry_route") in ("Direct from bachelor's", "Either")),
        "EU_FUNDED_LIST": names(eu, lambda r: code(r, "funding") in ("Guaranteed", "Typical")),
        "EU_COMPETITIVE_LIST": names(eu, lambda r: code(r, "funding") == "Competitive"),
        "DEADLINE_TABLE": md_table(
            ["Deadline", "Program", "Country", "Note"],
            [[deadline_text(r), short(r), r["country"], flags_text(r["fields"]["deadline"]) or ""] for r in by_deadline],
        ),
        "SUPERVISOR_TABLE": md_table(
            ["Program", "Supervisor before admission", "What the page says"],
            [[short(r), code(r, "supervisor"), r["fields"]["supervisor"]["value"]] for r in recs if r["country"] == "Canada"],
        ),
        "EU_TABLE": md_table(
            ["Program", "Country", "Deadline", "Supervisor first?", "Funding", "Entry", "Fee"],
            [[short(r), r["country"], deadline_text(r), code(r, "supervisor"), code(r, "funding"), code(r, "entry_route"),
              code(r, "app_fee")] for r in sorted(eu, key=lambda r: (r["country"], short(r)))],
        ),
    }


def md_table(head, rows):
    esc = lambda s: str(s).replace("|", "/")
    lines = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    lines += ["| " + " | ".join(esc(c) for c in row) + " |" for row in rows]
    return "\n".join(lines)


def fill(text, values):
    def rep(m):
        key = m.group(1)
        if key not in values:
            raise KeyError(f"unfilled placeholder {key}")
        return values[key]
    return re.sub(r"\{\{([A-Z_]+)\}\}", rep, text)


# ---------------------------------------------------------------- outputs

def write_csv(recs, path):
    head = ["Institution", "Department", "Country", "Region"]
    for k, lab in FIELD_LABELS.items():
        head += [lab, f"{lab} - detail", f"{lab} - source"]
    head += ["Notes", "Admissions page", "Checked"]
    with path.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(head)
        for r in recs:
            row = [r["institution"], r["department"], r["country"], r["region"]]
            for k in FIELD_LABELS:
                f = r["fields"][k]
                detail = f["value"] + (f" [{flags_text(f)}]" if flags_text(f) else "")
                row += [f["code"], detail, f["url"]]
            row += [r["notes"], r["program_page"], r["checked"]]
            w.writerow(row)


HEADER_FILL = PatternFill("solid", fgColor="1F5F8B")
HEADER_FONT = Font(bold=True, color="FFFFFF")
INPUT_FILL = PatternFill("solid", fgColor="FFF7D6")


def style_header(ws, widths):
    for i, wdt in enumerate(widths, start=1):
        c = ws.cell(row=1, column=i)
        c.fill, c.font = HEADER_FILL, HEADER_FONT
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.column_dimensions[get_column_letter(i)].width = wdt
    ws.freeze_panes = "B2"


def write_xlsx(recs, path, values):
    wb = Workbook()
    st = wb.active
    st.title = "Start"
    lines = [
        ("Physics PhD Atlas 2027: planner workbook", True),
        (f"Version {VERSION} · {values['N']} programs · data checked {values['CHECKED']}", False),
        ("", False),
        ("1. Programs: every program with deadline, fee, waivers, tests, supervisor rule and funding. Filter with the header arrows.", False),
        ("2. Shortlist: choose a program from the drop-down in column A; the other columns fill in automatically. Yellow cells are yours to edit.", False),
        ("3. Budget: totals your shortlisted application fees by currency. Add score-sending and transcript costs from the official sites, and today's exchange rates.", False),
        ("4. Recommenders and Supervisor outreach: track requests; follow-up dates calculate themselves.", False),
        ("5. Sources: the exact official sentence and link behind every value.", False),
        ("", False),
        ("'Not stated' = the official pages checked did not say (not a 'no'). Always confirm on the official page before paying or submitting.", False),
        ("Not affiliated with any university. Not immigration, visa or legal advice.", False),
    ]
    for i, (txt, bold) in enumerate(lines, start=1):
        c = st.cell(row=i, column=1, value=txt)
        c.font = Font(bold=bold, size=14 if bold else 11)
    st.column_dimensions["A"].width = 120

    # Programs
    ws = wb.create_sheet("Programs")
    head = ["Program", "Institution and department", "Country", "Region", "Deadline", "Deadline note", "Fee amount", "Fee currency",
            "Intl fee waiver", "Fee waiver detail", "GRE General", "Physics GRE", "TOEFL minimum", "English waiver",
            "English detail", "Supervisor", "Supervisor detail", "Funding", "Funding detail", "Entry route",
            "Notes", "Admissions page", "Checked"]
    ws.append(head)
    for r in recs:
        F = r["fields"]
        amount, cur = fee_parts(F["app_fee"]["code"])
        dl = deadline_cell(r)
        ws.append([
            short(r), f"{r['institution']} · {r['department']}", r["country"], r["region"],
            dl if dl else F["deadline"]["code"], F["deadline"]["value"],
            amount if amount is not None else "Not stated", cur,
            F["fee_waiver"]["code"], F["fee_waiver"]["value"], F["gre_general"]["code"], F["gre_physics"]["code"],
            F["toefl_min"]["code"], F["english_waiver"]["code"], F["english_waiver"]["value"],
            F["supervisor"]["code"], F["supervisor"]["value"], F["funding"]["code"], F["funding"]["value"],
            F["entry_route"]["code"], r["notes"], r["program_page"], r["checked"],
        ])
        row = ws.max_row
        if dl:
            ws.cell(row=row, column=5).number_format = "yyyy-mm-dd"
        link = ws.cell(row=row, column=22)
        link.hyperlink = r["program_page"]
        link.font = Font(color="1F5F8B", underline="single")
    style_header(ws, [34, 26, 9, 16, 12, 40, 10, 9, 14, 40, 13, 13, 12, 13, 40, 14, 40, 12, 40, 18, 40, 40, 11])
    ws.auto_filter.ref = f"A1:{get_column_letter(len(head))}{ws.max_row}"
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    last = ws.max_row

    # Shortlist
    sl = wb.create_sheet("Shortlist")
    sl_head = ["Program (choose)", "Country", "Deadline", "Days left", "Fee", "Currency", "Intl fee waiver",
               "Physics GRE", "English waiver", "Supervisor", "Status", "SOP ready", "Letters confirmed",
               "Fee paid / waiver", "My notes"]
    sl.append(sl_head)
    rng = f"Programs!$A$2:$A${last}"

    def look(col, r):
        return f'=IF($A{r}="","",INDEX(Programs!${col}$2:${col}${last},MATCH($A{r},{rng},0)))'

    for r in range(2, 32):
        sl[f"A{r}"].fill = INPUT_FILL
        sl[f"B{r}"] = look("C", r)
        sl[f"C{r}"] = look("E", r)
        sl[f"C{r}"].number_format = "yyyy-mm-dd"
        sl[f"D{r}"] = f'=IF(ISNUMBER(C{r}),C{r}-TODAY(),"")'
        sl[f"E{r}"] = look("G", r)
        sl[f"F{r}"] = look("H", r)
        sl[f"G{r}"] = look("I", r)
        sl[f"H{r}"] = look("L", r)
        sl[f"I{r}"] = look("N", r)
        sl[f"J{r}"] = look("P", r)
        for col in "KLMNO":
            sl[f"{col}{r}"].fill = INPUT_FILL
    dv_prog = DataValidation(type="list", formula1=rng, allow_blank=True)
    dv_status = DataValidation(type="list", formula1='"Researching,Emailed supervisor,Writing,Submitted,Interview,Offer,Declined,Accepted"', allow_blank=True)
    dv_yes = DataValidation(type="list", formula1='"Yes,No"', allow_blank=True)
    dv_letters = DataValidation(type="list", formula1='"0,1,2,3"', allow_blank=True)
    dv_fee = DataValidation(type="list", formula1='"Not yet,Waiver requested,Waived,Paid"', allow_blank=True)
    for dv, ref in [(dv_prog, "A2:A31"), (dv_status, "K2:K31"), (dv_yes, "L2:L31"), (dv_letters, "M2:M31"), (dv_fee, "N2:N31")]:
        sl.add_data_validation(dv)
        dv.add(ref)
    style_header(sl, [36, 9, 12, 9, 8, 9, 14, 13, 14, 14, 18, 9, 9, 16, 40])

    # Budget: one column per currency, totals converted with rates the owner types in
    bd = wb.create_sheet("Budget")
    bd.column_dimensions["A"].width = 58
    cols = "BCDEF"
    for col in cols + "G":
        bd.column_dimensions[col].width = 13
    bd.column_dimensions["G"].width = 40
    bd.append(["Item"] + CURRENCIES + ["Notes"])
    fee_row = ["Application fees on your shortlist (excludes rows marked Waived)"]
    for cur in CURRENCIES:
        fee_row.append(f'=SUMIFS(Shortlist!$E$2:$E$31,Shortlist!$F$2:$F$31,"{cur}",Shortlist!$N$2:$N$31,"<>Waived")')
    bd.append(fee_row + ["Calculated"])
    for item, note in [("English test (booking + extra score reports)", "Enter from the official test website"),
                       ("GRE / Physics GRE (booking + score reports)", "Enter only if a program on your list needs it"),
                       ("Transcripts, credential evaluation, courier", "Enter from your university / evaluator"),
                       ("Other", "")]:
        bd.append([item] + [None] * len(CURRENCIES) + [note])
    bd.append(["Total"] + [f"=SUM({c}2:{c}6)" for c in cols] + [""])
    bd.append([])
    inr = FX["cad_per_unit"]["INR"]
    bd.append([f"Rupees per 1 unit (Bank of Canada, {FX['date']}): edit to today's rate, or your own currency"]
              + [round(FX["cad_per_unit"][c] / inr, 2) for c in CURRENCIES] + ["Pre-filled; banks and cards add a margin"])
    conv = "+".join(f'IF({c}9="",0,{c}7*{c}9)' for c in cols)
    bd.append(["Total in rupees (approximate)", f"={conv}"] + [None] * (len(CURRENCIES) - 1) + ["Currencies without a rate are left out"])
    bd["B10"].number_format = "#,##0"
    for c in bd[1]:
        c.fill, c.font = HEADER_FILL, HEADER_FONT
    for r in range(3, 7):
        for col in cols:
            bd[f"{col}{r}"].fill = INPUT_FILL
    for col in cols:
        bd[f"{col}9"].fill = INPUT_FILL
    bd["A7"].font = Font(bold=True)
    bd["A10"].font = Font(bold=True)

    # Recommenders
    rc = wb.create_sheet("Recommenders")
    rc.append(["Recommender", "Email", "Relationship", "Asked on", "Packet sent", "Programs invited", "Status", "Follow up by"])
    for r in range(2, 9):
        rc[f"H{r}"] = f'=IF(D{r}="","",D{r}+14)'
        rc[f"D{r}"].number_format = rc[f"H{r}"].number_format = "yyyy-mm-dd"
        for col in "ABCDEFG":
            rc[f"{col}{r}"].fill = INPUT_FILL
    dv_rs = DataValidation(type="list", formula1='"Not asked,Agreed,Invited,Submitted some,All submitted"', allow_blank=True)
    rc.add_data_validation(dv_rs)
    dv_rs.add("G2:G8")
    style_header(rc, [24, 28, 18, 12, 11, 36, 16, 12])

    # Supervisor outreach
    so = wb.create_sheet("Supervisor outreach")
    so.append(["Professor", "University", "Group / topic", "Paper you read", "Emailed on", "Follow up on", "Reply", "Next step"])
    for r in range(2, 31):
        so[f"F{r}"] = f'=IF(E{r}="","",E{r}+10)'
        so[f"E{r}"].number_format = so[f"F{r}"].number_format = "yyyy-mm-dd"
        for col in "ABCDEGH":
            so[f"{col}{r}"].fill = INPUT_FILL
    dv_rep = DataValidation(type="list", formula1='"No reply yet,Positive,Apply and mention me,Not taking students,Other"', allow_blank=True)
    so.add_data_validation(dv_rep)
    dv_rep.add("G2:G30")
    style_header(so, [22, 22, 26, 34, 12, 12, 20, 30])

    # Sources
    src = wb.create_sheet("Sources")
    src.append(["Program", "Field", "Code", "Value", "Official quote", "Source URL", "Flags", "Checked"])
    for r in recs:
        for k, lab in FIELD_LABELS.items():
            f = r["fields"][k]
            quote = f["quote"] + "".join(f"  ||  {a['quote']} ({a['url']})" for a in f.get("also", []))
            src.append([r["institution"], lab, f["code"], f["value"], quote or "(no statement found)", f["url"], flags_text(f), r["checked"]])
    style_header(src, [30, 22, 14, 40, 70, 40, 18, 11])
    src.auto_filter.ref = f"A1:H{src.max_row}"
    for row in src.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")

    wb.save(path)


def write_explorer(recs, path, values):
    tpl = (TEMPLATES / "atlas.html").read_text()
    progs = []
    for r in recs:
        amount, cur = fee_parts(r["fields"]["app_fee"]["code"])
        usd, inr = (convert(amount, cur, "USD"), convert(amount, cur, "INR")) if cur else (None, None)
        progs.append({**r, "short": short(r),
                      "fee_usd": round(usd) if usd is not None else (0 if amount == 0 else None),
                      "fee_inr": round(inr, -2) if inr is not None else (0 if amount == 0 else None)})
    fx = {"date": FX["date"], "source": FX["source"], "usd_inr": round(FX["cad_per_unit"]["USD"] / FX["cad_per_unit"]["INR"], 2)}
    payload = {"version": VERSION, "checked": max(r["checked"] for r in recs), "fx": fx, "programs": progs}
    data = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    marker = "/*__ATLAS_DATA__*/null"
    if marker not in tpl:
        raise RuntimeError("explorer template marker missing")
    path.write_text(tpl.replace(marker, data, 1), encoding="utf-8")


def node_env():
    env = dict(os.environ)
    env["NODE_PATH"] = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    return env


def html_doc(title, body_html):
    css = (TEMPLATES / "doc.css").read_text()
    return f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>{html.escape(title)}</title><style>{css}</style></head><body>{body_html}</body></html>"


def md_to_html(md):
    out = subprocess.run(["pandoc", "-f", "gfm+yaml_metadata_block", "-t", "html5"], input=md, capture_output=True, text=True, check=True)
    return out.stdout


def to_pdf(html_text, pdf_path, name):
    BUILD.mkdir(parents=True, exist_ok=True)
    src = BUILD / f"{name}.html"
    src.write_text(html_text, encoding="utf-8")
    subprocess.run(["node", str(ROOT / "product" / "pdf.cjs"), str(src), str(pdf_path)], check=True, env=node_env())


def write_sample(recs, path, values):
    chosen = [r for r in recs if r["id"] in SAMPLE_IDS]
    rows = []
    for r in chosen:
        F = r["fields"]
        cells = [
            f"<b>{html.escape(short(r))}</b><br><span class='note'>{html.escape(r['country'])}</span>",
            html.escape(deadline_text(r)),
            html.escape(F["app_fee"]["code"]),
            html.escape(F["fee_waiver"]["value"]),
            html.escape(F["gre_physics"]["code"]),
            html.escape(F["english_waiver"]["value"]),
            html.escape(F["supervisor"]["code"]),
        ]
        rows.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
    table = ("<table><tr><th>Program</th><th>Deadline</th><th>Fee</th><th>Fee waiver (internationals)</th>"
             "<th>Physics GRE</th><th>English-test waiver</th><th>Supervisor first?</th></tr>" + "".join(rows) + "</table>")
    body = f"""
<div class="cover" style="padding-top:6mm"><span class="tag">FREE SAMPLE · {values['CHECKED']}</span>
<h1>Physics PhD Atlas 2027</h1>
<p><b>{len(chosen)} of {values['N']} programs</b> from the full Atlas for international physics applicants (US, Canada and Europe), with every value copied from the program's own official page.</p></div>
<h2>Six things international physics applicants miss this cycle</h2>
<ol>
<li><b>The Physics GRE is back at some top programs.</b> In the full Atlas, it's required this cycle at {html.escape(values['PGRE_REQUIRED_NAMES'])}.</li>
<li><b>Some fees are free right now.</b> Penn State waives its fee for everyone with code PHYS2027. Rice runs a worldwide fee-waiver window until {values['RICE_WAIVER_DATE']}.</li>
<li><b>"My degree was in English" isn't always enough.</b> Waterloo rejects medium-of-instruction letters. Alberta's exemption list includes the IITs and IISc but not the IISERs. UT Austin exempts applicants from India outright.</li>
<li><b>TOEFL changed scales on Jan 21, 2026.</b> Programs now list two minimums (e.g., UBC: 90 old scale / 4.5 new scale).</li>
<li><b>Canada often admits supervisor-first.</b> Waterloo requires a supervisor match, Ottawa wants a supervisor's name at application, and Calgary admits only if a supervisor will fund you.</li>
<li><b>Europe runs on different rules.</b> EPFL charges no application fee; Cambridge charges £20 per year for up to 7 doctoral applications; Heidelberg's physics graduate-school portal closes Nov 1; at ETH Zurich and Leiden you apply to a professor or an advertised paid position instead of a central committee.</li>
</ol>
<h2>Sample: {len(chosen)} programs</h2>
{table}
<p class="note">Deadline years are inferred where a page gives only a day and month. Confirm every value on the official page before paying or submitting.</p>
<h2>The full kit</h2>
<ul>
<li><b>Offline explorer</b> for all {values['N']} programs: filter by Physics GRE, English waiver, fee waivers and supervisor rules, and tap any value to see the official quote.</li>
<li><b>Planner workbook</b>: auto-filling shortlist, deadline countdown, fee budget, recommender and supervisor-outreach trackers.</li>
<li><b>Playbook</b>: timeline, English-test rules, GRE decisions, Canadian supervisor emails, how Europe differs, physics SOP framework, letter kit, ethical fee-waiver requests.</li>
<li>Free updates for the Fall 2027 cycle. 14-day refund.</li>
</ul>
<p><b>{PRICE_LINE}</b></p>
<p class="note">Not affiliated with any university. Not immigration, visa or legal advice.</p>
"""
    to_pdf(html_doc("Physics PhD Atlas 2027: Free Sample", body), path, "sample")


def build():
    errors, warnings, n = validate()
    if errors:
        print("\n".join(errors))
        raise SystemExit("data validation failed; not building")
    recs = load()
    labels = [short(r) for r in recs]
    dupes = {x for x in labels if labels.count(x) > 1}
    if dupes:
        raise SystemExit(f"program labels must be unique (add SHORT names): {sorted(dupes)}")
    values = stats(recs)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    write_csv(recs, OUT / "Atlas.csv")
    write_xlsx(recs, OUT / "Atlas.xlsx", values)
    write_explorer(recs, OUT / "Atlas.html", values)

    playbook_md = fill((CONTENT / "playbook.md").read_text(), values)
    body = md_to_html(playbook_md)
    body = body.replace("<h1", "<div class='cover'><span class='tag'>Version " + VERSION + "</span></div><h1", 1)
    to_pdf(html_doc("Physics PhD Atlas 2027: Playbook", body), OUT / "Playbook.pdf", "playbook")

    start_md = fill((CONTENT / "start-here.md").read_text(), values)
    to_pdf(html_doc("Start here", md_to_html(start_md)), OUT / "START-HERE.pdf", "start-here")
    shutil.copy(CONTENT / "LICENSE.txt", OUT / "LICENSE.txt")

    write_sample(recs, DIST / f"Free-Sample-{PRODUCT}.pdf", values)

    zpath = DIST / f"{PRODUCT}-v{VERSION}.zip"
    if zpath.exists():
        zpath.unlink()
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(OUT.iterdir()):
            z.write(f, f"{PRODUCT}/{f.name}")
    print(f"built {zpath.relative_to(ROOT)} with {len(recs)} programs; warnings: {len(warnings)}")
    return zpath


if __name__ == "__main__":
    build()
