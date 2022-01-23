from math import radians, sin, cos, tan
print('====== Desafio 018 ======')
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
print()
print('< Calcular o seno, o cosseno e a tangente de um ângulo qualquer >')
print('-' * 51)
ang = float(input('Digite um ângulo qualquer: '))
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Seno: {:.2f} | Cosseno: {:.2f} | Tangente: {:.2f}'.format(sin, cos, tan))
print('-' * 51)
