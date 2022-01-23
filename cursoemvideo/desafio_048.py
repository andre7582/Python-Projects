print(f'{" Desafio 048 ":=^99}')
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontrem no
# intervalo de 1 até 500.
print('>>> SOMA DOS ÍMPARES')
print('.' * 99)
i = int(input('Escolha o inicio do intervalo: '))
f = int(input('Escolha o final do intervalo: '))
p = i % 2
s = 0
n = 0
if p == 0:
    for c in range(i + 1, f, 2):
        if c % 3 == 0:
            n = n + 1
            s = s + c
else:
    for c in range(i + 2, f, 2):
        if c % 3 == 0:
            n = n + 1
            s = s + c
print('A soma de todos os {} valores ímpares divisíveis por 3 é igual a {}.'.format(n, s))
print('.' * 99)
