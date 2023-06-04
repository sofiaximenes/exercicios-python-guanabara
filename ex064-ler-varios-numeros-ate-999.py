n = 0
cont = 0
s = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
    s = n + s
    if n == 999:
        break
print(f'Foram digitados {cont} números e a soma entre eles é {s}')
