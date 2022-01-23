print('====== Desafio 027 ======')
# Faça um programa que leia o nome completo de uma pessoa mostrando o primeiro e o último nome separadamente.
print()
n = str(input('Digite seu nome completo: ')).strip()
ns = n.split()
print('Seu primeiro nome é {}.'.format(ns[0]))
print('Seu último nome é {}.'.format(ns[len(ns)-1]))
