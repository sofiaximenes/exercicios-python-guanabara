print ('{:-^40}'.format ('LOJAS XIMENES'))
preco = float(input('Digite o valor do produto: R$ '))
print('''Escolha uma das formas de pagamento:
[ 1 ] à vista/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3 x ou mais no cartão''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    total = preco - (preco *0.1)
   # print(f'O produto custa {preco:.2f}, mas comprado à vista no dinheiro ou no cheque, custará {preco - (preco * 0.1):.2f}')
elif opção == 2:
    total = preco - (preco * 0.05)
    #print(f'O produto custa {preco:.2f}, mas comprado à vista no cartão, custará {preco - (preco * 0.05):.2f}')
elif opção == 3:
    total = preco
    #print(f'O produto custará {preco:.2f}, quando for pago em até 2x no cartão)')
elif opção == 4:
    total = preco + (preco * 0.2)
    #print(f'O produto custa {preco:.2f}, mas comprado em 3x parcelas ou mais, custará {preco + (preco * 0.2):.2f}')
print (f'Sua compra de R${preco:.2f} vai custar R${total} no final. ')


