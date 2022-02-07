print(f'{" Challenge 094 ":=^99}')
# Write a program that reads the name, gender and age of multiple people, storing each person's data in
# a dictionary and all dictionaries in a list. In the end, show: a) How many people were registered;
# b) The average age; c) A list of women; d) A list of people who are above average age.
print('>>> Final part of dictionaries and lists')
print("INSTRUCTIONS:\nEnter the data and the programa shows some select info about the people.")
print('-' * 99)
person = dict()
people = list()
amount = average = 0
while True:
	person['name'] = str(input('Name: '))
	person['gender'] = str(input('Gender [M/F]: ')).upper().strip()[0]
	while person['gender'] not in 'MF':
		print('Unexpected answer!')
		person['gender'] = str(input('Gender [Male/Female]: ')).upper().strip()[0]
	person['age'] = int(input('Age: '))
	amount += person['age']
	people.append(person.copy())
	towant = str(input('Do you want to enter more people? ')).upper().strip()[0]
	while towant not in 'YN':
		print('Unexpected answer!')
		towant = str(input('Do you want to enter more people? ')).upper().strip()[0]
	if towant in 'N':
		break
print('-' * 99)
print(f'a) {len(people)} people registered.')
average = amount / len(people)
print(f'b) The average age is: {average:2.1f} years.')
print(f'c) Registered women: ', end='')
for index in people:
	if index['gender'] in 'F':
		print(f'{index["name"]}; ', end='')
print()
'''print(f'd) People who are above average age: ', end='')
for index in people:
	if index['age'] > average:
		print(f'{index["name"]}; ', end='')
print()'''
print(f'd) List of people who are above average age: ')
for index in people:
	if index['age'] > average:
		print('   - ', end='')
		print(f'{index["name"]};')
'''print(f'd) List of people who are above average age: ')
for index in people:
	if index['age'] > average:
		print('    * ', end='')
		for key, value in index.items():
			print(f'{key}: {value}; ', end='')
		print()'''
print('=' * 99)
# print(person)
# print(people)
