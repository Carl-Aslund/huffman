from config import CHR_BITS

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
    @return: the portion of the binary string containing the
    """
    pass

def decode(codeDict, binText):
    """Converts prefix code into its plaintext equivalent.

    @param codeDict: a dictionary containing the prefix code
    @param binText: a string containing the encoded text
    @return: a string representing the original plaintext
    """
    pass

if __name__ == "__main__":
    # TODO: Write everything
