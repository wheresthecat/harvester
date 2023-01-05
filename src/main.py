import words_fnc


def main():
    filePath = "./data/really_big_file.txt"
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

    for i in sortedFrequency:
        print(f"{i[0]}:\t{i[1]}")

    
        

if __name__ == "__main__":
    main()