#!/usr/bin/python3
'''
0-nqueens.py mod
'''
from sys import argv, exit


def main():
    ''' enrty point '''
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    elif not argv[1].isnumeric():
        print('N must be a number')
        exit(1)
    N = int(argv[1])
    if N < 4:
        print('N must be at least 4')
        exit(1)
    return N


def validate(board, index, N):
    '''  '''
    y, x = index
    for i in range(y - 1, -1, -1):
        if board[i][x]:
            return False
        lft = x - (y - i)
        rt = x + (y - i)
        if lft >= 0 and board[i][lft]:
            return False
        if rt < N and board[i][rt]:
            return False
    return True


def nqueens(board, index, N, boards):
    '''main function'''
    y, x = index
    if y == N:
        return True
    if validate(board, index, N):
        board[y][x] = 1
        for i in range(N):
            if nqueens(board, (y + 1, i), N, boards):
                boards.append([[i, board[i].index(1)] for i in range(N)])
                break

        board[y][x] = 0


if __name__ == '__main__':
    N = main()
    board = [[0 for a in range(N)] for b in range(N)]
    boards = []
    for i in range(N):
        value = nqueens(board, (0, i), N, boards)
        board[0][i] = 0
    for board in boards:
        print(board)
