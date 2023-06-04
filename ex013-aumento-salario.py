# entrada
salario = float(input('Digite o seu atual salário: R$ '))
#aumento = 0
#novo_salario = 0

# cálculos
if salario <= 280:
    aumento = "20%"
    novosalario = float(salario + (salario * 0.2))

if salario > 280 and salario < 700:
    aumento = "15%"
    novosalario = float(salario + (salario * 0.15))

if salario >= 700 and salario < 1500:
    aumento = "10%"
    novosalario = float(salario + (salario * 0.10))

if salario >= 1500:
    aumento = "5%"
    novosalario = float(salario + (salario * 0.5))
# saídas
print(f'Seu novo salário com aumento de {aumento} corresponderá a: R${novosalario}')

