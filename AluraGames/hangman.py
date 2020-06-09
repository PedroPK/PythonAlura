import stringUtils
import random

def play():
    print_welcome_message()

    # Write the File to read it later
    secret_word      = get_random_word()
    secret_word_list  = get_random_word_as_list(secret_word)

    # This List will store the Char that were discovered. 
    # Ex: In banana word, when user press 'a', it will be like ['_', 'a', '_', 'a', '_', 'a']
    got_characters = new_underscore_list(secret_word_list)

    is_hanged              = False
    qt_remaining_chances   = 10

    got_word         = False 

    while ( not is_hanged and not got_word ) :
        guess_char = read_character()
        got_char     = False

        # Count the number of times that a Char exists in the String/List SecretWord
        qt_occurrences = count_occurrences_of_char_on_list(secret_word_list, guess_char)

        # Create a List of this Length
        list_of_positions_where_char_was_found          = get_list_same_size_secret_word(qt_occurrences)
        index_list_of_positions_where_char_was_found    =   0

        index = 0
        
        # Traverse the SecretWord, finding positions of the Char
        while index < len(secret_word_list) :

            if ( guess_char in secret_word_list ) :
                # Let's use the List .index() Function to make the algorithm more performatic, jumping unecessary iterations
                index       = secret_word_list.index(guess_char)

                got_char     = True

                # If the .index() return -1, we break the Iteration
                # Else, we can jump to this index, maybe using Continue and Comparison from Index variable with .index() result
                if ( secret_word_list[index].lower() == guess_char.lower() ) :
                    # Add this Positions in a List
                    add_found_positions_into_list(
                        index, 
                        list_of_positions_where_char_was_found, 
                        index_list_of_positions_where_char_was_found
                    )

                    # Incremet the Index of the List with Positions 
                    increment_index(index_list_of_positions_where_char_was_found)

                    # This will fill the List of Known Characters
                    add_found_positions_into_list(
                        secret_word_list[index], 
                        got_characters, 
                        index)

                    if ( "_" not in got_characters ) :
                        got_word     =   True
                        print_you_got_it()
                        break
                    
                    # Replace the found Character per "_"
                    replace_found_character(
                        secret_word_list, 
                        index)

                    # Removing this Break makes it to find All Occurrences of a Character in the Word
                    #break

                incremet_index(index)

            else :
                qt_remaining_chances = qt_remaining_chances - 1
                print_keep_trying()
                break
        
        print_got_characters(
            got_characters, 
            got_word)

        # If the Player has no more chances
        if qt_remaining_chances <= 0 :
            is_hanged = True
        
        # Convert the List with Positions of Char found into a String
        positionsString = stringUtils.list_to_string_with_commas(list_of_positions_where_char_was_found)

        # Will print the Character that the Player got right
        print_got_character(
            got_char, 
            guess_char, 
            positionsString, 
            got_word)

        # Will print how many chances the Player still have
        print_remaining_chances(
            qt_remaining_chances, 
            got_word)

        print_new_line()

    print_secret_word(
        got_word, 
        secret_word)

    print_ending_hangman()

def count_occurrences_of_char_on_list(secret_word_list, guess_char):
    qt_occurrences = secret_word_list.count(guess_char)
    return qt_occurrences

def increment_index(index):
    index = index + 1

def incremet_index(index_list_of_positions_where_char_was_found):
    increment_index(index_list_of_positions_where_char_was_found)

def new_underscore_list(secret_word_list):
    got_characters   = ["_"] * len(secret_word_list)
    return got_characters

def get_list_same_size_secret_word(qt_occurrences):
    list_of_positions_where_char_was_found        =  [-1] * qt_occurrences
    return list_of_positions_where_char_was_found

def print_you_got_it():
    print("You got it!")

def print_keep_trying():
    print("Keep trying")

def print_ending_hangman():
    print("Ending Hangman.")

def print_new_line():
    print("\n")

def print_secret_word(got_word, secret_word):
    if not got_word :
        print("The Secret Word was '{}'".format(secret_word))

def replace_found_character(secret_word_list, index):
    add_found_positions_into_list("_", secret_word_list, index)    #     +   secretWordList[index + 1: len(secretWordList)]

def print_got_character(got_char, guess_char, positionsString, pGotWord) :
    if not pGotWord and got_char :
        # Print the Message informing player all the positions the Char was found
        print("You got one. The character {} exists in position(s) {}".format(guess_char, positionsString))

def add_found_positions_into_list(index, list_of_positions_where_char_was_found, index_list_of_positions_where_char_was_found):
    # Add this Positions in a List
    list_of_positions_where_char_was_found[index_list_of_positions_where_char_was_found] = index

def print_remaining_chances(qtRemainingChances, pGotWord) :
    if not pGotWord :
        print("You still have {} chances".format(qtRemainingChances))

def print_welcome_message():
    print("#" * 30)
    print("Welcome to Hangman Game")
    print("#" * 30)
    print_new_line()

def read_character():
    guessChar   =   input("Type a character: ")
    guessChar   =   guessChar.strip()    # Java String.trim()
    return guessChar

def get_random_word_as_list(pWord):
    secretWord  =   ""
    
    if pWord != None :
        secretWord = pWord
    else :
        secretWord = get_random_word()
    
    secretWordList  =   stringUtils.string_to_list(secretWord)

    return secretWordList

def get_random_word():
    # Write the File to read it later
    writeWordOnFile()

    # Read Words from words.txt
    words = readWordsFromFile()

    # Generate a Random Index to select a Word
    randomInt = random.randrange(0, len(words))

    # Get the Word randomly selected
    
    return words[randomInt]

def print_got_characters(pList, pGotWord) :
    #if not pGotWord :
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
    file.write("lemon"      + "\n")
    file.write("grape"      + "\n")
    file.write("banana"     + "\n")
    file.write("melon"      + "\n")
    file.write("watermelon" + "\n")
    file.write("mango"      + "\n")
    file.write("papaya"     + "\n")

    file.close()

def readWordsFromFile() :
    file = open("words.txt", "r")

    words = []
    #lines = file.read()
    for line in file :
        words.append(line.strip())

    file.close()

    return words

if ( __name__ == "__main__" ) :
    play()
    #writeWordOnFile()
    #readWordsFromFile()