##Nathan Hinton

print('Loading the dictionarry...')
dictPathSmall = './englishDict/english-words-master/words.txt'#Old small dict
dictPathLarge = '/home/nathan/Desktop/enwiktionary-latest-all-titles-in-ns0'
def loadDict(dictPath):
    with open(dictPath) as file:
        d = file.read().split()
        dictionary = []
        for word in d:
            dictionary.append(word.lower())
        print('Loaded dictionary at %s'%dictPath)
        print('%s words found in dictionary file.'%len(dictionary))
    return dictionary

dictionary = loadDict(dictPathSmall)
dictionary2 = loadDict(dictPathLarge)
lst = list(dict.fromkeys(dictionary2+dictionary2))

def anagram(terms):
    p = []
    for word in dictionary:
        if len(word) == len(terms):
            maybe = 0
            for term in terms:
                if term in word:
                    maybe += 1
                else:
                    break
            if maybe == len(terms):
                p.append(word)
    return p

def anagram2(term):
    p = []
    for word in dictionary:
        maybe = 0
        for char in word:
            if char in term:
                maybe += 1
        if maybe == len(word):
            p.append(word)
    return p
