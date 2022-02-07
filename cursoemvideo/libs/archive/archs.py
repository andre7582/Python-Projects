def truefile(name):
	try:
		openfile = open(name, 'rt')
		openfile.close()
	except FileNotFoundError:
		return False
	else:
		return True


def mkfile(name):
	try:
		makefile = open(name, 'wt+')
		makefile.close()
	except FileExistsError:
		print('> Error! File already exists')
	else:
		print(f'> Created {name} file to save registered people.')


def readfile(name):
	try:
		rfile = open(name, 'rt')
	except FileNotFoundError:
		print('Error! File not found!')
	else:
		print('* Registered people:')
		# print(rfile.read())
		c = 1
		for line in rfile:
			entry = line.split(';')
			entry[1] = entry[1].replace('\n', '')
			print(f'{c} {entry[0]:<20}{entry[1]} yo.')
			c += 1

def registerfile(file):
	print('* New register:')
	name = str(input('Name: '))
	age = str(input('Age: '))
	register(file, name, age)


def register(file, name='Unknown', age='Unknown'):
	try:
		reg = open(file, 'at')
	except FileNotFoundError:
		print('Error 404')
	else:
		try:
			reg.write(f'{name};{age}\n')
		except FileNotFoundError:
			print('Error 404')
		else:
			print(f'{name} successfully registered!')
			reg.close()
