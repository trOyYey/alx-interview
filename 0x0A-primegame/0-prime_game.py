#!/usr/bin/python3
'''
prime_game mod
'''


def PrimesArray(n):
    '''
    Returns array up to n where the index
    '''
    if n <= 0:
        return []
    tray = [True for i in range(n + 1)]
    tray[0], tray[1] = False, False
    i = 2
    while(i * i <= n):
        if tray[i]:
            for j in range(i * i, n + 1, i):
                tray[j] = False
        i += 1
    return tray


def isWinner(x, nums):
    '''
    returns the winner betwent Maria and Ben
    '''
    if x <= 0 or nums is None:
        return

    numsL = len(nums)
    primes = builPrimesArray(max(nums))
    M = 0
    B = 0
    for round in range(x):
        valid = [n for n in range(2, nums[round % numsL] + 1) if primes[n]]
        if len(valid) % 2 == 1:
            M += 1
        else:
            B += 1
    if B == M:
        return
    elif B > M:
        return 'Ben'
    else:
        return 'Maria'