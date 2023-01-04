import files

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


def main():
    filePath = "./data/really_big_file.txt"
    srcFile = open(filePath, 'r')
    srcText = srcFile.read()  # copy a file to a string so we can close the file and forget it. 
    srcFile.close() # yeah, fuck you file



    words = files.getWords(srcText)         # get list of words
    uniqueWords = getUniqueWords(words)     # analyze the word count.



    print(f"Words total: {len(words)}")
    print(f"Unique words: {len(uniqueWords)}")
    print("==== Words: ====")
    
    for i in uniqueWords:
        print(i, end=" ")
    print()
    
    
        

if __name__ == "__main__":
    main()