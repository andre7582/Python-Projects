print(f'{" Challenge 102 ":=^99}')
# Create a program that has a factorial() function that receives two parameters: the first one that indicates
# the number to be calculated and another called show, which will be a logical value (optional) indicating whether
# the factorial calculation process will be shown on the screen.
print('>>> Factorial calculator ')
print("INSTRUCTIONS:\nInput a number to calculate factorial. Optional: You can see the calculation process.")
print('-' * 99)


def factorial(number, show=False):
	"""
	-> Calulates the factorial of a number, with the option to show the calculation process
	:param number: number to calculate the factorial
	:param show: option to show the calculation process
	:return: return the factorial of the typed number
	"""
	result = 1
	for count in range(number, 0, -1):
		if show:
			print(count, end='')
			if count > 1:
				print(' x ', end='')
			else:
				print(' = ', end='')
		result *= count
	return result


n = int(input('- Input a number to calculate factorial: '))
print(f'Answer: {factorial(n)}.')
question = str(input('- Do you want to see the factorial calculation process? [Y/N]: ')).strip().upper()[0]
if question in 'Y':
	print('Calculation process: ', end='')
	print(f'{factorial(n, show=True)}')
else:
	from time import sleep
	print('> Terminating the program..')
	sleep(1)
	print('> terminating the program...')
	sleep(0.5)
	print('> Program closed.')

print('=' * 99)
# help(factorial)
