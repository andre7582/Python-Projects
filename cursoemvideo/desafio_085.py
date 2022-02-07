print(f'{" Challenge 085 ":=^99}')
# Create a program where the user can enter seven numeric values and register them in a single list.
# At the end, show the even and odd values in ascending order.
print('>>> List with even and odd')
print("INSTRUCTIONS:\nEnter 7 numbers and the program will separate them into two lists: even numbers and odd numbers.")
print('-' * 99)
numbers = [[], []]
value = 0
for entry in range(1, 8):
	value = int(input(f'Enter the {entry}º number: '))
	if value % 2 ==0:
		numbers[0].append(value)
	else:
		numbers[1].append(value)
print('-' * 99)
numbers[0].sort()
numbers[1].sort()
print(f'List of even numbers: {numbers[0]} ')
print(f'List of odd numbers: {numbers[1]}')
print('-' * 99)
