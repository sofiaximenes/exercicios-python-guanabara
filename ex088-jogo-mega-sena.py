import random


random.randint(0, 60)
jogos = int(input('Digite quantos jogos você quer fazer: '))
lista_de_jogos = []
palpite = []

for jogo in range(0,jogos):
    for cada_palpite in range(0, 6):
        numero = random.randint(0,60)
        palpite.append(numero)
    lista_de_jogos.append(palpite)
    palpite=[]

print(lista_de_jogos)

