#!/usr/bin/env python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if the given data set represents a valid UTF-8 encoding.
    :param data: List of integers where each integer represents 1 byte.
    :return: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        """
        # Mask to get only the least significant 8 bits
        """
        byte = byte & 0xFF

        if num_bytes == 0:
            """
            # Determine how many bytes in the current UTF-8 character
            """
            if byte >> 7 == 0:
                """
                # 1-byte character (0xxxxxxx)
                """
                continue
            elif byte >> 5 == 0b110:
                """
                # 2-byte character (110xxxxx)
                """
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                """
                # 3-byte character (1110xxxx)
                """
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                """
                # 4-byte character (11110xxx)
                """
                num_bytes = 3
            else:
                """
                # Invalid first byte of a character
                """
                return False
        else:
            """
            # Continuation bytes must be in the form 10xxxxxx
            """
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
