lista_dados = []
dado = []
mais_velhos = []
mais_novos = []
total_de_idades = 0
media_de_idades = 0

# while True:
#     dado.append(str(input('Digite o nome da pessoa: ')))
#     dado.append(int(input('Digite a idade da pessoa: ')))
#     lista_dados.append(dado[:])
#     dado.clear()
#     resposta = input('Digite S caso você deseja incluir mais alguém da lista e N caso não queira.')
#     if resposta in "Nn":
#         break

lista_dados = [['sofia', 30], ['vitor', 35], ['jorge', 42], ['farofa', 43]]

for pessoa in lista_dados:
    total_de_idades += pessoa[1]

media_de_idades = total_de_idades / len(lista_dados)

for pessoa in lista_dados:
    if pessoa[1] >= media_de_idades:
        mais_velhos.append(pessoa[0])
    else:
        mais_novos.append(pessoa[0])

print(total_de_idades)
print(dado)
print(lista_dados)
print(f'A média das idades é: {media_de_idades}')
print(f'As pessoas mais novas são: {mais_novos[:]}')
print(f'As pessoas mais velhas são: {mais_velhos[:]}')

