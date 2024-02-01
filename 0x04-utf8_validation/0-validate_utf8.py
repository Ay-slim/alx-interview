#!/usr/bin/python3
"""utf8 validation module"""


from typing import List


def isNthByteChar(binary: str) -> bool:
    """
    isNthByteChar - Confirms if first two bits are 1 and 0
    @binary: Binary rep in string to check
    Returns: Whether or not it's an Nth byte char
    """
    return binary[0] == '1' and binary[1] == '0'


def numberOfBytes(binary: str) -> int:
    """
    numberOfBytes - Number of bites based on leading bit
    @binary: Binary representation in string format
    """
    if (binary[0] == '0'):
        return 0
    byteCounter = 0
    while binary[byteCounter] == '1' and byteCounter < len(binary):
        byteCounter += 1
    return byteCounter


def validUTF8Trial(data: List[int]) -> bool:
    """
    validUTF8 - Validates UTF8 data
    @data: List of integers to validate
    Returns: Whether or not data is valid utf8
    """
    progressTracker = 0
    dataInBinary = list(map(lambda x: bin(x)[2:], data))
    print(dataInBinary)
    while progressTracker < len(data):
        numBytes = numberOfBytes(dataInBinary[progressTracker])
        if numBytes == 1:
            return False
        progressTracker += 1
        if (len(data) - progressTracker) < (numBytes - 1):
            return False
        for followingByte in range(
              progressTracker, progressTracker + numBytes):
            if not isNthByteChar(dataInBinary[followingByte]):
                return False
        progressTracker += numBytes - 1
    return True


def validUTF8(data: List[int]) -> bool:
    """
    validUTF8 - Validates UTF8 data
    @data: List of integers to validate
    Returns: Whether or not data is valid utf8
    """
    position = 0
    for byte in data:
        if position == 0:
            if byte >> 7 == 0b0:
                position = 0
            elif byte >> 5 == 0b110:
                position = 1
            elif byte >> 4 == 0b1110:
                position = 2
            elif byte >> 3 == 0b11110:
                position = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            position -= 1
    return position == 0
