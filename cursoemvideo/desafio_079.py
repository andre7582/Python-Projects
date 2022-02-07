print(f'{" Desafio 079 ":=^99}')
# Crie um programa onde o usuário possa digitar vários valores e cadastre-os numa lista. Caso o número já exista
# ele não será adicionado. No final, serão exibidos todos os valores em ordem crescente.
print('>>> Valores únicos em uma Lista')
# print('-' * 99)
# print("INSTRUÇÕES:\n .")
print('-' * 99)
numbers = []
while True:
	value = int(input('Digite um valor: '))
	if value not in numbers:
		numbers.append(value)
		print('Valor adicionado!')
	else:
		print('O valor não foi adicionado à lista pois está duplicado.')
	answer = str(input('Quer continuar? [S/N]: '))
	while answer not in 'NnSs':
		print('Resposta não esperada!')
		answer = str(input('Quer continuar? [S/N]: '))
	if answer in 'Nn':
		break
numbers.sort()
print(f'Você digitou os valores: {numbers}.')
print('-' * 99)
