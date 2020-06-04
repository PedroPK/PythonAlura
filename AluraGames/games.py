import hangman
import advinhador

print("#" * 30)
print("Welcome to Alura Games")
print("#" * 30)

print("\n")
print("Choose the Game you want to play:")

print("\n")
print("(1) Guessing")
print("(2) Hangman")

choosen_game    =   int( input("Wich game? ") )

print("\n")
if ( choosen_game == 1 ) :

    print("Let's play Guessing!")
    advinhador.play()
elif ( choosen_game == 2 ):
    print("Let's play Hangman!")
    hangman.play()

    