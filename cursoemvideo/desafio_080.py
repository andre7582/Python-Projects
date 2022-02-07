print(f'{" Desafio 080 ":=^99}')
# Crie um programa onde o utilizador possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição de inserção. No final, mostre a lista ordenada na tela.
print('>>> Lista ordenada sem repetições')
# print('-' * 99)
# print("INSTRUÇÕES:\n .")
print('-' * 99)
numbers = []
for index in range(0, 5):
	value = int(input('Enter a number: '))
	if index == 0 or value > numbers[-1]:
		numbers.append(value)
	else:
		position = 0
		while position < len(numbers):
			if value <= numbers[position]:
				numbers.insert(position, value)
				break
			position += 1
print(f'The numbers entered were: {numbers}.')
print('-' * 99)
