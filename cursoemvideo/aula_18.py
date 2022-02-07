'''person = []
person.append('Mary')
person.append(10)
gang = []
gang.append(person[:])
person[0] = 'Laura'
person[1] = 11
gang.append(person[:])
print(gang)'''
'''group = [['Mary', 19], ['Laura', 11], ['Isabel', 30], ['Manu', 14]]
for girl in group:
	print(f'{girl[0]} have {girl[1]} yo.')'''
crowd = []
data = []
older = 0
younger = 0
for counter in range(0, 3):
	data.append(str(input('Name: ')))
	data.append(int(input('Age: ')))
	crowd.append(data[:])
	data.clear()
for girl in crowd:
	if girl[1] >= 18:
		print(f'{girl[0]} is 18 years old or older.')
		older += 1
	else:
		print(f'{girl[0]} is under than 18 years old.')
		younger += 1
print(f'There are {older} girls older than 18 y.o and {younger} girls under 18 y.o.')
