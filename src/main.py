import words_fnc


def main():
    filePath = "./data/short.txt"
    srcFile = open(filePath, 'r')
    srcText = srcFile.read()  # copy a file to a string so we can close the file and forget it. 
    srcFile.close() # yeah, fuck you file



    words =  words_fnc.getWords(srcText)         # get list of words
    uniqueWords = words_fnc.getUniqueWords(words)     # analyze the word count.

    #### Stuff with the dictionary
    wordFrequency = {}
    for item in uniqueWords:
        wordFrequency.update({item : 0})        # Fill it with zeroes.

    for item in words:
        value = wordFrequency.get(item)
        value += 1
        wordFrequency.update({item: value})

    sortedFrequency = words_fnc.getSortedWords(wordFrequency)


    print(f"Words total: {len(words)}")
    print(f"Unique words: {len(uniqueWords)}")
    print("==== Words: ====")
    
    # uniqueWords.sort()
    # counter = 0
    # for i in uniqueWords:
    #     print(f"{i}: {wordFrequency.get(i)}", end=" ")
    #     counter += 1
    #     if counter == 10:
    #         print()
    #         counter = 0
    # print()
    
    #print(wordFrequency)

    for i in sortedFrequency:
        print(f"{i[0]}: {i[1]}")

    
        

if __name__ == "__main__":
    main()