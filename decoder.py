from config import CHR_BITS
from unicodeBinary import binToDec, textToBin
from math import log2, ceil

def readFile(fileName):
    """Reads a specified text file.

    @param fileName: a string containing the relative path of the target file
    @return: a string containing the entire contents of that text file
    """
    openFile = open(fileName, 'r')
    contents = openFile.read()
    openFile.close()
    return contents

def writeFile(fileName, text):
    """Writes some text to a specified file.

    @param fileName: a string containing the relative path of the target file
    @param text: a string containing the text to be written
    """
    openFile = open(fileName, 'w')
    openFile.write(text)
    openFile.close()
    return

def readOverhead(binText):
    """Processes the overhead of a Huffman-encoded file.

    @param binText: the binary string obtained from converting the encoded file
    @return: a dictionary containing the code
    @return: the portion of the binary string containing the encoded message
    """
    frontBits = ceil(log2(CHR_BITS)) # Bits needed at front for zeroes
    binText = textToBin(binText)
    frontZeroes = binText[:frontBits]
    numZeroes = binToDec(frontZeroes) # Provides the number of ending zeroes
    leftoverText = binText[frontBits:] # Portion of text without leading bits
    i = 0
    codeDict = {}
    for charInt in range(2**CHR_BITS):
        numBitsBits = leftoverText[i:i+CHR_BITS]
        numBits = binToDec(numBitsBits)
        i += CHR_BITS
        if numBits == 0:
            continue
        else:
            codeDict[leftoverText[i:i+numBits]] = chr(charInt)
            i += numBits
    encodedText = binText[i:-numZeroes]
    return codeDict, encodedText

def decode(codeDict, encoded):
    """Converts prefix code into its plaintext equivalent.

    @param codeDict: a dictionary containing the prefix code
    @param encoded: a binary string containing the encoded text
    @return: a string representing the original plaintext
    """
    plaintext = ""
    i = 0
    for j in range(len(encoded)):
        if encoded[i:j+1] in codeDict:
            plaintext += codeDict[encoded[i:j+1]]
            i = j+1
    return plaintext

def main():
    name = input("Enter the name of the compressed file: ")
    contents = readFile("compressed/"+name+".huff")
    codeD, encoded = readOverhead(contents)
    plaintext = decode(codeD, encoded)
    writeFile("decompressed/"+name+".txt", plaintext)

if __name__ == "__main__":
    main()
