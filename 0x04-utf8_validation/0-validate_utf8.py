#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    # Loop through each byte in the data
    i = 0
    while i < len(data):
        # Check if the current byte is a single-byte character (ASCII)
        if data[i] >> 7 == 0:
            i += 1
        else:
            # Determine the number bytes for the multi-byte character
            num_bytes = 0
            while (data[i] >> (7 - num_bytes)) & 1:
                num_bytes += 1
            # Check if the number of bytes is within the valid range
            if num_bytes < 2 or num_bytes > 4:
                return False
            # Check continuation bytes
            for j in range(1, num_bytes):
                i += 1
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            i += 1  # Move to the next character
    return True
