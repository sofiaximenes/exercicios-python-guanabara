lista_pares = []
lista_impares = []
lista = []
while True:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    if int(numero % 2 == 0):
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    resposta = input("Você quer inserir mais algum número? Responda S se sim e N se não: ")
    if resposta in 'Nn':
        break
    elif resposta not in "NnSs":
        print("Você não digitou um comando executável. Por favor, digite 'S' ou 'N'")
        resposta = input("Você quer inserir mais algum número? Responda S se sim e N se não: ")

print(f'A lista de todos os números é {lista} \n'
      f'A lista dos números PARES é {lista_pares} \n'
      f'A lista dos números ÍMPARES é {lista_impares}')