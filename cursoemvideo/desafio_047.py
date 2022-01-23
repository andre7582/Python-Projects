print(f'{" Desafio 047 ":=^99}')
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('>>> SÓ OS PARES')
print('.' * 99)
i = int(input('Escolha o inicio do intervalo: '))
f = int(input('Escolha o final do intervalo: '))
p = i % 2
print('Os números pares no intervalo escolhido são:')
if p == 0:
    for c in range(i + 2, f, 2):
        print(c, end=' ')
else:
    for c in range(i + 1, f, 2):
        print(c, end=' ')
print()
print('.' * 99)
