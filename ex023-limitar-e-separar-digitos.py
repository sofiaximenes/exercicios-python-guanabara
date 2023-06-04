num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 1000 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidades: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milrar: {m}')
