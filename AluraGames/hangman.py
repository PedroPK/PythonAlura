import stringUtils

def play():
    print("#" * 30)
    print("Welcome to Hangman Game")
    print("#" * 30)
    print("\n")

    # This is the Word that the User should try to discover
    #secretWord      = "banana"
    secretWordList  =  stringUtils.string_to_list("banana")

    # This will produce a String like this "_ _ _ _ _ _"
    # knownWord       = ("_ " * len(secretWordList)).strip()

    # This List will store the Char that were discovered. 
    # Ex: In banana word, when user press 'a', it will be like ['_', 'a', '_', 'a', '_', 'a']
    gotCharacters   = ["_"] * len(secretWordList)

    isHanged              = False
    qtRemainingChances    = 6

    gotWord         = False 

    while ( not isHanged and not gotWord ) :
        guessChar   =   input("Type a character: ")
        guessChar   =   guessChar.strip()    # Java String.trim()
        gotChar     = False

        # Convert the SecretWord into a List
        # The variable below were replaced by secretWordList
        #listSecretWord = stringUtils.string_to_list(secretWord)

        # Count the number of times that a Char exists in the String/List SecretWord
        qtOccurrences = secretWordList.count(guessChar)
        #print("Count of Occurrences of the Character in the Secret Word: " + str(listSecretWord.count(character)))

        # Create a List of this Length
        listOfPositionsWhereCharWasFound        =  [-1] * qtOccurrences
        indexListOfPositionsWhereCharWasFound   =   0

        index = 0
        
        while index < len(secretWordList) :

            # Traverse the SecretWord, finding positions of the Char

            # Let's use the List .index() Function to make the algorithm more performatic, jumping unecessary iterations
            
            if ( guessChar in secretWordList ) :
                index       = secretWordList.index(guessChar)
                gotChar     = True

                # If the .index() return -1, we break the Iteration
                # Else, we can jump to this index, maybe using Continue and Comparison from Index variable with .index() result

                if ( secretWordList[index].lower() == guessChar.lower() ) :
                    # Add this Positions in a List
                    listOfPositionsWhereCharWasFound[indexListOfPositionsWhereCharWasFound] = index

                    # Incremet the Index of the List with Positions 
                    indexListOfPositionsWhereCharWasFound = indexListOfPositionsWhereCharWasFound + 1

                    # This will fill the List of Known Characters
                    gotCharacters[index]    =   secretWordList[index]

                    if ( "_" not in gotCharacters ) :
                        gotWord     =   True
                        print("You got it!")
                        break

                    secretWordList[index]    =   "_"    #     +   secretWordList[index + 1: len(secretWordList)]

                    # Removing this Break makes it to find All Occurrences of a Character in the Word
                    #break

                index = index + 1

            else :
                qtRemainingChances = qtRemainingChances - 1
                print("Keep trying")
                break
        
        print_got_characters(gotCharacters)

        if qtRemainingChances <= 0 :
            isHanged = True
        
        # Convert the List with Positions of Char found into a String
        positionsString = stringUtils.list_to_string_with_commas(listOfPositionsWhereCharWasFound)

        if gotChar :
            # Print the Message informing player all the positions the Char was found
            print("You got one. The character {} exists in position(s) {}".format(guessChar, positionsString))

        print("You still have {} chances".format(qtRemainingChances))

        print("\n")            

    print("Ending Hangman.")

def print_got_characters(pList) :
    string = ""
    for char in pList :
        string = string + " " + char
    
    string = string.strip()

    print(string)

def writeWordOnFile() :
    file = open("words.txt", "w")
    
    file.write("apple"      + "\n")
    file.write("pinapple"   + "\n")
    file.write("orange"     + "\n")
    file.write("cramberie"  + "\n")
    file.write("apple"      + "\n")
    file.write("blueberry"  + "\n")

    file.close()

def readWordOfFile() :
    file = open("words.txt", "r")

    #lines = file.read()
    for line in file :
        print(line.strip())

if ( __name__ == "__main__" ) :
    #play()
    #writeWordOnFile()
    readWordOfFile()