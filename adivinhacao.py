print ("*********************************")
print ("Bem vindo no jogo de adivinhação!")
print ("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu numero: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    qualtipo = type(acertou)

    if (acertou):
        print("-------------------------------------------------")
        print("O tipo da variavel acertou é", qualtipo, sep=": ")
        print("-------------------------------------------------")
        print("VOCÊ ACERTOU !!!")
        print("-------------------------------------------------")
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
    rodada = rodada +1

print("Fim do jogo")