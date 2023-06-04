from random import randint
escolhido = randint(0,10)
print('Hummm Estou escolhendo o numero....')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite um numero: '))
    palpites += 1
    if jogador == escolhido:
        acertou = True
    else:
        if jogador < escolhido:
            print('Tente um número maior...')
        elif jogador > escolhido:
            print('Tente um número menor...')
print(f'Acertou com {palpites} palpites.')


'''if numero == escolhido:
    print('PARABENS')
else:
    print('ERROU')'''

