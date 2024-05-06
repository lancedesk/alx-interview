#!/usr/bin/env python3
"""
Calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed.
    """
    if n <= 1:
        return n
    """
    Initialize an array to store the minimum operations
    required for each number of H characters
    """
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i  # Initialize to maximum possible value

        """
        Check all factors of i to find the minimum number of operations
        """
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
