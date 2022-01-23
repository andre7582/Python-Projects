print(f'{" Desafio 052 ":=^99}')
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('>>> NÚMEROS PRIMOS')
print('.' * 99)
num = int(input('Digite um número para ver se ele é primo: '))
qua = 0
print('Divisores do número escolhido (em azul): ')
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[36m', end='')
        qua += 1
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, qua))
if qua == 2:
    print('O {} é considerado um número primo!'.format(num))
else:
    print('O {} NÃO é primo!'.format(num))
print('.' * 99)
