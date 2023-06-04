print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer gerar?: '))
a = 0
b = 1
print(f'{a} -> {b}', end=' -> ')
cont = 3
while cont <= n:
    c = a + b
    print(f'{c}', end=' -> ')
    a = b
    b = c
    cont += 1
print(f'FIM')
