from random import shuffle
print('====== Desafio 020 ======')
# Um professor que sortear a ordem de apresentação de trabalhos dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
print()
print('< Ordem de apresentação dos alunos >')
print('-' * 51)
n1 = str(input('Digite o nome do primeiro: '))
n2 = str(input('Digite o nome do segundo: '))
n3 = str(input('Digite o nome do terceiro: '))
n4 = str(input('Digite o nome do quarto: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print()
print('A ordem de apresentação será...')
print(lista)
print('-' * 51)
