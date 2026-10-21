# Maintenance schedule

| When | What | Who | Time |
|---|---|---|---|
| Every Monday 13:00 UTC | `source-watch` GitHub Action re-reads every cited page and opens or updates an issue listing quotes that disappeared | Automated | 0 |
| Weekly | Review the issue (if any) and the inbox (see `WEEKLY_CHECKLIST.md`) | You | 20–30 min |
| Monthly in season (Nov, Dec, Jan) | Data refresh session: re-fetch, re-validate, add programs, rebuild, ship as v1.x | Claude session, then you upload | ~30 min of your time |
| Dec 15, 2026 | Validation gate decision | You | 15 min |
| Jan 15, 2027 | Season close: record results and lessons in Notion; set the listing to passive | You plus a Claude session | 20 min |
| August each year | New-cycle edition (if the gate passed) | Claude session, then you upload and relaunch | 1–2 h |

## How a data refresh works (for the Claude session)
1. `python3 scripts/research.py <url> --refresh --profile` for each changed page, then update `data/programs/<id>.json` with the new code, value, quote and URL.
2. `python3 scripts/validate_data.py --require-cache` must report 0 errors.
3. Bump `VERSION` in `product/build.py`, then run `python3 product/build.py` and `python3 -m pytest -q tests`.
4. `python3 scripts/check_sources.py --manifest`, then commit.

## Known automation limits
- Columbia's pages block automated fetching, so they appear in the weekly report as "could not be fetched". Spot-check them by hand monthly.
- The weekly check detects disappearing quotes, not new information. A program could add a new waiver without removing old text. The monthly refresh covers that.
