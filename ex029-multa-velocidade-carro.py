vel = int(input('Qual a velocidade do carro? '))
multa = (vel-80) * 7
if vel > 80:
        print(f'Tenha mais cuidado no trânsito! Você receberá uma multa por excesso de velocidade no valor de R${multa},00')
else:
        print('Parabéns, você está de acordo com o limite de velocidade deste local!')