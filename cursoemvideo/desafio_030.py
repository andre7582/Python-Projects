print('====== Desafio 030 ======')
# Crie um programa que leia um número inteiro e mostre na tela se ele é pra ou ímpar.
print()
print('< PAR OU ÍMPAR >')
print('-' * 51)
num = int(input('Digite um número inteiro: '))
numpi = num % 2
if numpi == 0:
    print('O número escolhido é \033[4:33mpar\033[m!')
else:
    print('O número que você escolheu é {}ímpar{}!'.format('\033[4:35m', '\033[m'))
print('-' * 51)
