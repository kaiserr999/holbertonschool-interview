#!/usr/bin/python3
"""Make change with the fewest number of coins."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to reach total."""
    if total <= 0:
        return 0

    if not coins:
        return -1

    max_value = total + 1
    best = [max_value] * (total + 1)
    best[0] = 0

    for coin in sorted(set(coins)):
        if coin > total:
            continue

        for amount in range(coin, total + 1):
            candidate = best[amount - coin] + 1
            if candidate < best[amount]:
                best[amount] = candidate

    if best[total] == max_value:
        return -1

    return best[total]