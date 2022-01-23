print('====== Desafio 034 ======')
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Condições: Para salários superiores a R$1.250.00, calcule um aumento de 10%. <= o aumento é de 15%.
print()
print('< Calcule o aumento do salário. >')
print('-' * 51)
sal = float(input('Digite o valor do salário: R$ '))
if sal <= 1250:
    ns = sal + (sal * 0.15)
else:
    ns = sal + (sal * 0.1)
print('Seu novo salário é de R$ \033[35m{:.2f}\033[m.'.format(ns))
# if sal > 1250:
#     print('O novo valor do salário é de R$ \033[34m{:.2f}\033[m.'.format(sal + sal * 0.1))
# else:
#     print('O novo valor do salário é de R$ \033[33m{:.2f}\033[m.'.format(sal + sal * 0.15))
print('-' * 51)
