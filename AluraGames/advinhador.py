import random

def play():
    print("#" * 32)
    print("Bem vindo ao Jogo de Advinhação")
    print("#" * 32)

    print("\n")

    print("Escolha o nível de dificuldade")
    print("(1) Fácil")
    print("(2) Médio")
    print("(3) Dificil")

    print("\n")

    difficult_level     = int(input("Nível selecionado: "))

    points              = 1000
    secret_number       = random.randint(0, 100)
    youGotIt            = False

    total_guesses = 15
    if ( difficult_level == 2 ) :
        total_guesses = 10
    elif ( difficult_level == 3 ) :
        total_guesses = 5


    for round in range(0, total_guesses) :
        print( "Tentativa {} de {}".format(round + 1, total_guesses) )

        guest_number = int( input("Digite um número entre 1 e 100: ") )

        print("Você digitou {:02}".format(guest_number))

        if ( guest_number < 1 or guest_number > 100 ) :
            print("Você digitou um valor fora so intervalo")
            continue

        youGotIt    =   guest_number    ==      secret_number
        bigger      =   guest_number    >       secret_number
        smaller     =   guest_number    <       secret_number

        if ( youGotIt ) :
            print("Você acertou o número!")
            break
        else:
            if ( bigger ) :
                print("Você errou pra cima.")
                ##print("Sua Pontuação agora é de {}".format(points))
            elif ( smaller ) :
                print("Você errou para baixo")
                ##print("Sua Pontuação agora é de {}".format(points))
        
        diff_points = guest_number - secret_number
        
        points = points - abs(diff_points)

        print("\n")

    print("\n")
    print(f"O Número Secreto era {secret_number}")
    print("Sua Pontuação Final foi de {}".format(points) )
    print("Fim do Jogo.")
