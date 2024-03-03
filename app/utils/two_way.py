"""

"""

def calc_l(k1: float, k2: float) -> float:
    """
    Calculates the L. L must be less than 1 to make a profit.
    The lower the L, the higher the profit.

    Args:
        k1 (float): The betting odds for k1.
        k2 (float): The betting odds for k2.

    Returns:
        float: The variable L, representing the inverse of the sum of the inverse of the betting odds.
    """
    k1 = 1 / k1
    k2 = 1 / k2
    return k1 + k2


def calc_vn(v: float, kn: float, l: float) -> float:
    """
    Calculate the amount of money to bet on k1.

    Args:
        v (float): The total amount of money to be bet.
        kn (float): The value of k1 or k2.
        l (float): The value of l.

    Returns:
        float: The amount of money to bet on kn.
    """
    vn = 1 / kn
    l = 1 / l
    return vn * l * v


def two_way_amount_to_bet(k1: float, k2: float, v: float) -> tuple[float, float]:
    """
    Calculate the amount of money to bet on k1 and k2.

    Args:
        k1 (float): The betting odds for k1.
        k2 (float): The betting odds for k2.
        v (float): The total amount of money to be bet.

    Returns:
        Tuple[float, float]: The amount of money to bet on k1 and k2.
    """
    l = calc_l(k1, k2)
    if l >= 1:
        return 0, 0
    v1 = calc_vn(v, k1, l)
    v2 = calc_vn(v, k2, l)
    return v1, v2


def two_way_pct_profit(v1, v2, k1, k2, v):
    """
    Calculate the average percentage profit of the bet.

    Args:
        v1 (float): The amount of money to bet on k1.
        v2 (float): The amount of money to bet on k2.
        k1 (float): The betting odds for k1.
        k2 (float): The betting odds for k2.
        v (float): The total amount of money to be bet.

    Returns:
        float: The percentage profit of the bet.
    """
    pv1 = ((v1 * k1 - v) / v) * 100
    pv2 = ((v2 * k2 - v) / v) * 100
    return (pv1 + pv2) / 2
