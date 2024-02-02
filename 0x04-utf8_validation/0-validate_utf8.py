#!/usr/bin/python3
def validUTF8(data):
    """Validates if a given data set represents a valid UTF-8 encoding"""
    bytes = 0
    for byte in data:
        byte = format(byte, '#010b')[-8:]
        if bytes == 0:
            for bit in byte:
                if bit == '0':
                    break
                bytes += 1
            if bytes == 0:
                continue
            if bytes == 1 or bytes > 4:
                return False
        else:
            if not (byte[0] == '1' and byte[1] == '0'):
                return False
        bytes -= 1
    return bytes == 0