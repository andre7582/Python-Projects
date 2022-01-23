from random import randint
from time import sleep
print('====== Desafio 028 ======')
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# Condição: o programa deverá escrever na tela se o usuário acertou ou não.
print()
print('< Adivinhe o número que o computador escolherá! >')
print('-' * 51)
random_num = randint(0, 5)
num = int(input('Digite um número de 0 a 5: '))
print('Analisando o número...')
sleep(3)
if num == random_num:
    print('Parabéns! Você acertou!\nO número que o computador pensou era realmente o {}.'.format(random_num))
else:
    print('Que pena você perdeu!\nO computador pensou no número {}.'.format(random_num))
print('-' * 51)
