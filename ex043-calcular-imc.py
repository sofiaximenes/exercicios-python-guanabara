peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura:'))
imc = float(peso / (altura ** 2))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal.')
elif 25 <= imc < 30:
    print('Você está com obesidade.')
elif imc > 40:
    print('Você está com obesidade mórbida.')