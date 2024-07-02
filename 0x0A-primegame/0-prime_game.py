#!/usr/bin/python3
"""
Determine the winner of each round of the prime game.
"""


def isWinner(x, nums):
    """
    Determine the winner of each round of the prime game.

    Args:
    - x: Number of rounds
    - nums: List of integers n for each round

    Returns:
    - Name of the player that won the most rounds ('Maria' or 'Ben')
    - None if the winner cannot be determined (tie)
    """
    def sieve_of_eratosthenes(max_num):
        """
        Return a list of primes up to max_num (inclusive)
        using Sieve of Eratosthenes.
        """
        is_prime = [True] * (max_num + 1)
        p = 2
        while (p * p <= max_num):
            if is_prime[p]:
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes
        return [p for p in range(max_num + 1) if is_prime[p]]

    max_n = max(nums)  # Find the maximum n in the input
    primes = sieve_of_eratosthenes(max_n)  # Find all primes up to max_n

    results = []
    for n in nums:
        if n == 1:
            # If n is 1, Ben wins because there are no prime numbers
            # for Maria to choose
            results.append('Ben')
            continue

        # Simulate the game for this round
        current_set = set(range(1, n + 1))
        maria_turn = True
        while True:
            prime_chosen = False
            for p in primes:
                if p in current_set:
                    prime_chosen = True
                    current_set.difference_update(range(p, n + 1, p))
                    break
            if not prime_chosen:
                break
            maria_turn = not maria_turn

        # Determine the winner of this round
        if maria_turn:
            results.append('Ben')  # Maria cannot make a move
        else:
            results.append('Maria')  # Ben cannot make a move

    # Count the wins
    maria_wins = results.count('Maria')
    ben_wins = results.count('Ben')

    # Determine the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None  # Tie case
