listagem = ('Lápis', 2.60,
            'Caderno', 18.20,
            'Borracha', 2.00,
            'Caneta', 3.15,
            'Estojo', 13.00,
            'Mochila', 120.50,
            'Livro', 38.90)
print('.' * 50 )
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('.' * 50)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>10.2f}')
print('.'*50)