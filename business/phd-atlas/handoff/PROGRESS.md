# STEM PhD Atlas 2027 — Progress Log

## Phase 0 — 2026-10-29
- Branch: `claude/magical-dirac-6pfq3g` (pulled `origin/claude/magical-dirac-6pfq3g` `f304198a`, plus local Windows cross-platform build/test & explorer boot-time fix `9edc13c6`; zero changes to `data/` or `data/staging/`).
- `validate_data.py --dir data --require-cache`: `285 universities, 2968 programs, 0 errors, 0 warnings` (`rc=0`).
- `validate_data.py --dir data/staging --require-cache`: `36 universities, 227 programs, 0 errors, 0 warnings` (`rc=0`).
- `coverage.py`: `285 of 340 listed universities have a record; 283 have programs; 2968 programs`; `Not stated overall: 9920/32648 = 30%`; per-field `26%–35%` (`rc=0`).
- `handoff/measure.py`: `TOTAL 69% -> 56%` (`rc=0`).
- `product/build.py && pytest -q tests`: `explorer: 2968 programs, data 6.4 MB raw, file 1.58 MB`, `warnings: 0` (`rc=0`); `22 passed, 2 skipped` (`rc=0`).
  - Difference noted vs handoff ("expect 24 passed (1 may skip without LibreOffice)"): **2** tests skip when `soffice` is not installed (`test_workbook_formulas_calculate_in_libreoffice` in `tests/test_product.py:262` and `test_ops_workbook_formulas_calculate_in_libreoffice` in `tests/test_ops.py:47`).
- Status: Waiting on owner decisions D1–D5 (plus Canterbury NZ `canterbury-nz--biomed.json` in §7) before changing any data.

## Phase 1 (D1 Subject-Test Schema Fix) — 2026-10-29
- Added `"No subject test"` to `gre_subject` in `data/schema.json` (cited verbatim to ETS `score-users/about/subject-tests.html` and `test-takers/subject-tests/scores.html`), updated `data/fields.json` (`chemistry` `subject_gre: null` after May 2023 discontinuation), `data/staging/RESEARCH_BRIEF.md`, `product/templates/atlas.html`, `product/sample.py`, `product/build.py`, `product/content/playbook.md`, and `tests/test_product.py`.
- Applied via `handoff/apply_no_subject_test.py` to 1,953 live programs and 158 staged programs where `field not in {"physics", "math", "neuro"}` and `gre_subject.code == "Not stated"`.
- Validation: `data` (`285 universities, 2968 programs, 0 errors`), `data/staging` (`36 universities, 227 programs, 0 errors`), `pytest` (`22 passed, 2 skipped`, `rc=0`).
- Overall `Not stated` (`coverage.py`): `30% (9920/32648)` -> `24% (7967/32648)`.

## Phase 2 & 3 (Wave 1 Review & Batch 1 Promotion) — 2026-10-29
- Universities: 49 promoted (`akron`, `auburn`, `bonn-cologne`, `canterbury-nz`, `dtu`, `freiburg`, `fuberlin`, `heidelberg`, `helsinki`, `icfo`, `imprs-qd`, `ipparis`, `kit`, `leiden`, `lmu`, `lund`, `mines`, `mst`, `munich-mcqst`, `nau`, `ntnu`, `okstate`, `otago`, `padova`, `paris-saclay`, `sissa`, `sorbonne`, `southdakota`, `southdakotastate`, `stockholm`, `tuberlin`, `tudresden`, `tuebingen`, `tufts`, `tuwien`, `uab`, `uga-fr`, `unibas`, `unibe`, `unibo`, `unige`, `unr`, `upc`, `utrecht`, `uva`, `uwa`, `vcu`, `wayne`, `wpi`).
- Staged universities measured: `62% -> 50%` Not stated across staged records (`vcu`: `59% -> 25%`, `mst`: filled app fee/waiver/English waiver, `uab`: filled $60 fee/TOEFL 4.0/IELTS 6.5/English waiver, `nau`: filled $75 fee/TOEFL 80/English waiver, `wayne`: $0 fee/TOEFL 4.5/IELTS 6.5, `wpi`: $70 fee/TOEFL 4.5/IELTS 6.5).
- Promoted 276 files (49 universities, 227 programs) into `data/`.
- All §7 open review items addressed and verified:
  - `mines`: department Fall priority funding deadline March 1 noted (`deadline: "Not stated"` with `time_sensitive: "2027-03-01"`).
  - `mst`: `app_fee: "75 USD"`, `fee_waiver: "Limited"`, `toefl_min: "4.5 (new scale)"` (ECE 80 noted as conflict), `english_waiver: "No"`.
  - `akron`: `akron--chemistry.json` review begins Feb 1 -> `deadline: "Not stated"` with `time_sensitive: "2027-02-01"`.
  - `tuwien`: `tuwien.json` `english_waiver` changed to `"Conditional"`.
  - `paris-saclay`: `paris-saclay--physics.json` `funding` changed to `"Competitive"`.
  - `unibo`: `unibo.json` kept at EUR 10 with DEI BME and Health & Technologies conflict noted.
  - `southdakota`: `southdakota.json` `app_fee: "38 USD"` admissions page used with catalog $40 noted as conflict; catalog overrides removed from programs.
  - `southdakotastate`: `southdakotastate.json` `toefl_min: "Not stated"`.
  - `unibe`: `unibe--*.json` deadlines updated to GCB 2026-12-15 and year-round Rolling.
  - `canterbury-nz`: `canterbury-nz--*.json` deadlines updated to year-round Rolling with UC Doctoral Scholarship May 15 time_sensitive.
  - `auburn`: `auburn--chemistry.json` GRE General waiver verified from Graduate School official waiver list.
- Live validation: `288 universities, 2996 programs, 0 errors, 0 warnings` (`rc=0`).
- Overall `Not stated` (`coverage.py`): `24% (7967/32648)` -> `23% (7641/32956)`.
- 14 of 18 fields are now `< 25%` Not stated (`biology` 22%, `biomed` 22%, `bme` 22%, `chemistry` 22%, `earth` 22%, `astronomy` 23%, `chemeng` 23%, `cs` 23%, `ece` 23%, `environment` 23%, `materials` 23%, `civil` 24%, `mech` 24%, `neuro` 24%).

## Phase 4 (Wave 2 Batch A High-Yield University Promotions) — 2026-10-29
- Universities: 9 enriched (`auckland`, `dalhousie`, `oregonstate`, `syracuse`, `unt`, `uottawa`, `usask`, `utep`, `western`).
- Key university-level enrichments verified with primary sources cached:
  - `oregonstate` (16 programs): verified `toefl_min: "80"`, `ielts_min: "6.5"`, `english_waiver: "No"`, `gre_general: "Not required"`. Dropped from 44% to 18% Not stated.
  - `syracuse` (11 programs): verified `gre_general: "Optional"`, `english_waiver: "No"`. Dropped from 38% to 29% Not stated.
  - `unt` (9 programs): verified `toefl_min: "79"`, `english_waiver: "No"`, `gre_general: "Not required"`. Dropped from 49% to 30% Not stated.
  - `auckland` (14 programs): verified `app_fee: "100 NZD"`.
  - `utep` (14 programs): verified `gre_general: "Not required"`, `english_waiver: "No"`. Dropped from 38% to 25% Not stated.
  - `usask` (14 programs): verified `fee_waiver: "None"` ($145 CAD), `gre_general: "Not required"`. Dropped from 19% to 1% Not stated.
  - `western` (15 programs): verified `fee_waiver: "None"` ($185 CAD), `gre_general: "Not required"`. Dropped from 24% to 7% Not stated.
  - `dalhousie` (16 programs): verified `fee_waiver: "None"` ($115 CAD), `gre_general: "Not required"`. Dropped from 23% to 7% Not stated.
  - `uottawa` (15 programs): verified `fee_waiver: "None"`, `gre_general: "Not required"`. Dropped from 20% to 2% Not stated.
- Live validation: `288 universities, 2996 programs, 0 errors, 0 warnings` (`rc=0`).
- Overall `Not stated` (`coverage.py`): `7,641 -> 7,418 / 32,956 = 22.51%`.
- 15 of 18 fields are now `< 25%` (`statistics` joined the < 25% club at 24%). Only 3 remain slightly above: `datasci` (26%), `physics` (27%), `math` (29%).

## Phase 5 (Wave 2 Batch B High-Yield Gapfills & DataSci Targeted Strike) — 2026-10-29
- Universities: 9 enriched (`cmu`, `clevelandstate`, `drexel`, `princeton`, `rochester`, `slu`, `tulane`, `unimelb`, `uvm`) + targeted department strike on `datasci` and `statistics` programs.
- Key enrichments verified with primary sources cached:
  - `drexel` (15 programs): verified `app_fee: "65 USD"`, `fee_waiver: "None"`, `gre_general: "Optional"`, `toefl_min: "90"`, `ielts_min: "6.5"`, `english_waiver: "No"`, `drexel--math.json` deadline and funding, `drexel--physics.json` funding.
  - `unimelb` (13 programs): verified `gre_general: "Not required"`, `english_waiver: "Conditional"`.
  - `slu` (10 programs): verified `app_fee: "0 USD"`, `fee_waiver: "No fee"`, `gre_general: "Not required"`.
  - `princeton` (14 programs): verified `gre_general: "Not required"`.
  - `rochester` (14 programs): verified `fee_waiver: "Limited"`, `gre_general: "Not required"`.
  - `tulane` (13 programs): verified `app_fee: "0 (no fee)"`, `fee_waiver: "No fee"`, `gre_general: "Not required"`, `toefl_min: "87"`, `ielts_min: "7"`, `english_waiver: "No"`, `tulane--biomed.json` funding and supervisor.
  - `uvm` (11 programs): verified `toefl_min: "90"`.
  - `cmu` (9 programs): verified `fee_waiver: "Limited"`, `gre_general: "Not required"`, `cmu--physics.json` funding (`Guaranteed`), `cmu--math.json` supervisor (`Not required`). Both CMU physics and math are 100% complete.
  - Targeted programs: `uchicago--datasci`, `oregonstate--datasci`, `utah--datasci`, `baylor--statistics`, `udel--datasci`, `stonybrook--datasci`, `clevelandstate--datasci`, `njit--datasci`.
- Live validation: `288 universities, 2996 programs, 0 errors, 0 warnings` (`rc=0`).
- Overall `Not stated` (`coverage.py`): `7,418 -> 7,257 / 32,956 = 22.02%`.
- 16 of 18 fields are now `< 25%` (`datasci` dropped to 24%). Only 2 fields remain above 25%: `physics` (27%) and `math` (28%).
