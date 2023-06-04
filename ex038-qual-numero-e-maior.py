a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
if a > b:
    print(f'O número {a} é maior que {b}.')
elif b > a:
    print(f'O número {b} é maior que {a}.')
elif a == b:
    print (f'Os números são iguais!')