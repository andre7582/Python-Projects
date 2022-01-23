print(f'{" Desafio 065 ":=^99}')
# Crie um programa que leia vários números inteiros com uma condição para parar caso o usuário deseje.
# No final mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
print('>>> TRATANDO VÁRIOS VALORES - MAIOR E MENOR VALOR')
print('.' * 99)
print("INSTRUÇÕES:\nDigite quantos números você quiser que o programa vai calcular média entre eles e identificar "
      "o \nmaior e o menor valor digitado. Quando desejar parar de inserir mais números responda 'N'.")
print('.' * 99)
res = 'S'
con = som = 0
num = int(input('Digite um número: '))
som += num
con += 1
mai = men = num
while res == 'S':
    num = int(input('Digite mais um número: '))
    con += 1
    som += num
    if num > mai:
        mai = num
    elif num < men:
        men = num
    res = str(input('Digite [S] para continuar e [N] para parar: ')).upper().strip()[0]
med = som / con
print()
print('O maior valor que você digitou foi o {} e o menor foi o {}.'.format(mai, men))
print('Você inseriu {} números e a média entre eles é {}.'.format(con, med))
print('.' * 99)
