#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """coin change problem"""
    if total <= 0:
        return 0

    count = 0
    while total > 0:
        if not coins:
            return -1
        if max(coins) > total:
            coins.remove(max(coins))
        else:
            total -= max(coins)
            count += 1
    return count
