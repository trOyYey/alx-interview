#!/usr/bin/python3
"""
utf8 module
"""


def binary(x):
    '''
        validates number of bytes
    '''
    for i in range(7, 2, -1):
        if not x >> i & 1:
            return 7 - i
    return -1


def validUTF8(data):
    '''
        validates UTF-8 incoded data
    '''
    prev = 0
    for x in data:
        n_bytes = binary(x)
        if prev == 0:
            if n_bytes == 1:
                return False
            else:
                prev = n_bytes
        elif n_bytes != 1:
            return False
        prev = prev - 1 if prev != 0 else prev

    return prev == 0
