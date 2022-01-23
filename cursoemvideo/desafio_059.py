from time import sleep
from math import floor
print(f'{" Desafio 059 ":=^99}')
# Crie um programa que leia dois valores e mostre na tela um menu de opções com +, x, >, novos números e opção de sair.
print('>>> NÚMEROS E OPERAÇÕES COM MENU DE OPÇÕES')
print('.' * 99)
print('Escolha dois números inteiros para realizar operações entre eles:')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
programa = True
while programa:
    print()
    print('OPÇÕES: [0] Fechar programa [1] Somar  [2] Subtrair [3] Multiplicar  [4] Dividir [5] Escolher novos números')
    oe = int(input('Digite o número que represente a opção escolhida: '))
    print()
    if oe == 1:
        a = n1 + n2
        print('Resp.: {} ({} + {} = {}).'.format(a, n1, n2, a))
    elif oe == 2:
        if n1 > n2:
            s = n1 - n2
            print('Resp.: {} ({} - {} = {}).'.format(s, n1, n2, s))
        else:
            s = n2 - n1
            print('Resp.: {} ({} - {} = {}).'.format(s, n2, n1, s))
    elif oe == 3:
        m = n1 * n2
        print('Resp.: {} ({} x {} = {}).'.format(m, n1, n2, m))
    elif oe == 4:
        if n1 > n2:
            d = n1 / n2
            r = n1 % n2
            print('Resp.: {} ({} / {} = {}). Resto = {}.'.format(floor(d), n1, n2, floor(d), r))
        else:
            d = n2 / n1
            r = n2 % n1
            print('Resp.: {} ({} / {} = {}). Resto = {}.'.format(floor(d), n2, n1, floor(d), r))
    elif oe == 5:
        print('Escolha os números novamente:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif oe == 0:
        programa = False
        print('Encerrando o programa...')
        sleep(2)
        print('Programa finalizado!')
    else:
        print('Opção inválida, escolha novamente:')
print('.' * 99)
