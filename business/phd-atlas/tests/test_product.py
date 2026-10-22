"""End-to-end checks of the built kit: data integrity, every customer file,
the offline explorer in a real browser, and the workbook formulas recalculated
by LibreOffice. Run after `python3 product/build.py`:

    python3 -m pytest -q tests
"""

import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import pytest
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "product"))

import build  # noqa: E402
from validate_data import validate  # noqa: E402

OUT = build.OUT
ZIP = build.DIST / f"{build.PRODUCT}-v{build.VERSION}.zip"
RECS = build.load()


def node_env():
    env = dict(os.environ)
    env["NODE_PATH"] = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    return env


def test_data_validates():
    errors, warnings, n = validate()
    assert errors == []
    assert n >= 30


def test_saved_page_import_rejects_bot_check_pages(tmp_path):
    bad = tmp_path / "blocked.html"
    bad.write_text("<html><body>Performing security verification</body></html>")
    res = subprocess.run([sys.executable, str(ROOT / "scripts" / "import_saved_page.py"),
                          "https://example.org/blocked", str(bad)], capture_output=True, text=True)
    assert res.returncode != 0 and "bot check" in res.stderr


def test_every_known_value_has_a_quote_and_https_source():
    for r in RECS:
        for name, f in r["fields"].items():
            assert f["url"].startswith("https://"), (r["id"], name)
            if f["code"] not in ("Not stated", "Check tool"):
                assert f["quote"].strip(), (r["id"], name)


def test_zip_contains_exactly_the_product_files():
    with zipfile.ZipFile(ZIP) as z:
        names = sorted(z.namelist())
    expected = sorted(f"{build.PRODUCT}/{n}" for n in
                      ["Atlas.csv", "Atlas.html", "Atlas.xlsx", "LICENSE.txt", "Playbook.pdf", "START-HERE.pdf"])
    assert names == expected


def test_csv_has_one_row_per_program():
    with (OUT / "Atlas.csv").open(encoding="utf-8-sig") as fh:
        rows = list(csv.reader(fh))
    assert len(rows) == len(RECS) + 1
    assert rows[0][0] == "Institution"


def pdf_text(path):
    return subprocess.run(["pdftotext", str(path), "-"], capture_output=True, text=True, check=True).stdout


def test_playbook_has_all_sections_and_no_unfilled_placeholders():
    text = pdf_text(OUT / "Playbook.pdf")
    for heading in ["1. Start here", "2. Your remaining timeline", "4. English tests in 2026", "5. GRE and Physics GRE",
                    "6. The UK", "7. The rest of Europe", "8. Australia and New Zealand", "9. Canada",
                    "10. Supervisor emails", "11. Statement of purpose", "12. Recommendation letters", "13. Fee waivers",
                    "14. Submission checklist", "16. How this data was built"]:
        assert heading in text, heading
    assert "{{" not in text and "}}" not in text
    assert f"Version {build.VERSION}" in text
    for subsection in ["Max Planck Schools (Germany)", "Marie Skłodowska-Curie Doctoral Networks", "Study permits in 2026"]:
        assert subsection in text, subsection


def test_start_here_and_sample_render():
    start = pdf_text(OUT / "START-HERE.pdf")
    assert "Your first 15 minutes" in start
    # Gumroad can't email buyers until the seller's first payout, so updates must not be promised by email.
    assert "always serves the newest version" in start and "Gumroad emails you" not in start
    sample = pdf_text(build.DIST / f"Free-Sample-{build.PRODUCT}.pdf")
    assert "FREE SAMPLE" in sample and "Penn State" in sample
    assert ("Get the full Atlas" in sample) == bool(build.PAID_URL)


@pytest.fixture(scope="module")
def explorer():
    res = subprocess.run(["node", str(ROOT / "tests" / "explorer_check.cjs"), str(OUT / "Atlas.html")],
                         capture_output=True, text=True, env=node_env(), timeout=180)
    assert res.returncode == 0, res.stderr
    return json.loads(res.stdout)


def test_customer_journey_from_downloaded_zip():
    """Unzip the delivered file elsewhere and use it the way a buyer would."""
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(ZIP) as z:
            z.extractall(tmp)
        folder = Path(tmp) / build.PRODUCT
        assert "Your first 15 minutes" in pdf_text(folder / "START-HERE.pdf")
        res = subprocess.run(["node", str(ROOT / "tests" / "explorer_check.cjs"), str(folder / "Atlas.html")],
                             capture_output=True, text=True, env=node_env(), timeout=180)
        assert res.returncode == 0, res.stderr
        out = json.loads(res.stdout)
        assert out["errors"] == [] and out["requests"] == [] and out["total"] == len(RECS)
        wb = load_workbook(folder / "Atlas.xlsx")
        assert wb["Programs"].max_row == len(RECS) + 1


def test_explorer_loads_offline_without_errors(explorer):
    assert explorer["errors"] == []
    assert explorer["requests"] == [], "explorer tried to reach the network"
    assert explorer["total"] == len(RECS)


def test_explorer_filters_match_the_data(explorer):
    assert explorer["canada"] == sum(r["country"] == "Canada" for r in RECS)
    assert explorer["europe"] == sum(build.area(r) == "Europe" for r in RECS) > 0
    assert explorer["countryOptions"] == len({r["country"] for r in RECS}) + 1
    assert explorer["pgreRequired"] == sum(r["fields"]["gre_physics"]["code"] == "Required" for r in RECS)
    assert explorer["free"] == sum(r["fields"]["app_fee"]["code"].startswith("0") for r in RECS)
    assert explorer["perPositionShown"] is True
    hay = lambda r: " ".join([build.short(r), r["institution"], r["department"], r["region"], r["country"], r["notes"]]
                             + [f["value"] for f in r["fields"].values()]).lower()
    assert explorer["search"] == sum("waterloo" in hay(r) for r in RECS) >= 1


def test_explorer_detail_shows_official_quote(explorer):
    assert explorer["dialogOpen"] is True
    assert explorer["dialogLink"].startswith("https://")
    assert len(explorer["dialogQuote"]) > 20


def test_explorer_shortlist_export_and_persistence(explorer):
    assert explorer["starred"] == 2
    assert explorer["csvLines"] == 3  # header + 2 programs
    assert explorer["csvName"] == "my-shortlist.csv"
    assert explorer["persistedStars"] >= 2


def test_explorer_phone_layout(explorer):
    assert explorer["cardsVisible"] is True
    assert explorer["horizontalOverflow"] is False


def test_explorer_earliest_deadline_first(explorer):
    first = min((r for r in RECS if build.deadline_cell(r)), key=lambda r: (r["fields"]["deadline"]["code"], build.short(r)))
    assert explorer["firstByDeadline"] == build.short(first)


def test_explorer_quick_picks_and_new_filters(explorer):
    bachelor = sum(r["fields"]["entry_route"]["code"] in ("Direct from bachelor's", "Either") for r in RECS)
    funded = sum(r["fields"]["funding"]["code"] in ("Guaranteed", "Typical") for r in RECS)
    assert explorer["pickBachelor"] == bachelor > 0
    assert explorer["pickBachelorPressed"] == "true"
    assert explorer["funded"] == funded > 0
    assert explorer["filtersSummary"].startswith("Filters (")


def test_explorer_shows_rupee_estimates(explorer):
    assert explorer["inrHints"] >= sum(1 for r in RECS if build.fee_parts(r["fields"]["app_fee"]["code"])[0])
    assert "₹" in explorer["feeDialogExtra"]


def test_explorer_phone_starts_with_filters_folded(explorer):
    assert explorer["phoneFiltersOpen"] is False
    assert explorer["phoneFirstCardTop"] < 800, "first program should be visible without scrolling far"


@pytest.mark.skipif(shutil.which("soffice") is None, reason="LibreOffice not installed")
def test_workbook_formulas_calculate_in_libreoffice():
    """Fill two shortlist rows, recalculate with LibreOffice, read the results back."""
    wb = load_workbook(OUT / "Atlas.xlsx")
    for name in ["Start", "Programs", "Shortlist", "Budget", "Recommenders", "Supervisor outreach", "Sources"]:
        assert name in wb.sheetnames
    toronto = next(r for r in RECS if r["id"] == "utoronto")
    uiuc = next(r for r in RECS if r["id"] == "uiuc")
    sl = wb["Shortlist"]
    sl["A2"] = build.short(toronto)
    sl["A3"] = build.short(uiuc)
    sl["N3"] = "Waived"
    wb["Supervisor outreach"]["E2"] = __import__("datetime").date(2026, 11, 3)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "filled.xlsx"
        wb.save(src)
        outdir = Path(tmp) / "out"
        subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", str(outdir), str(src)],
                       capture_output=True, check=True, timeout=180)
        calc = load_workbook(outdir / "filled.xlsx", data_only=True)
    s = calc["Shortlist"]
    assert s["B2"].value == "Canada"
    assert s["E2"].value == 135
    assert s["F2"].value == "CAD"
    assert str(s["C2"].value).startswith("2026-12-11")
    assert isinstance(s["D2"].value, (int, float))
    assert s["H3"].value == "Optional"
    b = calc["Budget"]
    col = {c.value: c.column_letter for c in b[1]}
    assert b[f"{col['CAD']}2"].value == 135    # Toronto fee counted
    assert b[f"{col['USD']}2"].value == 0      # UIUC marked Waived, so excluded
    assert b["B10"].value > 0                  # converted to rupees with the pre-filled rates
    f = calc["Supervisor outreach"]["F2"].value
    assert str(f).startswith("2026-11-13")
