#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys


def computes_metric(total_size, status_codes):
    """ Prints computed metric """
    print(f"File size: {total_size}")
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print(f"{key}: {value}")


total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 2:
            size = int(parts[-1])
            status = (parts[-2])
            total_size += size
            if status in status_codes:
                status_codes[status] += 1

            line_count += 1

            if line_count % 10 == 0:
                computes_metric(total_size, status_codes)
                line_count = 0

except KeyboardInterrupt:
    pass
finally:
    computes_metric(total_size, status_codes)
