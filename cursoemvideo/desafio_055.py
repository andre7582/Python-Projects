print(f'{" Desafio 055 ":=^99}')
# Faça um programa que leia o peso de cinco pessoas e no final mostre qual foi o maior e o menor peso lidos.
print('>>> MAIOR E MENOR DA SEQUÊNCIA COM PESOS')
print('.' * 99)
maior = 0
menor = 0
n = int(input('Quantos pesos serão comparados? '))
for p in range(1, n + 1):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg e o menor de {}kg.'.format(maior, menor))
print('.' * 99)
