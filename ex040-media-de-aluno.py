nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Infelizmente o aluno teve a média {media:.1f} e então será reprovado.')
elif 5 <= media <= 6.9:
    print(f'O aluno ficará de recuperação, pois teve média {media:.1f}.')
elif media >= 7:
    print(f'PARABÉNS! Sua média foi {media:.1f} e você está APROVADO(A)!!')