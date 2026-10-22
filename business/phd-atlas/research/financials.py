"""Scenario model for the Physics PhD Atlas. Every number here is an ASSUMPTION
except Gumroad's published fees, checked 2026-10-21:
  - 10% + $0.50 per direct sale, plus card processing 2.9% + $0.30 (gumroad.com/help/article/66-gumroads-fees)
  - 30% flat on Discover marketplace sales, processing included (same page)
  - on a refund Gumroad returns its own fee; only the processing part is kept (same page)
  - PPP discounts range from 20% to 60% (gumroad.com/help/article/327-purchasing-power-parity)

Pricing (owner decision 2026-10-21: "it needs to be really affordable" for Indian students):
  $5 list price with PPP on and no cap. India's World Bank PPP factor (~22 INR per
  international $) is far below the market rate, so India is expected (ESTIMATE) to get the
  maximum 60% discount: about $2, shown in rupees at checkout, payable by UPI.

Usage: python3 research/financials.py   -> prints a markdown table, writes research/financials.csv
"""

import csv
from pathlib import Path

LIST_PRICE = 5.00           # USD, decision: affordability first
PPP_PRICE = 2.00
BATCH_PRICE = 20.00        # batch licence, up to 30 students
BATCH_PPP_PRICE = 8.00     # batch licence after the 60% PPP discount (India)            # ESTIMATE: India and similar countries at Gumroad's 60% maximum PPP discount
GUMROAD_PCT, GUMROAD_FLAT = 0.10, 0.50      # published, direct sales
DISCOVER_PCT = 0.30                          # published, Discover sales (processing included)
CARD_PCT, CARD_FLAT = 0.029, 0.30            # published processing on direct sales (UPI assumed the same)
PAYOUT_PCT = 0.02                            # ASSUMED currency-conversion cost on payout to a CAD bank account

SCENARIOS = {
    # name: (orders this season, orders next full season, share buying at PPP price,
    #        share via Discover, refund rate, owner hours this season, owner hours next season)
    "Conservative": (10, 50, 0.80, 0.00, 0.08, 12, 30),
    "Base": (40, 200, 0.75, 0.05, 0.05, 14, 34),
    "Optimistic": (120, 600, 0.70, 0.10, 0.04, 18, 45),
}


def per_sale_net(price, discover=False):
    """What one sale at this price leaves after Gumroad's fees (before refunds and payout)."""
    if discover:
        return round(price * (1 - DISCOVER_PCT), 2)
    return round(price - (GUMROAD_PCT * price + GUMROAD_FLAT) - (CARD_PCT * price + CARD_FLAT), 2)


def season(orders, ppp_share, discover_share, refund_rate, hours):
    gross_per = ppp_share * PPP_PRICE + (1 - ppp_share) * LIST_PRICE
    gross = orders * gross_per
    direct = orders * (1 - discover_share)
    disc = orders * discover_share
    gumroad_fee = direct * (GUMROAD_PCT * gross_per + GUMROAD_FLAT) * (1 - refund_rate)  # returned on refunds
    processing = direct * (CARD_PCT * gross_per + CARD_FLAT)                              # kept on refunds
    discover_fee = disc * DISCOVER_PCT * gross_per
    fees = gumroad_fee + processing + discover_fee
    refunds = refund_rate * gross
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
    print(f"Per sale after Gumroad fees: ${LIST_PRICE:.2f} -> ${per_sale_net(LIST_PRICE):.2f}; "
          f"${PPP_PRICE:.2f} (India, PPP) -> ${per_sale_net(PPP_PRICE):.2f}")
    print(f"Batch licence: ${BATCH_PRICE:.2f} (bought abroad, e.g. an alumnus sponsor) -> "
          f"${per_sale_net(BATCH_PRICE):.2f}; ${BATCH_PPP_PRICE:.2f} (India, PPP) -> "
          f"${per_sale_net(BATCH_PPP_PRICE):.2f}. One sponsored batch nets as much as "
          f"{per_sale_net(BATCH_PRICE) / per_sale_net(PPP_PRICE):.1f} Indian personal sales.\n")
    cols = ["scenario", "period", "orders", "avg_price", "gross", "platform_and_card_fees", "refunds", "payout_fee", "net", "owner_hours", "net_per_owner_hour"]
    print("| " + " | ".join(cols) + " |")
    print("|" + "---|" * len(cols))
    for r in rows:
        print("| " + " | ".join(str(r[c]) for c in cols) + " |")


if __name__ == "__main__":
    main()
