##Nathan Hinton
#For finding words

from string import ascii_lowercase as alpha

print('Loading the dictionarry...')
dictPath = 'englishDict/english-words-master/words_alpha.txt'
with open(dictPath) as file:
    d = file.read().split()
    dictionary = []
    for word in d:
        dictionary.append(word.lower())
    print('%s words found in dictionary file.'%len(dictionary))
def findOld(term, exempt=[]):
    
    search = term.lower()
    searchLength = 0
    searchLst = []
    for char in search:
        if searchLength != -1:
            searchLength += 1
        if char == '*':
            searchLength = -1
        elif char == '?':
            searchLst.append('?')
        elif char in alpha:
            searchLst.append(str(char))
        else:
            print("ERROR! Unrecognized characater found when parsing input!")
    print('Begining search for %s'%search)
    searchWords = []
    print('filtering by length...')
    if searchLength == -1:
        searchWords = dictionary
    else:
        for word in dictionary:
            if len(word) == searchLength:
                searchWords.append(word)
    print('looking at leters...')
    options = []
    for word in searchWords:
        yes = True
        ltrA = False
        ltrB = False
        ltrC = False
        for x in range(0, searchLength):
            if search[x] == '?':
                pass
            elif search[x] == 'A':
                if ltrA == False:
                    ltrA = word[x]
                elif ltrA == word[x]:
                    pass
                else:
                    yes = False
            elif search[x] == 'B':
                if ltrB == False:
                    ltrB = word[x]
                elif ltrB == word[x]:
                    pass
                else:
                    yes = False
            elif search[x] == 'C':
                if ltrC == False:
                    ltrC = word[x]
                elif ltrC == word[x]:
                    pass
                else:
                    yes = False
            else:
                if word[x] == search[x]:
                    pass
                else:
                    yes = False
        for char in exempt:
            if char in word:
                yes = False
        if yes == True:
            options.append(word)
    print()
    print()
    print()
    print("Found %s matches:"%len(options))
    i = input("Print? ")
    if i == 'y':
        options.sort()
        for word in options:
            print(word)
    return options

def printList(lst):
    for x in lst:
        print(x)

def compare(word1, word2):
    words1 = find(word1)
    words2 = find(word2)
    pos = 0
    for x in word1:
        if x == '?':
            for word in words1:
                wds = []
                pnt = False
                for test in words2:
                    if test[pos] == word[pos]:
                        pnt = True
                        wds.append(test)
                print("---------------")
                print(word)
                printList(wds)
        pos +=1

def searchDict(chars):
    output = []
    for word in dictionary:
        if chars in word:
            output.append(word)
    return output

def find(searchTerm, exempt = []):
    terms = []
    for term in searchTerm.split('*'):#Filter the search term:
        if term == []:
            pass
        else:
            terms.append(term)
    options = []
    for term in terms:
        options.append(searchDict(term))
    for word in options:
        for term in terms:
            if term in word:
                pass
            else:
                print(word)
    if exempt != []:
        for word in options:
            for char in exempt:
                if char in word:
                    options.remove(word)
    return options
                    
    
find('st*in')
