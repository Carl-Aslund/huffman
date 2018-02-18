from config import CHR_BITS

def binToDec(binStr):
    """Converts a binary string into a decimal number.

    @param bin: a string of 1's and 0's
    @return: an integer equivalent
    """
    decimal = 0
    for digit in binStr:
        decimal = 2 * decimal + int(digit)
    return decimal

def decToBin(dec):
    """Converts a decimal number into a binary string.

    @param dec: an integer in base-10
    @return: a binary-string equivalent
    """
    binStr = ""
    i = 1
    while dec > 0:
        if (dec % 2**i) != 0:
            binStr = "1" + binStr
            dec -= 2**(i-1)
        else:
            binStr = "0" + binStr
        i += 1
    return "0"*(CHR_BITS-len(binStr)) + binStr

def uniToBin(char):
    """Converts a Unicode character into a binary string.

    @param char: a unicode character (must not require more bits than available)
    @return: an equivalent binary string
    """
    decimal = ord(char)
    return decToBin(decimal)

def binToUni(binStr):
    """Converts a binary string into a Unicode character.

    @param char: a binary string
    @return: an equivalent Unicode character
    """
    decimal = binToDec(binStr)
    return chr(decimal)
