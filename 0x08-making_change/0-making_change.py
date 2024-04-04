#!/usr/bin/python3

def makeChange(coins, total):
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
