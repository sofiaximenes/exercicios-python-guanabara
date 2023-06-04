from random import randint

itens = ('pedra', 'papel', 'teosura')
computador = randint(0, 2)
print ('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual será a sua jogada? '))
print('-' * 30)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador {itens[computador]}.')
print('-'* 30)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O JOGADOR VENCEU!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print ('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print ('EMPATE!')
    elif jogador == 2:
            print('O JOGADOR VENCEU!')

    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print ('O JOGADOR PERDEU!')
    elif jogador == 1:
        print('O JOGADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')