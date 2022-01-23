from math import trunc
print('====== Desafio 016 ======')
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
print()
num = float(input('Digite um número com decimais: '))
print('O valor digitado foi {} e a sua parte inteira é {}.'.format(num, trunc(num)))