"""Scenario model for the Physics PhD Atlas. Every number here is an ASSUMPTION
except Gumroad's published 10% + $0.50 direct-sale fee and 30% Discover fee
(gumroad.com/pricing, checked 2026-10-21).

Usage: python3 research/financials.py   -> prints a markdown table, writes research/financials.csv
"""

import csv
from pathlib import Path

LIST_PRICE = 15.00          # USD, hypothesis to test
PPP_PRICE = 7.50            # Gumroad PPP with discount capped at 50% (India)
GUMROAD_PCT, GUMROAD_FLAT = 0.10, 0.50      # published, direct sales
DISCOVER_PCT = 0.30                          # published, Discover marketplace sales
CARD_PCT, CARD_FLAT = 0.029, 0.30            # ASSUMED extra processing cost (conservative)
PAYOUT_PCT = 0.02                            # ASSUMED PayPal payout fee if bank deposit unavailable

SCENARIOS = {
    # name: (orders this season, orders next full season, share buying at PPP price,
    #        share via Discover, refund rate, owner hours this season, owner hours next season)
    "Conservative": (5, 30, 0.70, 0.00, 0.10, 12, 30),
    "Base": (25, 120, 0.60, 0.05, 0.07, 14, 34),
    "Optimistic": (80, 400, 0.50, 0.10, 0.05, 18, 45),
}


def season(orders, ppp_share, discover_share, refund_rate, hours):
    gross_per = ppp_share * PPP_PRICE + (1 - ppp_share) * LIST_PRICE
    gross = orders * gross_per
    direct = orders * (1 - discover_share)
    disc = orders * discover_share
    fees = (direct * (GUMROAD_PCT * gross_per + GUMROAD_FLAT)
            + disc * (DISCOVER_PCT * gross_per)
            + orders * (CARD_PCT * gross_per + CARD_FLAT))
    refunds = refund_rate * gross            # conservative: fees on refunded orders are not returned
    payout = PAYOUT_PCT * max(gross - fees - refunds, 0)
    net = gross - fees - refunds - payout
    return {
        "orders": orders, "avg_price": round(gross_per, 2), "gross": round(gross, 2), "platform_and_card_fees": round(fees, 2),
        "refunds": round(refunds, 2), "payout_fee": round(payout, 2), "fixed_costs": 0.0, "net": round(net, 2),
        "owner_hours": hours, "net_per_owner_hour": round(net / hours, 2) if hours else 0.0,
    }


def main():
    rows = []
    for name, (o1, o2, ppp, disc, ref, h1, h2) in SCENARIOS.items():
        rows.append({"scenario": name, "period": "This season (Nov 2026-Jan 2027)", **season(o1, ppp, disc, ref, h1)})
        rows.append({"scenario": name, "period": "Next full season (Aug 2027-Jan 2028)", **season(o2, ppp, disc, ref, h2)})
    out = Path(__file__).with_name("financials.csv")
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    cols = ["scenario", "period", "orders", "avg_price", "gross", "platform_and_card_fees", "refunds", "payout_fee", "net", "owner_hours", "net_per_owner_hour"]
    print("| " + " | ".join(cols) + " |")
    print("|" + "---|" * len(cols))
    for r in rows:
        print("| " + " | ".join(str(r[c]) for c in cols) + " |")


if __name__ == "__main__":
    main()
