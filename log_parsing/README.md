# Log Parsing

`0-stats.py` reads HTTP log lines from stdin, in the format
`<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`,
and prints metrics every 10 lines and on `CTRL + C`:

- `File size: <total size>`: the sum of all file sizes read so far
- `<status code>: <number>`: the line count for each status code
  (200, 301, 400, 401, 403, 404, 405, 500), in ascending order, only for
  codes that appeared

Lines that don't match the format are skipped.

## Files

- `0-stats.py`: the log parsing script
- `0-generator.py`: generates random log lines for testing

## Usage

```
./0-generator.py | ./0-stats.py
```
