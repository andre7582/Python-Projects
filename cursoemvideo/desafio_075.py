print(f'{" Desafio 075 ":=^99}')
# Crie um programa que leia 4 valores pelo teclado e guarde-os numa tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9; Em que posição foi digitado o primeiro valor 3; c) quais foram os números pares.
print('>>> Análise de dados em uma tupla')
# print('-' * 99)
# print("INSTRUÇÕES:\n .")
print('-' * 99)
numbers = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais outro número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os números: {numbers}')
print(f'O número 9 apareceu {numbers.count(9)} vezes.')
if 3 in numbers:
	print(f"O número 3 apareceu na {numbers.index(3) + 1}ª posição.")
else:
	print('O número 3 não foi digitado.')
print('Os valores pares digitados: ')
for n in numbers:
	if n % 2 == 0:
		print(n)
print('-' * 99)
