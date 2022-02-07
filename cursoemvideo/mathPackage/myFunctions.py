# Math functions


"""def factoriali(num):
	fac = 1
	for i in range(1, num + 1):
		fac = fac * i
	return fac"""


def factoriali(num):
	fac = 1
	i = 1
	while i <= num:
		fac = fac * i
		i = i + 1
	return fac


def squaredi(num):
	return num ** 2


def squaredrooti(num):
	return num ** 0.5


def doublei(num):
	return num * 2


def triplei(num):
	return num * 3


def quadruplei(num):
	return num * 4


def halfi(num):
	return num / 2


def thirdi(num):
	return num / 3


def quarteri(num):
	return num / 4


def currencyp(price=100, currency='US$'):
	return f'{currency}{price:.2f}'


def increasep(price=100, rate=10):
	return price + (price * rate/100)


def decreasep(price=100, rate=10):
	return price - (price * rate/100)


def doublep(price=100):
	return price * 2


def halfp(price=100):
	return price / 2


def shortcurrencyp(price=100, increase=10, decrease=10):
	# print(f'Price: {currencyp(price)}')
	print(f'* Half of {currencyp(price)}: {currencyp(halfp(price))}.')
	print(f'* Double of {currencyp(price)}: {currencyp(doublep(price))}')
	print(f'* Increasing by {increase}%: {currencyp(increasep(price, increase))}')
	print(f'* With {decrease}% discount: {currencyp(decreasep(price, decrease))}')


def ismoneyp(entry):
	valid = False
	while not valid:
		answer = str(input(entry)).replace(',', '.').strip()
		if answer.isalpha() or answer == '':
			print(f'\033[0;31mError! Please enter a valid value!\033[m')
		else:
			valid = True
			return float(answer)


def readintp(answer):
	ok = False
	value = 0
	while True:
		num = str(input(answer))
		if num.isnumeric():
			value = int(num)
			ok = True
		else:
			print('\033[0;33m% Error 404 %\033[m')
		if ok:
			break
	return value


def readfloatp(answer):
	while True:
		try:
			num = float(input(answer))
		except Exception as erro:
			print(f'404 {erro.__class__}')
			continue
		else:
			return num
