#!/usr/bin/python3


def validUTF8(data):
    """UTF-8 Validation"""
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & num:
                n_bytes += 1
                mask >>= 1
            # 1-byte character
            if n_bytes == 0:
                continue
            # Invalid scenarios according to UTF-8 encoding rules
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1

    return n_bytes == 0
