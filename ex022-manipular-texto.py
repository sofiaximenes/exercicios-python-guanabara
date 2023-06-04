nome = str(input('Digite aqui o nome completo: ')).strip()
# nomemai = nome.upper()
print (f'O nome em letras maiúsculas é: {nome.upper()}')

# nomemin = nome.lower()
print (f'O nome em letras minúscula é: {nome.lower()}')

# nomese = len(nome.replace(' ',''))
# nomeses = len(nome[0])
# print (f'O nome tem {nomese} e o seu primeiro {nomeses} letras')

## print (f'Seu nome tem ao todo {(len(nome) - nome.count())} letras')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome tem {} letras'.format(nome.find('')))