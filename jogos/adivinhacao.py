import random

def jogar():
    print("***************")
    print("Adivinhe o número!")
    print("***************")

    random_number = random.randrange(1, 101)
    total = 0

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total = 20
    elif(nivel == 2):
        total = 10
    elif(nivel == 3):
        total = 5
    else:
        print("Insira um nível válido!")

    for rodada in range(1, total+1):
        print("Tentativa {} de {}".format(rodada, total))
        print("")
        chute_str = input("Insira um número: ")

        chute = int(chute_str)


        if (random_number == chute):
            print("Correto!")
            break
        else:
            if (chute > random_number):
                print("Errado! Você chutou um valor maior que o número secreto.")
            elif (chute < random_number):
                print("Errado! Você chutou um valor menor que o número secreto.")
if(__name__ == "__main__"):
    jogar()