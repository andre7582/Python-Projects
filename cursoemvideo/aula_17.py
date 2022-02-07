# Listas:
numbers = list()
for grupo in range(0, 3):
	numbers.append(int(input(f'Digite um número para a Posição {grupo}: ')))
# numbers = [2, 5, 9, 1, 7]
print(numbers)
numbers.append(4)
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.insert(0, 2)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
if 5 in numbers:
	numbers.remove(5)
else:
	print('No Seven!')
print(numbers)
for position, valor in enumerate(numbers):
	print(f'Na posição {position} está o valor {valor}!')
valores = numbers[:]
valores[0] = 8
valores.append(3)
for valor in valores:
	print(f'{valor}, ', end='')
