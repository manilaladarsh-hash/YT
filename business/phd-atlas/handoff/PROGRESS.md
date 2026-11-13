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
2026-10-31 | CARD 2 | Repaired umich (6 programs) | Not stated 20.61% -> 20.61% | generic_page 66 -> 60 (-6)








2026-10-31 | CARD 2 | Repaired unimelb (6 programs) | Not stated 20.61% -> 20.62% | generic_page 60 -> 54 (-6)
2026-11-12 | CARD 2 | Repaired unsw (6 programs) | Not stated 20.62% -> 20.62% | generic_page 54 -> 48 (-6)
2026-11-12 | CARD 2 | Repaired usyd (6 programs) | Not stated 20.66% -> 20.66% | generic_page 48 -> 42 (-6)
2026-11-12 | CARD 2 | Repaired washu (6 programs) | Not stated 20.66% -> 20.66% | generic_page 42 -> 36 (-6)
2026-11-12 | CARD 2 | Repaired gwu (5 programs) | Not stated 20.66% -> 20.65% | generic_page 36 -> 31 (-5)
2026-11-12 | CARD 2 | Repaired miami (5 programs) | Not stated 20.65% -> 20.63% | generic_page 31 -> 26 (-5)
2026-11-12 | CARD 2 | Repaired oxford (5 programs) | Not stated 20.63% -> 20.63% | generic_page 26 -> 21 (-5)
2026-11-12 | CARD 2 | Repaired uconn (5 programs) | Not stated 20.63% -> 20.63% | generic_page 21 -> 16 (-5)
2026-11-12 | CARD 3 | Reviewed 10 audit rows (adelaide, albany, anu, arizona, auckland, baylor, bristol) | off_topic 657 -> 650, absence 123 -> 122, 3 anu rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (byu, canterbury-nz, clemson, clevelandstate, cmu, colostate) | off_topic 650 -> 642, absence 122 -> 120
2026-11-12 | CARD 3 | Reviewed 10 audit rows (dalhousie, denver, dtu, ecu) | off_topic 642 -> 636, absence 120 -> 116
2026-11-12 | CARD 3 | Reviewed 10 audit rows (floridatech, freiburg, fuberlin, georgetown, glasgow) | off_topic 636 -> 631, absence 116 -> 114, 3 glasgow rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (heidelberg, imperial, ipparis) | off_topic 631 -> 626, absence 114 -> 109
2026-11-12 | CARD 3 | Reviewed 10 audit rows (ku, leiden, lmu, louisville) | off_topic 626 -> 620, absence 109 -> 105
2026-11-12 | CARD 3 | Reviewed 10 audit rows (loyolachicago, lsu, marquette, memphis, mines, minnesota, mps-photonics, ou, portlandstate) | off_topic 620 -> 611, absence 105 -> 104
2026-11-12 | CARD 3 | Reviewed 10 audit rows (portlandstate, princeton, rockefeller, sissa, siucarbondale, sorbonne) | off_topic 611 -> 604, absence 104 -> 100
2026-11-12 | CARD 3 | Reviewed 10 audit rows (sorbonne, stanford, stockholm, stuttgart, syracuse) | off_topic 604 -> 598, absence 100 -> 96
2026-11-12 | CARD 3 | Reviewed 10 audit rows (tuberlin, tudresden, twente, ua, uab, uark) | off_topic 598 -> 593, absence 96 -> 94, odd_cache 46 -> 28, 3 uark rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uci, ucr, uga-fr, ugent, uic, uiowa) | off_topic 593 -> 586, absence 94 -> 91
2026-11-12 | CARD 3 | Reviewed 10 audit rows (umontreal, unibe, unlv, unt, uppsala) | off_topic 586 -> 582, absence 91 -> 88, 3 umontreal rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uq, uri, uta, utrecht) | off_topic 582 -> 576, absence 88 -> 85, 1 uta row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (utrecht, uts, uva, uwa) | off_topic 576 -> 571, absence 85 -> 82, 2 uwa rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uwa, vcu, warwick, washu, western, wrightstate, wur, aarhus) | off_topic 571 -> 563, absence 82 -> 81, 1 uwa row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (akron, alabamahuntsville x5 programs) | off_topic 563 -> 557, absence 81 -> 76
2026-11-12 | CARD 3 | Reviewed 10 audit rows (alabamahuntsville x3, baylor x4 programs) | off_topic 557 -> 551, absence 76 -> 73, 1 baylor--neuro row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (berkeley x2, bgsu, boise, bonn-cologne, bostonu, brandeis, bristol x3) | off_topic 551 -> 541, absence 73 -> 73
2026-11-12 | CARD 3 | Reviewed 10 audit rows (buffalo x2, byu x3, calgary x5) | off_topic 541 -> 538, absence 73 -> 73, 7 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (calgary--bme, chemeng, chemistry, civil) | off_topic 538 -> 538, absence 73 -> 73, 10 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (calgary--cs, earth, ece, math) | off_topic 538 -> 538, absence 73 -> 73, 10 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (calgary--mech, neuro x6; canterbury-nz x4) | off_topic 538 -> 534, absence 73 -> 73, 6 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (canterbury-nz x7, claremontgrad--biology, clarkson x2) | off_topic 534 -> 525, absence 73 -> 73, 1 row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (clemson x3, cmu x2, colostate x5; updated clemson--physics toefl_min) | off_topic 525 -> 516, absence 73 -> 73, 1 row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (concordia, cornell x4, denver x2, dtu, edinburgh x2) | off_topic 516 -> 508, absence 73 -> 73, 2 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (epfl x5, ethz--neuro, fau x4) | off_topic 508 -> 502, absence 73 -> 73, 4 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (fau--mech, fiu x3, floridatech x6) | off_topic 502 -> 496, absence 73 -> 69
2026-11-12 | CARD 3 | Reviewed 10 audit rows (floridatech--bme, chemeng, chemistry, civil, ece gre_general) | off_topic 496 -> 491, absence 69 -> 64
2026-11-12 | CARD 3 | Reviewed 10 audit rows (floridatech--environment, math, mech, physics; fordham--biology; fsu--biology) | off_topic 491 -> 485, absence 64 -> 60
2026-11-12 | CARD 3 | Reviewed 10 audit rows (fsu--math, georgiatech x3, gmu x2, goettingen x3, hamburg--biomed) | off_topic 485 -> 476, absence 60 -> 60, 1 row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (hamburg x2, illinoistech x6, imperial x2 + ielts_min) | off_topic 476 -> 466, absence 60 -> 60, 1 row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (imperial x3, imprs-cpqm, iub x2, jhu--cs, kcl--bme, kent--biomed) | off_topic 466 -> 462, absence 60 -> 59, 5 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (kent--math, kit--mech, ksu x2, ku x3, leeds x3) | off_topic 462 -> 453, absence 59 -> 59, 1 row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (leeds--chemeng..neuro deadline) | off_topic 453 -> 443, absence 59 -> 59
2026-11-12 | CARD 3 | Reviewed 10 audit rows (leeds x2, lehigh--biology, lmu x5, louisville--math x2) | off_topic 443 -> 435, absence 59 -> 58, 1 row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (loyolachicago--cs, lsu--math, lund x8) | off_topic 435 -> 431, absence 58 -> 58, 6 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (lund x4, marquette--chemistry, maryland--physics x2, mcmaster x3) | off_topic 431 -> 427, absence 58 -> 57, 5 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (memphis x2, miami x2, miamiohio x6) | off_topic 427 -> 420, absence 57 -> 54
2026-11-12 | CARD 3 | Reviewed 10 audit rows (minnesota--biomed x2, mit x3, mizzou x2, montana x3) | off_topic 420 -> 410, absence 54 -> 54
2026-11-12 | CARD 3 | Reviewed 10 audit rows (msstate--math, msu--statistics x2, mtu x7) | off_topic 410 -> 401, absence 54 -> 53
2026-11-12 | CARD 3 | Reviewed 10 audit rows (mtu x6, nau--civil, ncsu--chemeng x2, ncsu--chemistry) | off_topic 401 -> 394, absence 53 -> 53, 3 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (ncsu--earth x2, ncsu--materials x2, newcastle x6 + physics deadline) | off_topic 394 -> 388, absence 53 -> 53, 4 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (newcastle x10 entry_route + x9 deadline) | off_topic 388 -> 378, absence 53 -> 53
2026-11-12 | CARD 3 | Reviewed 10 audit rows (nmsu--ece, northwestern x4, nyu--math/mech, odu--biology/environment) | off_topic 378 -> 370, absence 53 -> 51, 1 row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (odu--math x2, ohiostate x4, ohsu x2, okstate--chemistry, olemiss--physics) | off_topic 370 -> 362, absence 51 -> 50, 1 row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (oregonstate x2, ou--physics, paris-saclay x6, pitt--biology) | off_topic 362 -> 356, absence 50 -> 50, 4 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (pitt--bme, portlandstate--chemistry, princeton x4, qmul x4) | off_topic 356 -> 347, absence 50 -> 50, 1 row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (qmul x7, queens x3) | off_topic 347 -> 340, absence 50 -> 50, 3 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (queens--civil, queens--physics, rit x8) | off_topic 340 -> 338, absence 50 -> 50, 8 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (rochester--neuro x2, rpi--cs, rutgers--physics, rwth x5, scripps--biology) | off_topic 338 -> 329, absence 50 -> 49, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (sfu--earth, smu--physics, sorbonne x8) | off_topic 329 -> 319, absence 49 -> 49, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (sorbonne x4, southalabama--cs, southdakotastate x3, stevens--physics, stockholm--chemistry) | off_topic 319 -> 309, absence 49 -> 49, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (stockholm x2, strathclyde x2, stuttgart x6) | off_topic 309 -> 299, absence 49 -> 49, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (syracuse x8, tamu--astronomy, tudresden--civil) | off_topic 299 -> 290, absence 49 -> 49, 1 row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (tuebingen--math, tufts--biomed, uab x2, ualberta x4, uark--astronomy x2) | off_topic 290 -> 283, absence 49 -> 49, odd_cache 28 -> 26, 3 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uark--biology, biomed x2, bme x4, chemeng, chemistry, civil) | off_topic 283 -> 283, absence 49 -> 49, odd_cache 26 -> 16, 9 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uark--cs x2, earth x2, ece x2, environment x3, materials) | off_topic 283 -> 283, absence 49 -> 49, odd_cache 16 -> 6, 10 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uark--math, mech, physics x4; ubc--chemistry, physics; uc--bme; ucd--civil) | off_topic 283 -> 279, absence 49 -> 49, odd_cache 6 -> 0, 6 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (ucd--ece, ucd--mech x2, ucdavis--biomed, uchicago--biology x2, biomed x2, datasci, neuro) | off_topic 279 -> 269, absence 49 -> 49, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uchicago--neuro, statistics; uci--chemistry; uconn--math; ucph--chemistry, physics; ucsb--earth; udel--biology, chemeng, chemistry) | off_topic 269 -> 259, absence 49 -> 49, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (udel--ece, math; uga-fr--chemistry x2, earth x2, ece x2; uhm--chemistry; uhouston--math) | off_topic 259 -> 255, absence 49 -> 49, 6 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uhouston--statistics; uic--biology x2, bme, chemeng x2, chemistry, civil x2, cs) | off_topic 255 -> 245, absence 49 -> 49, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uic--ece x2, materials x2, math x2, physics, statistics x2; uiowa--biology) | off_topic 245 -> 235, absence 49 -> 49, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uiowa--biomed, bme, chemeng, chemistry, civil, cs, ece, math, mech, physics entry_route) | off_topic 235 -> 225, absence 49 -> 49, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uiowa--statistics; uiuc--astronomy, physics; uky--ece, physics; umanitoba--math; umass--astronomy, statistics x2; umbc--mech) | off_topic 225 -> 217, absence 49 -> 48, 1 row reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (umkc--biology, chemistry, earth, math, physics; uml--chemeng, chemistry, civil, ece; umontana--chemistry) | off_topic 217 -> 207, absence 48 -> 48, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (umontreal--biology x2, biomed x2, bme, chemistry x2, cs, math x2) | off_topic 207 -> 207, absence 48 -> 48, 10 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (umontreal--neuro x2, physics x2, statistics x2; uncg--biology; unige--biology; univie--astronomy, biology) | off_topic 207 -> 204, absence 48 -> 48, 7 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (univie--chemistry, cs, earth, environment, math, neuro, physics; unlv--astronomy x3) | off_topic 204 -> 197, absence 48 -> 48, 3 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (unlv--astronomy, biology x2, earth x2, ece, environment x2, mech x2) | off_topic 197 -> 194, absence 48 -> 48, 7 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uoregon--cs; upc--civil x2, environment, math; uq--biomed; usu--cs; uta--chemistry; utah--bme, cs) | off_topic 194 -> 189, absence 48 -> 48, 5 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (utah--cs, datasci x2, earth, materials, neuro x2; utaustin--math; utdallas--cs; utoledo--biomed) | off_topic 189 -> 179, absence 48 -> 48, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (utoronto--astronomy, biology x2, chemeng, ece, materials, physics; utsa--biology, biomed, cs) | off_topic 179 -> 170, absence 48 -> 47, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (utsa--datasci, physics, statistics x2; uvic--physics; uwashington--environment; uwmilwaukee--biology x3; uzh--chemistry) | off_topic 170 -> 161, absence 47 -> 46, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (uzh--chemistry, earth; villanova--ece + fee/waiver; vuw--biology; warwick--materials; waterloo--math x2; wayne--materials x2; western--chemistry) | off_topic 161 -> 151, absence 46 -> 46, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (western--earth, neuro x2, physics, statistics; wfu--biomed x2, bme x2, neuro x2) | off_topic 151 -> 143, absence 46 -> 43, 0 rows reviewed
2026-11-12 | CARD 3 | Reviewed 10 audit rows (wisconsin--chemistry, cs x2, materials, math, mech, physics; wmu--civil, ece x2) | off_topic 143 -> 135, absence 43 -> 43, 2 rows reviewed
2026-11-13 | CARD 3 | Reviewed 10 audit rows (wpi--biology x2, biomed x3, bme x3, chemeng, chemistry + absence) | off_topic 135 -> 126, absence 43 -> 41, 0 rows reviewed
2026-11-13 | CARD 3 | Reviewed 10 audit rows (wpi--civil x2, cs x3, datasci x3, ece x2) | off_topic 126 -> 120, absence 41 -> 37, 0 rows reviewed
2026-11-13 | CARD 3 | Reviewed 10 audit rows (wpi--materials, math x2, mech x3, physics, statistics x4) | off_topic 120 -> 111, absence 37 -> 35, 0 rows reviewed
2026-11-13 | CARD 3 | Reviewed 5 final audit rows (wpi--math, wpi--statistics, wrightstate--mech, wvu--earth, yorku--cs) | off_topic 111 -> 106, absence 35 -> 35, 0 rows left in Phase A
2026-11-13 | CARD 4 | Added cunygc (8 programs) | Not stated 21% -> 21%
2026-11-13 | CARD 4 | iuindy | added Indiana University Indianapolis (10 STEM PhD programs)
2026-11-13 | CARD 4 | umassboston | added University of Massachusetts-Boston (10 STEM PhD programs)
2026-11-13 | CARD 5/4 | bcm | added Baylor College of Medicine (2 STEM PhD programs: biomed, neuro)
2026-11-13 | CARD 5/4 | musc | added Medical University of South Carolina (2 STEM PhD programs: biomed, neuro)
2026-11-13 | CARD 5/4 | uthsc | added The University of Tennessee Health Science Center (2 STEM PhD programs: biomed [incl. neuro], bme)
2026-11-13 | CARD 5/4 | uthealth | added The University of Texas Health Science Center at Houston (2 STEM PhD programs: biomed, neuro)
2026-11-13 | CARD 5/4 | uthscsa | added The University of Texas Health Science Center at San Antonio (2 STEM PhD programs: biomed [incl. neuro], bme)
2026-11-13 | CARD 5/4 | utsw | added The University of Texas Southwestern Medical Center (2 STEM PhD programs: biomed [incl. neuro], bme)
2026-11-13 | CARD 5/4 | ucsf | added University of California, San Francisco (4 STEM PhD programs: biomed, neuro, biology [Tetrad], bme [joint UC Berkeley]) — UCSF Drupal/Cloudflare pages 403, catalog.ucsf.edu + UC Berkeley joint BioE used
2026-11-13 | CARD 7 | Refreshed business docs (342 universities, 3675 programs, 18 fields, Not stated 21%)
2026-11-13 | CARD 5/4 | cuanschutz | added University of Colorado Denver/Anschutz Medical Campus (4 STEM PhD programs: biomed, neuro, bme, biology)
2026-11-13 | CARD 5/4 | unmc | added University of Nebraska Medical Center (2 STEM PhD programs: biomed, neuro via IGPBS)
2026-11-13 | CARD 5/4 | weillcornell | added Weill Cornell Medicine (3 STEM PhD programs: biomed, neuro, biology)
2026-11-13 | CARD 5/4 | american | added American University (3 STEM PhD programs: biomed, cs, neuro)
2026-11-13 | CARD 5/4 | catholic | added Catholic University of America (9 STEM PhD programs: biology, physics, materials, bme, civil, cs, ece, environment, mech)
2026-11-13 | CARD 5/4 | nova | added Nova Southeastern University (3 STEM PhD programs: cs, environment [also biology, earth], biomed)
2026-11-13 | CARD 4 | afit | added Air Force Institute of Technology Graduate School of Engineering & Management (7 STEM PhD programs: physics, materials, math [also statistics], cs, datasci, ece, mech)
2026-11-13 | CARD 4 | astate | added Arkansas State University (2 STEM PhD programs: environment, biology [also biomed])
2026-11-13 | CARD 4 | cmich | added Central Michigan University (7 STEM PhD programs: biology [also biomed, chemistry], earth [also environment], math, neuro, physics [also astronomy], materials [also chemistry, physics], statistics [also datasci])
2026-11-13 | CARD 4 | clark | added Clark University (5 STEM PhD programs: physics, chemistry, biomed, biology, environment [also earth])
2026-11-13 | CARD 7 | Refreshed business docs (352 universities, 3720 programs, 18 fields, Not stated 21%)
2026-11-13 | CARD 4 | ccny | added CUNY City College (5 STEM PhD programs: bme, chemeng, civil, ece, mech)
2026-11-13 | CARD 4 | Screened out CUNY Hunter College: no standalone STEM PhD (STEM PhDs administered via CUNY Graduate Center [cunygc]; Hunter doctorates are Nursing PhD/DNP, DPT, EdD). Source: https://www.hunter.cuny.edu/academics/majors-degree-tracks/
2026-11-13 | CARD 4 | desu | added Delaware State University (5 STEM PhD programs: chemistry, environment, math [also physics], neuro, physics)
2026-11-13 | CARD 4 | etsu | added East Tennessee State University (1 STEM PhD program: biomed [also neuro])
2026-11-13 | CARD 4 | Screened out East Texas A&M University: no STEM PhD in the 18 Atlas fields (doctoral majors are Counselor Education and Supervision PhD, Educational Administration EdD, English PhD, Higher Education EdD, Supervision, Curriculum and Instruction EdD, and an online cognition/education-focused Experimental Psychology PhD). Source: https://coursecatalog.tamuc.edu/grad/office-of-graduate-studies/
2026-11-13 | CARD 4 | emich | added Eastern Michigan University (1 STEM PhD program: materials [also cs, civil])
2026-11-13 | CARD 4 | famu | added Florida Agricultural and Mechanical University (8 STEM PhD programs: physics, environment, biomed, chemeng [also bme], civil, ece, materials, mech)
2026-11-13 | CARD 4 | jsums | added Jackson State University (5 STEM PhD programs: chemistry, environment, datasci [also cs, math, statistics], ece, civil)
2026-11-13 | CARD 4 | lsuneworleans | added Louisiana State University New Orleans (10 STEM PhD programs: biology, chemistry, neuro, cs, earth [also environment], math, physics, civil, ece, mech)
2026-11-13 | CARD 4 | marshall | added Marshall University (7 STEM PhD programs: biomed [also neuro], bme, civil, cs, datasci, ece, mech)
2026-11-13 | CARD 4 | montclair | added Montclair State University (1 STEM PhD program: environment)
2026-11-13 | CARD 4 | morganstate | added Morgan State University (6 STEM PhD programs: biology [also environment], cs [also datasci], ece, math, materials, civil)
2026-11-13 | CARD 7 | Refreshed business docs (362 universities, 3769 programs, 18 fields, Not stated 21%)
