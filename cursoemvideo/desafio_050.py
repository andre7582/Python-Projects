print(f'{" Desafio 050 ":=^99}')
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
print('>>> SOMA DOS PARES')
print('.' * 99)
q = int(input('Quantos números você deseja digitar? '))
s = 0
for c in range(1, q + 1):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        s = s + n
print('A soma dos números pares foi {}.'.format(s))
print('.' * 99)
