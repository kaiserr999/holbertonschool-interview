#!/usr/bin/python3
"""Read HTTP log lines from stdin and print size and status code metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print the total file size and the count of each status code."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Parse stdin, printing stats every 10 lines and on interruption."""
    codes = ("200", "301", "400", "401", "403", "404", "405", "500")
    status_counts = {code: 0 for code in codes}
    total_size = 0
    line_count = 0
    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 2:
                continue
            try:
                total_size += int(parts[-1])
            except ValueError:
                continue
            if parts[-2] in status_counts:
                status_counts[parts[-2]] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    finally:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
