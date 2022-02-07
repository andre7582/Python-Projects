# Aula 23 (Erros e excessões)

try:
	a = int(input('Numerator: '))
	b = int(input('Denominator: '))
	r = a / b


except ZeroDivisionError:
	print('Denominator do not be zero!')

except Exception as erro:
	print(f'404 {erro.__class__}')

else:
	print(f'r = {r}')
finally:
	print('END')
