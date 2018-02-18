from config import CHR_BITS

def readFile(fileName):
    """Reads a specified text file.

    @param fileName: a string containing the relative path of the target file
    @return: a string containing the entire contents of that text file
    """
    pass

def writeFile(fileName, text):
    """Writes some text to a specified file.

    @param fileName: a string containing the relative path of the target file
    @param text: a string containing the text to be written
    """
    pass

def isValid(text):
    """Determines if all the characters can be represented by allocated bits.

    @param text: a string containing the content in question
    @return: a boolean for whether or not the text can be handled
    """
    maxOrd = 2**CHR_BITS - 1
    for char in text:
        if ord(char) > maxOrd:
            return False
    return True


def countFrequency(text):
    """Counts the number of occurences of each character in a chunk of text.

    @param text: a string containing the characters to be counted
    @return: a dictionary containing the number of occurences of each character
    """
    pass

def buildTree(freqDict):
    """Constructs a Huffman tree from provided character frequencies.

    @param freqDict: a dictionary with all characters and their frequencies
    @return: a list-styled Huffman tree: [count, leftTree, rightTree]
    """
    pass

def makeCode(huffTree, prefix=""):
    """Recursively generates a prefix code from a given Huffman tree.

    @param huffTree: a list-styled Huffman tree: [count, leftTree, rightTree]
    @param prefix: a string of digits accumulated by traversing a branch
    @return: a dictionary containing the code
    """
    pass

def encode(codeDict, text):
    """Converts plaintext letters into their prefix code equivalent.

    @param codeDict: a dictionary containing the prefix code
    @param text: a string containing the original plaintext
    @return: a string representing the encoded text
    """
    pass

def writeOverhead(codeDict):
    """Generates the overhead dictionary for

    @param codeDict: a dictionary containing the prefix code
    @return:
    """
    pass

if __name__ == "__main__":
    # TODO: Write everything
