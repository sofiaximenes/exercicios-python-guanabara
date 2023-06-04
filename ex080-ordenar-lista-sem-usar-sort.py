lista_de_numero = []
maior_numero = 0
menor_numero = 0

for c in range(0, 5):
    lista_de_numero.append(int(input("Digite um número: ")))
    for i, v in (lista_de_numero):
        if i == 0:
            maior_numero = menor_numero = lista_de_numero
print(lista_de_numero)