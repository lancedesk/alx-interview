#!/usr/bin/env python3
"""
Reads stdin line by line and computes metrics.
"""

import sys


def print_statistics(total_size, status_codes):
    """
    Prints the computed statistics.
    """
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        print("{}: {}".format(code, count))


def main():
    """
    Main function to read stdin and compute metrics.
    """
    total_size = 0
    status_codes = {
                    '200': 0,
                    '301': 0,
                    '400': 0,
                    '401': 0,
                    '403': 0,
                    '404': 0,
                    '405': 0,
                    '500': 0
                   }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.strip().split()
            if len(parts) >= 9:
                status_code = parts[-3]
                file_size = parts[-1]
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += int(file_size)
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
