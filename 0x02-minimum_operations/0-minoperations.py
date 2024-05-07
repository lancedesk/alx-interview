#!/usr/bin/python3
"""
Module for calculating the fewest number of operations
needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed.
    """
    if n < 2:
        return 0
    
    num_operations = 0
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            num_operations += divisor
            n = n // divisor
            divisor -= 1
        divisor += 1
    return num_operations
