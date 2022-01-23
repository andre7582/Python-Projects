print('====== Desafio 013 ======')
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
s = float(input('Digite o valor de um salário que você deseja ver com 15% de aumento: R$ '))
s = float(s + (s * 0.15))
print('O novo valor do salário é de R$ {:.2f}.'.format(s))
