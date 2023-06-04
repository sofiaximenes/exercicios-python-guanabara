lista_geral = []
lista_impar = []
lista_par = []
i = 0
numero = 0
for c in range (0,7):

    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        lista_par.append(numero)
        lista_geral.append(numero)
    else:
        lista_impar.append(numero)
        lista_geral.insert(0, numero)

lista_par.sort()
lista_impar.sort()

print(lista_geral)
print(lista_impar)
print(lista_par)

