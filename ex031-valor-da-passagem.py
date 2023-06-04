dist = float(input('Digite a distância percorrida: '))
passagem1 = float(dist * 0.50)
passagem2 = float(dist * 0.45)
if (dist <= 200):
    print(f'O preço da viagem será R${passagem1:.2f}')
else:
    print(f'O preço da passagem será R${passagem2:.2f}.')

100
