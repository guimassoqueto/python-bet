from app.utils.two_way import two_way_amount_to_bet, two_way_pct_profit


if __name__ == "__main__":
    k1 = 1.5
    k2 = 9.5
    v = 100
    v1, v2 = two_way_amount_to_bet(k1, k2, v)
    print(f"Amount to bet on k1: {v1:.2f}")
    print(f"Amount to bet on k2: {v2:.2f}")

    pct_profit = two_way_pct_profit(v1, v2, k1, k2, v)
    print(f"Percentage profit: {pct_profit:.2f}%")
