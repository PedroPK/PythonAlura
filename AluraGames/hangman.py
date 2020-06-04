def play():
    print("#" * 30)
    print("Welcome to Hangman Game")
    print("#" * 30)
    print("\n")

    secretWord = "banana"

    isHanged        = False
    gotWord         = False 

    while ( not isHanged and not gotWord ) :
        guess   =   input("Type a character: ")
        gotCharacter    = False

        index = 0
        for character in secretWord :
            if ( character == guess) :
                print("You got one. The character {} exists in position {}".format(character, index))
                gotCharacter = True
                break
            index = index + 1

        if ( not gotCharacter ) :
            print("Keep trying")

    print("\n")
    print("Ending Hangman.")

if ( __name__ == "__main__" ) :
    play()