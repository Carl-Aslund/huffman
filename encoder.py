from config import CHR_BITS
from functools import reduce

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
            print("ERROR: "+char+" cannot be represented by "+CHR_BITS+" bits.")
            return False
    return True

def countFrequency(text):
    """Counts the number of occurences of each character in a chunk of text.

    @param text: a string containing the characters to be counted
    @return: a dictionary containing the number of occurences of each character
    """
    freqDict = {}
    for char in text:
        if char in freqDict:
            freqDict[char] += 1
        else:
            freqDict[char] = 1
    return freqDict

def leafMin(leaf1, leaf2):
    """Returns the lesser of two leaves.

    @param leaf1: the first leaf
    @param leaf2: the second leaf
    return: the lesser leaf between leaf1 and leaf2
    """
    if leaf1[0] < leaf2[0]:
        return leaf1
    else:
        return leaf2

def buildTree(freqDict):
    """Constructs a Huffman tree from provided character frequencies.

    @param freqDict: a dictionary with all characters and their frequencies
    @return: a list-styled Huffman tree: [count, leftTree, rightTree]
    """
    protoTree = [[freqDict[key],key] for key in freqDict]
    while len(protoTree) > 2:
        firstLeaf = reduce(leafMin,protoTree)
        protoTree.remove(firstLeaf)
        secondLeaf = reduce(leafMin,protoTree)
        protoTree.remove(secondLeaf)
        newLeaf = [firstLeaf[0]+secondLeaf[0], [firstLeaf[1],secondLeaf[1]]]
        protoTree.append(newLeaf)
    huffTree = [protoTree[0][1],protoTree[1][1]]
    return huffTree

def makeCode(huffTree, prefix=""):
    """Recursively generates a prefix code from a given Huffman tree.

    @param huffTree: a list-styled Huffman tree: [count, leftTree, rightTree]
    @param prefix: a string of digits accumulated by traversing a branch
    @return: a dictionary containing the code
    """
    if type(huffTree) == type(''):
        return {huffTree : prefix}
    else:
        leftDict = makeCode(huffTree[0], prefix+"0")
        rightDict = makeCode(huffTree[1], prefix+"1")
        leftDict.update(rightDict)
        return leftDict

def encode(codeDict, text):
    """Converts plaintext letters into their prefix code equivalent.

    @param codeDict: a dictionary containing the prefix code
    @param text: a string containing the original plaintext
    @return: a string representing the encoded text
    """
    pass

def writeOverhead(codeDict):
    """Generates the overhead dictionary for the encoded file.

    @param codeDict: a dictionary containing the prefix code
    @return: the bits used to represent the dictionary
    """
    pass

if __name__ == "__main__":
    # TODO: Write everything
    print()
