#!/usr/bin/python3
"""A script that read stdin line and computes the metrics
"""
import sys

def print_statistics(total_size, status_counts):
    """function that prints all the sizes and counts"""
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

def main():
    """the main function initialization"""
    total_size = 0
    status_counts = {}
    try:
        line_count = 0
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            if len(parts) != 10:
                continue
            ip, _, _, method, path, _, status_code, size, *_ = parts
            try:
                size = int(size)
                status_code = int(status_code)
            except ValueError:
                continue
            total_size += size
            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()

