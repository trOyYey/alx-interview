#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations needed to result in exactly n H characters in the file

    """
    if n <= 1:
        return 0
    primes = 0
    while n != 1:
        for i in range(2, n + 1):
            if (n % i) == 0:
                primes += i
                n = n // i
                break
    return primes
