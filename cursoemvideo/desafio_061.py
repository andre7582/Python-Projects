print(f'{" Desafio 062 ":=^99}')
# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, usando a estrutura while.
print('>>> PROGRESSÃO ARITMÉTICA V2.0')
print('.' * 99)
pt = int(input('Primeiro termo da PA: '))
rz = int(input('Razão: '))
ct = 1
while ct <= 10:
    print('Resp.: ' if ct == 1 else '', end='')
    print('{}'.format(pt), end='')
    print(', ' if ct < 10 else '.', end='')
    pt += rz
    ct += 1
print()
print('.' * 99)
