from random import randint
numero = int(input('Digite um numero: '))

print('Hummm Estou analisando o numero....')

escolhido = randint(0,5)

print(f'O número sorteado foi o {escolhido}, portanto você...')

if numero == escolhido:
    print('PARABENS')
else:
    print('ERROU')
