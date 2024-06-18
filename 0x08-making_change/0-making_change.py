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

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
