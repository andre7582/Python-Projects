from datetime import date
print('====== Desafio 041 ======')
# Crie um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com sua idade:
print()
print('< Categoria dos atletas >')
print('.' * 99)
dat = date.today().year
nas = int(input('Ano de nascimento: '))
ida = dat - nas
print('O atleta tem {} anos.'.format(ida))
if ida <= 9:
    print('Classificação: MIRIM')
elif ida <= 14:
    print('Classificação: INFANTIL')
elif ida <= 19:
    print('Clasificação: JUNIOR')
elif ida <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
print('.' * 99)
