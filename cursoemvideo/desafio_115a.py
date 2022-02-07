from libs.interfaces.menus import *
print(f'{" Challenge 115a ":=^99}')
#
print('>>> ')
print("INSTRUCTIONS:\n# .")
print('-' * 99)
# main program

while True:
	answer = menu(['Register people', 'List people', 'Exit the program'])
	if answer == 1:
		print('> Option 1:')
	elif answer == 2:
		print('> Option 2:')
	elif answer == 3:
		print('> See you later alligator!')
		break
	else:
		print('> Error! Input a valid option!')
print('=' * 99)
