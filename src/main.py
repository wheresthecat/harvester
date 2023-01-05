import words_fnc


def main():
    filePath = "./data/short.txt"
    srcFile = open(filePath, 'r')
    srcText = srcFile.read()  # copy a file to a string so we can close the file and forget it. 
    srcFile.close() # yeah, fuck you file



    words =  words_fnc.getWords(srcText)         # get list of words
    uniqueWords = words_fnc.getUniqueWords(words)     # analyze the word count.



    print(f"Words total: {len(words)}")
    print(f"Unique words: {len(uniqueWords)}")
    print("==== Words: ====")
    
    uniqueWords.sort()
    counter = 0
    for i in uniqueWords:
        print(i, end=" ")
        counter += 1
        if counter == 15:
            print()
            counter = 0
    print()
    
    
        

if __name__ == "__main__":
    main()