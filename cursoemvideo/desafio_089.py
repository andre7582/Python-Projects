print(f'{" Challenge 089 ":=^99}')
# Make a program that reads the name and two grades of several students storing all the data in a composite list.
# At the end, show a report card containing the average grades of each one.
# The program should also allow the user to be more like each student's grades individually.
print('>>> School report card')
print("INSTRUCTIONS:\nEnter students grades and compare average grades.")
print('-' * 99)
data = []
while True:
	name = str(input('Name: '))
	grade1 = float(input('Grade 1: '))
	grade2 = float(input('Grade 2: '))
	average = (grade1 + grade2) / 2
	data.append([name, [grade1, grade2], average])
	answer = str(input('Do you want to add more one student? [Y/N]: ')).strip()[0]
	while answer not in 'YyNn':
		print('Unexpectd answer!')
		answer = str(input('Do YOU WANT to add more one student? [Yes/No]: ')).strip()[0]
	if answer in 'Nn':
		break
print('-' * 99)
print('-' * 32)
print(f' {"Nº":<5}{"Name":<15}{"Average":>10}')
print('_' * 32)
for entry, student in enumerate(data):
	print(f' {entry+1:<5}{student[0]:<15}{student[2]:>10.1f}')
print('-' * 32)
print('-' * 99)
while True:
	print()
	question = int(input('Show grades of which student? [0 stop the program]: '))
	number = question - 1
	if number < 0:
		break
	elif number <= len(data) - 1:
		print(f'Grades of {data[number][0]} are: {data[number][1]}')
print('-' * 99)
# print(data)
print('=' * 99)
