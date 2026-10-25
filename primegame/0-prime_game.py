#!/usr/bin/python3
"""Prime game module."""


def isWinner(x, nums):
    """Return the name of the player who won the most rounds, or None.

    Each move removes one prime and its multiples, and no other prime is
    ever removed, so a round lasts exactly as many moves as there are
    primes up to n. Maria goes first: she wins when that count is odd.
    """
    if not isinstance(x, int) or x < 1 or not nums:
        return None
    rounds = nums[:x]
    limit = max(max(rounds), 1)
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, limit + 1, i):
                sieve[multiple] = False
    prime_count = [0] * (limit + 1)
    for i in range(1, limit + 1):
        prime_count[i] = prime_count[i - 1] + sieve[i]
    maria = 0
    for n in rounds:
        if n > 0 and prime_count[n] % 2 == 1:
            maria += 1
    ben = len(rounds) - maria
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
