# Island Perimeter

`island_perimeter(grid)` returns the perimeter of the single island in
`grid`, a rectangular list of lists where `0` is water and `1` is land.
Cells are squares of side 1, connected horizontally and vertically.

## How it works

Each land cell adds 4 sides. Every pair of land cells sharing a side hides
2 of them, so the function subtracts 2 for each land neighbour above or to
the left (each shared side is counted once).

## Files

- `0-island_perimeter.py`: the `island_perimeter(grid)` function
- `0-main.py`: test file
