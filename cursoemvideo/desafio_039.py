print('====== Desafio 039 ======')
# EFala um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda
# vai se alistar ou se já passou o tempo do alistamento. Seu programa também deverá mostrar o tempo que falta
# ou o tempo que passou do prazo.
print('< Alistamento militar >')
print('.' * 91)
from datetime import date
aat = date.today().year
ana = int(input('Ano de nascimento: '))
ida = aat - ana
print('Quem nasceu em {} tem {} anos em {}.'.format(ana, ida, aat))
if ida == 18:
    print('Você precisa se alistar esse ano!')
elif ida < 18:
    dif = 18 - ida
    ano = aat + dif
    print('Ainda faltam {} anos para você se alistar!'.format(dif))
    print('Seu alistamento será em {}.'.format(ano))
elif ida > 18:
    sob = ida - 18
    anu = aat - sob
    print('Você já deveria ter se alistado há {} anos!'.format(sob))
    print('Seu alistamento foi em {}.'.format(anu))
print('.' * 91)
