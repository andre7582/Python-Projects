print('====== Desafio 023B ======')
# Faça um programa que leia um número de 0 a 999999 e mostre na tela o valor posicional de cada algarismo.
print()
print('< Informar o valor posicional de um algarismo no número >')
print('-' * 51)
num = int(input('Digite um número (até 999999): '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
dm = num // 10000 % 10
cm = num // 100000 % 10
print('Analisando o número...')
if u == 0:
    print('A ordem da UNIDADE está vazia!')
else:
    print('O algarismo na ordem da UNIDADE vale...: {}'.format(u * 1))
if d == 0:
    print('A ordem da DEZENA está vazia!')
else:
    print('O algarismo na ordem da DEZENA vale...: {}'.format(d * 10))
if c == 0:
    print('A ordem da CENTENA está vazia!')
else:
    print('O algarismo na ordem da CENTENA vale...: {}'.format(c * 100))
if um == 0:
    print('A ordem da UNIDADE DE MILHAR está vazia!')
else:
    print('O algarismo na ordem da UNIDADE DE MILHAR vale...: {}'.format(um * 1000))
if dm == 0:
    print('A ordem da DEZENA DE MILHAR está vazia!')
else:
    print('O algarismo na ordem da DEZENA DE MILHAR vale...: {}'.format(dm * 10000))
if cm == 0:
    print('A ordem da CENTENA DE MILHAR está vazia!')
else:
    print('O algarismo na ordem da CENTENA DE MILHAR vale...: {}'.format(cm * 100000))
print('-' * 51)
