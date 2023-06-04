numeros = ('um', 'dois', 'três',
           'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove',
           'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

print('.' * 30)
print(f'A lista dos números é {numeros}')
print('.' * 30)
print(f'Os cinco primeiros números são os{numeros[0:5]}')
print('.' * 30)
print(f'Os quatro últimos números são os {numeros[-4:]}')
print('.' * 30)
print(f'A ordem alfabética dos números corresponde a seguinte sequência: {sorted(numeros)}')
print('.'*30)
print(f'O número catorze está na {numeros.index("catorze")+1}ª posição')