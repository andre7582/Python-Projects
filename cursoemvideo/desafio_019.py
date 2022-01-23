import random
print('====== Desafio 019 ======')
# Um professor que sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.
print()
print('< Um dos 4 azarados >')
print('-' * 51)
n1 = str(input('Digite o nome do primeiro: '))
n2 = str(input('Digite o nome do segundo: '))
n3 = str(input('Digite o nome do terceiro: '))
n4 = str(input('Digite o nome do quarto: '))
lista = [n1, n2, n3, n4]
az = random.choice(lista)
print()
print('O azarado foi...{}'.format(az))
print('-' * 51)