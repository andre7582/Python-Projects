print('====== Desafio 015 ======')
# .
print()
print('Quer saber quanto vai custar o aluguel do carro?')
print('-' * 51)
d = float(input('Informe o valor da diária: R$ '))
da = float(input('Informe quantos dias o carro foi alugado: '))
k = float(input('Informe o valor cobrado por Km rodados: R$ '))
kp = float(input('Informe quantos Km você andou com o carro: '))
t = d * da + k * kp
print()
print('O total a pagar é de aproximadamente R$ {:.2f}.'.format(t))
print('-' * 51)
