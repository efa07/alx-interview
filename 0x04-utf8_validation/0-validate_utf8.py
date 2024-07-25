#!/usr/bin/python3


def validUTF8(data):
    """UTF-8 Validtor"""

    n_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Extract the 8 least significant bits of num
        num = num & 0xFF

        if n_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (num & mask1) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (num & (mask1 >> 1)) == mask1:
                n_bytes = 1
            elif (num & (mask1 >> 2)) == (mask1 >> 1):
                n_bytes = 2
            elif (num & (mask1 >> 3)) == (mask1 >> 2):
                n_bytes = 3
            else:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
