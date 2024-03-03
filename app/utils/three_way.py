"""
v: total amount of money to be bet

k1: betting odds for k1
k2: betting odds for k2
k3: betting odds for k3

l1: the inverse of the sum of the inverse of the betting odds
l2: the division of k1 and k2
l3: the value of l3 based on the given l2 and k3

v1: the amount of money to bet on k1
v2: the amount of money to bet on k2
v3: the amount of money to bet on k3
"""


def calc_l1(k1: float, k2: float, k3: float) -> float:
    """
    Calculates the L. L must be less than 1 to make a profit.
    The lower the L, the higher the profit.

    Args:
        k1 (float): The betting odds for k1.
        k2 (float): The betting odds for k2.
        k3 (float): The betting odds for k3.

    Returns:
        float: The variable L, representing the inverse of the sum of the inverse of the betting odds.
    """
    k1 = 1 / k1
    k2 = 1 / k2
    k3 = 1 / k3
    return k1 + k2 + k3


def calc_l2(k1: float, k2: float) -> float:
    """
    Calculates the division of two numbers.

    Args:
        k1 (float): The betting odds for k1.
        k2 (float): The betting odds for k2.

    Returns:
        float: The result of the division.
    """
    return k1 / k2


def calc_l3(l2: float, k3: float) -> float:
    """
    Calculate the value of l3 based on the given l2 and k3.

    Args:
        l2 (float): The value of l2.
        k3 (float): The value of k3.

    Returns:
        float: The calculated value of l3.
    """
    l2 = 1 + l2
    k3 = k3 - 1
    return l2 / k3


def calc_v1(v: float, l2: float, l3: float) -> float:
    """
    Calculate the amount of money to bet on k1.

    Args:
        v (float): The total amount of money to be bet.
        l2 (float): The value of l2.
        l3 (float): The value of l3.

    Returns:
        float: The amount of money to bet on k1.
    """
    return v / (1 + l2 + l3)


def calc_v2(v: float, l2: float, l3: float) -> float:
    """
    Calculate the amount of money to bet on k2.

    Args:
        v (float): The total amount of money to be bet.
        l2 (float): The value of l2.
        l3 (float): The value of l3.

    Returns:
        float: The amount of money to bet on k2.
    """
    return (l2 * v) / (1 + l2 + l3)


def calc_v3(v: float, l2: float, l3: float) -> float:
    """
    Calculate the amount of money to bet on k3.

    Args:
        v (float): The total amount of money to be bet.
        l2 (float): The value of l2.
        l3 (float): The value of l3.

    Returns:
        float: The amount of money to bet on k3.
    """
    return (l3 * v) / (1 + l2 + l3)


def three_way_amount_to_bet(k1: float, k2: float, k3: float, v: float) -> tuple[float, float, float]:
    """
    Calculate the amount of money to bet on each outcome.

    Args:
        v (float): The total amount of money to be bet.
        k1 (float): The betting odds for k1.
        k2 (float): The betting odds for k2.
        k3 (float): The betting odds for k3.

    Returns:
        tuple: The amount of money to bet on each outcome.
    """
    l1 = calc_l1(k1, k2, k3)
    if l1 > 1:
        return 0, 0, 0
    l2 = calc_l2(k1, k2)
    l3 = calc_l3(l2, k3)
    v1 = calc_v1(v, l2, l3)
    v2 = calc_v2(v, l2, l3)
    v3 = calc_v3(v, l2, l3)
    return v1, v2, v3


def three_way_pct_profit(v1, v2, v3, k1, k2, k3, v):
    """
    Calculate the average percentage profit of the bet.

    Args:
        v1 (float): The amount of money to bet on k1.
        v2 (float): The amount of money to bet on k2.
        v3 (float): The amount of money to bet on k3.
        k1 (float): The betting odds for k1.
        k2 (float): The betting odds for k2.
        k3 (float): The betting odds for k3.
        v (float): The total amount of money to be bet.

    Returns:
        float: The percentage profit of the bet.
    """
    pv1 = ((v1 * k1 - v) / v) * 100
    pv2 = ((v2 * k2 - v) / v) * 100
    pv3 = ((v3 * k3 - v) / v) * 100
    return (pv1 + pv2 + pv3) / 3