somadeidade = 0
mediaidadehomem = 0
homemmaisvelho = 0
nomevelho = ''
mulhermenor20 = 0
for pessoa in range(1, 5):
    print(f'-------{pessoa}ª PESSOA-------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somadeidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        homemmaisvelho = nome
    if sexo in 'Mm' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomevelho = nome
mediaidade = somadeidade/4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homemm mais velho tem {homemmaisvelho} e se chama {nomevelho}')
