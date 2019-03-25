print ("*********************************")
print ("Bem vindo no jogo de adivinhação!")
print ("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um numero de 1 a 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

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
        print(" VOCÊ ACERTOU !!!  \o/ \o/ \o/")
        print("-------------------------------------------------")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
    rodada = rodada +1

print("Fim do jogo")