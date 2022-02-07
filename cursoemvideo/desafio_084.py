print(f'{" Challenge 084 ":=^99}')
# Make a program that reads the name and weight of several people and saves everything in a list. At the end, show:
# a) How many people were registered; b) A list of the heaviest persons; c) Another list with the lightest ones.
print('>>> Composite list and data analysis')
print('-' * 99)
print("INSTRUCTIONS:\nRegister people and compare their weights.")
print('-' * 99)
temp = []
data = []
heaviest = 0
lighter = 0
while True:
	temp.append(str(input('Name: ')))
	temp.append(float(input('Weight: ')))
	if len(data) == 0:
		heaviest = lighter = temp[1]
	else:
		if temp[1] > heaviest:
			heaviest = temp[1]
		if temp[1] < lighter:
			lighter = temp[1]
	data.append(temp[:])
	temp.clear()
	answer = str(input('Do you want to enter more data? [Y/N]: ')).strip()[0]
	while answer not in 'YyNn':
		print('Unexpected answer!')
		answer = str(input('Do you want to continue enter more data? [Yes/No]: ')).strip()[0]
	if answer in 'Nn':
		break
print('-' * 99)
# print(f'All data: {data}')
print(f'You registered {len(data)} people.')
print(f'The heaviest weight was {heaviest} Kg. ', end='')
for heavy in data:
	if heavy[1] == heaviest:
		print(f'-> {heavy[0]} ', end='')
print()
print(f'The lighter weight was {lighter} Kg. ', end='')
for light in data:
	if light[1] == lighter:
		print(f'-> {light[0]} ', end='')
print()
print('-' * 99)
