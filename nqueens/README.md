# N Queens

`0-nqueens.py` prints every way to place N non-attacking queens on an N×N
chessboard, one solution per line, as a list of `[row, column]` pairs.

It uses backtracking: queens are placed row by row, skipping any column or
diagonal already under attack, and undoing the last placement when a row
has no safe square.

## Usage

```
./0-nqueens.py N
```

- Wrong number of arguments: prints `Usage: nqueens N` and exits with status 1
- N not an integer: prints `N must be a number` and exits with status 1
- N smaller than 4: prints `N must be at least 4` and exits with status 1

## Example

```
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```
