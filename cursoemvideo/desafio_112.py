from mathPackage.myFunctions import *
print(f'{" Challenge 112 ":=^99}')
#
print('>>> Price analyzer (validating a input)')
print("INSTRUCTIONS:\n# Input a price and see the magic happens.")
print('-' * 99)
# main program
price = ismoneyp('> Input a price: US$')
shortcurrencyp(price)
print('=' * 99)
