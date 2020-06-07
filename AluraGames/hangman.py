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

        index = 0
        for character in secretWord :
            if ( character.lower() == guess.lower() ) :
                print("You got one. The character {} exists in position {}".format(character, index))
                gotCharacter            = True

                # This will fill the List of Known Characters
                gotCharacters[index]    =   character
                print(gotCharacters)
                if ( "_" not in gotCharacters ) :
                    gotWord     =   True
                    print("You got it!")
                    break
                
                print("gotCharacters 1 = " + stringUtils.list_to_string_without_commas(gotCharacters))

                if ( index == 0 ) :
                    secretWord          =   "_"     +   secretWord[index + 1: len(secretWord)]
                elif ( index == len(secretWord) ) :
                    secretWord          =   secretWord[0: len(secretWord) - 1]  + "_"
                else :
                    secretWord          =   secretWord[0: index] + "_" + secretWord[index + 1: len(secretWord)]

                print("secretWord 2 = " + stringUtils.list_to_string_without_commas(secretWord))

                # Removing this Break makes it to find All Occurrences of a Character in the Word
                #break
            
            print("\n")

            index = index + 1

        if ( not gotCharacter and not gotWord) :
            print("Keep trying")

    print("\n")
    print("Ending Hangman.")

if ( __name__ == "__main__" ) :
    play()