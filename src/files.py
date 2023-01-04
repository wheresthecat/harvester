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
