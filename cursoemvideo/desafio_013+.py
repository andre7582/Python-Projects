print('====== Desafio 013 ======')
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
print()
print('Quer saber quanto vai receber após o aumento?')
s = float(input('Digite o valor do seu salário: R$ '))
a = float(input('Digite o aumento em porcentagem: '))
sa = s + (s * a / 100)
print()
print('O novo valor do seu salário com {:.0f}% de aumento é de R$ {:.2f}.'.format(a, sa))
