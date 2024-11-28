#!/usr/bin/python3
'''
making_change file
'''


def makeChange(coins, total):
    '''
    Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total
    '''
    if total <= 0:
        return 0
    c = sorted(coins, reverse=True)
    change = 0
    for coin in c:
        while total - coin >= 0:
            change += 1
            total -= coin
    return change if total == 0 else -1
