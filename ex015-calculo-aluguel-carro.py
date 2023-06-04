km = float(input('Digite aqui a quantidade de quilômetros percorridos com o carro: '))
dias = int(input('Digite aqui quantos dias o carro esteve alugado: '))
preco = float(dias * 60) + (km * 0.15)
print(f'O preço total do aluguel corresponde à {preco}')