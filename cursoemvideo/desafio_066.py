print(f'{" Desafio 066 ":=^99}')
# Crie um programa que leia vários números inteiros com uma condição para parar o programa: digitar 999.
# No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print('>>> TRATANDO VÁRIOS VALORES V2.0')
print('.' * 99)
print("INSTRUÇÕES:\nDigite quantos números você quiser que o programa vai calcular a soma deles.\nQuando desejar parar "
      "de inserir mais números digite o valor 999.  ")
print('.' * 99)
con = som = 0
num = int(input('Digite um número: '))
while True:
    con += 1
    som += num
    num = int(input('Digite mais um número: '))
    if num == 999:
        break
if con == 1:
    print(f'Você inseriu um número apenas com o seu valor igual a {som}.')
else:
    print(f'Você inseriu {con} números e a soma entre eles é igual a {som}.')
print('.' * 99)
