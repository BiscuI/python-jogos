import random

def jogar():
    imprime_boas_vindas()
    palavra_secreta = ler_arquivo()
    valores = inicializa_lista_letras(palavra_secreta)

    tentativas = 7
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        imprime_cabecalho_rodada(tentativas, valores)
        chute = recebe_palpite()

        if(len(chute)!=1):
            print("Seu palpite deve ser de apenas uma letra!")
            continue

        if(chute in palavra_secreta):
            valores = busca_char(chute, palavra_secreta, valores)

        else:
            print("A palavra não possui essa letra. Uma tentativa a menos :(")
            tentativas -= 1
        print("...Jogando...")

        #Verificando se já usou todas as tentativas
        enforcou = tentativas == 0
        if(enforcou):
           imprime_mensagem_derrota(palavra_secreta)

        #Verificando se já encontrou todas as letras
        acertou = '_' not in valores
        if(acertou):
            imprime_mensagem_vitoria(palavra_secreta)

    print("Fim do jogo!")

def imprime_boas_vindas():
    print("***************")
    print("Jogo da forca!")
    print("***************")

def ler_arquivo():
    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    random_number = random.randrange(0, len(palavras))
    arquivo.close()
    return palavras[random_number]

def inicializa_lista_letras(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def recebe_palpite():
    chute = input("Qual sua letra?").strip()
    return chute

def busca_char(chute, palavra_secreta, valores):
    indice = 0
    for letra in palavra_secreta:
        if (chute.lower() == letra.lower()):
            print("Encontrei a letra {} na posição {} ^^".format(letra, indice))
            valores[indice] = letra

        indice += 1
    return valores

#Mensagens de fluxo
def imprime_cabecalho_rodada(tentativas, valores):
    print("")
    print("*********************")
    print("Você tem {} tentativas".format(tentativas))
    print(" ".join(str(char) for char in valores))
    print("*********************")
    print("")
    imprime_forca(tentativas)

def imprime_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vitoria(palavra_secreta):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()