# Stuffs words from the source file (string) to the list. Returns list with words.
def getWords(srcStr):
    wordInProgress = ""
    finishedWord = ""
    words = []

    for character in srcStr:
        if character.lower().isalpha():
            wordInProgress += character.lower()  # if a char is a letter it adds to string
        else:
            finishedWord = wordInProgress # if not, it copies already saved characters to another variable
            if len(finishedWord) > 0: # if it has more than zero characters (new line?) it is append to list
                words.append(finishedWord)
                wordInProgress = "" # empty the temp variable
    
    return words


# Gets all the unique words from 
def getUniqueWords(srcWords):
    uniqueWords = []
    isUnique = True

    for item in srcWords:      # listing through words in string
        testedWord = item   # temp variable for better readability.
        if len(uniqueWords) == 0:   # first unique word if a list is empty.
            uniqueWords.append(testedWord)
        for refWord in uniqueWords: # testing item word against a list of unique words.
            if item == refWord:
                isUnique = False
                break
            else:
                isUnique = True
        if isUnique:
            uniqueWords.append(testedWord)
    return uniqueWords


# Sorts dict with word count from most frequent to least frequent. Returns a list.
def getSortedWords(unsortedDict):

    sortedDict = {}
    sortedDict = sorted(unsortedDict.items(), key=lambda x:x[1], reverse=True)

    return sortedDict
