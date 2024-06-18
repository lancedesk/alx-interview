#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): List of coin values.
        total (int): Target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
             Returns -1 if total cannot be met by any combination of coins.

    Example:
        print(makeChange([1, 2, 25], 37))  # Output: 7
        print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
    """

    if total <= 0:
        return 0
    coins.sort(reverse=True)
    needed_coins = 0
    for coin in coins:
        if total / coin > 0:
            needed_coins = needed_coins + (total // coin)
            total = total % coin
        if not total:
            break

    if total != 0 or needed_coins == 0:
        return -1
    return needed_coins
