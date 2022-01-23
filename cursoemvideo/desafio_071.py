print(f'{" Desafio 071 ":=^99}')
# Crie um programa que simule o funcionamento de um caixa eletrônico. Pergunte qual será o valor a ser sacado
# e informe quantas cédulas de cada valor serão entregues.
print('>>> SIMULADOR DE CAIXA ELETRÔNICO')
print('.' * 99)
print("INSTRUÇÕES:\nDigite o valor que deseja sacar.\nEspere para ver o valor das notas que sairão do caixa.")
print('.' * 99)
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
saque = int(input('Valor a ser sacado: R$ '))
total = saque
dinheiro = 100
cedulas = 0
while True:
	if total >= dinheiro:
		total -= dinheiro
		cedulas += 1
	else:
		if cedulas > 0:
			print(f'Total de {cedulas} cédulas de R$ {dinheiro}.')
		if dinheiro == 100:
			dinheiro = 50
		elif dinheiro == 50:
			dinheiro = 20
		elif dinheiro == 20:
			dinheiro = 10
		elif dinheiro == 10:
			dinheiro = 5
		elif dinheiro == 5:
			dinheiro = 2
		elif dinheiro == 2:
			dinheiro = 1
		cedulas = 0
		if total == 0:
			break
print('Obrigado por usar nosso banco!')

print('.' * 99)
