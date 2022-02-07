print(f'{" Challenge 106 ":=^99}')
#
print('>>> "PyHelp" program')
print("INSTRUCTIONS:\n# Enter a Function or Library to see its help manual.")
print('-' * 99)
colors = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m')


def hellp(command):
	text(f'{command} manual:', 2)
	help(command)


def text(txt, color=0):
	# linelen = len(txt) + 6
	print(colors[color], end='')
	# print('*' * linelen)
	print(f'# {txt}')
	# print('*' * linelen)
	print(colors[0], end='')


# main program
entry = ''
while True:
	text('PyHelp', 4)
	entry = str(input('> Enter a Function or Library to see its help manual [input END to close the program]\n> '))
	if entry.upper() == 'END':
		break
	else:
		print()
		hellp(entry)

text('BYE!', 4)

print('=' * 99)
