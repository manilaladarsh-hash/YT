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

## Phase 1 (D1 Subject-Test Schema Fix) ? 2026-10-29
- Added `"No subject test"` to `gre_subject` in `data/schema.json` (cited verbatim to ETS `score-users/about/subject-tests.html` and `test-takers/subject-tests/scores.html`), updated `data/fields.json` (`chemistry` `subject_gre: null` after May 2023 discontinuation), `data/staging/RESEARCH_BRIEF.md`, `product/templates/atlas.html`, `product/sample.py`, `product/build.py`, `product/content/playbook.md`, and `tests/test_product.py`.
- Applied via `handoff/apply_no_subject_test.py` to 1,953 live programs and 158 staged programs where `field not in {"physics", "math", "neuro"}` and `gre_subject.code == "Not stated"`.
- Validation: `data` (`285 universities, 2968 programs, 0 errors`), `data/staging` (`36 universities, 227 programs, 0 errors`), `pytest` (`22 passed, 2 skipped`, `rc=0`).
- Overall `Not stated` (`coverage.py`): `30% (9920/32648)` -> `24% (7967/32648)`.
