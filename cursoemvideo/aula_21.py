# Aula 21 - Funções(Parte2)
def separator():
	print('.' * 99)


def add(a=7, b=7, c=7):
	s = a + b + c
	print(f'a + b + c = {s}')


add(3, 2)
separator()


def add(a=1, b=5, c=0):
	s = a + b + c
	print(f'a + b + c = {s}')


add(b=3, c=2)
separator()


def add(a=0, b=8, c=3):
	s = a + b + c
	return s


r1 = add(1, 2, 3)
r2 = add(4, c=5)
r3 = add(b=6)

print(f'{r1}, {r2}, {r3}.')
separator()


def test(b):
	a = 1
	b = 2
	c = 3
	print(f'{a}')
	print(f'{b}')
	print(f'{c}')


a = 4
test(a)
print(f'{a}')
separator()


def func():
	n2 = 2
	n3 = 3
	print(f'{n2}')
	print(f'{n3}')
	n1 = 4
	print(f'{n1}')


n1 = 1
func()
print(f'{n1}')
separator()


def data(b):
	global a
	a = 1
	b = 2
	print(f'{a}')
	print(f'{b}')


a = 3
data(a)
print(f'{a}')
separator()


def factorial(num=1):
	f = 1
	for c in range(num, 0, -1):
		f *= c
	return f


r1 = factorial(5)
r2 = factorial(10)
r3 = factorial(2)
print(f'{r1}, {r2}, {r3}.')
separator()


def pair(n=0):
	if n % 2 == 0:
		return True
	else:
		return False


num = int(input('Number: '))
if pair(num):
	print('Pair')
else:
	print('No Pair')
separator()
