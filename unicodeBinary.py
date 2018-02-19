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

def decToBin(dec, bits=CHR_BITS):
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
    return "0"*(bits-len(binStr)) + binStr

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

def textToBin(text):
    """Converts unicode text into a binary string.

    @param text: a string of plaintext input
    @return: a string representing the binary output
    """
    binText = ""
    for char in text:
        binText += uniToBin(char)
    return binText

def binToText(text):
    """Converts a binary string into unicode text.

    @param text: a string of binary input
    @return: a string of translated plaintext
    """
    if len(text)%CHR_BITS != 0:
        print("ERROR: Invalid binary input length.")
    else:
        output = ""
        for i in range(0, len(text), CHR_BITS):
            output += binToUni(text[i:i+CHR_BITS])
        return output
