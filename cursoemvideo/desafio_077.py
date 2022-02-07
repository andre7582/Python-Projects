print(f'{" Desafio 077 ":=^99}')
# Crie um program que tenha uma tupla com várias palavras, depois disso, você deve mostrar, para cada
# palavras, as vogais.
print('>>> Contando Vogais em Tupla')
# print('-' * 99)
# print("INSTRUÇÕES:\n .")
print('-' * 99)
palavras = ('bola', 'menina', 'praia', 'escola', 'melão', 'computador', 'café', 'tubaína', 'cajú')
for palavra in palavras:
	print(f'\nNa palavra {palavra.upper()} temos: ', end='')
	for letra in palavra:
		if letra.lower() in 'aáãâeéêioóõôuú':
			print(letra, end=', ')
print('\n')
print('-' * 99)
