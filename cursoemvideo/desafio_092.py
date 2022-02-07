from datetime import datetime
print(f'{" Challenge 092 ":=^99}')
# Create a program that reads name, year of birth and employment card and registers it (with age) in a dictionary.
# If by chance the employment card is different from ZERO, the dictionary will also receive the year of employment
# and salary. Calculate and add, in addition to age, at what age the person will retire.
print('>>> Employment Life')
print("INSTRUCTIONS:\nEnter the data and the program will show some employment life results.")
print('-' * 99)
data = dict()
data['name'] = str(input('Name: '))
birth = int(input('Year of birth: '))
data['age'] = datetime.now().year - birth
data['ecnum'] = int(input('Employment Card number [Not have = 0]: '))
if data['ecnum'] != 0:
	data['hired'] = int(input('Year of hire: '))
	data['wage'] = float(input('Wage: US$ '))
	data['retirement'] = ((data['hired'] + 30) - datetime.now().year) + data['age']
print('-' * 99)
print(f'{"Employment Info":*^30}')
for key, value in data.items():
	print(f' {key}: {value}')
print('=' * 99)
# print(data)
