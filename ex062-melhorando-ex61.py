primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termos = 10
a = 2
s = s
n = n
print(f"{primeiro}", end=" ")
while a <= termos:
    an = primeiro + (a - 1) * razao
    print(f" {an}")
    a += 1

resposta = input('Você deseja mostrar um novo termo?[S/N]').upper()
if resposta == S:
    termos = resposta
    an = primeiro + (a - 1) * razao
    print(f"{primeiro}, ", end="")
while a <= termos:
    an = primeiro + (n - 1) * razao
    print(f" {an}", end=",")
    a += 1