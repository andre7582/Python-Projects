print(f'{" Challenge 087 ":=^99}')
# Improve the previous exercise, showing at the end: a) The sum of all even values;
# b) The sum of the values in the third column; c) The largest value of the second row.
print('>>> 3x3 Table')
print("INSTRUCTIONS:\nEnter nine values (0 to 99) for the program to generate a 3x3 table with them & show some info.")
print('-' * 99)
table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spairs = scolumn = hvalue = 0
for line in range(0, 3):
	for column in range(0, 3):
		table[line][column] = int(input(f'Enter the number for [{line},{column}]: '))
print('-' * 99)
print('# TABLE 3x3 #')
for line in range(0, 3):
	for column in range(0, 3):
		print(f'[{table[line][column]:>2}] ', end='')
		if table[line][column] % 2 == 0:
			spairs += table[line][column]
	print()
print('-' * 99)
# print(spairs)
print(f'a) The sum of even numbers is: {spairs}.')
for line in range(0, 3):
	scolumn += table[line][2]
print(f'b) The sum of the values in the third column is: {scolumn}.')
for column in range(0, 3):
	if column == 0:
		hvalue = table[1][column]
	elif table[1][column] > hvalue:
		hvalue = table[1][column]
print(f'c) The highest value of the second row is: {hvalue}.')
print('=' * 99)
