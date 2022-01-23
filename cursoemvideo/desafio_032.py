from datetime import date
print('====== Desafio 032 ======')
# Crie um programa que leia um ano qualquer e mostre se ele é bissexto.
print()
print('< O ANO É BISSEXTO? >')
print('-' * 51)
ano = int(input('Que ano quer analisar? (Coloque 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} {}é BISSEXTO!{}'.format(ano, '\033[32m', '\033[m'))
else:
    print('O ano {} {}NÃO é BISSEXTO!{}'.format(ano, '\033[31m', '\033[m'))
print('-' * 51)
