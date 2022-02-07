from libs.interfaces.menus import *
from libs.archive.archs import *
print(f'{" Challenge 115b ":=^99}')
#
print('>>> ')
print("INSTRUCTIONS:\n# .")
print('-' * 99)
# main program
file = 'infox.txt'
if not truefile(file):
	mkfile(file)

while True:
	answer = menu(['Register people', 'List registered people', 'Exit the program'])
	if answer == 1:
		registerfile(file)
	elif answer == 2:
		readfile(file)
	elif answer == 3:
		print('> See you later alligator!')
		break
	else:
		print('> Error! Input a valid option!')
print('=' * 99)
