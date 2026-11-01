#!/usr/bin/env bash
# Run every check. Prints ALL CHECKS PASSED or the name of the check that failed.
# Usage: bash handoff/check.sh          (run from business/phd-atlas)
cd "$(dirname "$0")/.." || exit 1
fail() { echo; echo "FAILED: $1 -- fix this before you commit."; exit 1; }
python3 scripts/validate_data.py --dir data --require-cache | tail -1; [ "${PIPESTATUS[0]}" -eq 0 ] || fail "live data validation"
if ls data/staging/universities/*.json data/staging/programs/*.json >/dev/null 2>&1; then
    python3 scripts/validate_data.py --dir data/staging --require-cache | tail -1; [ "${PIPESTATUS[0]}" -eq 0 ] || fail "staging validation"
fi
python3 scripts/audit_quality.py | tail -4
python3 scripts/coverage.py | sed -n 1,2p
echo; echo "ALL CHECKS PASSED"
