from random import randint
print(f'{" Desafio 074 ":=^99}')
# Crie um programa que vai gerar cinco números aleatórios e colocar numa tupla. Depois mostre a listagem de números
# e indique o menor e maior valor que estão na tupla.
print('>>> Maior e Menor Valor Sorteados')
# print('-' * 99)
# print("INSTRUÇÕES:\n .")
print('-' * 99)
numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Números sorteados: {numbers}')
print(f'O maior valor sorteado foi {max(numbers)}.')
print(f'O menor valor sorteado foi {min(numbers)}.')
print('-' * 99)
