##Nathan Hinton
##This is testing the use of a * in a search.

from time import time
start = time()

from string import ascii_lowercase as alpha


print('Loading the dictionarry...')
#dictPath = './englishDict/english-words-master/words_alpha.txt'
dictPath = '/home/nathan/Desktop/enwiktionary-latest-all-titles-in-ns0'
with open(dictPath) as file:
    d = file.read().split()
    dictionary = []
    for word in d:
        dictionary.append(word.lower())
    print('%s words found in dictionary file.'%len(dictionary))



def find(searchTerm):
    terms = searchTerm.split('*')#This is a really general thing. it assumes a * at the end of the search term.
    possiblties = []
    for word in dictionary:
        lastIndex = 0
        maybe = 1
        for term in terms:#This lacks checking to see if it matches the order of the input.
            if term in word:
                if word.index(term) > lastIndex:
                    lastIndex = word.index(term)
                    maybe += 1
            else:
                break
            if maybe == len(terms):
                possiblties.append(word)
##    print(possiblties)
    return possiblties
