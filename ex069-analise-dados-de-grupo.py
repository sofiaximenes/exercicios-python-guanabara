pessoas_maiores_18 = 0
mulheres_menores_20 = 0
homens_cadastrados = 0

while True:
    idade = int(input('Quantos anos você tem? '))
    sexo = str(input('Qual o seu sexo? [F/M]')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Qual o seu sexo? [F/M]')).strip().upper()[0]
    if idade >= 18:
        pessoas_maiores_18 += 1
    if sexo == 'M':
        homens_cadastrados += 1
    if sexo == 'F' and idade <= 20:
        mulheres_menores_20 += 1
    continuar = str(input('Mais alguém precisa ser cadastrado? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Mais alguém precisa ser cadastrado? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{pessoas_maiores_18} pessoas têm mais que 18 anos.\n {homens_cadastrados} homens foram cadastrados,\n '
      f'{mulheres_menores_20} mulheres têm menos de vinte anos.')



