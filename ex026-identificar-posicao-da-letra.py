frase = str(input('Digite uma frase? ')).strip().upper()
print(f"A letra 'A' aparece {frase.upper().count('A')} vezes na sua frase")
print(f"a letra 'A' aparece pela primeira vez na posição {frase.find('A')+1}")
print(f"A letra 'A' aparece pela última vez na posição {frase.rfind('A')+1}")
