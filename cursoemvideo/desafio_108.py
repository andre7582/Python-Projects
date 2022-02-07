from mathPackage.myFunctions import *
print(f'{" Challenge 108 ":=^99}')
#
print('>>> Price analyzer v2.0')
print("INSTRUCTIONS:\n# Input a price and see the magic happens.")
print('-' * 99)
# main program
price = float(input('> Input a price: US$'))
increase = int(input('> Choose a % increse: '))
decrease = int(input('> Choose a % discount: '))
print(f'* Half of {currencyp(price)} is {currencyp(halfp(price))}.')
print(f'* The double of {currencyp(price)} is {currencyp(doublep(price))}')
print(f'* Increasing the price by {increase}% we have {currencyp(increasep(price, increase))}')
print(f'* The price with {decrease}% discount is {currencyp(decreasep(price, decrease))}')
print('=' * 99)
