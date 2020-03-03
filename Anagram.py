##Nathan Hinton

print('Loading the dictionarry...')
dictPath = './englishDict/english-words-master/words_alpha.txt'
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

def anagram2(term):#This will be a different way to do this. It will sort the letters after checking the length
    p = []
    terms = []
    for t in term:
        terms.append(t)
    for word in dictionary:
        if len(word) == len(terms):#Make sure the length is the same
            letters = []
            for l in word:
                letters.append(l)
            letters.sort()
            terms.sort()
            if letters == terms:#If the two words can be sorted the same they have the same stuff
                p.append(word)
    return p
                
