#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 2:
            size = int(parts[-1])
            status = int(parts[-2])
            total_size += size
            if status in status_codes:
                status_codes[status] += 1

            line_count += 1
            if line_count % 10 == 0:
                print(f"File size: {total_size}")
                for code in sorted(status_codes.keys()):
                    if status_codes[code] > 0:
                        print(f"{code}: {status_codes[code]}")
                print()

except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
