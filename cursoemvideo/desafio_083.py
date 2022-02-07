print(f'{" Challenge 083 ":=^99}')
# Crie um programa onde o utilizador digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
# analisar se a expressão contém parênteses abertos e fechados na ordem correta.
print('>>> Validating mathematical expression')
print('-' * 99)
print("INSTRUCTIONS:\nType a math expression and make sure the parentheses are in pairs.")
print('-' * 99)
box = []
expression = str(input('Type a expression: '))
for symbol in expression:
	if symbol == '(':
		box.append('(')
	elif symbol == ')':
		if len(box) > 0:
			box.pop()
		else:
			box.append(')')
			break
if len(box) == 0:
	print('Your expression is valid!')
else:
	print('Your expression is wrong.')
print('-' * 99)
