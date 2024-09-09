#!/usr/bin/python3
'''A program that reads stdin line by line, processes log data, and calculates statistics'''

import sys

status_count = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}

total_size = 0
line_counter = 0


def display_metrics():
    print('File size: {}'.format(total_size))
    for key, count in sorted(status_count.items()):
        if count > 0:
            print('{}: {}'.format(key, count))


try:
    for line in sys.stdin:
        line_parts = line.split(" ")

        if len(line_parts) < 2:
            continue

        try:
            status_code = line_parts[-2]
            file_size = int(line_parts[-1])
        except (ValueError, IndexError):
            continue

        if status_code in status_count:
            status_count[status_code] += 1

        total_size += file_size
        line_counter += 1

        if line_counter == 10:
            display_metrics()
            line_counter = 0

except KeyboardInterrupt:
    display_metrics()
    sys.exit(0)

except Exception as e:
    sys.stderr.write(f"Error: {e}\n")

finally:
    display_metrics()
