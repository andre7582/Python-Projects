print('====== Desafio 014 ======')
# Escreva um programa que converta uma temperatura digitada em ºC para ºF.
print()
print('Conversor de temperaturas > Celsius para Fahrenheit')
print('-' * 51)
c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print()
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!.'.format(c, f))
print('-' * 51)
