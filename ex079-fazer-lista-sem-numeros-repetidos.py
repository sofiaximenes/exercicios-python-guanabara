lista = []
numero = 0

while True:
    numero = input("Digite um número: ")
    if numero not in lista:
        lista.append(numero)
    else:
        print("número já existe na lista")
    resposta = input("Digite S caso deseje adicionar mais algum número e N caso não queira: ")
    if resposta in 'Nn':
        break
lista.sort()
print(f'{lista}')