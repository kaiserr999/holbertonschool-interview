#!/usr/bin/python3
"""UTF-8 validation module."""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else False.

    Each integer in data is one byte; only its 8 least significant bits
    are used. A character is 1 to 4 bytes long: the leading byte tells
    how many continuation bytes (10xxxxxx) must follow.
    """
    remaining = 0
    for value in data:
        byte = value & 0xFF
        if remaining:
            if byte >> 6 != 0b10:
                return False
            remaining -= 1
        elif byte >> 7 == 0:
            continue
        elif byte >> 5 == 0b110:
            remaining = 1
        elif byte >> 4 == 0b1110:
            remaining = 2
        elif byte >> 3 == 0b11110:
            remaining = 3
        else:
            return False
    return remaining == 0
