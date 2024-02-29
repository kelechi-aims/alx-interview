#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine
    the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    count = 0
    coin_index = 0
    n = len(coins)
    while total > 0:
        if coin_index >= n:
            return -1
        if total - sorted_coins[coin_index] >= 0:
            total -= sorted_coins[coin_index]
            count += 1
        else:
            coin_index += 1
    return count
