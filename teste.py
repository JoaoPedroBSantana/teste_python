import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhaçao!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 100

    print("Qual o nivel que voce deseja? ")
    print("1 -- FACIL || 2 -- MEDIO || 3 - DIFICIL")

    nivel = int(input("Escolha o Nivel: "))

    if nivel == 1:
        tentativas = 10
    elif nivel == 2:
        tentativas = 5
    else:
        tentativas = 3

    for rodada in range(1, tentativas + 1):
        print('Tentativas {} de {}'.format(rodada, tentativas))

        chute = int(input("Digite o seu numero entre 1 e 100: "))
        print("Voce digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabens!!! voce acertou o numero e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("O seu chute foi maior que o número secreto")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))

    print("O numero era: ", numero_secreto)
    print("Fim de Jogo!")

if __name__ == "__main__":
    jogar()