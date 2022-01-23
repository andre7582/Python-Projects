print(f'{" Desafio 051 ":=^99}')
# Crie um programa que leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos.
print('>>> PROGRESSÃO ARITMÉTICA')
print('.' * 99)
pt = int(input('Primeiro termo da PA: '))
rz = int(input('Razão: '))
de = pt + (10 - 1) * rz
for c in range(pt, de + rz, rz):
    print('{} '.format(c), end=' -> ')
print('Acabou!')
print('.' * 99)
