# Questions for Owner Review

- UCL (University College London): All `ucl.ac.uk` prospective students, admissions, and departmental postgraduate research pages return Cloudflare 403 blocks (`chars=321`) to automated fetchers (`research.py`). Cannot fetch individual program pages or verify quotes until Cloudflare bypass or manual cache import is provided. 16 programs (`ucl--*.json`) marked in `audit_reviewed.csv` to proceed with remaining universities.
- `handoff/check.sh`: Updated staging check to only run `validate_data.py` on staging when files are present in `data/staging/`, preventing a false failure when all staged files have been successfully promoted into `data/`.
