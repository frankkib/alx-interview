#!/usr/bin/python3
"""UTF-8  validation module"""


def validUTF8(data):
    """UTF-8 validation funtion"""
    num_of_bytes = 0
    for num in data:
        byte = num & 0xFF
        if num_of_bytes == 0:
            if (byte >> 7) == 0:
                continue
            elif (byte >> 5) == 0b110:
                num_of_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_of_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_of_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_of_bytes -= 1
    return num_of_bytes == 0
