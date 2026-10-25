#!/usr/bin/python3
"""Minimum operations module."""


def minOperations(n):
    """Return the fewest Copy All / Paste operations to get n H characters.

    The answer is the sum of the prime factors of n: reaching a multiple
    k * m of the current count costs one Copy All and k - 1 Pastes.
    Returns 0 if n cannot be reached (n < 2 or not an integer).
    """
    if not isinstance(n, int) or n < 2:
        return 0
    operations = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    if n > 1:
        operations += n
    return operations
