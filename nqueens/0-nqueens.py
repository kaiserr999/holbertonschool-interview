#!/usr/bin/python3
"""Print every solution to the N queens puzzle using backtracking."""
import sys


def solve(n, row, queens, cols, diags, anti_diags):
    """Place a queen on each row from row onward, printing full boards.

    queens holds the [row, col] pairs placed so far; cols, diags and
    anti_diags hold the columns and diagonals already under attack.
    """
    if row == n:
        print(queens)
        return
    for col in range(n):
        if col in cols or row - col in diags or row + col in anti_diags:
            continue
        queens.append([row, col])
        cols.add(col)
        diags.add(row - col)
        anti_diags.add(row + col)
        solve(n, row + 1, queens, cols, diags, anti_diags)
        queens.pop()
        cols.remove(col)
        diags.remove(row - col)
        anti_diags.remove(row + col)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(n, 0, [], set(), set(), set())
