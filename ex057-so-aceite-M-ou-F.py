'''M = 'M'
F = 'F'
sexo = str(input('Sexo: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    if sexo not in 'MF':
        print('Digite novamente uma opção válida')
        sexo = str(input('Sexo: ')).upper()
print('Obrigada por sua resposta.')'''

sexo = str(input('Informe seu sexo: [M/F}')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor digite novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')