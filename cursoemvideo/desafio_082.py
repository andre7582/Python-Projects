print(f'{" Desafio 082 ":=^99}')
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas que vão
# conter apenas valores pares e ímpares deigitados. Ao final, mostre o conteúdo das três listas geradas.
print('>>> Dividindo valores em várias listas')
# print('-' * 99)
# print("INSTRUÇÕES:\n .")
print('-' * 99)
numbers = list()
pairs = []
odd = []
while True:
	numbers.append(int(input('Enter a number: ')))
	answer = str(input('Do you want to continue? [Y/N]: ')).strip()[0]
	while answer not in 'YyNn':
		print('Unexpected answer!')
		answer = str(input('Do you want to continue? [Yes/No]: ')).strip()[0]
	if answer in 'Nn':
		break
for index, value in enumerate(numbers):
	if value % 2 == 0:
		pairs.append(value)
	elif value % 2 == 1:
		odd.append(value)
print(f'The complete list is: {numbers}.')
print(f'The list of even numbers is: {pairs}.')
print(f'The odd list is: {odd}')
print('-' * 99)
