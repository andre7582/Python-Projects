print('====== Desafio 011 ======')
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la. Considere que cada litro de tinta pinta uma área de aproximadamente 2m²
print()
print('Quer saber a quantidade de tinta que você vai precisar comprar para pintar uma parede?')
lp = float(input('Digite um valor para a largura da parede em metros: '))
ap = float(input('Digite um valor para a altura da parede em metros: '))
a = lp * ap
t = a / 2
print()
print('Resp.: A parede tem {} m² de área e são necessários {} litros de tinta para pintá-la.'.format(a, t))
