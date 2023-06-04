expressao = input('Digite uma expressão aritmética: ')
lista = []
parenteses_aberto = 0
parenteses_fechado = 0

for i, v in (0, expressao):

        if i == "(" or  i == ")":
            lista.append()

if (parenteses_aberto + parenteses_fechado) % 2 == 0:
    print("A sua expressão é válida!")

else:
    print("A sua expressão não está válida.")
