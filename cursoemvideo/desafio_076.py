print(f'{" Desafio 076 ":=^99}')
# Crie um programa que tenha uma tupla única com os nomes de produtos e seus respectivos preços.
# No final, mostre uma listagem de preços organizando os dados em forma tabular.
print('>>> Lista de preços com tupla')
# print('-' * 99)
# print("INSTRUÇÕES:\n .")
print('-' * 99)
lista = ('Lápis', 1.75,
         'Borracha', 2.50,
         'Caderno', 17.80,
         'Estojo', 11.25,
         'Mochila', 69.90,
         'Caneta', 3.40,
         'Cola', 3.70)
print('LISTA DE PREÇOS:')
for position in range(0, len(lista)):
	if position % 2 == 0:
		print(f'{lista[position]:.<21}', end='')
	else:
		print(f' R$ {lista[position]:>5.2f}')
print('-' * 99)
