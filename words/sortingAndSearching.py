##Nathan Hinton
##This file is for different methods of sorting and accessing the data

from string import ascii_lowercase as alphabet

customDict = './customDict'

def loadDict(dictPath):
    with open(dictPath) as file:
        d = file.read().split()
        dictionary = []
        for word in d:
            dictionary.append(word.lower())
        print('Loaded dictionary at %s'%dictPath)
        print('%s words found in dictionary file.'%len(dictionary))
    return dictionary

def letterToNumber(char):
    return alphabet.index(char.lower())+1

def binarySearch(term, lst):##This takes a term and a list if data
    tmpLst = []
    lst = lst.sort()#Sort so that I can use it better
    found = False
    while found == False:
        pass

##This will use a trie method

class Node:
    def __init__(self):
        self.children : Dict[str, Node] = {}
        self.value : Any = None


        
def find(node: Node, key: str):
    """Find value by key in node."""
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node.value

def insert(node: Node, key: str):
    """Insert key/value pair into node."""
    value = ''
    for char in key:
        value += char
        if char not in node.children:
            node.children[char] = Node()
        node = node.children[char]
        node.value = value
    node.value = value
