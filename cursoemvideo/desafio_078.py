print(f'{" Desafio 078 ":=^99}')
# Faça um programa que leia 5 valores e guarde-os em uma lista. No final, mostre qual foi o menor e o maior valor
# e suas respectivas posições.
print('>>> Maior e menor valor em Lista')
# print('-' * 99)
# print("INSTRUÇÕES:\n .")
print('-' * 99)
# numbers = list()
numbers = []
bigger = 0
smaller = 0
for position in range(0, 5):
	numbers.append(int(input(f'Digite um valor para a Posição {position}: ')))
	if position == 0:
		bigger = smaller = numbers[position]
	else:
		if numbers[position] > bigger:
			bigger = numbers[position]
		if numbers[position] < smaller:
			smaller = numbers[position]
print(f'Você digitou os valores: {numbers}.')
print(f'O maior valor digitado foi o {bigger}, nas posições: ', end='')
for index, value in enumerate(numbers):
	if value == bigger:
		print(f'{index}, ', end='')
print()
print(f'O menor valor digitado foi o {smaller}, nas posições: ', end='')
for index, value in enumerate(numbers):
	if value == smaller:
		print(f'{index}, ', end='')
print()
print('-' * 99)
