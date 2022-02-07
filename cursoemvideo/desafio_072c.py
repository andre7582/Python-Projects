from time import sleep
print(f'{" Desafio 072 ":=^99}')
# Crie em programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 até 20.
# Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.
print('>>> Números por extenso (0 a 20)')
print('-' * 99)
print("INSTRUÇÕES:\nDigite um número de 0 até 20 para ver sua escrita extensa.")
print('-' * 99)
full = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
answer = ''
while True:
	value = int(input('Digite um valor: '))
	if value >= 0 | value <= 20:
		print(f'Você digitou o número "{full[value]}".')
	else:
		print('Os números devem pertencer conjunto informado nas instruções.')
	answer = str(input('Quer continuar? [S/N]: '))
	if answer in 'Nn':
		print('Finalizando programa.')
		sleep(1)
		print('Finalizando programa..')
		sleep(0.5)
		print('Programa finalizado.')
		break
	while answer not in 'NnSs':
		print('Resposta não esperada!')
		answer = str(input('Quer continuar? [S/N]: '))
print('=' * 99)
