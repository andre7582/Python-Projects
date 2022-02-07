from mathPackage.myFunctions import *
print(f'{" Challenge 104 ":=^99}')
# Create a program that has the readint() function, which will work similarly to the Python input() function,
# only validating to accept only a numeric value.
print(">>>  Validating a numeric value")
print("INSTRUCTIONS:\n# Input a value and the program will validating it as a positive integer or not.")
print('-' * 99)


"""def readintp(answer):
	ok = False
	value = 0
	while True:
		num = str(input(answer))
		if num.isnumeric():
			value = int(num)
			ok = True
		else:
			print('% Error 404 %')
		if ok:
			break
	return value"""


number = readintp('- Input a number (positive integer): ')
print(f'> You just typed the number {number}.')

print('=' * 99)
