n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS''')
    opcao = int(input('Qual a sua opção?'))
    if opcao == 1:
        print(f'A soma de {n1} e {n2} equivale a {n1 + n2}.')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} equivale à {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que {n2}')
        elif n2 > n1:
            print(f'O número {n2} é maior que {n1}')
        elif n1 == n2:
            print ('Os números são iguais!')
    elif opcao == 4:
        n1 = int(input('1º valor: '))
        n2 = int(input('2º valor: '))


print('Você saiu do programa. Volte sempre!')