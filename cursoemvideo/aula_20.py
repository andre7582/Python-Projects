# Aula 20 - Funções(Parte 1)

def showline():
	print('-' * 60)


# showline()
# print(f'{"TEXT":^30}')
# showline()


def title(txt):
	showline()
	print(f'{txt:^60}')
	showline()


title('COUNTER')


def entry(*num):
	length = len(num)
	totalsum = 0
	for number in num:
		totalsum += number
	print(f'Input: {length} numbers; Adding the values {num} we have {totalsum}.')


entry(1, 2, 3)
entry(4, 5)
entry(6, 7, 8, 9)
entry(1, 9)
