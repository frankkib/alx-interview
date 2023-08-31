#!/usr/bin/python3
"""
The N queen interview question
"""

import sys


def nqueens(n):
    """
    Solve the N queens puzzle and print solutions
    """
    board = [-1] * n
    solve_nqueens(board, 0, n)


def is_valid(board, row, col):
    """
    Check if it's safe to place a queen at the given row and column
    """
    for prev_row in range(row):
        if (
            board[prev_row] == col
            or abs(board[prev_row] - col) == abs(prev_row - row)
        ):
            return False
    return True


def solve_nqueens(board, row, n):
    """
    Recursively solve the N queens puzzle by placing queens on the board.
    """
    if row == n:
        print([board[i] for i in range(n)])
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("n must be 4")
        sys.exit(1)

    nqueens(n)
