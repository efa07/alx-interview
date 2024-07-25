#!/usr/bin/python3
"""UTF-8 Validation"""


def count_leading_ones(byte):
    """Returns the number of leading 1s in the given byte."""
    leading_ones = 0
    mask = 1 << 7
    while mask & byte:
        leading_ones += 1
        mask >>= 1
    return leading_ones


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    remaining_bytes = 0
    for byte in data:
        if remaining_bytes == 0:
            remaining_bytes = count_leading_ones(byte)
            # 1-byte character (0xxxxxxx)
            if remaining_bytes == 0:
                continue
            # A character in UTF-8 can be 1 to 4 bytes long
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            # Check if the byte has the format 10xxxxxx
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
        remaining_bytes -= 1
    return remaining_bytes == 0
