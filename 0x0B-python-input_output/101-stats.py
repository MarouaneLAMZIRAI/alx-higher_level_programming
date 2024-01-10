#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys

def print_stats(total_size, status_codes):
    """
    Prints the statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary with status codes and their counts.
    """
    print("File size: {:d}".format(total_size))
    for key in sorted(status_codes.keys()):
        print("{:s}: {:d}".format(key, status_codes[key]))

if __name__ == "__main__":
    try:
        total_size = 0
        status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                        "403": 0, "404": 0, "405": 0, "500": 0}
        count = 0

        for line in sys.stdin:
            count += 1
            tokens = line.split()
            if len(tokens) > 1 and tokens[-2].isdigit():
                total_size += int(tokens[-2])
            if len(tokens) > 2 and tokens[-2] in status_codes:
                status_codes[tokens[-2]] += 1

            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

