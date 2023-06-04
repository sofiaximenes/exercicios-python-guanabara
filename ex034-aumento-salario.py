sal = float(input('Digite o valor do seu salário: R$'))
if (sal <= 1.250,00):
    novo = sal + (sal * 0.15)

else:
   novo = sal + (sal * 0.10)

   # como prever o cálculo para números com dois pontos como R$1.250,00
print(f'Quem recebia R${sal:.2f} passará a receber R${novo:.2f}')