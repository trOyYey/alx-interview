#!/usr/bin/python3
'''
prime_game mod
'''


def Priming(n):
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
    primes = Priming(max(nums))
    Mari = 0
    Beni = 0
    for round in range(x):
        valid = [n for n in range(2, nums[round % numsL] + 1) if primes[n]]
        if len(valid) % 2 == 1:
            Mari += 1
        else:
            Beni += 1
    if Beni == Mari:
        return
    elif Beni > Mari:
        return 'Ben'
    else:
        return 'Maria'
