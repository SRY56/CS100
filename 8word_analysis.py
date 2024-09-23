# Shailesh Yannam
# cs 100 2023S section 012
# HW 08, April 14, 2023

# Problem 1
def initialLetterCount(wordList):
    initialLetters = {}
    for wrd in wordList:
        key = wrd[0]
        vo = 0
        for x in wordList:
            if x[0] == key:
                vo += 1
        initialLetters[key] = vo
    return initialLetters
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))
messi = ['You', 'have', 'to', 'fight', 'to', 'reach', 'your', 'dream']
print(initialLetterCount(messi))
pele = [',The', 'more', 'difficult', 'the', 'victory', 'the', 'greater', 'the', 'happiness', 'in', 'winning']
print(initialLetterCount(pele))

print()

# Problem 2
def initialLetters(wordList):
    dictionary = {}
    for word in wordList:
        keys = word[0]
        val = []
        for x in wordList:
            if x[0] == keys and x not in val:
                val.append(x)
        dictionary[keys] = val
    return dictionary
horton1 = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetters(horton1))
messi1 = ['You', 'have', 'to', 'fight', 'to', 'reach', 'your', 'dream']
print(initialLetters(messi1))
pele1 = [',The', 'more', 'difficult', 'the', 'victory', 'the', 'greater', 'the', 'happiness', 'in', 'winning']
print(initialLetters(pele1))

print()

# Problem 3
def shareOneLetter(wordList):
    dictionary = {}
    for word in wordList:
        val = []
        for letters in word:
            for x in wordList:
                if letters in x and x not in val:
                    val.append(x)
        dictionary[word] = val
    return dictionary
horton2 = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(shareOneLetter(horton2))
messi2 = ['You', 'have', 'to', 'fight', 'to', 'reach', 'your', 'dream']
print(shareOneLetter(messi2))
pele2 = [',The', 'more', 'difficult', 'the', 'victory', 'the', 'greater', 'the', 'happiness', 'in', 'winning']
print(shareOneLetter(pele2))
