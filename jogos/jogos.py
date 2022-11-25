import forca
import adivinhacao

print("***************")
print("ESCOLHA O SEU JOGO!")
print("***************")

print("1 - Forca")
print("2 - Advinhação")

escolha = int(input("Qual jogo?"))

if(escolha == 1):
    forca.jogar()
elif(escolha == 2):
    adivinhacao.jogar()