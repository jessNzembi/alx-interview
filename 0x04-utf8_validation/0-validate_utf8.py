#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """
    Function to check if the given sequence
    of bytes follows UTF-8 encoding rules
    """
    def check_following_bytes(data, start_index, num_following):
        """Check if there are enough bytes remaining"""
        if len(data) < start_index + num_following:
            return False
        for i in range(start_index + 1, start_index + num_following + 1):
            if data[i] >> 6 != 0b10:
                return False
        return True

    i = 0
    while i < len(data):
        num_bytes = 0
        mask = 0b10000000
        while data[i] & mask:
            num_bytes += 1
            mask >>= 1

        if num_bytes == 1 or num_bytes > 4:
            return False

        if not check_following_bytes(data, i, num_bytes - 1):
            return False

        i += 1

    return True
