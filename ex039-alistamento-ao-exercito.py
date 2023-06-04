#ano = int(input('Digite aqui o ano em que você nasceu: '))
#if (2022 - ano) < 18:
    # print(f'Faltam {2022 - ano} ano(s) para você se alistar.')
#elif (2022 - ano) > 18:
    # print(f'Vixi, era pra você ter se alistado há {(2022 - ano) - 18} ano(s).')
#elif (2022 - ano) == 18:
    # print (f'Está na hora de você se alistar!')
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
     print(f'Está na hora de você se alistar!')
elif idade < 18:
     saldo = 18 - idade
     print(f'Faltam {saldo} ano(s) para você se alistar.')
elif idade > 18:
     saldo = idade - 18
     print('Você já deveria ter se alistado há {saldo} anos')
