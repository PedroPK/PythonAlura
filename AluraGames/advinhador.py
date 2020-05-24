print("################################")
print("Bem vindo ao Jogo de Advinhação")
print("################################")

secret_number       = 42
total_guests        = 5
youGotIt            = False

for round in range(0, total_guests) :
    print( "Tentativa {} de {}".format(round + 1, total_guests) )

    guest_number = int( input("Digite um número entre 1 e 100: ") )

    print("Você digitou ", guest_number)

    if ( guest_number < 1 or guest_number > 100 ) :
        print("Você digitou um valor fora so intervalo")

    youGotIt    =   guest_number    ==      secret_number
    bigger      =   guest_number    >       secret_number
    smaller     =   guest_number    <       secret_number

    if ( youGotIt ) :
        print("Você acertou o número!")
        break
    else:
        if ( bigger ) :
            print("Você errou pra cima.")
        elif ( smaller ) :
            print("Você errou para baixo")

    print("\n")

print(type(guest_number))
print("Fim do Jogo.")
