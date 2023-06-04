from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1,8):
    nasc = int(input(f'Qual a {pess}ª nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'No total, tivemos {totalmaior} pessoas maiores de idade e {totalmenor} pessoas menores de idade')