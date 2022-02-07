from libs.interfaces.menus import *
from libs.archive.archs import *
print(f'{" Challenge 115b ":=^99}')
#
print('>>> ')
print("INSTRUCTIONS:\n# .")
print('-' * 99)
# main program
file = 'infox.txt'
if truefile(file):
	print('> File ready to use.')
else:
	print('> File not found.')
	mkfile(file)

while True:
	answer = menu(['Register people', 'List people', 'Exit the program'])
	if answer == 1:
		print('> Option 1:')
	elif answer == 2:
		readfile(file)
	elif answer == 3:
		print('> See you later alligator!')
		break
	else:
		print('> Error! Input a valid option!')
print('=' * 99)
