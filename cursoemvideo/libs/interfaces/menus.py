def line(length=69):
	return '*' * length


def header(text):
	print(line())
	print(text.center(69))
	print(line())


def menu(listi):
	header('Files v.1.0')
	count = 1
	for item in listi:
		print(f'{count} > {item}')
		count += 1
	print(line())
	answer = readintp('Choosen option: ')
	return answer


def readintp(answer):
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
	return value
