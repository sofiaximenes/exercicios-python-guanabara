print('Vamos ver se poderemos formar um triângulo com as linhas com o tamanho escolhido por você?')

a = float(input('Digite o tamanho do lado A: '))
b = float(input('Digite o tamanho do lado B: '))
c = float(input('Digite o tamanho do lado C: '))
if a < b + c and  b < c + a and  c < a + b:
    print('Sim, poderá ser formado um triângulo!')
else:
    print('Vixi, com essas linhas nós não conseguiremos formar um triângulo :(')