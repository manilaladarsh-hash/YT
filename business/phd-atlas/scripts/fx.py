"""Save official exchange rates for the fee estimates shown in the kit.

Source: Bank of Canada daily average rates (Valet API), quoted in CAD per unit.
The kit converts application fees to approximate INR and USD with these rates and
labels them as approximate, with the date. Re-run before each release.

Usage: python3 scripts/fx.py   -> writes data/fx.json
"""

import json
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
SERIES = {"USD": "FXUSDCAD", "GBP": "FXGBPCAD", "EUR": "FXEURCAD", "CHF": "FXCHFCAD",
          "INR": "FXINRCAD", "SEK": "FXSEKCAD", "NOK": "FXNOKCAD",
          "AUD": "FXAUDCAD", "NZD": "FXNZDCAD"}
URL = "https://www.bankofcanada.ca/valet/observations/" + ",".join(SERIES.values()) + "/json?recent=1"


def main():
    obs = requests.get(URL, timeout=30).json()["observations"][-1]
    cad_per = {"CAD": 1.0}
    for cur, series in SERIES.items():
        cad_per[cur] = float(obs[series]["v"])
    out = {"date": obs["d"], "source": "Bank of Canada daily average exchange rates",
           "source_url": "https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/",
           "cad_per_unit": cad_per}
    path = ROOT / "data" / "fx.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(f"wrote {path.relative_to(ROOT)} for {obs['d']}: 1 USD = {cad_per['USD'] / cad_per['INR']:.2f} INR")


if __name__ == "__main__":
    main()
