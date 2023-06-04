idade = int(input('Digite a idade do(a) competidor(a): '))
if idade <= 9:
    print('O(A) competidor(a) está na categoria MIRIM!')
elif 9 < idade <= 14:
    print('O(A) competidor(a) está na categoria INFANTIL!')
elif 14 < idade <= 19:
    print('O(A) competidor(a) está na categoria JÚNIOR!')
elif 19 < idade <= 20:
    print('O(A) competidor(a) está na categoria SÊNIOR!')
elif idade > 20:
    print('O(A) competidor(a) está na categoria MASTER!')