# Prime Game

Maria and Ben take turns picking a prime from the set `1..n` and removing it
with all its multiples; the player who cannot move loses. Maria always goes
first and both play optimally.

`isWinner(x, nums)` plays `x` rounds (one per `n` in `nums`) and returns the
name of the player who won the most rounds, or `None` on a tie.

## How it works

Each move removes exactly one prime (its multiples are never prime), so a
round lasts as many moves as there are primes up to `n`. Maria wins when
that count is odd. A sieve of Eratosthenes counts the primes once for every
`n` up to the largest one.

## Files

- `0-prime_game.py`: the `isWinner(x, nums)` function
- `main_0.py`: test file
