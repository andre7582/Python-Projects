from mathPackage.myFunctions import *
print(f'{" Challenge 107 ":=^99}')
#
print('>>> Price analyzer')
print("INSTRUCTIONS:\n# Input a price and see the magic happens.")
print('-' * 99)
# main program
price = float(input('> Input a price: US$'))
print(f'* Half of US${price:.2f} is US${halfp(price):.2f}.')
print(f'* The double of US${price:.2f} is US${doublep(price):.2f}')
print(f'* Increasing the price by 10% we have US${increasep(price, 10):.2f}')
print(f'* The price with 10% discount is US${decreasep(price, 10):.2f}')
print('=' * 99)
