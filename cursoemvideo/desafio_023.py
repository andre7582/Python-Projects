print('====== Desafio 023 ======')
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
print()
print('< Identificar a ordem de um dígito no número >')
print('-' * 51)
num = int(input('Digite um número (até 9999): '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número...')
if u == 0:
    print('A ordem da UNIDADE está vazia!')
else:
    print('Algarismo na casa da UNIDADE: {}'.format(u))
if d == 0:
    print('A ordem da DEZENA está vazia!')
else:
    print('Algarismo na casa da DEZENA: {}'.format(d))
if c == 0:
    print('A ordem da CENTENA está vazia!')
else:
    print('Algarismo na casa da CENTENA: {}'.format(c))
if m == 0:
    print('A ordem da UNIDADE DE MILHAR está vazia!')
else:
    print('Algarismo na casa da UNIDADE DE MILHAR: {}'.format(m))
print('-' * 51)
