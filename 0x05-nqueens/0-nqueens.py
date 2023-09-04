#!/usr/bin/python3
"""
The N queens puzzle
"""

import sys


def nqueens(N):
    """
    Solve the N queens puzzle and print solutions
    """
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

    def solve_nqueens(board, row, N):
        """
        Recursively solve the N queens puzzle by placing queens on the board.
        """
        if row == N:
            print([[i, board[i]] for i in range(N)])
            return

        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve_nqueens(board, row + 1, N)

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
