from random import randint
from time import sleep
print(f'{" Desafio 045 ":=^99}')
# Crie um programa que faça o computador jogar Jokenpô com você.
print('>>> JOKENPÔ')
print('.' * 99)
itens = ('Spock', 'Pedra', 'Papel', 'Tesoura')
compu = randint(1, 3)
print('''Suas opções:
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA''')
sleep(1)
jog = int(input('Qual é a sua jogada? '))
sleep(1)
print('    JO...')
sleep(1)
print('        KEN...')
sleep(1)
print('            PÔ!')
print('O computador jogou {} e você jogou {}.'.format(itens[compu], itens[jog]))
sleep(1)
if compu == 1:
    if jog == 1:
        print('Empatou!')
    elif jog == 2:
        print('Você venceu!')
    elif jog == 3:
        print('O computador venceu!')
    else:
        print('JOGADA INVÁLIDA!')
elif compu == 2:
    if jog == 1:
        print('O computador venceu!')
    elif jog == 2:
        print('Empatou!')
    elif jog == 3:
        print('Você venceu!')
    else:
        print('JOGADA INVÁLIDA!')
elif compu == 3:
    if jog == 1:
        print('Você venceu!')
    elif jog == 2:
        print('O computador venceu!')
    elif jog == 3:
        print('Empatou!')
    else:
        print('JOGADA INVÁLIDA!')
print('.' * 99)
