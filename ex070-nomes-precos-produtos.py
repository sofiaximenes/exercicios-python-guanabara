print('-' * 30)
print ('MERCADINHO SUPERBARATO')
print('-' * 30)
cont = total = preco_maior_que_mil = produto_mais_barato = 0

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto:'))
    cont += 1
    total += preco
    if preco > 1000:
        preco_maior_que_mil += 1
    if cont == 1:
        produto_mais_barato = produto
    else:
        if preco < produto_mais_barato:
            produto_mais_barato = preco
    continuar = ' '
    print('-' * 30)
    continuar = str(input('Você deseja incluir mais algum produto? [SIM/NÃO] ')).strip().upper()[0]
    print('-' * 30)
    while continuar not in 'SN':
        continuar = str('Você deseja incluir mais algum produto? [SIM/NÃO] ').strip().upper()[0]
    if continuar == 'N':
        break

print(f'O total da compra foi de R${total:.2f }. Você comprou {preco_maior_que_mil} produtos que custam mais que R$1.000')
print(f'O produto mais barato foi o(a) {produto_mais_barato})'
      f'')
