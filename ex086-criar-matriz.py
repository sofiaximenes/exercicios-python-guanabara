matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_pares = 0
soma_terceira_coluna = 0
maior_numero = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("-" * 50)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()

for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_terceira_coluna += matriz[l][c]
for c in range (0, 3):
    if c == 0 or matriz[1][c] > maior_numero:
        maior_numero = matriz[1][c]


print(f'A soma dos valores da pares é {soma_pares}')
print(f'Asoma dos valores da última coluna é {soma_terceira_coluna}')
print(f'O maior número da segunda linha é o {maior_numero}')