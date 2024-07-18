#!/usr/bin/python3
"""
log parsing
"""


from collections import defaultdict


# Define valid status codes
VALID_STATUS_CODES = {200, 301, 400, 401, 403, 404, 405, 500}

total_size = 0
line_count = 0
status_counts = defaultdict(int)

try:
    for line in iter(input, ""):
        line_count += 1

        parts = line.split()

        if len(parts) != 6 or not parts[0].isdigit() or not
        parts[-2].isdigit():
            continue

        file_size = int(parts[-1])

        total_size += file_size
        status_counts[int(parts[-2])] += 1

        if line_count % 10 == 0 or line_count == 1:
            print(f"Total file size: {total_size}")
            for code, count in sorted(status_counts.items()):
                if code in VALID_STATUS_CODES:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if code in VALID_STATUS_CODES:
            print(f"{code}: {count}")
