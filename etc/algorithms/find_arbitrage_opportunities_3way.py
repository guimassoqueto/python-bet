# todo: add pydantic for type checking


def find_arbitrage_opportunities_3way(odds):
    # Initialize a dictionary to store the best odds for each outcome
    best_odds = {"Real Madrid": 0, "Barcelona": 0, "Draw": 0}

    # Loop through each bookmaker to find the best odds for each outcome
    for bookmaker, odds_list in odds.items():
        for odd in odds_list:
            for outcome, value in odd.items():
                if value > best_odds[outcome]:
                    best_odds[outcome] = value

    # Calculate the arbitrage percentage using the formula: 1/odd1 + 1/odd2 + 1/odd3 for a 3-way bet
    arbitrage_percentage = sum([1 / odd for odd in best_odds.values()])

    # If the arbitrage percentage is less than 1, there's an arbitrage opportunity
    is_arbitrage = arbitrage_percentage < 1
    return is_arbitrage, arbitrage_percentage, best_odds
