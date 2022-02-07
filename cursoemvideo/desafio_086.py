print(f'{" Challenge 086 ":=^99}')
# Write a program that creates a 3x3 dimensional table and fill it with values entered by keyboard.
# At the end, show the matrix on the screen, with the correct formatting.
print('>>> 3x3 Table')
print("INSTRUCTIONS:\nEnter nine values (0 to 99) for the program to generate a 3x3 table with them.")
print('-' * 99)
table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for line in range(0, 3):
	for column in range(0, 3):
		table[line][column] = int(input(f'Enter the number for [{line},{column}]: '))
print('-' * 99)
for line in range(0, 3):
	for column in range(0, 3):
		print(f'[{table[line][column]:>2}] ', end='')
	print()
print('-' * 99)
