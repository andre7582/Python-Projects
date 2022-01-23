from math import hypot
print('====== Desafio 017 ======')
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
print()
print('< Calcular a hipotenusa de um triângulo retângulo >')
print('-' * 51)
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1 / 2)
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(hi))
print('-' * 51)
