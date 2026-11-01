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

## Phase 6 (Wave 2 Batch C High-Yield Gapfills & Physics/Math Strike) — 2026-10-29
- Universities: 5 universities enriched at central level (`clemson`, `lehigh`, `iub`, `lmu`, `tudresden`) + 10 targeted department programs (`clemson--math`, `lehigh--math`, `iub--physics`, `iub--math`, `nyu--math`, `brown--physics`, `clarkson--physics`, `buffalo--physics`, `lmu--physics`, `lmu--math`).
- Key enrichments verified with primary sources cached:
  - `clemson` (15 programs): `toefl_min: "4.0 (new scale)"`, `ielts_min: "6.5"`. Removed redundant department overrides.
  - `lehigh` (12 programs): `gre_general: "Not required"`, `ielts_min: "6.5"`, `lehigh--math.json` `supervisor: "Not required"`. `lehigh--math.json` is 100% complete.
  - `iub` (11 programs): `toefl_min: "79"`, `ielts_min: "6.5"`, `iub--physics.json` `supervisor: "Not required"`. Both IUB math and physics are 100% complete.
  - `nyu`: `nyu--math.json` `deadline: "2027-01-04"`, `supervisor: "Not required"`.
  - `brown`: `brown--physics.json` `supervisor: "Recommended"`. 100% complete.
  - `clarkson`: `clarkson--physics.json` `supervisor: "Not required"`. 100% complete.
  - `buffalo`: `buffalo--physics.json` `gre_general: "Optional"`. 100% complete.
  - `lmu` (6 programs): `app_fee: "0 (no fee)"`, `fee_waiver: "No fee"`, `gre_general: "Not required"`, `lmu--physics.json` `funding: "Competitive"`, `lmu--math.json` `funding: "Competitive"`.
  - `tudresden` (9 programs): `toefl_min: "Not required"`, `ielts_min: "Not required"`, `gre_general: "Not required"`.
- Live validation: `288 universities, 2996 programs, 0 errors, 0 warnings` (`rc=0`).
- Overall `Not stated` (`coverage.py`): `7,257 -> 7,187 / 32,956 = 21.81%`.
- 16 of 18 fields `< 25%`. Remaining fields: `physics` (26.78%, need 66 resolved), `math` (28.12%, need 99 resolved).

## Phase 7 (Wave 2 Batch D–H European University Enrichments & Math/Physics Milestone) — 2026-10-29
- Universities: 20 European universities enriched at central level (`kit`, `heidelberg`, `stuttgart`, `unibe`, `fuberlin`, `paris-saclay`, `tuberlin`, `sorbonne`, `ntnu`, `uppsala`, `dtu`, `leiden`, `utrecht`, `freiburg`, `uga-fr`, `upc`, `ugent`, `uva`, `stockholm`, `ipparis`).
- 23 targeted department gapfills in `math` and `physics`:
  - `temple--physics.json`: `supervisor: "Not required"`
  - `columbia--physics.json`: `funding: "Guaranteed"`
  - `claremontgrad--math.json`: `gre_subject: "Optional"`, `supervisor: "Not required"`
  - `binghamton--physics.json`: `funding: "Typical"`, `gre_general: "Optional"`
  - `bgsu--math.json`: `entry_route: "Master's usually required"`, `funding: "Competitive"`
  - `bc--math.json`: `deadline: "2027-01-20"`
  - `denver--math.json`: `gre_subject: "Optional"`, `supervisor: "Not required"`
  - `illinoistech--math.json`: `gre_subject: "Optional"`
  - `marquette--math.json`: `gre_subject: "Optional"`
  - `miami--math.json`: `gre_subject: "Optional"`
  - `ohiou--math.json`: `gre_subject: "Optional"`
  - `oregonstate--math.json`: `gre_subject: "Optional"`
  - `ou--math.json`: `gre_subject: "Not required"`
  - `utoledo--math.json`: `gre_subject: "Optional"`
  - `epfl--math.json`: `gre_subject: "Recommended"`
  - `dayton--physics.json`: `gre_subject: "Not required"`
  - `denver--physics.json`: `gre_subject: "Optional"`, `supervisor: "Not required"`
  - `louisville--physics.json`: `gre_subject: "Not required"`
  - `bostonu--physics.json`: `supervisor: "Not required"`
  - `cornell--physics.json`: `supervisor: "Not required"`
  - `uchicago--math.json`: `supervisor: "Not required"`
  - `temple--math.json`: `supervisor: "Not required"`
  - `cornell--math.json`: `supervisor: "Not required"`
- **HISTORIC MILESTONE REACHED**:
  - **ALL 18 fields are now `< 25%` Not stated!**
    - `astronomy`: 19.30%
    - `biology`: 18.11%
    - `biomed`: 19.45%
    - `bme`: 20.01%
    - `chemeng`: 19.82%
    - `chemistry`: 17.51%
    - `civil`: 20.96%
    - `cs`: 19.25%
    - `datasci`: 23.27%
    - `earth`: 18.75%
    - `ece`: 20.12%
    - `environment`: 19.83%
    - `materials`: 19.98%
    - `math`: **24.95%** (656 / 2,629)
    - `mech`: 21.12%
    - `neuro`: 23.47%
    - `physics`: **24.22%** (674 / 2,783)
    - `statistics`: 18.66%
- Live validation: `288 universities, 2996 programs, 0 errors, 0 warnings` (`rc=0`).
- Overall `Not stated` (`coverage.py`): `7,187 -> 6,617 / 32,956 = 20%`.

## Phase 8 (44 Added Universities: US R1/R2, Australia, Europe, UK) — 2026-10-29 to 2026-10-30
- Universities added: 44 (total: 332 universities, 3,649 programs):
  - US R1/R2 (30): `uark`, `uwyo`, `unh`, `umaine`, `ohsu`, `rit`, `wpi`, `wayne`, `uah`, `uaf`, `ucsd`, `ufl`, `uga`, `ucf`, `uconn`, `ucr`, `ucsc`, `uhouston`, `uic`, `uiowa`, `umich`, `unc`, `unm`, `uoregon`, `usc`, `utdallas`, `utk`, `virginiatech`, `washu`, `wsu`.
  - Australia (3): `macquarie`, `qut`, `monash`.
  - Europe (2): `univie`, `kuleuven`.
  - UK (13): `oxford`, `ucl`, `manchester`, `birmingham`, `leeds`, `sheffield`, `southampton`, `nottingham`, `bath`, `exeter`, `cardiff`, `newcastle`, `liverpool`.
- Commits:
  - `dd909eb6` Add and promote verified universities: uark, uwyo, unh, umaine, ohsu with STEM PhD programs
  - `55210bb0` Add and promote verified university and 10 STEM PhD programs for rit
  - `f0919b2d` Add and promote 14 verified STEM PhD programs for wpi
  - `f1151081` Add and promote 13 verified STEM PhD programs for wayne
  - `972c5bfd` Add verified STEM PhD records for UAH and UAF
  - `3f63736c` Add verified STEM PhD records for UCSD
  - `548325e9` Add verified STEM PhD records for UFL
  - `9f7e7148` Add verified STEM PhD records for UGA
  - `cb755765` Add verified STEM PhD records for UCF
  - `a630024b` Add verified STEM PhD records for UConn
  - `f9b03e43` Add University of California, Riverside (ucr) with 16 STEM PhD programs
  - `b745a6cb` Add University of California, Santa Cruz (ucsc) with 13 STEM PhD programs
  - `f7649d97` Add University of Houston (uhouston) with 9 STEM PhD programs
  - `d1c83ded` Add University of Illinois Chicago (uic) with 12 STEM PhD programs
  - `6e6390cb` Add University of Iowa (uiowa) with 12 STEM PhD programs
  - `64f87d78` Add University of Michigan (umich) with 11 STEM PhD programs
  - `ebac613b` Add University of North Carolina at Chapel Hill (unc) with 9 STEM PhD programs
  - `b5477f3d` Add unm (University of New Mexico) with 11 STEM PhD programs and cached pages
  - `1a55ab02` Add uoregon (University of Oregon) with 6 STEM PhD programs and cached pages
  - `dae74844` Add USC with 12 STEM PhD programs and cached sources
  - `f45c62c5` Add UT Dallas with 12 STEM PhD programs and cached sources
  - `e4c8d048` Add UT Knoxville with 13 STEM PhD programs and cached sources
  - `c191973a` Add Virginia Tech (virginiatech) with 13 STEM PhD programs and cached pages
  - `dce56965` Add Washington University in St. Louis (washu) with 12 STEM PhD programs and cached pages
  - `ef2fdead` Add Washington State University (wsu) with 12 STEM PhD programs and cached pages
  - `ec3cfb9f` Add Macquarie University (macquarie) with 12 STEM PhD programs and cached pages
  - `86660039` Add Queensland University of Technology (qut) with 14 STEM PhD programs and cached pages
  - `c9acd4e5` Add Monash University (monash) with 14 STEM PhD programs and cached pages
  - `cce9bb1a` Add University of Vienna (univie) with 9 STEM PhD programs and cached pages
  - `25297f02` Add KU Leuven (kuleuven) with 15 STEM PhD programs and cached pages
  - `2449ea0a` Add University of Oxford (oxford) with 16 STEM DPhil programs and cached pages
  - `14cfd9a3` Add University College London (ucl) with 16 STEM MPhil/PhD programs and cached pages
  - `cd275283` Add University of Manchester (manchester) with 17 STEM PhD programs and cached pages
  - `d92bb48f` Add University of Birmingham (birmingham) with 17 STEM PhD programs and cached pages
  - `5cd822c0` Add University of Leeds (leeds) with 17 STEM PhD programs and cached pages
  - `0e4546d7` Add University of Sheffield (sheffield) with 17 STEM PhD programs and cached pages
  - `ec010bbd` Add University of Southampton (southampton) with 17 STEM PhD programs and cached pages
  - `cd4c9ac7` Add University of Nottingham (nottingham) with 17 STEM PhD programs and cached pages
  - `efba135a` Add University of Bath (bath) with 17 STEM PhD programs and cached pages
  - `9e35609a` Add University of Exeter (exeter) with 17 STEM PhD programs and cached pages
  - `110323ae` Add Cardiff University (cardiff) with 17 STEM PhD programs and cached pages
  - `adc031f9` Add Newcastle University (newcastle) with 17 STEM PhD programs and cached pages
  - `6e21f347` Add University of Liverpool (liverpool) with 17 STEM PhD programs and cached pages
  - `c1946806` Handoff v2: audit of recent research, US R1/R2 coverage plan, quality audit script
- Verification numbers:
  - `validate_data.py --dir data --require-cache`: 332 universities, 3649 programs, 0 errors, 0 warnings (`rc=0`).
  - `coverage.py --gate`: 332 of 340 listed universities have a record; 332 have programs; 3649 programs. Not stated overall: 8,304 / 40,139 = 20.69% (`rc=1`, gate ceiling is 15% overall; `math` at 25.4% exceeds 25% field ceiling).
  - `audit_quality.py`: 3,981 records checked: `generic_page: 426`, `off_topic: 742`, `absence: 123`, `odd_cache: 46`.
  - `product/build.py && pytest -q tests`: Explorer built with 3,649 programs into `dist/STEM-PhD-Atlas-2027-v2.0.zip`; 22 passed, 2 skipped (`rc=0`).
- Quality Audit Findings (`HANDOFF.md` §1):
  - 426 programs across 37 universities used generic "how to apply" / catalog landing pages with identical quotes across programs (existence of department PhD unproven on department page). Heavily concentrated in UK Russell Group (11 universities x 17 programs) and others (UCL, UCR, KU Leuven, Caltech, QUT, UCF, Monash, UCSC, Macquarie).
  - 742 off-topic quotes flagged (e.g. deadline quoted for funding).
  - 123 inferred from silence quotes (e.g. GRE not mentioned -> "Not required").
  - 46 odd cache entries (cached via non-`research.py` helper scripts, mainly `uark`, `uwyo`).
- Status: Phase 0 verified. Pausing for owner decisions E1–E5 before Phase A repairs.

## Phase A Batch 1 (Repair Birmingham) — 2026-10-31
Universities: added 0 | repaired 1 (birmingham) | screened out 0
Programs: +0 new, −1 moved to _removed (birmingham--bme: no standalone Biomedical Engineering PhD at Birmingham; research conducted under Mechanical Engineering PhD and Chemical Engineering PhD; bme added to also_fields of birmingham--mech)
Not stated: overall 20.69% (8304/40139) -> 20.68% (8297/40128) | math 25% | physics 24%
audit_quality: generic_page 426 -> 409 (-17) / off_topic 742 / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: 1c2bd815

## Phase A Batch 2 (Repair Bath) — 2026-10-31
Universities: added 0 | repaired 1 (bath) | screened out 0
Programs: +0 new, −4 moved to _removed (bath--bme, bath--materials, bath--earth, bath--environment: no standalone PhD in BME, Materials, Earth Sciences, or Environmental Science at Bath; bme mapped to also_fields of bath--mech, materials mapped to also_fields of bath--chemeng, environment mapped to also_fields of bath--civil; Bath offers no Earth Sciences degree)
Not stated: overall 20.68% (8297/40128) -> 20.66% (8283/40084) | math 25% | physics 24%
audit_quality: generic_page 409 -> 392 (-17) / off_topic 742 / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: ede53a2f

## Phase A Batch 3 (Repair Leeds) — 2026-10-31
Universities: added 0 | repaired 1 (leeds) | screened out 0
Programs: +0 new, −2 moved to _removed (leeds--bme, leeds--materials: no standalone PhD in BME or Materials Science at Leeds; research conducted under Mechanical Engineering PhD and Chemical and Process Engineering PhD; bme added to also_fields of leeds--mech, materials added to also_fields of leeds--chemeng)
Not stated: overall 20.66% (8283/40084) -> 20.66% (8275/40062) | math 25% | physics 24%
audit_quality: generic_page 392 -> 375 (-17) / off_topic 740 (-2) / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: 737952dc

## Phase A Batch 4 (Repair Sheffield) — 2026-10-31
Universities: added 0 | repaired 1 (sheffield) | screened out 0
Programs: +0 new, −0 moved to _removed (all 17 PhD fields verified across departmental/school research pages: cs, chemistry, math, statistics, physics, astronomy, mech, civil, chemeng, materials, bme, ece, biology, biomed, earth, environment, neuro)
Not stated: overall 20.66% (8275/40062) -> 20.66% (8275/40062) | math 25% | physics 24%
audit_quality: generic_page 375 -> 358 (-17) / off_topic 740 -> 723 (-17) / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: 2735bc38

## Phase A Batch 5 (Repair Exeter) — 2026-10-31
Universities: added 0 | repaired 1 (exeter) | screened out 0
Programs: +0 new, −4 moved to _removed (exeter--chemistry, exeter--chemeng, exeter--bme, exeter--materials: Exeter has no Department or PhD in Chemistry or Chemical Engineering; Biomedical Engineering and Materials Engineering are sub-areas under MPhil/PhD Engineering and mapped to also_fields of exeter--mech)
Not stated: overall 20.66% (8275/40062) -> 20.65% (8263/40018) | math 25% | physics 24%
audit_quality: generic_page 358 -> 341 (-17) / off_topic 723 / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: 78948a0a

## Phase A Batch 6 (Repair Newcastle) — 2026-10-31
Universities: added 0 | repaired 1 (newcastle) | screened out 0
Programs: +0 new, −1 moved to _removed (newcastle--bme: no standalone Biomedical Engineering PhD at Newcastle; research conducted through Centre for Biomedical Engineering within Mechanical and Systems Engineering; bme added to also_fields of newcastle--mech)
Not stated: overall 20.65% (8263/40018) -> 20.65% (8260/40007) | math 25% | physics 24%
audit_quality: generic_page 341 -> 324 (-17) / off_topic 723 -> 705 (-18) / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: 98702d2c

## Phase A Batch 7 (Repair Cardiff) — 2026-10-31
Universities: added 0 | repaired 1 (cardiff) | screened out 0
Programs: +0 new, −0 moved to _removed (all 17 PhD fields verified across departmental and school research degree pages: cs, chemistry, math, statistics, physics, astronomy, biology, biomed, neuro, earth, environment, mech, materials, ece, bme, civil, chemeng)
Not stated: overall 20.65% (8260/40007) -> 20.65% (8260/40007) | math 25% | physics 24%
audit_quality: generic_page 324 -> 307 (-17) / off_topic 705 -> 688 (-17) / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: 4e411a01

## Phase A Batch 8 (Repair Manchester) — 2026-10-31
Universities: added 0 | repaired 1 (manchester) | screened out 0
Programs: +0 new, −1 moved to _removed (manchester--bme: no standalone Biomedical Engineering PhD at Manchester; research delivered through Biomaterials PhD/MPhil and projects in Mechanical Engineering / EEE; bme added to also_fields of manchester--mech)
Not stated: overall 20.65% (8260/40007) -> 20.64% (8257/39996) | math 25% | physics 24%
audit_quality: generic_page 307 -> 290 (-17) / off_topic 688 / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: 9bc32d38

## Phase A Batch 9 (Repair Liverpool) — 2026-10-31
Universities: added 0 | repaired 1 (liverpool) | screened out 0
Programs: +0 new, −2 moved to _removed (liverpool--chemeng, liverpool--astronomy: Liverpool has no standalone Chemical Engineering department or PhD, research conducted in Chemistry and Materials; Astrophysics Research Institute is based at LJMU rather than Liverpool; chemeng added to also_fields of liverpool--chemistry, astronomy added to also_fields of liverpool--physics)
Not stated: overall 20.64% (8257/39996) -> 20.63% (8248/39974) | math 25% | physics 24%
audit_quality: generic_page 290 -> 273 (-17) / off_topic 688 -> 671 (-17) / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: 454ae850

## Phase A Batch 10 (Repair Nottingham) — 2026-10-31
Universities: added 0 | repaired 1 (nottingham) | screened out 0
Programs: +0 new, −1 moved to _removed (nottingham--bme: no standalone Biomedical Engineering PhD at Nottingham; research delivered through Materials Engineering and EEE; bme added to also_fields of nottingham--mech)
Not stated: overall 20.63% (8248/39974) -> 20.63% (8244/39963) | math 25% | physics 24%
audit_quality: generic_page 273 -> 256 (-17) / off_topic 671 / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: c1f8ea47

## Phase A Batch 11 (Repair Southampton — UK Eleven Complete!) — 2026-10-31
Universities: added 0 | repaired 1 (southampton) | screened out 0
Programs: +0 new, −2 moved to _removed (southampton--bme, southampton--materials: Southampton has no standalone Department of Biomedical Engineering or Materials Science PhD, research delivered within Department of Mechanical Engineering; bme and materials added to also_fields of southampton--mech)
Not stated: overall 20.63% (8244/39963) -> 20.61% (8234/39941) | math 25% | physics 24%
audit_quality: generic_page 256 -> 239 (-17) / off_topic 671 / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: c332602e

## Phase A Batch 12 (Repair UCR) — 2026-10-31
Universities: added 0 | repaired 1 (ucr) | screened out 0
Programs: +0 new, −0 moved to _removed (all 16 PhD programs verified across departmental homepages: cs, ece, mech, bme, chemeng, chemistry, materials, math, statistics, physics, astronomy, earth, environment, biology, neuro, biomed)
Not stated: overall 20.61% (8234/39941) -> 20.61% (8234/39941) | math 25% | physics 24%
audit_quality: generic_page 239 -> 223 (-16) / off_topic 671 / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: 00937f45










## Phase A Batch 13 (Repair Caltech) — 2026-10-31
Universities: added 0 | repaired 1 (caltech) | screened out 0
Programs: +0 new, −0 moved to _removed (all 14 PhD programs verified across departmental option homepages: astronomy, biology, bme, chemeng, chemistry, civil, cs, earth, ece, environment, materials, math, mech, neuro)
Not stated: overall 20.61% (8234/39941) -> 20.61% (8234/39941) | math 25% | physics 24%
audit_quality: generic_page 223 -> 209 (-14) / off_topic 671 -> 657 (-14) / absence 123 / odd_cache 46
Blocked pages (for owner): none
Owner questions: none
Commit: 7c5f0815
2026-10-31 | CARD 2 | Repaired kuleuven (15 programs) | Not stated 20.61% -> 20.61% | commit 6dfcaf7
2026-10-31 | CARD 2 | Repaired monash (14 programs) | Not stated 20.61% -> 20.61% | commit 5202a274
2026-10-31 | CARD 2 | Repaired qut (14 programs) | Not stated 20.61% -> 20.61% | commit 381458f0
2026-10-31 | CARD 2 | Repaired ucf (14 programs) | Not stated 20.61% -> 20.61% | commit 166e1cbf
2026-10-31 | CARD 2 | Repaired ucsc (13 programs) | Not stated 20.61% -> 20.61% | commit 4098d2d7
2026-10-31 | CARD 2 | Repaired macquarie (12 programs) | Not stated 20.61% -> 20.61% | commit e5fb10cf
2026-10-31 | CARD 2 | Repaired auburn (11 programs) | Not stated 20.61% -> 20.61% | commit cb7963b0
2026-10-31 | CARD 2 | Repaired univie (9 programs) | Not stated 20.61% -> 20.61% | generic_page 116 -> 107 (-9)
2026-10-31 | CARD 2 | Repaired groningen (8 programs) | Not stated 20.61% -> 20.61% | generic_page 107 -> 99 (-8)
2026-10-31 | CARD 2 | Repaired adelaide (7 programs) | Not stated 20.61% -> 20.61% | generic_page 99 -> 92 (-7)
2026-10-31 | CARD 2 | Repaired ugent (7 programs) | Not stated 20.61% -> 20.61% | generic_page 92 -> 85 (-7)
2026-10-31 | CARD 2 | Repaired usc (7 programs) | Not stated 20.61% -> 20.61% | generic_page 85 -> 78 (-7)
2026-10-31 | CARD 2 | Repaired uga (6 programs) | Not stated 20.61% -> 20.61% | generic_page 78 -> 72 (-6)
2026-10-31 | CARD 2 | Repaired uio (6 programs) | Not stated 20.61% -> 20.61% | generic_page 72 -> 66 (-6)







