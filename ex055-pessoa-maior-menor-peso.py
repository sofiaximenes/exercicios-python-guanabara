#pesomaior = 0
#pesomenor = 99999
#for pess in range(1, 6):
  #  peso = int(input(f'Qual o peso da {pess}ª pessoa? '))
   # if peso > pesomaior:
    #    pesomaior = peso
    #elif peso < pesomenor:
        #pesomenor = peso
#print(f'O maior peso digitado foi {pesomaior} e o menor foi {pesomenor}')

maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi o de {maior}Kg e o menor foi de {menor}Kg.')