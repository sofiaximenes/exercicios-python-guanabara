while True:
    n = int(input('Você quer ver a tabuada de que número? '))
    print('-' * 30)
    if n < 0:
        break

    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print(f'A multiplicação de números negativos não está autorizada.')