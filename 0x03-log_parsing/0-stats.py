#!/usr/bin/python3
"""
log parsing
"""

import sys
import re


def output(total_size: int, line_count: int, status_counts: dict) -> None:
  """
  helper function to display stats
  """
  print(f"Total file size: {total_size}")
  for code, count in sorted(status_counts.items()):
    if count:
      print(f"{code}: {count}")


if __name__ == "__main__":
  regex = re.compile(
      r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\]"GET /projects/260 HTTP/1.1" (.{3}) (\d+)')

  line_count = 0
  total_size = 0
  status_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

  try:
    for line in sys.stdin:
      line = line.strip()
      match = regex.fullmatch(line)
      if match:
        line_count += 1
        code = match.group(1)
        file_size = int(match.group(2))

        # Update metrics
        total_size += file_size
        status_counts[code] += 1

        # Print statistics every 10 lines or on interruption
        if line_count % 10 == 0 or line_count == 1:
          output(total_size, line_count, status_counts.copy())  # Avoid modifying original dict

  except KeyboardInterrupt:
    # Print statistics on interruption
    output(total_size, line_count, status_counts.copy())

