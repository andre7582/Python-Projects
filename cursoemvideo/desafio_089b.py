print(f'{" Challenge 089 ":=^99}')
# Make a program that reads the name and two grades of several students storing all the data in a composite list.
# At the end, show a report card containing the average grades of each one.
# The program should also allow the user to be more like each student's grades individually.
print('>>> School report card')
print("INSTRUCTIONS:\nEnter students grades and compare average grades.")
print('-' * 99)
data = []
while True:
	number = int(input('Number: '))
	name = str(input('Name: '))
	grade1 = float(input('Grade 1: '))
	grade2 = float(input('Grade 2: '))
	grade3 = float(input('Grade 3: '))
	average = (grade1 + grade2 + grade3) / 3
	data.append([number, name, grade1, grade2, grade3, average])
	answer = str(input('Do you want to add more one student? [Y/N]: ')).strip()[0]
	while answer not in 'YyNn':
		print('Unexpectd answer!')
		answer = str(input('Do YOU WANT to add more one student? [Yes/No]: ')).strip()[0]
	if answer in 'Nn':
		break
print('_' * 99)
print(f'| {"Nº":<3} | {"Name":<37} | {"Grade 1":>10} | {"Grade 2":>10} | {"Grade 3":>10} | {"Average":>10} |')
print('_' * 99)
for entry, pupil in enumerate(data):
	print(f'| {pupil[0]:<3} | {pupil[1]:<37} | {pupil[2]:>10} | {pupil[3]:>10} | {pupil[4]:>10} | {pupil[5]:>10.1f} |')
print('_' * 99)
# print(data)
print('=' * 99)
