#!/usr/bin/python3

"""Change module"""


def makeChange(coins, total):
    """
    makeChange - Function to calculate min no of coins for change
    @coins: Array of available coin values
    @total: Total change to return
    Returns: Minimum no of coins
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    min_coins = 0
    for coin in coins:
        if total < coin:
            break
        min_coins += total // coin
        new_total = total % coin
        if new_total <= 0:
            return min_coins
        total = new_total
    return -1
