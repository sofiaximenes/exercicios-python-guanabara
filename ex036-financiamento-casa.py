valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Didite o valor do seu salário: R$ '))
anos = int(input('Digite em quantos anos você quer pagar a casa: '))
anos_em_meses = anos * 12
valor_da_prestacao = (valor_casa / anos_em_meses)
trinta_por_cento = (salario * 0.3)

if valor_da_prestacao > trinta_por_cento:
    print('Infelizmente o seu empréstimo não foi autorizado.')
else:
    print('PARABÉNS!! Seu empréstimo foi aprovado, você passará o resto da sua vida com uma dívida com o banco iiiieei')