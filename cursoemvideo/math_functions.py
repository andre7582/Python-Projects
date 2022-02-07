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
