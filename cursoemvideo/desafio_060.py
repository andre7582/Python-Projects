from math import factorial
from time import sleep
print(f'{" Desafio 060 ":=^99}')
# Crie um programa que leia um número inteiro e mostre seu fatorial.
print('>>> CALCULADORA DE FATORIAL')
print('.' * 99)
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('Calculando {}!...'.format(n))
sleep(2)
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    n -= 1
print('{}.'.format(f))
print('.' * 99)
