from time import sleep
print(f'{" Challenge 099 ":=^99}')
# Write a program that has a function called bigger(), which takes several parameters with integer values.
# Your program has to analyze all the values and say which one is the biggest.
print('>>> Biggest')
print("INSTRUCTIONS:\nInput several integer values and the program will show you which one is the biggest.")
print('-' * 99)


def separator():
	print('.' * 99)


def bigger(*numbers):
	count = 0
	biggest = 0
	print('Analyzing the numbers...')
	for value in numbers:
		print(f'{value}; ', end='')
		sleep(0.3)
		if count == 0:
			biggest = value
		elif value > biggest:
			biggest = value
		count += 1
	print()
	print(f'* {count} numbers were entered.')
	print(f'* The biggest number was {biggest}.')
	separator()


bigger(3, 7, 4)
bigger(12, 34, 1, 5, 8, 9, 11)
bigger()
bigger(8, -5, 7, 0)
bigger(-1, -5)

print('=' * 99)
