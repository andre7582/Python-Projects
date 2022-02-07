from time import sleep
print(f'{" Desafio 072 ":=^99}')
# Crie em programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 até 20.
# Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.
print('>>> Números por extenso (0 a 20)')
print('-' * 99)
print("INSTRUÇÕES:\nDigite um número de 0 até 20 para ver sua escrita extensa.")
print('-' * 99)
extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
resposta = ''
while True:
	numero = int(input("Digite um número entre 0 e 20: "))
	if 0 <= numero <= 20:
		print(f'Você digitou o número "{extensos[numero]}".')
		print('')
		resposta = str(input('Quer digitar outro número? ')).upper().strip()[0]
		print('')
		if resposta == 'S':
			sleep(1)
		elif resposta == 'N':
			print('Finalizando programa.')
			sleep(1)
			print('Finalizando programa..')
			sleep(1)
			print('Finalizando programa...')
			sleep(0.5)
			print('Programa finalizado.')
			break
		else:
			print('Entrada inesperada! Tente novamente.')
	else:
		print('Os números devem pertencer conjunto informado nas instruções.')
		print('')
print('=' * 99)
