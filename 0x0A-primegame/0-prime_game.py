#!/usr/bin/python3
"""Prime game"""


def era_sieve(primes):
    """Use Erasthonenes sieve to find primes"""
    outter_idx = 0
    while outter_idx < len(primes):
        innner_idx = outter_idx + 1
        while innner_idx < len(primes):
            if primes[innner_idx] % primes[outter_idx] == 0:
                primes.pop(innner_idx)
            else:
                innner_idx += 1
            outter_idx += 1
    return primes


def isWinner(x, nums):
    """Get the game winner"""
    maria_score = 0
    ben_score = 0
    for game in range(x):
        primes_list = era_sieve([i for i in range(2, nums[game])])
        if len(primes_list) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    if maria_score > ben_score:
        return 'Maria'
    if ben_score > maria_score:
        return 'Ben'
    return None
