import random
print ("*********************************")
print ("Bem vindo no jogo de adivinhação!")
print ("*********************************")
nome_jogador = input("Digite o nome do Jogador: ")

numero_secreto = random.randrange(1,101)
print(numero_secreto)

total_de_tentativas = 3

for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {:02d} de {:02d}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um numero de 1 a 100: ")
    chute = int(chute_str)
    print("Você digitou {:2d}".format(chute))


    if(chute < 1 or chute > 100):
        print("----------------------------------------")
        print("Você deve digitar valores entre 1 e 100.")
        print("----------------------------------------")

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    qualtipo = type(acertou)

    if (acertou):
        print("-------------------------------------------------")
        print("O tipo da variavel acertou é", qualtipo, sep=": ")
        print("-------------------------------------------------")
        print(f"Jogador {nome_jogador.upper()}\nVOCÊ ACERTOU !!!  \o/ \o/ \o/")
        print("-------------------------------------------------")
        break
    else:
        if(maior):
            print(f"\nJogador {nome_jogador.upper()}\nO seu chute foi maior do que o número secreto!")
        elif(menor):
            print(f"\nJogador {nome_jogador.upper()}\nO seu chute foi menor do que o número secreto!")
    rodada = rodada +1

print("Fim do jogo")