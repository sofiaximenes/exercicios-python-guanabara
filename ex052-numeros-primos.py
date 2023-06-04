#numero = int(input('Digite o número: '))
#if numero % numero == 0:
#    print(f'O número {numero} é primo! ')

numero = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[m')
    print('{}'.format(c), end='')
print(f'\n\033[mO número {numero} foi divisível {total} vezes.')
if total == 2:
    print('Por isso ele é PRIMO.')
else:
    print('Por isso ele NÃO É PRIMO.')