##Nathan Hinton

print('Loading the dictionarry...')
dictPath = '/home/nathan/words_alpha.txt'
with open(dictPath) as file:
    d = file.read().split()
    dictionary = []
    for word in d:
        dictionary.append(word.lower())
    print('%s words found in dictionary file.'%len(dictionary))


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
