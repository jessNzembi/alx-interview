#!/usr/bin/python3
"""log parsing script"""

import sys
from collections import defaultdict


def parse_line(line):
    """parsing a line"""
    parts = line.split()
    if len(parts) != 10:
        return None
    ip_address, _, _, status_code, file_size = parts[:5]
    if not status_code.isdigit():
        return None
    return ip_address, int(status_code), int(file_size)


def print_metrics(total_file_size, status_code_counts):
    """prints the metrics"""
    print("Total file size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts.keys()):
        print("{}: {}".format(status_code, status_code_counts[status_code]))


def main():
    """main function"""
    total_file_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed_line = parse_line(line)
            if parsed_line:
                ip_address, status_code, file_size = parsed_line
                total_file_size += file_size
                status_code_counts[status_code] += 1
                line_count += 1

            if line_count == 10:
                print_metrics(total_file_size, status_code_counts)
                line_count = 0

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_code_counts)


if __name__ == "__main__":
    main()
