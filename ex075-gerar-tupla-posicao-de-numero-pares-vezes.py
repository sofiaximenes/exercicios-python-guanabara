cont9 = 0
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
numeros = (n1, n2, n3, n4)
print(f'O número 9 aparece {numeros.count(9)} vezes nesta sequência')
print(f'O primeiro número 3 foi digitado na {numeros.index(3)+1}ª sequência')
for n in numeros:
    if n % 2 == 0:
        print(f'O(s) número(s) par(es) é(são) os {n}')
