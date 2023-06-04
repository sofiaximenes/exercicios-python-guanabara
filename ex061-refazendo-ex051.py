primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termos = 10
n = 2
print(f"{primeiro}, ", end="")
while n <= termos:
    an = primeiro + (n - 1) * razao
    print (f" {an}", end=", ")
    n += 1

    #print(f' x ' if c > 1 else ' = ', end='')

#decimo = primeiro + (10 - 1) * razao
#while decimo < 10 and decimo > 0:
#    print(f'{decimo}')
#print('ACABOU')