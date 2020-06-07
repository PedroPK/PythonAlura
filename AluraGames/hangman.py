import stringUtils

def play():
    print("#" * 30)
    print("Welcome to Hangman Game")
    print("#" * 30)
    print("\n")

    # This is the Word that the User should try to discover
    secretWord      = "banana"

    # This will produce a String like this "_ _ _ _ _ _"
    knownWord       = ("_ " * len(secretWord)).strip()
    gotCharacters   = ["_"] * len(secretWord)
    #print(knownWord)

    isHanged        = False
    gotWord         = False 

    while ( not isHanged and not gotWord ) :
        guess   =   input("Type a character: ")
        guess   =   guess.strip()           # Java String.trim()
        gotCharacter    = False

        # Convert the SecretWord into a List
        listSecretWord = stringUtils.string_to_list(secretWord)

        # Count the number of times that a Char exists in the String/List SecretWord
        qtOccurrences = listSecretWord.count(guess)
        #print("Count of Occurrences of the Character in the Secret Word: " + str(listSecretWord.count(character)))

        # Create a List of this Length
        listOfPositionsWhereCharWasFound        =  [-1] * qtOccurrences
        indexListOfPositionsWhereCharWasFound   =   0

        index = 0
        for character in secretWord :

            # Traverse the SecretWord, finding positions of the Char

            if ( character.lower() == guess.lower() ) :
                # Add this Positions in a List
                listOfPositionsWhereCharWasFound[indexListOfPositionsWhereCharWasFound] = index

                # Incremet the Index of the List with Positions 
                indexListOfPositionsWhereCharWasFound = indexListOfPositionsWhereCharWasFound + 1

                # Commenting line below to print it only once, outside the FOR
                #print("You got one. The character {} exists in position {}".format(character, index))
                gotCharacter            = True

                # This will fill the List of Known Characters
                gotCharacters[index]    =   character
                #print(gotCharacters)
                #print_got_characters(gotCharacters)

                if ( "_" not in gotCharacters ) :
                    gotWord     =   True
                    print("You got it!")
                    break

                if ( index == 0 ) :
                    secretWord          =   "_"     +   secretWord[index + 1: len(secretWord)]
                elif ( index == len(secretWord) ) :
                    secretWord          =   secretWord[0: len(secretWord) - 1]  + "_"
                else :
                    secretWord          =   secretWord[0: index] + "_" + secretWord[index + 1: len(secretWord)]

                # Removing this Break makes it to find All Occurrences of a Character in the Word
                #break

            index = index + 1

        print_got_characters(gotCharacters)
        
        # Convert the List with Positions of Char found into a String
        positionsString = stringUtils.list_to_string_with_commas(listOfPositionsWhereCharWasFound)

        # Print the Message informing player all the positions the Char was found
        print("You got one. The character {} exists in position(s) {}".format(character, positionsString))

        print("\n")

        if ( not gotCharacter and not gotWord) :
            print("Keep trying")

    print("\n")
    print("Ending Hangman.")

def print_got_characters(pList) :
    string = ""
    for char in pList :
        string = string + " " + char
    
    string = string.strip()

    print(string)

if ( __name__ == "__main__" ) :
    play()