lista = list()
numero_cinco = 5

while True:
    n = int(input("Digite um número: "))
    if n not in lista:
        lista.append(n)
    resposta = str(input(f"Digite 'S' caso você queira adicionar mais números e 'N' caso você não queira adicionar mais números."))
    if resposta in "Nn":
        break
    elif resposta not in "Nn" or resposta not in "Sn":
        print("Você não digitou um comando executável. Por favor, digite 'S' ou 'N'")
       lista.sort(reverse=True)
print(f"Você digitou {len(lista)} números \n"
      f"Foram digitados os seguintes números: {lista}")
if numero_cinco in lista:
    print(f"O número 5 foi digitado.")
