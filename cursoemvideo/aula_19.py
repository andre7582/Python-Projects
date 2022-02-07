'''movie = dict(title='Star Wars', year=1977, director='George Lucas')
for key, value in movie.items():
	print(f'The {key} is {value}.')
print('.' * 99)
girl = {'name': 'Laura', 'age': 11, 'eyes': 'brown'}
for key, value in girl.items():
	print(f'The {key} is {value}.')
print('+' * 19)
girl['name'] = 'Maria'
girl['age'] = 10
for key, value in girl.items():
	print(f'The {key} is {value}.')
print('+' * 19)
girl['name'] = 'Isabely'
del girl['eyes']
girl['weight'] = 32
for key, value in girl.items():
	print(f'The {key} is {value}.')'''

girl = dict()
course = list()
for entry in range(0, 3):
	girl['name'] = str(input('Name: '))
	girl['Age'] = str(input('Age: '))
	course.append(girl.copy())
for girl in course:
	for key, value in girl.items():
		print(f'{key}: {value}', end=' | ')
	print()
