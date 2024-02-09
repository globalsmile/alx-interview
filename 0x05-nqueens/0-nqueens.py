#!/usr/bin/python3
"""N queens problem"""
import sys


def isSafe(board, row, col, n):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or \
          board[i] + i == col + row:
            return False
    return True


def solveNQ(board, row, n):
    if row == n:
        print(str([[i, board[i]] for i in range(n)]))
    for i in range(n):
        if isSafe(board, row, i, n):
            board[row] = i
            solveNQ(board, row + 1, n)


def nqueens(n):
    if n < 4:
        print("N must be at least 4")
        exit(1)
    board = [0 for i in range(n)]
    solveNQ(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    nqueens(n)
