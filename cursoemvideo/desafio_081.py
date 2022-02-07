print(f'{" Desafio 081 ":=^99}')
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: a) quantos valores
# foram digitados; b) A lista de valores em ordem decrescente; # c) Se o valor 5 foi digitado e está ou não na lista.
print('>>> Extraindo dados de uma Lista')
# print('-' * 99)
# print("INSTRUÇÕES:\n .")
print('-' * 99)
numbers = []
while True:
	numbers.append(int(input('Enter a number: ')))
	answer = str(input('Do you want to continue? [Y/N]: ')).strip()[0]
	while answer not in 'YyNn':
		print('Unexpected answer!')
		answer = str(input('Do you want to continue? [Yes/No]: ')).strip()[0]
	if answer in 'Nn':
		break
print(f'You typed {len(numbers)} numbers.')
numbers.sort(reverse=True)
print(f'The values in descending order are: {numbers}')
if 5 in numbers:
	print('The number 5 is on the list!')
else:
	print('The number "five" was not typed.')
print('-' * 99)
